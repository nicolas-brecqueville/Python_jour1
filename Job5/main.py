letterAscii = ord("a")
alphabet = ""

while letterAscii != 123: #123 est le code ASCII du caractère z
    alphabet += chr(letterAscii)
    letterAscii += 1

print(alphabet[::-1])