import pygame
import sys
import random

pygame.init()

szerokosc, wysokosc = 800, 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Miasto Mruczenia")

bialy = (255, 255, 255)
czarny = (0, 0, 0)

class Kot(pygame.sprite.Sprite):
    def __init__(self, imie, x, y):
        super().__init__()
        self.imie = imie
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rybki = 0
        self.bonusy = {"happiness": 0, "fishing_skill": 0, "jump_skill": 0}

    def rysuj(self):
        ekran.blit(self.image, self.rect)

class Przechodzacy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def rysuj(self):
        ekran.blit(self.image, self.rect)

class Auto(pygame.sprite.Sprite):
    def __init__(self, x, y, predkosc):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.predkosc = predkosc

    def rysuj(self):
        ekran.blit(self.image, self.rect)

class Taxi(Auto):
    def __init__(self, x, y, predkosc, koszt_podrozy):
        super().__init__(x, y, predkosc)
        self.koszt_podrozy = koszt_podrozy

def interakcja_auto(kot):
    print(f"{kot.imie} spotyka auto na ulicy!")
    # Tutaj można dodać logikę interakcji z autem

def interakcja_taxi(kot):
    print(f"{kot.imie} znajduje taksówkę!")
    print(f"Podróż taksówką kosztuje {Taxi.koszt_podrozy} rybek.")
    odp = input("Czy chcesz skorzystać z taksówki? (t/n): ")
    if odp.lower() == 't':
        if kot.rybki >= Taxi.koszt_podrozy:
            kot.rybki -= Taxi.koszt_podrozy
            print(f"{kot.imie} podróżuje taksówką!")
            # Tutaj dodaj logikę podróżowania taksówką
        else:
            print("Niewystarczająca ilość rybek.")

# Dodane minigry
class Minigra:
    def __init__(self, nazwa, trudnosc, nagroda):
        self.nazwa = nazwa
        self.trudnosc = trudnosc
        self.nagroda = nagroda

minigry_dostepne = [
    Minigra("Złap Rybkę", 1, {"fishing_skill": 5}),
    Minigra("Skakanka", 2, {"jump_skill": 8}),
    # Dodaj więcej minigier z różnymi poziomami trudności i nagrodami
]

def interakcja_minigra(kot):
    print(f"{kot.imie} znalazł minigrę!")
    print("Dostępne minigry:")
    for i, minigra in enumerate(minigry_dostepne, 1):
        print(f"{i}. {minigra.nazwa} - Trudność: {minigra.trudnosc}")

    wybor = input("Wybierz numer minigry (lub wpisz 'q' aby zakończyć): ")
    if wybor.lower() == 'q':
        return

    try:
        numer_minigry = int(wybor)
        wybrana_minigra = minigry_dostepne[numer_minigry - 1]
        print(f"{kot.imie} bierze udział w minigrze: {wybrana_minigra.nazwa}")
        if random.randint(1, 10) <= wybrana_minigra.trudnosc:
            print("Udało się! Zdobywasz nagrodę.")
            kot.bonusy.update(wybrana_minigra.nagroda)
        else:
            print("Niestety, nie udało się tym razem.")
    except (ValueError, IndexError):
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

# Dodane sklep ogrodniczy
class SklepOgrodniczy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((150, 150))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()

