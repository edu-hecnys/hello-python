print("hello world")


def frågesport():
    frågor = [
        {
            "fråga": "Vad heter Sveriges huvudstad?",
            "alternativ": ["A. Göteborg", "B. Stockholm", "C. Malmö"],
            "svar": "B"
        },
        {
            "fråga": "Hur många ben har en spindel?",
            "alternativ": ["A. 6", "B. 8", "C. 10"],
            "svar": "B"
        },
        {
            "fråga": "Vad är 5 + 7?",
            "alternativ": ["A. 10", "B. 11", "C. 12"],
            "svar": "C"
        },
        {
            "fråga": "Vilken planet kallas den röda planeten?",
            "alternativ": ["A. Mars", "B. Venus", "C. Jupiter"],
            "svar": "A"
        },
        {
            "fråga": "Vilket djur säger 'mjau'?",
            "alternativ": ["A. Hunden", "B. Katten", "C. Hästen"],
            "svar": "B"
        }
    ]

    poäng = 0

    print("🎉 Välkommen till frågesporten!")
    print("Svara med A, B eller C.\n")

    for nummer, fråga in enumerate(frågor, start=1):
        print(f"Fråga {nummer}: {fråga['fråga']}")

        for alternativ in fråga["alternativ"]:
            print(alternativ)

        svar = input("Ditt svar: ").strip().upper()

        if svar == fråga["svar"]:
            print("Rätt svar! ✅\n")
            poäng += 1
        else:
            print(
                f"Fel svar! ❌ "
                f"Rätt svar var {fråga['svar']}.\n"
            )

    print("🏁 Frågesporten är slut!")
    print(f"Du fick {poäng} av {len(frågor)} poäng.")

    if poäng == len(frågor):
        print("Fantastiskt! Du fick alla rätt! 🌟")
    elif poäng >= 3:
        print("Bra jobbat! 👏")
    else:
        print("Försök igen – du klarar det! 💪")


frågesport()