txt_dig = input("Digite uma frase ou palavra: ")
###Texto digitado pelo User

resultado = 0
###Número de A's

for char in txt_dig:
    if char == "a" or char == "A":
        resultado += 1
###Verifica se tem "A" na frase/palavra e soma a variavel "resultado"

if resultado > 0:
    print(f'Em "{txt_dig}", a letra A aparece {resultado} vezes ')
else:
    print(f'Em {txt_dig}, não existe a letra A')