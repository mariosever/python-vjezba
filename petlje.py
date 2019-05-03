# Petlje

import random

tajnibroj = random.randint(1,30)

pogodi = 0


for x in range(5):

    pogodi = int(input("Pogodi jedan broj između 1 i 30: "))

    if pogodi == tajnibroj:
        print("Bravo, pogodio si broj.")
        break
    elif pogodi > tajnibroj:
        print("Fulao si, probaj neki manji broj.")
    elif pogodi < tajnibroj:
        print("Fulao si, probaj neki veći broj.")

print("Kraj programa..")
print("Traženi broj u ovoj igri bio je: " + str(tajnibroj))

