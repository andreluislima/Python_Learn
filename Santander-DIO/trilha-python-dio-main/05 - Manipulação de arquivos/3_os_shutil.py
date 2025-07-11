import os
import shutil
from pathlib import Path

print(__file__)
ROOT_PATH = Path(__file__).parent


# CRIANDO A PASTA com o divisor '/' correto.
# os.mkdir(ROOT_PATH / "novo-diretorio-andre") 

# CRIANDO O ARQUIVO
# arquivo = open(ROOT_PATH / "teste_simples_2.txt", "w")
# arquivo.close()

# CRIANDO O ARQUIVO dentro da pasta 'novo-diretorio-andre'
# arquivo = open(ROOT_PATH / "novo-diretorio-andre"/ "teste4", "w")
# arquivo.close()

# RENOMEANDO
# os.rename(ROOT_PATH / "teste_andre.txt", ROOT_PATH / "alterado_andre.txt")


# REMOVENDO
# os.remove(ROOT_PATH / "teste.txt")

# MOVENDO

shutil.move(ROOT_PATH /"teste_simples_2.txt", ROOT_PATH / "novo-diretorio-andre"/"teste_simples_2.txt")
# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
