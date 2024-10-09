def inverte_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Digite uma string: ")
print(f"String invertida: {inverte_string(string)}")
