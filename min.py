Kwh_correto=False
while not Kwh_correto:
    try:
        KWH=float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
    except ValueError:
        print ("Digite um número!")
    else:
        if KWH<0: 
            print ("O valor deve ser maior que zero!")
        elif KWH<5:
            print ("🟢 Alta sustentabilidade!")
            Kwh_correto=True
        elif KWH<10:
            print ("🟡 Moderada sustentabilidade!")
            Kwh_correto=True
        else:
            print ("🔴 Baixa Sustentabilidade!")
            Kwh_correto=True

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
        elif Porcent>50:
            print ("🟢 Alta sustentabilidade!")
            Porcent_correta=True
        elif Porcent>20:
            print ("🟡 Moderada sustentabilidade!")
            Porcent_correta=True
        else:
            print ("🔴 Baixa Sustentabilidade!")
            Porcent_correta=True

print ("\n1. Transporte público 🚌 \n2. Bicileta 🚲 \n3. Caminhada 🚶 \n4. Carro (com gasolina) 🚗 \n5. Carro elétrico 💡 \n6. Carona Compartilhada 👥 \n")
Mtransporte_correto=False
while not Mtransporte_correto:
    try:
        MeioTransporte=int(input("Qual meio de transporte você utilizou hoje? "))
    except ValueError:
        print ("Digite um número!")
    else:
        if MeioTransporte<1 or MeioTransporte>6:
            print ("Escolha um meio de transporte de 1 a 6!")
        elif MeioTransporte==5 or MeioTransporte==2 or MeioTransporte==3:
            print ("🟢 Alta sustentabilidade!")
            Mtransporte_correto=True
        elif MeioTransporte==6 or MeioTransporte==1:
            print ("🟡 Moderada sustentabilidade!")
            Mtransporte_correto=True
        else:
            print ("🔴 Baixa Sustentabilidade!")
            Mtransporte_correto=True

Litro_Correto=False
while not Litro_Correto:
    try:
        resposta=int(input("Quantos litros foram consumidos hoje? "))
    except ValueError:
        print("o valor inserido é invalido")
    else:
        if resposta<0:
            print("o valor inserido é invalido")
        else:
            Litro_Correto=True
            if resposta<150:
                print("🟢Alta sustentabilidade!")
            elif resposta<200:
                print ("🟡 Sustentabilidade Moderada!")
            elif resposta>200:
                print ("🔴Baixa Sustentabilidade!")
            elif resposta==200:
                print("Sustentabilidade Moderada!")

print ("PROGRAMA ENCERRADO")
    