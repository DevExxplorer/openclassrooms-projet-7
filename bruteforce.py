from itertools import combinations

def bruteforce(actions):
    budget = 500  # Budget en euros

    # Convertir le prix et le bénéfice en centimes pour éviter les erreurs d'arrondi
    actions_centimes = [(name, int(price * 100), float(benefit)) for name, price, benefit in actions]
    budget_centimes = int(budget * 100)

    # Rechercher la meilleure combinaison
    best_combination = []
    best_benefit = 0

    for r in range(1, len(actions_centimes) + 1):
        for combination in combinations(actions_centimes, r):
            total_cost = sum(action[1] for action in combination)
            if total_cost <= budget_centimes:
                benefit = sum(action[1] * float(action[2]) / 100 for action in combination)
                if benefit > best_benefit:
                    best_benefit = benefit
                    best_combination = combination

    # Affichage du résultat
    print("\nActions sélectionnées :")
    for action in best_combination:
        print(f"{action[0]}")

    print("")
    print(f"Total des bénéfices: {best_benefit / 100}")
    print(f"Total des coûts: {sum(action[1] for action in best_combination) / 100}")
