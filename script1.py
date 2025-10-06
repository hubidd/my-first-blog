import os
while True:
    print("Kalkulator BMI")
    waga = input("Podaj wagę: ")
    wzrost = input("Podaj wzrost: ")
    try:
        waga = float(waga)
        wzrost = float(wzrost)
    except ValueError:
        print("Niepoprawne dane")
        continue

    if wzrost <= 0:
        print("Wzrost musi być większy od zera")
        continue
    bmi = waga / (wzrost ** 2)
    if bmi <= 18.5:
        print("Niedowaga")
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
    elif 18.5 < bmi <= 24.9:
        print("Waga prawidłowa")
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    elif 25 <= bmi <= 29.9:
        print("Nadwaga")
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
    else:
        print("Otyłość")
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')

    kontynuuj = input("Czy chcesz obliczyć BMI dla kolejnej osoby? (t/n): ").lower()
    if kontynuuj != 't':
        print("Zakończono program.")
        break
