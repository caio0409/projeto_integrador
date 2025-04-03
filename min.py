KG_correto=False
while not KG_correto:
    try:
        KG=float(input("Quantos KG de resíduos não recicláveis você gerou hoje? "))
    except ValueError:
        print ("Digite um número!")
    else:
        if KG<0: 
            print ("O valor deve ser maior que zero!")
        else:
            KG_correto=True

Porcent_correta=False
while not Porcent_correta:
    try:
        Porcent=int(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
    except ValueError:
        print ("Digite um número!")
    else:
        if Porcent<0 or Porcent>100:
            print ("A porcentagem deve ser de 0 a 100%!")
        else:
            if Porcent>50:
                print ("Alta sustentabilidade!")
                Porcent_correta=True
            else:
                if Porcent>20:
                    print ("Moderada sustentabilidade!")
                    Porcent_correta=True
                else:
                    print ("Baixa Sustentabilidade!")
                    Porcent_correta=True

print ("\n1. Transporte público \n2. Bicileta \n3. Caminhada \n4. Carro (com gasolina) \n5. Carro elétrico \n6.Carona Compartilhada \n")
Mtransporte_correto=False
while not Mtransporte_correto:
    try:
        MeioTransporte=int(input("Qual meio de transporte você utilizou hoje? "))
    except ValueError:
        print ("Digite um número!")
    else:
        if MeioTransporte<1 or MeioTransporte>9:
            print ("Escolha um meio de transporte de 1 a 9!")
        else:
            if MeioTransporte==5 or MeioTransporte==2 or MeioTransporte==3:
                print ("Alta Sustentabilidade!")
                Mtransporte_correto=True
            elif MeioTransporte==6 or MeioTransporte==1:
                print ("Moderada sustentabilidade!")
                Mtransporte_correto=True
            else:
                print ("Baixa Sustentabilidade!")
                Mtransporte_correto=True