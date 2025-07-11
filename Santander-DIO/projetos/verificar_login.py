# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

if (usuario in usuarios) and senha == usuarios[usuario]:
    print('Acesso permitido')
else:
    print('Usuário ou senha incorretos')