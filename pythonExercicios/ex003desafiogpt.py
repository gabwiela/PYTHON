'''
Peça ao usuário para inserir seu nome, número de telefone e endereço de email. Use .format() para criar um cartão de visita que exiba essas informações organizadas em diferentes linhas.
'''

nome = input("Digite seu nome e sobrenome: ")
tel = input("Digite seu telefone: ")
email = input("Digite seu email: ")

print("=====DADOS DO USUÁRIO=====")
print("Nome: {}".format(nome))
print("Telefone: {}".format(tel))
print("Email: {}".format(email))
print('==========================')

