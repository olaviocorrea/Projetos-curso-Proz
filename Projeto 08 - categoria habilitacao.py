""" Desenvolva um código que utilize as seguintes características de um veículo:
 Quantidade de rodas;
 Peso bruto em quilogramas;
 Quantidade de pessoas no veículo.

 Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
 A: Veículos com duas ou três rodas;
 B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
 C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
 D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
"""

rodas = 4
peso = 4000
passageiros = 5

if(rodas <= 3):
    print("Categoria A")
elif(rodas == 4 and peso <= 3500 and passageiros <= 8):
    print("Categoria B")
elif(peso > 3500 and peso < 6000):
    print("Categoria C")
else:
    print("Categoria D")