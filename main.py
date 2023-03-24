#Calculador com Menu

opção = 0
while(opção!=5):
    print("Calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opção = int(input("Escolha a opção adequada: "))
    if (opção==1):
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        soma = numero1 + numero2
        print ("Soma: ", soma)
    elif(opção==2):
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        subtração = numero1 - numero2
        print("Subtração: ", subtração)
    elif(opção==3):
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        multiplicação = numero1 * numero2
        print("Multiplicação: ", multiplicação)
    elif(opção==4):
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        divisão = numero1 / numero2
        print("Divisão: ", divisão)
    elif(opção==5):
         print("Programa Encerrado")
    else:
        print("Opção inválida")