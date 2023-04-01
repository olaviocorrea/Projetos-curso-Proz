'''
Desenvolva um programa que recebe do usuário nome completo 
e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do 
usuário e a idade que completou, ou completará, no ano atual
(2022). Caso o usuário não digite um número ou apareça 
um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja
preenchido.
'''
nome = input('Digite seu nome: ')
ano_correto = False
while(ano_correto == False):
    try:
        ano = int(input('Digite o ano de seu nascimento: '))       
        if(ano > 1922 and ano < 2021):
            ano_correto = True
            idade = 2022 - ano
            print('Seu nome é: ', nome)
            print('Sua idade é ', idade, 'anos')
        else:
            print('Erro! Ano informado inválido!')
    except:
        print('Você digitou um caracter inválido!')
print('Código finalizado')


