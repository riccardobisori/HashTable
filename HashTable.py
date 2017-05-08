# -*- coding: utf-8 -*-

import List
import numpy as np


# Funzione per determinare se un numero è primo

def primeNumber(n):
    if n in range(0, 3):
        return True
    j = 2
    while j < n:
        if n % j == 0:
            return False
        j += 1
    return True


# =====================================================================================================================
# Classe Hash Table con Indirizzamento Aperto
# =====================================================================================================================

class IndirizzamentoAperto:
    # Costruttore
    def __init__(self, length):
        if not primeNumber(length):
            self.m = self.biggestPrimeNumber(length)
            print "Hai inserito", length
            print "La dimensione dell'Hash Table con indirizzamento aperto è:", self.m, '\n'
        else:
            self.m = length

        self.table = np.array([None for _ in range(self.m)])
        self.collision = 0
        self.inspection = []  # Array contenente, per ogni casella, la lunghezza dell'ispezione fatta per ogni insert()

    # Getters
    def getCollision(self):
        return self.collision

    def getInspection(self):
        return self.inspection

    # Funzione Hash: ispezione lineare
    def ispezioneLineare(self, i, k):
        return ((k % self.m) + i) % self.m

    # Stampa la tabella
    def stampa(self):
        print self.table, '\n\n', "Collisioni:", self.collision, '\n', "Ispezioni:", np.sum(self.inspection), '\n'

    # Ricerca
    def search(self, k):
        i = 0
        j = self.ispezioneLineare(i, k)
        while self.table[j] is not None or i != self.m:
            if self.table[j] == k:
                print j, '\n'
                return j
            i += 1
            j = self.ispezioneLineare(i, k)
        return None

    # Inserimento
    def insert(self, k):
        i = 0
        j = self.ispezioneLineare(i, k)

        while i != self.m:
            if self.table[j] is None or self.table[j] is -1:
                self.table[j] = k
                self.inspection.append(i)
                return j
            else:
                self.collision += 1
                i += 1
                j = self.ispezioneLineare(i, k)

        print "!!Overflow!!", '\n'
        return None

    # Cancellazione
    def remove(self, k):
        print "Rimosso elemento in posizione: "
        j = self.search(k)
        if j is not None:
            self.table[j] = -1
            return j
        return None

    # Pulizia della tabella
    def clear(self):
        self.table = np.array([None for _ in range(self.m)])
        self.collision = 0
        self.inspection = []

    # Trova il numero primo più grande e più vicino a quello immesso
    @staticmethod
    def biggestPrimeNumber(n):
        while not primeNumber(n):
            n += 1
        return n


# =====================================================================================================================
# Classe Hash Table con Concatenamento
# =====================================================================================================================

class Concatenamento:
    # Costruttore
    def __init__(self, length):
        if not primeNumber(length):
            self.m = self.smallerPrimeNumber(length)
            print "Hai inserito", length
            print "La dimensione delll'Hash Table con concatenamento è: ", self.m
        else:
            self.m = length

        self.table = np.empty([self.m, ], dtype=list)
        for i in range(self.m):
            self.table[i] = List.LinkedList()

        self.collision = 0

    # Funzione hash, metodo della divisione
    def hash(self, k):
        return k % self.m

    # Getter
    def getCollision(self):
        return self.collision

    # Stampa la tabella
    def stampa(self):
        for j in range(self.m):
            print j, "[]"
            self.table[j].PrintL()
        print "\n"
        print "Collisioni:", self.collision
        print "\n"

    # Ricerca
    def search(self, k):
        j = self.hash(k)
        return self.table[j].search(j)

    # Inserimento
    def insert(self, k):
        j = self.hash(k)
        if not self.table[j].is_empty():
            self.collision += 1

        self.table[j].add(k)

    # Cancellazione
    def remove(self, k):
        j = self.hash(k)
        self.table[j].remove(k)

    # Pulizia tabella
    def clear(self):
        self.table = np.empty([self.m, ], dtype=list)
        for i in range(self.m):
            self.table[i] = (List.LinkedList())
        self.collision = 0

    # Trova il numero primo più piccolo e più vicino al numero immesso
    @staticmethod
    def smallerPrimeNumber(n):
        while not primeNumber(n):
            n -= 1
        return n
