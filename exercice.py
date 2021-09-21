#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >= 0:
        result = number
    elif number < 0:
        result = number*(-1)
    return result


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for letter in prefixes:
        liste_nom.append(letter+suffixe)
    return liste_nom


def prime_integer_summation() -> int:
    somme = 0
    liste_premiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197
                      , 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
                      313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433
                      , 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    for nombre in liste_premiers:
        somme +=nombre
    return somme


def factorial(number: int) -> int:
    result = 1
    while number > 1:
        result = result*number
        number -= 1
    return result


def use_continue() -> None:
    for entier in range(1, 11):
        if entier ==5:
            continue
        print (entier)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accepted = []
    for position in range(len(groups)):
        if any(element==25 for element in groups[position]):
            accepted.append(groups[position])
        else:
            if len(groups[position]) >10:
                pass
            elif len(groups[position]) <= 3:
                pass
            elif any(element<18 for element in groups[position]):
                pass
            elif any(element>70 for element in groups[position]) and any (element==50 for element in groups[position]):
                pass
            else:
                accepted.append(groups[position])
    return accepted


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
