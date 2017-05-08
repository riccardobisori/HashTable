import pickle
import Test
import matplotlib.pyplot as mp

m = 1000
percentuali = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

valoriTest = (m, percentuali)

pickle.dump(valoriTest, open("test.p", "wb"))

Test.testResult()

risultatoOpen = pickle.load(open("risultatoOpen.p", "rb"))
risultatoChained = pickle.load(open("risultatoChained.p", "rb"))

collisioniOpen = risultatoOpen[0]
ispezioniOpen = risultatoOpen[1]

x = percentuali

# =====================================================================================================================
# Plot delle collisioni della classe con Concatenamento
# =====================================================================================================================

yMax = [i[0] for i in risultatoChained]
yMin = [i[1] for i in risultatoChained]
yAvg = [i[2] for i in risultatoChained]

mp.plot(x, yMin)
mp.plot(x, yAvg)
mp.plot(x, yMax)

mp.xlabel('Percentuale elementi')
mp.ylabel('Numero di collisioni')
mp.legend(['Min', 'Media', 'Max'], loc=2)
mp.title("Collisioni Hash Table con Concatenamento")
mp.show()

# =====================================================================================================================
# Plot delle collisioni della classe con Indirizzamento Aperto
# =====================================================================================================================

yMax = [i[0] for i in collisioniOpen]
yMin = [i[1] for i in collisioniOpen]
yAvg = [i[2] for i in collisioniOpen]

mp.plot(x, yMin)
mp.plot(x, yAvg)
mp.plot(x, yMax)

mp.xlabel('Percentuale elementi')
mp.ylabel('Numero di Collisioni')
mp.legend(['Min', 'Media', 'Max'], loc=2)
mp.title("Collisioni Hash Table con Indirizzamento Aperto")
mp.show()

# =====================================================================================================================
# Plot delle ispezioni della classe con Indirizzamento Aperto
# =====================================================================================================================

yMax = [i[0] for i in ispezioniOpen]
yMin = [i[1] for i in ispezioniOpen]
yAvg = [i[2] for i in ispezioniOpen]

mp.plot(x, yMin)
mp.plot(x, yAvg)
mp.plot(x, yMax)

mp.xlabel('Percentuale elementi')
mp.ylabel('Numero ispezioni')
mp.legend(['Min', 'Media', 'Max'], loc=2)
mp.title("Ispezioni Hash Table con Indirizzamento Aperto")
mp.show()





