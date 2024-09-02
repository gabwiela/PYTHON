#Faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input("Digite alguma coisa: ")
print("O tipo primitivo dele é ",type(palavra))
print("Ele tem alfa numérico?", palavra.isalnum()) #alfanumerico
print("Ele usa letra maiuscula? ", palavra.isupper()) #letras maiusculas
print("Tem letras?", palavra.isalpha()) #letras
print("É um número?", palavra.isnumeric()) #numeros
print("Ele é um caractere ASCII?", palavra.isascii()) #ASCII
print("Ele tem decimal?", palavra.isdecimal()) #decimal
print("Ele tem digitos?", palavra.isdigit()) #digitos
print("Ele é um identificador válido?", palavra.isidentifier()) #identificador valido
print("Ele ta em maiusculo?", palavra.islower()) #letras minusculas
print("Ele é imprimivel?", palavra.isprintable()) #imprimiveis
print("Tem espaços em branco?", palavra.isspace()) #espaços em brancos
print("Ele começa com a letra maiuscula?", palavra.istitle()) #Se cada palavra começa com letra maiuscula