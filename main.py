#### Imports et définition des variables globales
"""
exo08-lecture-donnees-marieEmilienneGNAMIEN
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    numbers = "1234567890"
    l = []
    lprime = []
    lfinal = []
    with open(filename, mode='r', encoding='utf8') as f:
        l = list(f)
        for elt in l:
            nb = ""
            for letter in elt:
                if letter in numbers:
                    nb += letter
                elif letter not in numbers:
                    lprime += [int(nb)]
                    nb = ""
            lfinal.append(lprime)
            lprime = []
        return lfinal

print("test read_data", read_data(FILENAME))


def get_list_k(data, k):
    """
    retourne la liste d'indice k (k passé en argument)
    Args:
    l (liste): liste d'entiers
    k (entier) : indice
    Returns:
    Retourne la liste d'indice k
    """
    return data[k]

print("hello")
print(get_list_k(read_data(FILENAME),4))

def get_first(l):
    """
    retourne la somme de la liste en arg
    Args:
    l (liste): liste d'entiers
    Returns:
    Retourne le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    retourne le dernier élément de la liste
    Args:
    l (liste): liste d'entiers
    Returns:
    Retourne le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    retourne le maximum de la liste en arg
    Args:
    l (liste): liste d'entiers
    Returns:
    Retourne le maximum de la liste
    """
    return max(l)

def get_min(l):
    """
    retourne le minimum de la liste en arg
    Args:
    l (liste): liste d'entiers
    Returns:
    Retourne le minimum de la liste
    """
    return min(l)

def get_sum(l):
    """
    retourne la somme de la liste en arg
    Args:
    l (liste): liste d'entiers
    Returns:
    Retourne une somme d'entiers
    """
    return sum(l)


#### Fonction principale
print("hello", 43)

def main():
    """
    utilisation de nos fonctions secondaires

    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
