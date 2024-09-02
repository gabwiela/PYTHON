'''Peça as notas de três provas'''

nota1 = float(input("Nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 2

mensagem = "Sua média é de {}".format(media)
print("======BOLETIM DE NOTAS =======")
print("AV1: {}".format(nota1))
print("AV2: {}".format(nota2))
print("AV3: {}".format(nota3))

mensagem = "Sua média nesta matéria é de {}".format(media)
print(mensagem)