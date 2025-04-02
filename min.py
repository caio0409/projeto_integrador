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
            else:
                if Porcent>20 or Porcent<50:
                    print ("Moderada sustentabilidade!")
                else:
                    if Porcent<20:
                        print ("Baixa Sustentabilidade!")
                    else:
                        Porcent_correta=True