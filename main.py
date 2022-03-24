from random import choice

n1 = str(input('Primeiro: '));
n2 = str(input('Segundo: '));
n3 = str(input('Terceiro: '));
n4 = str(input('Quarto: '));
n5 = str(input('Quinto: '));

Lista = [n1, n2, n3, n4, n5]

Escolhido = choice(Lista)

print('O escolhido foi: {}'.format(Escolhido));