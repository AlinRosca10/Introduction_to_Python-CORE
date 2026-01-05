def calculed_total_venit(venituri):
    """
    Calculeaza totalul veniturilor dintr-o lista de venituri.

    :param venituri: Lista de venituri
    :return: Totalul veniturilor
    """
    total = 0
    for venit in venituri:
        total += venit
    return total
# Exemplu de utilizare
venituri = [23200, 15000, 12000, 18000, 20000]
total_venit = calculed_total_venit(venituri)
print(f"Total venit: {total_venit}")
