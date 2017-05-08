import pickle
import HashTable
import random


# Funzione che esegue i test. Legge un file pickle contenente grandezza dell'Hash Table e valori percentuali e ne scrive
# uno nuovo coi risultati dei test
def testResult():
    testStart = pickle.load(open("test.p", "rb"))
    risultatoOpen = testOpen(testStart)
    risultatoChained = testChained(testStart)

    pickle.dump(risultatoOpen, open("risultatoOpen.p", "wb"))
    pickle.dump(risultatoChained, open("risultatoChained.p", "wb"))


# Test per l'Hash Table con concatenamento
def testChained(testStart):
    m = testStart[0]
    percentuali = testStart[1]

    chainedTable = HashTable.Concatenamento(m)

    collisioni = []
    risultatoCollisioni = []

    for p in percentuali:
        for j in range(20):
            for i in range((m * p) / 100):
                val = random.randint(0, 100 * m)
                chainedTable.insert(val)

            collisioni.append(chainedTable.getCollision())
            chainedTable.clear()

        maxCollisioni = max(collisioni)
        minCollisioni = min(collisioni)
        mediaCollisioni = (sum(collisioni)) / len(collisioni)
        listaCollisioni = [maxCollisioni, minCollisioni, mediaCollisioni]

        risultatoCollisioni.append(listaCollisioni)

        collisioni = []

    return risultatoCollisioni


# Test per l'Hash Table con indirizzamento diretto
def testOpen(testStart):
    m = testStart[0]
    percentuali = testStart[1]

    openTable = HashTable.IndirizzamentoAperto(m)

    collisioni = []
    ispezioni = []

    risultatoCollisioni = []
    risultatoIspezioni = []

    for p in percentuali:
        for j in range(0, 20):
            for i in range((m * p) / 100):
                val = random.randint(0, 100 * m)
                openTable.insert(val)

            collisioni.append(openTable.getCollision())
            ispezioni.append(openTable.getInspection())
            openTable.clear()

        maxCollisioni = max(collisioni)
        minCollisioni = min(collisioni)
        mediaCollisioni = sum(collisioni) / len(collisioni)
        listaCollisioni = [maxCollisioni, minCollisioni, mediaCollisioni]

        risultatoCollisioni.append(listaCollisioni)

        maxIspezioni = max(max(j) for j in ispezioni)
        minIspezioni = min(min(j) for j in ispezioni)
        mediaIspezioni = sum(sum(j) / len(j) for j in ispezioni) / len(ispezioni)
        listaIspezioni = [maxIspezioni, minIspezioni, mediaIspezioni]

        risultatoIspezioni.append(listaIspezioni)

        collisioni = []
        ispezioni = []

    return risultatoCollisioni, risultatoIspezioni
