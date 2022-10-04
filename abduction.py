def explain(observations, kb, explanation=set()):
    if observations:
        o = observations[0]

        if o in kb['assumables']:
            return explain(observations[1:], kb, explanation | {o})
        else:
            bodies = kb['rules'][o]
            explanations = []

            for body in bodies:
                explanations += explain(body + observations[1:], kb, explanation)

            return explanations

    return [explanation]


def get_minimal_explanations(explanations):
    not_minimal = []

    for i in range(len(explanations)):
        for j in range(len(explanations)):
            if explanations[i].issubset(explanations[j]) and i != j:
                not_minimal.append(j)

    return [explanations[i] for i in range(len(explanations)) if i not in not_minimal]


if __name__ == "__main__":
    kb = {'rules': {'a': [['b', 'c']],
                    'b': [['d'], ['c']],
                    'd': [['h']],
                    'g': [['a', 'b', 'c']],
                    'f': [['h', 'b']]},
          'askables': ['c', 'e']}

    kb2 = {'rules': {'bronchitis': [['influenza'], ['smokes']],
                     'coughing': [['bronchitis']],
                     'wheezing': [['bronchitis']],
                     'fever': [['influenza'], ['infection']],
                     'sore_throat': [['influenza']],
                     'False': [['smokes', 'non-smoker']]
                     },
           'assumables': ['smokes', 'influenza', 'infection']}

    explanations = explain(['bronchitis', 'fever'], kb2)

    print(explanations)

    print(get_minimal_explanations(explanations))
