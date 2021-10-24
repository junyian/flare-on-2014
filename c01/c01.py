# Written with Python 3.10.0
with open('rev_challenge_1.dat_secret.encode','rb') as file:
    text = ''
    for b in file.read():
        text += chr((b >> 4 | b << 4 & 240) ^ 41)
    print(text)
