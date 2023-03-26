"""
Faça uma função calculadora que os números e as operações 
serão feitas pelo usuário. O código deve ficar rodando
infinitamente até que o usuário escolha a opção de sair.
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário
introduza qualquer outro, o sistema deve mostrar a mensagem
“Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o
primeiro e segundo valor, um de cada. Depois precisa executar a 
operação e mostrar o resultado na tela. Quando o usuário escolher 
a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar 
uma operação e mostrar o resultado. 
"""

def calcular(num1,num2,oper):
  try:
    if(oper == 1):
      return num1 + num2        
    elif(oper == 2):
      return num1 - num2       
    elif(oper == 3):
      return num1 * num2        
    elif(oper == 4):
      return num1 / num2        
    else:
      return 0
  except:
    print("Erro! Escolha números inteiros para o cálculo")


continuar = True
while continuar == True:
    oper = int(input("Digite 0 para sair ou escolha uma das opções de cálculo: \n 1: Soma \n 2: Subtração \n 3: Mulplicação \n 4: Divisão \n "))
    if oper == 0:
      continuar = False
    elif oper > 4 or oper < 0:
      print("escolha uma opção válida")
    else:
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))   
      resultado = calcular(num1,num2,oper)
      print("O resultado do cálculo é:",resultado)