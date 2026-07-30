# Primind această listă de numere:
#
# numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17],
#
# Si lista de persoane:
#
# people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]
#  Creati o functie care returnează: o lista de dicționare, care arată astfel:
#
# result = { "name": "Codrin", "age": 30, "of_age": True}
#
# Pentru fiecare persoană, alegeți un număr random din lista de numere.
# Unde of_age este true doar daca numărul ales este mai mare de 18
#
# import random
# picked = random.choice(numbers)
#
# Creati o altă funcție care filtrează toate persoanele și returnează doar persoanele of_age.
# Creați oldest_person, o funcție care returnează cea mai bătrână persoană
# La fel și pentru youngest_person, cea mai tânără
#
# Printați acel rezultat.

import random

# Listele primite
numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]

people = [
    "Codrin",
    "Adrian",
    "John",
    "Maria",
    "Tudor",
    "Maximilian",
    "Spike"
]


# Creează lista de dicționare
def create_people(people, numbers):
    result = []

    for person in people:
        age = random.choice(numbers)

        result.append({
            "name": person,
            "age": age,
            "of_age": age > 18
        })

    return result


# Returnează doar persoanele majore
def filter_of_age(people_list):
    result = []

    for person in people_list:
        if person["of_age"]:
            result.append(person)

    return result


# Returnează cea mai bătrână persoană
def oldest_person(people_list):
    oldest = people_list[0]

    for person in people_list:
        if person["age"] > oldest["age"]:
            oldest = person

    return oldest


# Returnează cea mai tânără persoană
def youngest_person(people_list):
    youngest = people_list[0]

    for person in people_list:
        if person["age"] < youngest["age"]:
            youngest = person

    return youngest


# Program principal
result = create_people(people, numbers)

print("Toate persoanele:")
for person in result:
    print(person)

print("\nPersoanele majore:")
adults = filter_of_age(result)
for person in adults:
    print(person)

print("\nCea mai bătrână persoană:")
print(oldest_person(result))

print("\nCea mai tânără persoană:")
print(youngest_person(result))