"""Projeto_08_Curso_Proz

Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)"""

for i in range(1,21,1):
  if (i == 13):
    continue
  print("Andar", i)

"""Contando em ordem decrescente:"""

for i in range(20,0,-1):
  if (i == 13):
    continue
  print("Andar", i)

"""Usando o laço while"""

i = 1
while (i < 20):
  if (i == 13):
    i = i + 1
    continue
  print("Andar:", i)
  i = i + 1

"""imprimindo em ordem decrescente com while:"""

i = 20
while (i > 0):
  if (i == 13):
    i = i - 1
    continue
  print("Andar:", i)
  i = i - 1