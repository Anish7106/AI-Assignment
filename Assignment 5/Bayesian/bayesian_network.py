"""
Bayesian Network Example

Example: Burglary-Alarm Bayesian Network

Variables:
B = Burglary
E = Earthquake
A = Alarm
J = John Calls
M = Mary Calls

Run:
    python bayesian_network.py
"""


class BayesianNetwork:
    def __init__(self):
        self.variables = []
        self.parents = {}
        self.cpt = {}

    def add_variable(self, name, parents, cpt):
        self.variables.append(name)
        self.parents[name] = parents
        self.cpt[name] = cpt

    def probability(self, variable, value, evidence):
        parents = self.parents[variable]

        if not parents:
            p_true = self.cpt[variable][()]
        else:
            key = tuple(evidence[parent] for parent in parents)
            p_true = self.cpt[variable][key]

        return p_true if value else 1 - p_true


def enumeration_ask(query_var, evidence, bn):
    """
    Exact inference by enumeration.
    Returns normalized probability distribution for query_var.
    """
    distribution = {}

    for query_value in [True, False]:
        extended_evidence = evidence.copy()
        extended_evidence[query_var] = query_value
        distribution[query_value] = enumerate_all(bn.variables, extended_evidence, bn)

    total = sum(distribution.values())
    for key in distribution:
        distribution[key] = distribution[key] / total

    return distribution


def enumerate_all(variables, evidence, bn):
    if not variables:
        return 1.0

    first = variables[0]
    rest = variables[1:]

    if first in evidence:
        prob = bn.probability(first, evidence[first], evidence)
        return prob * enumerate_all(rest, evidence, bn)

    total = 0
    for value in [True, False]:
        new_evidence = evidence.copy()
        new_evidence[first] = value
        prob = bn.probability(first, value, new_evidence)
        total += prob * enumerate_all(rest, new_evidence, bn)

    return total


def build_burglary_network():
    bn = BayesianNetwork()

    bn.add_variable("B", [], {(): 0.001})
    bn.add_variable("E", [], {(): 0.002})

    bn.add_variable(
        "A",
        ["B", "E"],
        {
            (True, True): 0.95,
            (True, False): 0.94,
            (False, True): 0.29,
            (False, False): 0.001
        }
    )

    bn.add_variable(
        "J",
        ["A"],
        {
            (True,): 0.90,
            (False,): 0.05
        }
    )

    bn.add_variable(
        "M",
        ["A"],
        {
            (True,): 0.70,
            (False,): 0.01
        }
    )

    return bn


if __name__ == "__main__":
    bn = build_burglary_network()

    evidence = {"J": True, "M": True}
    result = enumeration_ask("B", evidence, bn)

    print("Query: P(Burglary | JohnCalls=True, MaryCalls=True)")
    print("P(Burglary=True):", round(result[True], 5))
    print("P(Burglary=False):", round(result[False], 5))
