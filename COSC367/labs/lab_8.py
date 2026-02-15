def joint_prob(network, assignment):
    """
    Returns the probability of the assignment
    assignment: dictionary where keys are the var names and values are T or F.
    """
    p = 1  # p will eventually hold the value we are interested in
    parents_str = "Parents"
    CPT = "CPT"
    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT.
        parents = network[var][parents_str]
        if len(parents) == 0:
            var_prob = network[var][CPT].get(())
        else:
            parent_lookup = tuple(
                assignment[parent] for parent in network[var][parents_str]
            )
            var_prob = network[var][CPT][parent_lookup]

        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
        if assignment.get(var) == True:
            p *= var_prob
        else:
            p *= 1 - var_prob

    return p


# network = {
#     "Burglary": {"Parents": [], "CPT": {(): 0.001}},
#     "Earthquake": {
#         "Parents": [],
#         "CPT": {
#             (): 0.002,
#         },
#     },
#     "Alarm": {
#         "Parents": ["Burglary", "Earthquake"],
#         "CPT": {
#             (True, True): 0.95,
#             (True, False): 0.94,
#             (False, True): 0.29,
#             (False, False): 0.001,
#         },
#     },
#     "John": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.9,
#             (False,): 0.05,
#         },
#     },
#     "Mary": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.7,
#             (False,): 0.01,
#         },
#     },
# }

# p = joint_prob(
#     network,
#     {"John": True, "Mary": True, "Alarm": True, "Burglary": False, "Earthquake": False},
# )
# print("{:.8f}".format(p))


# network = {
#     "A": {"Parents": [], "CPT": {(): 0.1}},
#     "B": {
#         "Parents": ["A"],
#         "CPT": {
#             (True,): 0.8,
#             (False,): 0.7,
#         },
#     },
# }

# p = joint_prob(network, {"A": False, "B": True})
# print("{:.5f}".format(p))


# network = {
#     "A": {"Parents": [], "CPT": {(): 0.2}},
# }
# p = joint_prob(network, {"A": False})
# print("{:.5f}".format(p))


# network = {
#     'A': {
#         'Parents': [],
#         'CPT': {
#             (): 0.2
#             }},
# }
# p = joint_prob(network, {'A': True})
# print("{:.5f}".format(p))

from itertools import product


def query(network, query_var, evidence):
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    distribution = [0, 0]  # initialise a raw distribution
    assignment = dict(evidence)  # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            # Update the assignment (we now have a complete assignment)
            hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}

            # Update the raw distribution by the probability of the assignment.
            # COMPLETE
            assignment.update(hidden_assignments)
            if query_value:
                distribution[1] += joint_prob(network, assignment)
            else:
                distribution[0] += joint_prob(network, assignment)

    # Normalise the raw distribution and return it
    # COMPLETE
    total = sum(distribution)
    if total > 0:
        distribution = [x / total for x in distribution]
    return {True: distribution[1], False: distribution[0]}


# network = {
#     "A": {"Parents": [], "CPT": {(): 0.2}},
# }

# answer = query(network, "A", {})
# print("P(A=true) = {:.5f}".format(answer[True]))
# print("P(A=false) = {:.5f}".format(answer[False]))


# network = {
#     "A": {"Parents": [], "CPT": {(): 0.1}},
#     "B": {
#         "Parents": ["A"],
#         "CPT": {
#             (True,): 0.8,
#             (False,): 0.7,
#         },
#     },
# }

# answer = query(network, "B", {"A": False})
# print("P(B=true|A=false) = {:.5f}".format(answer[True]))
# print("P(B=false|A=false) = {:.5f}".format(answer[False]))


# network = {
#     "A": {"Parents": [], "CPT": {(): 0.1}},
#     "B": {
#         "Parents": ["A"],
#         "CPT": {
#             (True,): 0.8,
#             (False,): 0.7,
#         },
#     },
# }

# answer = query(network, "B", {})
# print("P(B=true) = {:.5f}".format(answer[True]))
# print("P(B=false) = {:.5f}".format(answer[False]))


# network = {
#     "Burglary": {"Parents": [], "CPT": {(): 0.001}},
#     "Earthquake": {
#         "Parents": [],
#         "CPT": {
#             (): 0.002,
#         },
#     },
#     "Alarm": {
#         "Parents": ["Burglary", "Earthquake"],
#         "CPT": {
#             (True, True): 0.95,
#             (True, False): 0.94,
#             (False, True): 0.29,
#             (False, False): 0.001,
#         },
#     },
#     "John": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.9,
#             (False,): 0.05,
#         },
#     },
#     "Mary": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.7,
#             (False,): 0.01,
#         },
#     },
# }

# answer = query(network, "Burglary", {"John": True, "Mary": True})
# print(
#     "Probability of a burglary when both\n"
#     "John and Mary have called: {:.3f}".format(answer[True])
# )


# network = {
#     "Burglary": {"Parents": [], "CPT": {(): 0.001}},
#     "Earthquake": {
#         "Parents": [],
#         "CPT": {
#             (): 0.002,
#         },
#     },
#     "Alarm": {
#         "Parents": ["Burglary", "Earthquake"],
#         "CPT": {
#             (True, True): 0.95,
#             (True, False): 0.94,
#             (False, True): 0.29,
#             (False, False): 0.001,
#         },
#     },
#     "John": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.9,
#             (False,): 0.05,
#         },
#     },
#     "Mary": {
#         "Parents": ["Alarm"],
#         "CPT": {
#             (True,): 0.7,
#             (False,): 0.01,
#         },
#     },
# }

# answer = query(network, "John", {"Mary": True})
# print("Probability of John calling if\n" "Mary has called: {:.5f}".format(answer[True]))


# network = {
#     "Disease": {
#         "Parents": [],
#         "CPT": {
#             (): 0.00001,
#         },
#     },
#     "Test": {
#         "Parents": ["Disease"],
#         "CPT": {
#             (True,): 0.99,
#             (False,): 0.01,
#         },
#     },
# }

# answer = query(network, "Disease", {"Test": True})
# print(
#     "The probability of having the disease\n"
#     "if the test comes back positive: {:.8f}".format(answer[True])
# )


# answer = query(network, "Disease", {"Test": False})
# print(
#     "The probability of having the disease\n"
#     "if the test comes back negative: {:.8f}".format(answer[True])
# )

network = {
    "Virus": {
        "Parents": [],
        "CPT": {
            (): 0.01,
        },
    },
    "A": {
        "Parents": ["Virus"],
        "CPT": {
            (True,): 0.95,
            (False,): 0.10,
        },
    },
    "B": {
        "Parents": ["Virus"],
        "CPT": {
            (True,): 0.90,
            (False,): 0.05,
        },
    },
}

answer = query(network, "Virus", {"A": True})
print(
    "The probability of carrying the virus\n"
    "if test A is positive: {:.5f}".format(answer[True])
)


answer = query(network, "Virus", {"B": True})
print(
    "The probability of carrying the virus\n"
    "if test B is positive: {:.5f}".format(answer[True])
)
