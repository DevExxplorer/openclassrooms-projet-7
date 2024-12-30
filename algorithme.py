def optimized(actions):
    budget = 500  # Budget en euros

    # Convertir le prix et le bénéfice en centimes pour éviter les erreurs d'arrondi
    actions_centimes = [(name, int(price * 100), round(price * float(benefit) / 100, 2)) for name, price, benefit in
                        actions]
    budget_centimes = int(budget * 100)

    # Création du tableau vide pour l'algorithme sac a dos
    tab = [[0 for _ in range(budget_centimes + 1)] for _ in range(len(actions_centimes) + 1)]

    # Ajout des données dans le tableau
    for i in range(1, len(actions_centimes) + 1):
        for w in range(1, budget_centimes + 1):
            if actions_centimes[i - 1][1] <= w:
                include_item = round(actions_centimes[i - 1][2], 2) + tab[i-1][w - actions_centimes[i - 1][1]]
                exclude_item = tab[i - 1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i - 1][w]

    """
    for row in tab:
        print(row)
    """

    items_included = []
    total_cost = 0
    total_benefit = 0
    w = budget_centimes
    for i in range(len(actions_centimes), 0, -1):
        if tab[i][w] != tab[i - 1][w]:
            items_included.append(actions_centimes[i - 1])
            total_benefit += actions_centimes[i - 1][2]
            total_cost += actions_centimes[i - 1][1]
            w -= actions_centimes[i - 1][1]

    print("\nItems à séléctionnés:")

    for items in items_included:
        print(f"{items[0]} - {str(items[1] / 100)}€")

    print(f"\nTotal cost: {total_cost / 100}€")
    print(f"Total return: {total_benefit}€")

    return tab[len(actions_centimes)][budget_centimes]
