#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input("Qual o seu salário: "))

cal = sal * 0.15
salcal = sal + cal

print("Seu salário antes era de {} reais mas com o aumento de 13% fica {} reais".format(sal,salcal))