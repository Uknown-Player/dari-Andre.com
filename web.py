import sys
import os
from time import sleep
from colorama import Fore, Style, init

# Inisialisasi colorama
init()

def print_lyrics():
    lines = [
        ("Know you're all that I want... This life", 0.10),
        ("I'll imagine we fell in love", 0.09),
        ("I'll nap under moonlight skies with you", 0.06),
        ("I think I'll picture us, you with the waves", 0.08),
        ("the oceans colors on your face", 0.06),
        ("I leave heart with you air", 0.08),
        ("so let me fly with you", 0.08),
        ("will you be.. for ever with me?~..", 0.10)
    ]
    delays = [3, 0.5, 1.3, 0.5, 1.5, 1.5, 2, 3.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            # Menampilkan teks dengan warna merah
            print(Fore.RED + char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        # Reset warna setelah setiap baris
        print(Style.RESET_ALL)

# Memanggil fungsi
print_lyrics()
