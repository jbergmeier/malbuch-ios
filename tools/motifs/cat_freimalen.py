from dsl import *
EMOJI, DE, EN, COLOR = "✏️", "Freies Malen", "Free Drawing", "#FF9F1C"


def leer():
    m = Motif("frei_leer", "Leeres Blatt", "Blank Page")
    m.f(rect(1, 1, 98, 98, 3))
    return m


def rahmen():
    m = Motif("frei_rahmen", "Blatt mit Rahmen", "Page with Frame")
    m.f(rect(1, 1, 98, 98, 3))
    m.f(rect(10, 10, 80, 80, 3))
    return m


def punkte():
    m = Motif("frei_punkte", "Punkteblatt", "Dotted Page")
    m.f(rect(1, 1, 98, 98, 3))
    for i in range(1, 8):
        for j in range(1, 8):
            m.dot((i * 12.5, j * 12.5, 0.9))
    return m


def himmel_wiese():
    m = Motif("frei_landschaft", "Himmel und Wiese", "Sky and Meadow")
    m.f(rect(1, 1, 98, 98, 3))
    m.f(blob([(1, 62), (25, 54), (50, 60), (75, 52), (99, 60), (99, 97), (1, 97)]))
    return m


def build():
    return [leer(), rahmen(), punkte(), himmel_wiese()]
