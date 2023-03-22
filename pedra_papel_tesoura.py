import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolha = [pedra, papel, tesoura]


escolha_jogador = int(input(
    "Qual você escolhe? \n0- pedra, 1- papel, 2- tesoura:\n"))
while escolha_jogador > 2:
    if escolha_jogador > 2 or escolha_jogador < 0:
        print("Você escolheu um número inválido. Tente novamente!\n")
        escolha_jogador = int(input("Escolha entre: 0- pedra, 1- papel, 2- tesoura:\n"))
print(escolha[escolha_jogador])

escolha_computer = random.randint(0, 2)
print("Escolha do computador:\n")
print(escolha[escolha_computer])


if escolha_jogador == escolha_computer:
    print("Empate!")
elif escolha_jogador == 2 and escolha_computer == 0:
    print("Você Perdeu!")
elif escolha_jogador == 0 and escolha_computer == 2:
    print("Você Ganhou!")
elif escolha_jogador > escolha_computer:
    print("Você Ganhou!")
elif escolha_jogador < escolha_computer:
    print("Você Perdeu!")




