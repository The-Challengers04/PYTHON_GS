
#Definindo a função de compra do produto
def compra():
    #Definindo as variáveis como global, para análise posterior
    global nome
    global cep_endereço
    global rua_endereço
    global motivacao
    global pessoas
    global projetos
    global tel_contato
    
    #Coletando dados iniciais do cliente
    print('-'*60)
    nome = input("Digite seu nome: ")
    print(f"Seja bem vindo(a) {nome}! Estamos muito felizes de te termos aqui! \nO projeto SmartGrow consiste no desenvolvimento de um sistema de agricultura vertical inteligente que visa maximizar o uso do espaço urbano. \n Para começar, precisamos dealgumas informações sobre sua comunidade")
    
    #Validando variável com try e except
    while True:    
        try: 
            cep_endereço = int(input("Digite seu CEP: "))
            break
        except:
            print('Digite apenas números!')

    #Coleta de dados
    rua_endereço = input('Digite o nome da sua rua: ')
    motivacao = input('Qual é a motivação da sua comunidade para entrar na missão SmartGrow? ')

    #Validando variável com try e except
    while True:
        try:
            pessoas = int(input('Quantas pessoas da sua comunidade estarão envolvidas no projeto? '))
            break
        except:
            print('Digite apenas números!')
    
    #Coleta de dados
    projetos = input('Sua comunidade já fez parte de algum projeto em grupo? O que era? E como ocorreu? ')
    print(f'Obrigado(a) {nome}. Suas informações serão analisadas pela nossa equipe.')
    tel_contato = int(input('Deixe aqui um telefone para contato para que possamos marcar uma visita a sua comunidade: '))
    print('')

#Definindo função 'sobre' para informações do projeto Smartgrow
def sobre():
    #Informações sobre o projeto
    print('-'*60)
    print(' O projeto Smartgrow propõe a utilização de estruturas modulares de agricultura vertical inteligente, que permitem o cultivo de alimentos de forma vertical em espaços urbanos, como telhados de prédios residenciais. \n Cada módulo é equipado com tecnologia inteligente, como sensores, iluminação artificial e controle de temperatura, para otimizar o crescimento das plantas. \n Essa abordagem inovadora permite o cultivo de uma quantidade significativa de alimentos em uma área reduzida, maximizando o uso do espaço disponível. ')
    print('')

#Definindo a função 'simulacao' em que o usuário poderá testar os alimentos ideais para plantio
def simulacao():
    print('-'*60)
    print('Aqui você poderá testar quais alimentos são ideais para o plantio na sua casa!')
    print('')
    print('Para isso iremos coletar algumas informações, como por exemplo o ph do solo.')

    #Validando variável com try e except e limitando o usuário na escala da ph (0-14)
    while True:
        try:
            ph = float(input('Ph do solo (0-14): '))
            if ph >= 0.0 and ph <= 14.0:
                break
            else:
                print('Digite um valor válido!')
        except ValueError:
            print('Digite apenas números (7, 8.5, 4.6, etc)')

    #Validando variável com try e except
    while True:
        try:
            nivelDeIluminacao = int(input('Nível de iluminação:\n1- Luz solar\n2- Luz solar indireta\n3- Luz de sombra parcial\n4- Luz de sombra\n'))
            match nivelDeIluminacao:  
                case 1:  
                    break
                case 2:  
                    break 
                case 3:  
                    break
                case 4:  
                    break  
                case other: 
                    print('Digite uma opção válida') 
        except ValueError:
            print('Digite apenas números')

    #Validando variável com try e except limitando o usuário a colocar valores altos ou baixos demais
    while True:
        try:
            tempMedia = int(input('Temperatura média durante o dia: '))
            if tempMedia >= -25 and tempMedia <= 40:
                break
            else:
                print('O valor digitado é alto ou baixo demais.')
        except ValueError:
            print('Digite apenas números!')

    #Definindo a lista de plantas ideais
    podeSerPlantado = []

    #Validando informações obitidas anteriormente, testando o ph, nível de iluminação e temperatura média do dia para cada planta abaixo
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 18 and tempMedia <= 24:
        podeSerPlantado.append('- Ervas: manjericão, salsa, cebolinha, hortelã, coentro e tomilho')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 2 or nivelDeIluminacao == 3 and tempMedia >= 15 and tempMedia <= 25:
        podeSerPlantado.append('- Saladas verdes: Alface, rúcula, espinafre, agrião')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 21 and tempMedia <= 27:
        podeSerPlantado.append('- Tomates cereja')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 20 and tempMedia <= 30:
        podeSerPlantado.append('- Pimentões')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 24 and tempMedia <= 32:
        podeSerPlantado.append('- Pepinos')
    if ph >= 5.5 and ph <= 6.5 and nivelDeIluminacao == 1 and tempMedia >= 15 and tempMedia <= 25:
        podeSerPlantado.append('- Morangos')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 15 and tempMedia <= 25:
        podeSerPlantado.append('- Ervilhas e feijões')
    if ph >= 6.0 and ph <= 7.0 and nivelDeIluminacao == 1 and tempMedia >= 18 and tempMedia <= 24:
        podeSerPlantado.append('- Ervas aromáticas: alecrim, orégano, sálvia e lavanda')

    #Imprimindo as plantas armazenadas utilizando for in, caso não seja validado nada será apresentado formas do usuário poder plantar algo
    if podeSerPlantado:
        print('-'*60)
        print('Pode ser plantado os seguintes itens:')
        for plantado in podeSerPlantado:
            print(plantado)
    else:
        print('Infelizmente você não pode plantar nada')
        print('Para resolver essa situação você pode:')
        print('- Tentar deixar o Ph do solo neutro, por volta de 6-7 ou deixar um pouco mais ácido no caso do morango')
        print('- Deixar o ambiente com luz direta ao sol, a maioria das plantas crescem em um ambiente com luz solar direta')
        print('- Buscar deixar o ambiente em uma temperatura mais agradável, em uma média de 18-25 °C')
        print('Nosso produto ajuda no controle desses fatores, para adiquirir-lo, vá para página de "Adiquirir produto"')
    print('')      

#Definindo a função main, em que o usuário irá selecionar a opção desejada
def main():
    
    #Validando a escolha com try e except 
    while True:
        try:
            print('----------- MENU -----------')
            print('Bem vindo ao Smartgrow!')
            menu = int(input('O que você deseja fazer hoje:\n1- Adiquirir produto\n2- Sobre\n3- Simulação\n4- sair\n')) 
            match menu:  
                case 1:  
                   compra() 
                case 2:  
                    sobre()
                case 3:  
                   simulacao()
                case 4:  
                    break  
                case other: 
                    print('Digite uma opção válida') 
        except ValueError:
            print('Opção inválida')

#executando a função main
main()
