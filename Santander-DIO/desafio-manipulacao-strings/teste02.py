# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

# Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
# Não pode começar ou terminar com "@". ok
# Não pode conter espaços.

# "E-mail válido" se o e-mail estiver no formato correto.
# "E-mail inválido" caso contrário.


if("@" not in email):
    print("E-mail inválido")
elif(email[0]== "@" or email[:]=="@"):
    print("E-mail inválido")
elif(("gmail.com" not in email) and ("outlook.com" not in email)):
    print("E-mail inválido")
else:
    email.strip()
    print("E-mail válido")
    # print(email)


# elif(email not in "@" or email not in "gmail.com" or email not in "outlook.com"):
#     print("E-mail inválido")
# else:
#     print("E-mail Válido")