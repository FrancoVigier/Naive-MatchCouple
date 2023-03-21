import itertools
from main import *


def test_imparejable():
    persona = ("Marcos", "Montenegro", "Rafaela", 10, "F", "A")
    persona2 = ("Julian", "Montenegro", "Rafaela", 14, "M", "N")
    persona3 = ("Francisco", "Montenegro", "Rafaela", 19, "M", "F")

    assert imparejable(persona)
    assert imparejable(persona2)
    assert not imparejable(persona3)


def test_matchea():
    persona1 = ("Julian", "Montenegro", "Rafaela", 14, "M", "F")
    persona2 = ("Marta", "Montenegro", "San Nicolas", 19, "F", "M")
    persona3 = ("Carla", "Montenegro", "Rafaela", 16, "F", "A")
    persona4 = ("Julio", "Montenegro", "San Nicolas", 11, "M", "F")
    persona5 = ("Micaela", "Montenegro", "Rafaela", 18, "F", "A")
    persona6 = ("Facundo", "Montenegro", "San Nicolas", 70, "M", "F")
    persona7 = ("Micaelo", "Montenegro", "Rafaela", 18, "M", "F")

    assert not matchea(persona1, persona2)
    assert not matchea(persona2, persona4)
    assert matchea(persona2, persona6)
    assert not matchea(persona3, persona5)
    assert matchea(persona7, persona5)
    assert matchea(persona3, persona1)


def test_matcheo():
    personas = [("Julio", "Montenegro", "A", 11, "M", "F"),
                ("Julian", "Montenegro", "B", 14, "M", "F"),
                ("Carla", "Montenegro", "B", 16, "F", "A"),
                ("Marta", "Montenegro", "A", 19, "F", "M"),
                ("Micaela", "Montenegro", "B", 18, "F", "A"),
                ("Facundo", "Montenegro", "A", 70, "M", "F"),
                ("Micaelo", "Montenegro", "B", 18, "M", "F"),
                ("Micaelo", "Montenegro", "C", 18, "M", "F"),
                ("Micaelo", "Montenegro", "C", 18, "M", "A")]

    for permutacion in list(itertools.permutations(personas)):
        divididos = dividir(permutacion)
        segregados, parejas = conquistar(divididos)

        assert len(segregados) == 3
        assert len(parejas) == 3


