def decoder1(encoded):
    text = ""
    text2 = "lulz"
    for i in range(len(encoded)):
        text += chr(ord(encoded[i]) ^ ord(text2[i % len(text2)]) )
    return text

def decoder2(encoded):
    text = ""
    text2 = "this"
    for i in range(len(encoded)):
        text += chr(ord(encoded[i]) ^ ord(text2[i % len(text2)]) )
    return text

def decoder3(encoded):
    text = ""
    text2 = "silly"
    for i in range(len(encoded)):
        text += chr(ord(encoded[i]) ^ ord(text2[i % len(text2)]) )
    return text

def decoder4(encoded):
    text = ""
    text2 = decoder2("\x1b\x05\x0eS\x1d\x1bI\x07\x1c\x01\x1aS\x00\x00\x0cS\x06\x0d\x08\x1fT\x07\x07\x16K")
    for i in range(len(encoded)):
        text += chr(ord(encoded[i]) ^ ord(text2[i % len(text2)]))
    return text


# print(decoder2("\x1b\x05\x0eS\x1d\x1bI\x07\x1c\x01\x1aS\x00\x00\x0cS\x06\x0d\x08\x1fT\x07\x07\x16K"))
# print(decoder1("(\x14\x18Z.\x10\x0d\x19\x03\x1bVpAXAWAXAWAXAWAXAWAXAWAXAWAXAWAXAWAXAp"))
# print(decoder2("\x15\x04X]\x10\x09\x1d]\x10\x09\x1d\x124\x0e\x05\x12\x06\x0dD\x1c\x1aF\n\x1c\x19"))

print(decoder4("\x0b\x0cP\x0e\x0fBA\x06\x0dG\x15I\x1a\x01\x16H\\\x09\x08\x02\x13/\x08\x09^\x1d\x08JO\x07]C\x1b\x05"))
