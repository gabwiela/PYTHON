#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

larg = int(input("Qual a largura em metros da parede? "))
alt = int(input("E a altura? "))

a = alt * larg
litro = a * 2**2

print("A quantidade de tinta necessária para pintar a parede é de {} litros".format(litro))
