
def compra():
    nome = input("Digite seu nome: ")
    print(f" Seja bem vindo(a) {nome}! Estamos muito felizes de te termos aqui! \n O projeto SmartGrow consiste no desenvolvimento de um sistema de agricultura vertical inteligente que visa maximizar o uso do espaço urbano. \n Para começar, precisamos dealgumas informações sobre sua comunidade")
    cep_endereço = input("Digite seu CEP: ")
    rua_endereço = input("Digite o nome da sua rua: ")
    motivacao = input("Qual é a motivação da sua comunidade para entrar na missão SmartGrow?")
    pessoas = input("Quantas pessoas da sua comunidade estarão envolvidas no projeto?")
    projetos = input("Sua comunidade já fez parte de algum projeto em grupo? O que era? E como ocorreu?")
    print(f'Obrigado(a) {nome}. Suas informações serão analisadas pela nossa equipe.')
    tel_contato = input('Deixe aqui um telefone para contato para que possamos marcar uma visita a sua comunidade.')


    
    

def sobre():
    print("O projeto Smartgrow propõe a utilização de estruturas modulares de agricultura vertical inteligente, que permitem o cultivo de alimentos de forma vertical em espaços urbanos, como telhados de prédios residenciais. \n Cada módulo é equipado com tecnologia inteligente, como sensores, iluminação artificial e controle de temperatura, para otimizar o crescimento das plantas. \n Essa abordagem inovadora permite o cultivo de uma quantidade significativa de alimentos em uma área reduzida, maximizando o uso do espaço disponível. ")
    

def simulacao():
    print("-"*60)
    print('Aqui você poderá testar quais alimentos são ideais para o plantio na sua casa!')
    print("")
    print('Para isso iremos coletar algumas informações, como por exemplo o ph do solo.')
    while True:
        try:
            ph = float(input('Ph do solo (0-14): '))
            if ph >= 0 and ph <= 14:
                break
            else:
                print('Digite um valor válido!')
        except ValueError:
            print('Digite apenas números!')
    while True:
        try:
            nivelDeIluminacao = int(input('Nível de iluminação:\n1- Luz solar\n2- Luz solar indireta\n3- Luz de sombra parcial\n4- Luz de sombra\n'))  # Solicita ao usuário a opção desejada no menu
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
    while True:
        try:
            tempMedia = int(input('Temperatura média durante o dia: '))
            if tempMedia >= -30 and tempMedia <= 40:
                break
            else:
                print('O valor digitado é alto ou baixo demais.')
        except ValueError:
            print('Digite apenas números!')

    podeSerPlantado = []

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

    if podeSerPlantado:
        print('-'*60)
        print('Pode ser plantado os seguintes itens:')
        for plantado in podeSerPlantado:
            print(plantado)
    else:
        print('Infelizmente você não pode plantar nada')
          

def main():
    while True:
        try:
            print('----- MENU -----')
            menu = int(input('O que você deseja fazer hoje:\n1- Adiquirir produto\n2- Sobre\n3- Simulação\n4- sair\n'))  # Solicita ao usuário a opção desejada no menu
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

main()