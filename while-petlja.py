# Program koji preračunava km u milje

print("Pozdrav, ovo je program koji preračunava km u milje.")

while True:

    print("Unesi broj kilometara koje želiš preračunati. Unesi samo broj! ")

    km = input("Kilometri: ")

    km = float(km.replace(",", "."))

    milje = km * 0.621371

    print("Rezultat: " + str(milje))

    izbor = input("Želiš li novi izračun? DA / NE: ")

    if izbor == "NE":
        break