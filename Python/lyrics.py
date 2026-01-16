import time
import sys

def print_lyrics():
    lyrics = [
        "Tere dil pe haq mera hai...",
        "Tu sanam beshaq mera hai.....",
        "Phir lakeerein hon ya na ho....",
        "Tu mera hai tu mera hai...",

        "Jo tu aag hai...........",
        "Haan to phir mujhe.......",
        "Jalne ka shauk hai........",
        "Jalne ka shauk hai.........",
        "Marne se kahin.............",
        "Jyada haan tujhe............",
        "Khone ka khauf hai...........",
        "Khone ka khauf hai..........",

    ]

    delays = [1.2, 1.8, 1.8, 2.0, 1.3, 2.0, 1.0]

    print("Deewaniyat:\n")
    time.sleep(1.4)

    delays = [1.2, 1.8, 1.8, 2.0, 1.3, 2.0, 1.0]

    print("Deewaniyat:\n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.11)
        print()
        time.sleep(delays[i])

print_lyrics()