# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

# READ
arquivo = open("lorem.txt", "r")
print(arquivo.read())
arquivo.close()


# READLINE
arquivo = open("lorem.txt", "r")
print(arquivo.readline())
arquivo.close()


# READLINES
arquivo = open("lorem.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()


# # tip
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()
