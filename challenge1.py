f = open('rev_challenge_1.dat_secret.encode','rb')
text = ""
for b in f.read():
    text += chr((ord(b) >> 4 | ord(b) << 4 & 240) ^ 41)
print(text)

text2 = ""
for j in range(0,len(text)-1,2):
    text2 += text[j + 1]
    text2 += text[j]
print(text2)

text3 = ""
for k in range(0,len(text2)-1):
    c = ord(text2[k])
    text3 += chr(c ^ 102)
print(text3)
