import string


def descrypted_message(text, enter_key):
    abc = string.ascii_letters
    s = ""
    enter_key = enter_key % 26
    for i in range(len(text)):
        if text[i].isalpha():
            for letter in range(len(abc)):
                if text[i] == abc[letter]:
                    if (letter - enter_key) < len(abc):
                        j = letter - enter_key
                    else:
                        j = letter - enter_key + len(abc)
                    if text[i].isupper():
                        char = abc[j].upper()
                    else:
                        char = abc[j].lower()
                    s = s + char
                    break
        else:
            s = s + text[i]
    print(s)


key = 1
text = "Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph."
descrypted_message(text, key)
