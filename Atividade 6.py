# coding: utf-8
user = raw_input("Nome de usuario: ")
senha = raw_input("Senha: ")

while (senha == user):
    senha = raw_input("Digite uma senha diferente do nome de usuário: ")

print ("Usuário: %s | Senha: %s" % (user, senha))
