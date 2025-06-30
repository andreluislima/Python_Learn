
# ARGS
    ## Use *args quando não sabe QUANTOS argumentos posicionais serão passados.
def somar_todos(*args):
    return sum(args)

print(somar_todos(1,10,12,398,0))
#  Recebe todos os valores extras como uma tupla. A função sum() soma esses valores.


# KWARGS
    ## Use **kwargs quando não sabe QUAIS argumentos nomeados serão passados.
def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}:{valor}')

mostrar_dados(nome = "Ana", idade = "32", Funcao = "Analista Financeira", dataNascimento = "1991-02-15")
# Recebe os dados como um dicionário. É útil quando os parâmetros nomeados podem variar.


# COMBINANDO ARGS E KWARGS
def cadastrar_usuario(*param_args, **param_kwagrs):
    print("Dados posicionais: ", param_args)
    print("Dados posicionais: ", param_kwagrs)

cadastrar_usuario("Admin", "funcao", "ativo", nome="João", email = "jao@gmail.com")
