import itertools
import re


def interpretations(atoms):
    atoms = sorted(atoms)
    interpretations = sorted(itertools.product([True, False], repeat=len(atoms)))

    result = []
    for truth in interpretations:
        interpretation = dict(zip(atoms, truth))
        result.append(interpretation)

    return result


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
    atoms_kb = [atoms(formula) for formula in knowledge_base]
    merged_atoms = set().union(*atoms_kb)
    interpretation_list = interpretations(merged_atoms)

    result = []
    for interpretation in interpretation_list:
        if all(value(formula, interpretation) for formula in knowledge_base):
            result.append(interpretation)

    return result


# knowledge_base = {lambda a, b: a and not b, lambda c: c}

# print(models(knowledge_base))


# knowledge_base = {lambda a, b: a and not b, lambda c, d: c or d}

# for interpretation in models(knowledge_base):
#     print(interpretation)


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
    C = set()
    definite_clauses = clauses(kb_string)
    while True:
        seen = set()
        for head, atoms in definite_clauses:
            if all(atom in C for atom in atoms) and head not in C:
                seen.add(head)
        if not seen:
            break
    C.update(seen)
    return C

def forward_deduce(kb_string):
    C = set()
    definite_clauses = clauses(kb_string)
    while True:
        seen = set()
        for head, atoms in definite_clauses:
            if all(atom in C for atom in atoms) and head not in C:
                seen.add(head)
        if not seen:
            break
        C.update(seen)
    return C


def forward_deduce(kb_string):
    C = set()
    definite_clauses = clauses(kb_string)

    while True:
        seen = set()
        for head, atoms in definite_clauses:
            if all(atom in C for atom in atoms) and head not in C:
                seen.add(head)
        if not seen:
            break
        C.update(seen)
    return C


def interpretations(atoms):
    atoms = sorted(atoms)
    intepretations_list = sorted(itertools.product([True, False], repeat = len(atoms)))

    result = []
    for truth in intepretations_list:
        interpretation = dict(zip(atoms, truth))
        result.append(interpretation)

    return result


def models(knowledge_base):
    atoms_kb  = [atoms(formula) for formula in knowledge_base]
    merged_atoms = set().union(*atoms_kb)
    interpretations_list = interpretations(merged_atoms)

    result = []
    for interpretation in interpretations_list:
        if all(value(formula, interpretation) for formula in knowledge_base):
            result.append(interpretation)

    return result

import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns a list of pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 20 Sep 2024

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    return [(mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or ""))
            for mo in re.finditer(CLAUSE, knowledge_base)]


# import any module as necessary

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


def interpretations(atoms):
    atoms = sorted(atoms)
    interpretation_list = sorted(itertools.product([True, False], repeat=len(atoms)))

    result = []
    for truth in interpretation_list:
        interpretation = dict(zip(atoms, truth))
        result.append(interpretation)

    return result


def models(knowledge_base):
    atoms_kb = [atoms(formula) for formula in knowledge_base]
    merged_atoms = set().union(*atoms_kb)
    interpretation_list = interpretations(merged_atoms)

    result = []
    for interpretation in interpretation_list:
        if all(value(formula, interpretation) for formula in knowledge_base):
            result.append(interpretation)

    return result


def forward_deduce(kb_string):
    definite_clauses = clauses(kb_string)
    C = set()
    while True:
        seen = []
        for head, atoms in definite_clauses:
            if all(atom not in C for atom in atoms) and head not in seen:
                C.add(head)
        if not seen:
            break
        C.update(seen)

    return C
