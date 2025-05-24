import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",      
        user="root",          
        password="120821",        
        database="BD_PI_Teste"     
    )
    cursor = conexao.cursor(dictionary=True)
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    exit()

def incluir_registro():
    nome = input("Digite seu nome completo: ").strip()

    dig_cor = False
    while not dig_cor:
        try:
            data_dia = int(input("Qual o dia?: "))
        except ValueError:
            print("Apenas números inteiros")
            continue
        if data_dia > 31 or data_dia <= 0:
            print("Digite um dia do mês entre 1 e 31")
        else:
            try:
                data_mes = int(input("Qual o mês?: "))
            except ValueError:
                print("Apenas números")
                continue
            if data_mes > 12 or data_mes <= 0:
                print("Digite mês entre 1 e 12")
                continue
            if data_dia > 29 and data_mes == 2:
                print("Esse mês tem 29 dias ou menos")
                continue
            if data_dia > 30 and data_mes in [4, 6, 9, 11]:
                print("Esse mês tem 30 dias ou menos")
                continue
            else:
                try:
                    data_ano = int(input("Qual o ano?: "))
                except ValueError:
                    print("Apenas números")
                    continue
                if data_ano > 3000 or data_ano < 1900:
                    print("Coloque um ano entre 1900 e 3000")
                    continue
                if data_dia == 29 and data_mes == 2 and data_ano % 4 != 0:
                    print("Fevereiro só tem 29 dias em anos bissextos")
                else:
                    dig_cor = True

    data_geral = f"{data_ano}-{data_mes:02}-{data_dia:02}" 

    while True:
        try:
            resposta = float(input("Quantos litros foram consumidos hoje? "))
            if resposta < 0:
                raise ValueError
            if resposta < 150:
                print("🟢 Alta sustentabilidade!")
            elif resposta < 200:
                print("🟡 Sustentabilidade Moderada!")
            else:
                print("🔴 Baixa Sustentabilidade!")
            break
        except ValueError:
            print("Valor inválido. Digite um número positivo.")

    while True:
        try:
            KWH = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
            if KWH < 0:
                raise ValueError
            if KWH < 5:
                print("🟢 Alta sustentabilidade!")
            elif KWH < 10:
                print("🟡 Moderada sustentabilidade!")
            else:
                print("🔴 Baixa Sustentabilidade!")
            break
        except ValueError:
            print("Digite um número positivo!")

    while True:
        try:
            KG = float(input("Quantos KG de resíduos não recicláveis você gerou hoje? "))
            if KG < 0:
                raise ValueError
            break
        except ValueError:
            print("Digite um número válido!")

    while True:
        try:
            Porcent = int(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
            if Porcent < 0 or Porcent > 100:
                raise ValueError
            if Porcent > 50:
                print("🟢 Alta sustentabilidade!")
            elif Porcent > 20:
                print("🟡 Moderada sustentabilidade!")
            else:
                print("🔴 Baixa Sustentabilidade!")
            break
        except ValueError:
            print("Digite um número entre 0 e 100!")

    print("\n1. Transporte público 🚌 \n2. Bicicleta 🚲 \n3. Caminhada 🚶 \n4. Carro (com gasolina) 🚗 \n5. Carro elétrico 💡 \n6. Carona Compartilhada 👥 \n")
    while True:
        try:
            MeioTransporte = int(input("Qual meio de transporte você utilizou hoje? "))
            if MeioTransporte not in [1, 2, 3, 4, 5, 6]:
                raise ValueError
            if MeioTransporte in [2, 3, 5]:
                print("🟢 Alta sustentabilidade!")
            elif MeioTransporte in [1, 6]:
                print("🟡 Moderada sustentabilidade!")
            else:
                print("🔴 Baixa Sustentabilidade!")
            break
        except ValueError:
            print("Escolha um meio de transporte de 1 a 6!")

    try:
        comando = """
            INSERT INTO InfoSustentaveis (Nome, Dia, Litros_Agua, Kwh, KG, Porcent_KG, Transporte)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        dados = (nome, data_geral, resposta, KWH, KG, Porcent, MeioTransporte)
        cursor.execute(comando, dados)
        conexao.commit()
        print("\n✅ Dados inseridos com sucesso no banco de dados!")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir os dados: {err}")

def buscar_registros():
    nome_busca = input("Digite o nome para buscar registros: ").strip()
    try:
        cursor.execute("SELECT * FROM InfoSustentaveis WHERE Nome = %s", (nome_busca,))
        resultados = cursor.fetchall()
        if resultados:
            print("\n📋 Registros encontrados:")
            for row in resultados:
                print()
                print(f"Nome.............: {row['Nome']}")
                print(f"Data.............: {row['Dia']}")
                print(f"Litros de água...: {row['Litros_Agua']}")
                print(f"kWh consumido....: {row['Kwh']}")
                print(f"Resíduos (KG)....: {row['KG']}")
                print(f"% Reciclado......: {row['Porcent_KG']}")
                print(f"Transporte.......: {row['Transporte']}")
        else:
            print("Nenhum registro encontrado para esse nome.")
    except mysql.connector.Error as err:
        print(f"Erro ao buscar: {err}")


def deletar_registro():
    nome_del = input("Digite o nome para deletar: ").strip()
    data_del = input("Digite a data do registro que deseja deletar (formato AAAA-MM-DD): ").strip()
    try:
        cursor.execute("DELETE FROM InfoSustentaveis WHERE Nome = %s AND Dia = %s", (nome_del, data_del))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Registro deletado com sucesso.")
        else:
            print("Nenhum registro encontrado com esse nome e data.")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar: {err}")

def alterar_registro():
    nome = input("Digite o nome: ").strip()
    data = input("Digite a data do registro (AAAA-MM-DD): ").strip()
    try:
        cursor.execute("SELECT * FROM InfoSustentaveis WHERE Nome = %s AND Dia = %s", (nome, data))
        resultado = cursor.fetchone()
        
        if resultado:
            litros = float(resultado["Litros_Agua"])
            kwh = float(resultado["Kwh"])
            kg = float(resultado["KG"])
            porcent = int(resultado["Porcent_KG"])
            transporte = int(resultado["Transporte"])

            while True:
                print("\nDados atuais:")
                print(f"1. Litros de água: {litros}")
                print(f"2. kWh: {kwh}")
                print(f"3. KG de resíduos: {kg}")
                print(f"4. % reciclado: {porcent}")
                print(f"5. Transporte: {transporte}")
                print("6. Finalizar alterações")

                try:
                    opc = int(input("Escolha o campo que deseja alterar (1-6): "))
                except ValueError:
                    print("Digite um número válido.")
                    continue

                if opc == 1:
                    litros = float(input("Novo valor para litros de água: "))
                elif opc == 2:
                    kwh = float(input("Novo valor para kWh: "))
                elif opc == 3:
                    kg = float(input("Novo valor para KG de resíduos: "))
                elif opc == 4:
                    porcent = int(input("Nova porcentagem reciclada: "))
                elif opc == 5:
                    print("\n1. Transporte público 🚌 \n2. Bicicleta 🚲 \n3. Caminhada 🚶 \n4. Carro (com gasolina) 🚗 \n5. Carro elétrico 💡 \n6. Carona Compartilhada 👥")
                    transporte = int(input("Novo meio de transporte: "))
                elif opc == 6:
                    break
                else:
                    print("Opção inválida.")

            cursor.execute("""
                UPDATE InfoSustentaveis
                SET Litros_Agua = %s, Kwh = %s, KG = %s, Porcent_KG = %s, Transporte = %s
                WHERE Nome = %s AND Dia = %s
            """, (litros, kwh, kg, porcent, transporte, nome, data))
            conexao.commit()
            print("✅ Registro atualizado com sucesso.")
        else:
            print("❌ Registro não encontrado.")
    except mysql.connector.Error as err:
        print("Erro ao atualizar:", err)



while True:
    print("\n==== MENU ====")
    print("1. Incluir novo registro")
    print("2. Buscar registros")
    print("3. Deletar um registro")
    print("4. Alterar um registro")
    print("5. Encerrar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        incluir_registro()
    elif opcao == "2":
        buscar_registros()
    elif opcao == "3":
        deletar_registro()
    elif opcao =="4":
        alterar_registro()
    elif opcao == "5":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida, tente novamente.")

cursor.close()
conexao.close()
print("CONEXÃO ENCERRADA")