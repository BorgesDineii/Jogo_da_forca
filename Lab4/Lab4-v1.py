# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

def limpar_tela():
     # windows
     if name == 'nt':
          _= system('cls')
     # Mac ou linux
     else:
          _= system('clear')
# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []
     
     def guess(self, letra):
          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          return True

     def hagman_over(self):
          return self.hangman_won() or (len(self.letras_erradas) == 6)

     def hangman_won(self):
          if '_' not in self .hide_palavra():
               return True
          return False

     def hide_palavra(self):
          rtn = ''
          for letra in self.palavra:
               if letra not in self.letras_escolhidas:
                    rtn += '_'
               else:
                    rtn += letra
          return rtn

     def print_game_status(self):
          print (board[len(self.letras_erradas)])
          print('\nPalavra: ' + self.hide_palavra())
          print('\nLetras erradas: ',)
          for letra in self.letras_erradas:
               print(letra,)
          print()
          print('Letras corretas: ',)

          for letra in self.letras_escolhidas:
               print(letra,)
          print()
     
def rand_palavra():
     palavras = ['banana', 'melancia', 'abacate', 'morango']
     palavra = random.choice(palavras)
     return palavra

def main():
     limpar_tela()
     game = Hangman(rand_palavra())

     while not game.hagman_over():
          game.print_game_status()
          user_input = input('\nDigite uma letra: ')
          game.guess(user_input)
     game.print_game_status()

     if game.hangman_won():
          print('\nParabens paizao! Tu venceu!!')
     else:
          print('\nAi não bro, tu perdeu!')
          print('A palavra era ' + game.palavra)
     print('\nFoi bom jogar com você! Volte sempre!\n')

if __name__ == "__main__":
     main()
