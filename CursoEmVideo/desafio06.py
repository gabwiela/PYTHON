#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input("Mande um número: "))

m2 = n * 2
m3 = n * 3
r = n ** (1/2)

print("O dobro do número {} é {}, o triplo é {} e a raiz quadrada é de {}".format(n,m2,m3,r))