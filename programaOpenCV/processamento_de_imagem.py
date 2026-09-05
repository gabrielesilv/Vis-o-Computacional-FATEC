import cv2

#CARREGAMENTO DA IMAGEM

imagem_original = cv2.imread("FluorescentCells.jpg")

#Verifica se a imagem foi carregada
if imagem_original is None:
    print("Erro: não foi possível carregar a imagem.")
    exit()

#A imagem atual irá começar como uma cópia da original
imagem_atual = imagem_original.copy()

#MENU PRINCIPAL

while True:

    print("\nPROCESSAMENTO DE IMAGEM")
    print("1 - Mostrar imagem original")
    print("2 - Inverter cores")
    print("3 - Separar canais BGR")
    print("4 - Converter para HSV")
    print("5 - Converter para YCrCb")
    print("6 - Converter para LAB")
    print("7 - Salvar imagem atual")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    #1 - IMAGEM ORIGINAL

    if opcao == "1":
        cv2.imshow("Imagem original", imagem_original)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #2 - INVERTER CORES

    elif opcao == "2":
        imagem_atual = cv2.bitwise_not(imagem_original)

        cv2.imshow("Imagem invertida", imagem_atual)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Imagem invertida criada.")


    #3 - SEPARAR CANAIS BGR

    elif opcao == "3":
        blue, green, red = cv2.split(imagem_original)

        cv2.imshow("Canal Blue", blue)
        cv2.imshow("Canal Green", green)
        cv2.imshow("Canal Red", red)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Canais BGR separados.")


    #4 - BGR PARA HSV

    elif opcao == "4":
        imagem_atual = cv2.cvtColor(imagem_original,cv2.COLOR_BGR2HSV)

        cv2.imshow("Imagem HSV", imagem_atual)

        matiz, saturacao, valor = cv2.split(imagem_atual) #Separando os canais da imagem HSV

        cv2.imshow("imhH.jpg", matiz)
        cv2.imshow("imhS.jpg", saturacao)
        cv2.imshow("imhV.jpg", valor)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Imagem convertida para HSV.")


    #5 - BGR PARA YCrCb

    elif opcao == "5":
        imagem_atual = cv2.cvtColor(imagem_original,cv2.COLOR_BGR2YCrCb)

        cv2.imshow("Imagem YCrCb", imagem_atual)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Imagem convertida para YCrCb.")


    #6 - BGR PARA LAB

    elif opcao == "6":
        imagem_atual = cv2.cvtColor(imagem_original,cv2.COLOR_BGR2LAB)

        cv2.imshow("Imagem LAB", imagem_atual)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Imagem convertida para LAB.")


    #7 - SALVAR IMAGEM ATUAL

    elif opcao == "7":
        while True:
            nome = input("Digite o nome do arquivo para salvar ""(ex: resultado.jpg): ")

            try:
                sucesso = cv2.imwrite(nome, imagem_atual)

                if sucesso:
                    print("Imagem salva com sucesso!")
                    break

                else:
                    print("Erro ao salvar a imagem.")
                    print("Tente novamente.")

            except cv2.error:
                print("Extensão inválida!")
                print("Use .jpg, .jpeg, .png ou .bmp.")
                print("Tente novamente.")

    #0 - SAIR

    elif opcao == "0":

        print("Programa encerrado.")
        break

    #OPÇÃO INVÁLIDA

    else:

        print("Opção inválida. Tente novamente."
        )