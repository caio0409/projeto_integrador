import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="172.16.12.14",      
        user="BD24022525",          
        password="Qzrgb5",        
        database="BD24022525"     
    )
    cursor = conexao.cursor()
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
            print("\nRegistros encontrados:")
            for row in resultados:
                print(row)
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

while True:
    print("\n==== MENU ====")
    print("1. Incluir novo registro")
    print("2. Buscar registros")
    print("3. Deletar um registro")
    print("4. Encerrar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        incluir_registro()
    elif opcao == "2":
        buscar_registros()
    elif opcao == "3":
        deletar_registro()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida, tente novamente.")

cursor.close()
conexao.close()
print("CONEXÃO ENCERRADA")
