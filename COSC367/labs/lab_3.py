from itertools import product


def interpretations(atoms):
    # add entries in alphabetical order
    # Pass a list (with two elements in the right order) to itertools.product
    atoms = sorted(atoms)
    interpretations = sorted(product([True, False], repeat=len(atoms)))

    results = []
    for truth in interpretations:
        interpretations = dict(zip(atoms, truth))
        results.append(interpretations)

    return results


# atoms = {"q", "p"}
# for i in interpretations(atoms):
#     print(i)

# atoms = {"human", "mortal", "rational"}
# for i in interpretations(atoms):
#     print(i)


def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """

    return {atom for atom in formula.__code__.co_varnames}


def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)


def models(knowledge_base):
    # takes a kb and returns a possibly empty list of interpretations that are the models of the kb
    # each formula is a lambda expression that returns a bool
    # the lambda parameters are the atoms in the formula
    # the keys and output list of the returned dict must be the same order as interpretations

    # You need to first construct a set that contains all the atoms used in the entire knowledge base.
    atoms_kb = [atoms(formula) for formula in knowledge_base]
    merged_atoms = set().union(*atoms_kb)
    interpretations_result = interpretations(merged_atoms)

    models = []
    for interpretation in interpretations_result:
        if all(value(formula, interpretation) for formula in knowledge_base):
            models.append(interpretation)

    return models


# knowledge_base = {lambda a, b: a and not b, lambda c: c}

# print(models(knowledge_base))

# knowledge_base = {lambda a, b: a and not b, lambda c, d: c or d}

# for interpretation in models(knowledge_base):
#     print(interpretation)


import re


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns a list of pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 20 Sep 2024

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    return [
        (mo.group("HEAD"), re.findall(ATOM, mo.group("BODY") or ""))
        for mo in re.finditer(CLAUSE, knowledge_base)
    ]


def forward_deduce(kb_string):
    # Bottom up proof procedure
    #  takes a string of a kb that contains propositional definite clauses
    # returns a collection (set or list) of all atoms (strings) that can be derived (true) from the kb
    C = set()
    definite_clauses = clauses(kb_string)
    while True:
        seen = set()

        for head, atoms in definite_clauses:
            # When the proposition is true, append the head to start looping the clauses
            # If the head is not in C and all of atoms meet
            if all(atom in C for atom in atoms) and head not in C:
                seen.add(head)
        if not seen:
            break

        C.update(seen)
    return C


kb_string = """
a :- b.
b.
"""

# print(", ".join(sorted(forward_deduce(kb_string))))

kb_string = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

# print(", ".join(sorted(forward_deduce(kb_string))))

kb_string = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

# print(", ".join(sorted(forward_deduce(kb_string))))


import re
from COSC367.graph_search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns a list of pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 20 Sep 2024

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    return [
        (mo.group("HEAD"), re.findall(ATOM, mo.group("BODY") or ""))
        for mo in re.finditer(CLAUSE, knowledge_base)
    ]


class KBGraph(Graph):
    # Top down procedure
    # DFS frontier class can provide implicit backtracking
    # nodes are the body of the answer clause
    # if the graph search determines the given query is true, the proof of it is done by printing the path
    # So have meaningful labels for the edges of the graph

    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        # I want the starting node to have the query body
        # the head needs to exist for it to go over to the expansion part of this code
        # which is the outgoing_arcs section
        return [("query", list(self.query))]

    def is_goal(self, node):
        # If the node we are in does not have a body then we have found the answer
        return len(node[1]) == 0

    def outgoing_arcs(self, tail_node):
        arcs = []
        head, body = tail_node

        # If we have reached the goal and hence there is no body
        if not body:
            return arcs

        # At the start we are grabbing the atom from the query which is in the body
        atom = body[0]

        for clause_head, clause_body in self.clauses:
            if clause_head == atom:
                # The new body has to be the clause body and the rest of the node body
                new_body = clause_body + body[1:]
                new_node = (head, new_body)
                arcs.append(
                    Arc(
                        tail=tail_node,
                        head=new_node,
                        action=f"{atom} <- {clause_body}",
                        cost=1,
                    )
                )

        return arcs

import heapq
heapq.heappop()

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration  # dont change this one


kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {"a"}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {"a", "b", "d"}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
all_tests_passed :- program_is_correct.
all_tests_passed.
"""

query = {"program_is_correct"}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
a :- b.
"""

query = {"c"}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")
