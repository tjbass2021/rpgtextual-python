"""
Este é um RPG textual feito para rodar inteiramente no terminal. Sua construção se deu com a finalidade de apenas desenvolver um jogo com certo nível de complexidade e abstração mas sem conter nenhum artifício gráfico.
"""
from curses.ascii import isalpha


dadosjogador = []
print("Olá, aventureiro! Bem-vindo a este mundo de possibilidades!")

nome = ''

while not nome:
    n = input('Digite o nome do seu personagem: ')
    if n.isalpha():
        nome = n
        dadosjogador.append(nome)

    else:
        print('Digite um nome válido')
        nome = ''

print(f'Seja bem vindo a este mundo incrível {dadosjogador[0]}!')

