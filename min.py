Litro_Correto=False
while not Litro_Correto:
    try:
        resposta=int(input("Quantos litros de água foram consumidos hoje? "))
    except ValueError:
        print("o valor inserido é invalido")
    else:
        if resposta<0:
            print("o valor inserido é invalido")
        else:
            Litro_Correto=True
            if resposta<150:
                print("Alta sustentabilidade!")
            elif resposta<200:
                print ("Sustentabilidade Moderada!")
            elif resposta>200:
                print ("Baixa Sustentabilidade!")
            elif resposta==200:
                print("Sustentabilidade Moderada!")

