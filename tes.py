import sys
from time import sleep

def print_lyrics():
    lines = [
        ("haloo cantikk", 0.10),
        ("jaga kesehatan yaa", 0.09),
        ("jangan begadang teruss, nanti lama sembuhnyaa", 0.06),
        ("trus, makan yang teratur yaa", 0.08),
        ("jangann main hp muluu", 0.06),
        ("jangan lupa juga minum air", 0.08),
        ("Stay Healthy yaa cantikk", 0.08),
        ("Dari Andre, untuk kamuu", 0.10)
    ]
    delays = [3, 0.5, 1.3, 0.5, 1.5, 1.5, 2, 3.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

# Input password
password = input("Masukkan password nya dong cantikk => ")

if password == "mantap":
    print_lyrics()
    /menampilkan gambar cantik.jpg
else:
    print("minta password dlu sana")
