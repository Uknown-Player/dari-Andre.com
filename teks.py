import random

def zalgo_text(text):
    # Kumpulan karakter Unicode untuk di atas, tengah, dan bawah teks
    up_chars = [
        '\u030d', '\u030e', '\u0304', '\u0305', '\u033f', '\u0311', '\u0306', '\u0310', 
        '\u0352', '\u0357', '\u035b', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', 
        '\u0368', '\u0369', '\u036a', '\u036b', '\u036c', '\u036d', '\u036e', '\u036f', 
        '\u033e', '\u0351', '\u033d'
    ]
    mid_chars = [
        '\u0315', '\u031b', '\u0340', '\u0341', '\u0358', '\u0321', '\u0322', '\u0327', 
        '\u0328', '\u0334', '\u0335', '\u0336', '\u034f', '\u035c', '\u035d', '\u035e', 
        '\u035f', '\u0360', '\u0362', '\u0338', '\u0337', '\u0361', '\u0489'
    ]
    down_chars = [
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031c', '\u031d', '\u031e', '\u031f', 
        '\u0320', '\u0324', '\u0325', '\u0326', '\u0329', '\u032a', '\u032b', '\u032c', 
        '\u032d', '\u032e', '\u032f', '\u0330', '\u0331', '\u0332', '\u0333', '\u0339', 
        '\u033a', '\u033b', '\u033c', '\u0345', '\u0347', '\u0348', '\u0349', '\u034d', 
        '\u034e', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035a'
    ]
    
    zalgo_text = ""
    for char in text:
        zalgo_text += char
        # Tambahkan karakter yang sangat panjang ke atas, tengah, dan bawah
        zalgo_text += ''.join(random.choice(up_chars) * 2 for _ in range(random.randint(3, 5)))
        zalgo_text += ''.join(random.choice(mid_chars) for _ in range(random.randint(2, 4)))
        zalgo_text += ''.join(random.choice(down_chars) * 2 for _ in range(random.randint(3, 5)))
    
    return zalgo_text

# Meminta input dari pengguna
input_text = input("Masukkan teks yang ingin diubah menjadi zalgo text: ")
print(zalgo_text(input_text))
