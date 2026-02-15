from csp import *
import itertools, copy

"""
Assignments are represented as dictionaries, the keys ar ethe variable names, the values are the values for that variable.
{'a': 3} is an assignment in which variable a has taken the value 3.
A constraint is represented as a lambda
"""


def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp[1]):
            yield assignment


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    # all the arcs in the network
    to_do = {(x, c) for c in csp.constraints for x in scope(c)}
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        # look at current domain of x
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            # look at domain of y, if there exists a combination in y such that constraint is satisfied
            # then x is in the new domain
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
        # if the older domain does not equal the new domain then something has changed
        # something got deleted from domain of x
        if csp.var_domains[x] != new_domain:
            # This means that we have to revisit the arcs that have changed
            for cprime in set(csp.constraints) - {c}:
                # Checking arcs involving other constraints that have x in their scope
                if x in scope(cprime):
                    #
                    for z in scope(cprime):
                        if x != z:  # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain  # COMPLETE
    return csp


domains = {x: set(range(10)) for x in "twofur"}
domains.update({"c1": {0, 1}, "c2": {0, 1}, "c3": {0, 1}})


# prune leading digits
# domains["t"].discard(0)
# domains["f"].discard(0)

# generate pairwise distinctness constraints
distinct_constraints = []
for a, b in itertools.combinations("twofur", 2):
    code = f"lambda {a}, {b}: {a} != {b}"
    distinct_constraints.append(eval(code))

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        # column constraints
        lambda o, r, c1: o + o == r + 10 * c1,
        lambda w, u, c1, c2: w + w + c1 == u + 10 * c2,
        lambda t, o, c2, c3: t + t + c2 == o + 10 * c3,
        lambda f, c3: f == c3,
        # no leading zeroes
        lambda t: t != 0,
        lambda f: f != 0,
        *distinct_constraints,
    },
)

# print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
# print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twofur"))

# new_csp = arc_consistent(cryptic_puzzle)
# print(sorted(new_csp.var_domains["r"]))

# new_csp = arc_consistent(cryptic_puzzle)
# print(sorted(new_csp.var_domains["w"]))

# new_csp = arc_consistent(cryptic_puzzle)
# solutions = []
# for solution in generate_and_test(new_csp):
#     solutions.append(sorted((x, v) for x, v in solution.items() if x in "twofur"))
# print(len(solutions))
# solutions.sort()
# print(solutions[0])
# print(solutions[5])
crossword_puzzle = CSP(
    var_domains={
        # read across:
        "across1": set("ant big bus car has".split()),
        "across3": set("book buys hold lane year".split()),
        "across4": set("ant big bus car has".split()),
        # read down:
        "down1": set("book buys hold lane year".split()),
        "down2": set("ginger search symbol syntax".split()),
    },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
    },
)
csp_instance = CSP(
    var_domains={var: {1, 2, 3, 4} for var in "abcd"},
    constraints={
        lambda a, b: a >= b,
        lambda a, b: b >= a,
        lambda a, b, c: c > a + b,
        lambda d: d <= d,
    },
)
new_csp = arc_consistent(csp_instance)

assert type(csp_instance) is CSP
print(sorted(csp_instance.var_domains.keys()))
print(len(csp_instance.constraints))
print(sorted(new_csp.var_domains.values()))
# Q7-----------------------------------------------------------------------------------------------

# simple_csp = CSP(
#     var_domains={x: set(range(1, 5)) for x in "abc"},
#     constraints={
#         lambda a, b: a < b,
#         lambda b, c: b < c,
#     },
# )
# relations = [
#     Relation(
#         header=["a", "b", "c"],
#         tuples={
#             (1, 0, 0),
#             (2, 0, 0),
#             (2, 1, 0),
#             (2, 0, 1),
#         },
#     ),
#     Relation(
#         header=["c, d"],
#         tuples={
#             (2, 0),
#             (1, 0),
#             (2, 1),
#         },
#     ),
# ]
# Q4-----------------------------------------------------------------------------------------------
# simple_csp = CSP(
#     var_domains={x: set(range(1, 5)) for x in "abc"},
#     constraints={
#         lambda a, b: a < b,
#         lambda b, c: b < c,
#     },
# )

# csp = arc_consistent(simple_csp)
# for var in sorted(csp.var_domains.keys()):
#     print("{}: {}".format(var, sorted(csp.var_domains[var])))


# csp = CSP(
#     var_domains={x: set(range(10)) for x in "abc"},
#     constraints={lambda a, b, c: 2 * a + b + 2 * c == 10},
# )

# csp = arc_consistent(csp)
# for var in sorted(csp.var_domains.keys()):
#     print("{}: {}".format(var, sorted(csp.var_domains[var])))


# Q1 -----------------------------------------------------------------------------------------------
# simple_csp = CSP(
#     var_domains={x: set(range(1, 5)) for x in 'abc'},
#     constraints={
#         lambda a, b: a < b,
#         lambda b, c: b < c,
#         })

# solutions = sorted(str(sorted(solution.items())) for solution
#                    in generate_and_test(simple_csp))
# print("\n".join(solutions))

# crossword_puzzle = CSP(
#     var_domains={
#         # read across:
#         'a1': set("ant,big,bus,car".split(',')),
#         'a3': set("book,buys,hold,lane,year".split(',')),
#         'a4': set("ant,big,bus,car,has".split(',')),
#         # read down:
#         'd1': set("book,buys,hold,lane,year".split(',')),
#         'd2': set("ginger,search,symbol,syntax".split(',')),
#         },
#     constraints={
#         lambda a1, d1: a1[0] == d1[0],
#         lambda d1, a3: d1[2] == a3[0],
#         lambda a1, d2: a1[2] == d2[0],
#         lambda d2, a3: d2[2] == a3[2],
#         lambda d2, a4: d2[4] == a4[0],
#         })

# crossword_puzzle = CSP(
#     var_domains={
#         # read across:
#         "across1": set("ant big bus car has".split()),
#         "across3": set("book buys hold lane year".split()),
#         "across4": set("ant big bus car has".split()),
#         # read down:
#         "down1": set("book buys hold lane year".split()),
#         "down2": set("ginger search symbol syntax".split()),
#     },
#     constraints={
#         lambda across1, down1: across1[0] == down1[0],
#         lambda down1, across3: down1[2] == across3[0],
#         lambda across1, down2: across1[2] == down2[0],
#         lambda down2, across3: down2[2] == across3[2],
#         lambda down2, across4: down2[4] == across4[0],
#     },
# )

# solution = next(iter(generate_and_test(crossword_puzzle)))
# print(sorted(crossword_puzzle.var_domains["across1"]))

# printing the puzzle similar to the way it actually  looks
# pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
#     solution['d1'], "", solution['d2'], fillvalue=" ")]
# pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
# print("\n".join(pretty_puzzle))

# ------------------------------------------------------------------------------------------------------------
