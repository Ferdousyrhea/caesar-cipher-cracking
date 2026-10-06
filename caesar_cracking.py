text = "Hwduytlwfusn nx kzs yt qjfws!"

for key in range(26):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            ci = ((ord(char) - 65 - key) % 26) + 65
            result += chr(ci)

        elif char.islower():
            ci = ((ord(char) - 97 - key) % 26) + 97
            result += chr(ci)

        else:
            result += char

    print("Key =", key, ":", result)