import random

from django.http import HttpRequest, HttpResponse


names = [
    "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
    "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
    "Diana", "Radu", "Laura", "Cristian", "Raluca", "Bianca",
]

numbers = [
    73, 28, 95, 14, 61, 39, 87, 5, 46, 32,
    345, 232, 12, 33, 99, 96, 35, 1, 9, 10,
]


def ordered_names(request: HttpRequest):
    sorted_names = sorted(names)

    return HttpResponse(str(sorted_names))


def ordered_numbers(request: HttpRequest):
    sorted_numbers = sorted(numbers, reverse=True)

    return HttpResponse(str(sorted_numbers))


def paired_names(request: HttpRequest):
    result = []

    for name in names:
        person = {
            "name": name,
            "count": random.choice(numbers),
        }

        result.append(person)

    return HttpResponse(str(result))