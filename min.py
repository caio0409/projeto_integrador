print ("Sistema de Sustentabilidade Pessoal")
dig_cor=False
while not dig_cor:
    try:
        data_dia=int(input("Qual o dia?: "))
    except ValueError:
        print("Apenas números inteiros")
        continue
    if data_dia>31 or data_dia<=0:
        print("Digite um dia do mês entre 1 e 31")
    else:
        try:
            data_mes=int(input("Qual o mês?: "))
        except ValueError:
            print("Apenas números")
            continue
        if data_mes>12 or data_mes<=0:
            print("Digite mês entre 1 e 12")
            continue
        if data_dia>29 and data_mes==2:
            print("Esse mês tem 29 dias ou menos")
            continue
        if data_dia>30 and data_mes==4 or data_mes==6 or data_mes==9 or data_mes==11:
            print("Esse mês tem 30 dias ou menos")
            continue
        else:
            try:
                data_ano=int(input("Qual o ano?: "))
            except ValueError:
                print("Apenas números")
                continue
            if data_ano>3000 or data_ano<1900:
                print("Coloque um ano na faixa de 1900 e 3000")
                continue
            if data_dia==29 and data_mes==2 and data_ano%4!=0:
                print("Fevereiro só tem 29 em anos bissextos")
            else:
                        dig_cor=True
data_geral=f"{data_dia}/{data_mes}/{data_ano}"
print("Data:", data_geral)

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
            if resposta<150:
                print("🟢Alta sustentabilidade!")
                Litro_Correto=True
            elif resposta<200:
                print ("🟡 Sustentabilidade Moderada!")
                Litro_Correto=True
            else:
                print ("🔴Baixa Sustentabilidade!")
                Litro_Correto=True


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

print ("PROGRAMA ENCERRADO")
    