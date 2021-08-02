import struct

def decode01(data, key):
    newdata = ''
    for i in range(len(data)):
        newdata += chr(data[i] ^ ord(key[i%len(key)]))
    return newdata

def decode02(data, key):
    newdata = ''
    for i in range(len(data)):
        newdata += chr(ord(data[i]) ^ ord(key[i%len(key)]))
    return newdata

def decode03(data, key):
    newdata = ''
    for i in range(len(data)):
        newdata += chr(ord(data[i]) ^ key)
    return newdata

def decode04(data, key, size):
    newdata = ''
    for i in range(len(data)):
        newdata += chr(ord(data[i]) ^ key[i%size])
    return newdata

f = open('c7shellcode_ori.bin', 'rb')
# f = open('c7shellcode.bin', 'rb')

bytes = f.read()
decoded = ''

# isDebugger1
data = decode01(bytes, 'the final countdown')
# data = decode01(bytes, 'oh happy dayz')

# isDebugger2
# data = decode02(data, 'UNACCEPTABLE!')
data = decode02(data, 'omglob')

# isVM1
# data = decode02(data, 'you\'re so good')
data = decode02(data, 'you\'re so bad')

# isVM2
data = decode02(data, 'f')
# data = decode03(data, 1)

# isDebugger3
# data = decode02(data, 'Sandboxes are fun to play in')
data = decode02(data, 'I\'m gonna sandbox your face')

# isDebugger4
# data = decode02(data, 'I can haz decode?')

# isDebugger5
# data = decode02(data, 'Feel the sting of the Monarch!')
data = decode04(data, [9,0,0,1], 4)
data = decode02(data, "Such fire. Much burn. Wow.")

# isFriday
data = decode02(data, '! 50 1337') # friday
# data = decode02(data, '1337') # not friday

# isBackdoge.exe
# data = decode02(data, 'LETS GO SHOPPING')
data = decode02(data, 'MATH IS HARD')

# isInternet1
# data = decode02(data, 'LETS GO MATH') # no
data = decode02(data, 'SHOPPING IS HARD') # yes

# is5pm
# data = decode04(data, [7,0x77], 2) # no
data = decode04(data, [1,2,3,5,0,0x78,0x30,0x38,0x0D], 9) # yes

# xor backdoge.exe
# data = decode02(data, 'E:\\Projects\\')
data = decode02(data, 'backdoge.exe')

# e.root-server.net
data = decode02(data, '192.203.230.10')

# jackRAT
data = decode02(data, 'jackRAT')

# for i in range(len(data)):
    # print('%02X %d' % (ord(data[i]), ord(data[i])))

o = open('gratz.exe', 'wb')
# for i in range(0,30):
for i in range(len(data)):
    o.write(struct.pack('B', ord(data[i])))
o.close()
