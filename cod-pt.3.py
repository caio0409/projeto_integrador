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
    nome = input("Digite seu nome: ").strip()

    while True:
        try:
            dia = int(input("Qual o dia?: "))
            mes = int(input("Qual o mês?: "))
            ano = int(input("Qual o ano?: "))
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 3000):
                raise ValueError
            if mes == 2 and (dia > 29 or (dia == 29 and ano % 4 != 0)):
                raise ValueError
            if mes in [4, 6, 9, 11] and dia > 30:
                raise ValueError
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    data_formatada = f"{ano}-{mes:02d}-{dia:02d}"

    def get_float(msg):
        while True:
            try:
                val = float(input(msg))
                if val < 0:
                    raise ValueError
                return val
            except ValueError:
                print("Valor inválido.")

    def get_int(msg, min_val=0, max_val=100):
        while True:
            try:
                val = int(input(msg))
                if val < min_val or val > max_val:
                    raise ValueError
                return val
            except ValueError:
                print(f"Digite um número entre {min_val} e {max_val}.")

    litros = get_float("Quantos litros foram consumidos hoje? ")
    kwh = get_float("Quantos kWh de energia você consumiu hoje? ")
    kg = get_float("Quantos KG de resíduos não recicláveis gerou hoje? ")
    porcent = get_int("Qual a porcentagem de resíduos reciclados no total (%): ")
    transporte = get_int("Meio de transporte (1: público, 2: bike, 3: caminhada, 4: carro, 5: elétrico, 6: carona): ", 1, 6)

    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO InfoSustentáveis (Nome, Dia, Litros_Agua, Kwh, KG, Porcent_KG, Transporte)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nome, data_formatada, litros, kwh, kg, porcent, transporte))
        conn.commit()
        print("Registro inserido com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir:", err)
    finally:
        cursor.close()
        conn.close()

def buscar_registros():
    nome = input("Digite o nome para buscar registros: ").strip()
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM InfoSustentáveis WHERE Nome = %s", (nome,))
        registros = cursor.fetchall()
        if registros:
            for r in registros:
                print(r)
        else:
            print("Nenhum registro encontrado.")
    except mysql.connector.Error as err:
        print("Erro ao buscar:", err)
    finally:
        cursor.close()
        conn.close()

def deletar_registro():
    nome = input("Digite o nome: ").strip()
    data = input("Digite a data (AAAA-MM-DD): ").strip()
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM InfoSustentáveis WHERE Nome = %s AND Dia = %s", (nome, data))
        conn.commit()
        if cursor.rowcount:
            print("Registro deletado com sucesso.")
        else:
            print("Registro não encontrado.")
    except mysql.connector.Error as err:
        print("Erro ao deletar:", err)
    finally:
        cursor.close()
        conn.close()

def alterar_registro():
    nome = input("Digite o nome: ").strip()
    data = input("Digite a data do registro (AAAA-MM-DD): ").strip()
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM InfoSustentáveis WHERE Nome = %s AND Dia = %s", (nome, data))
        if cursor.fetchone():
            print("Digite os novos valores:")
            litros = float(input("Litros de água: "))
            kwh = float(input("kWh: "))
            kg = float(input("KG de resíduos: "))
            porcent = int(input("Porcentagem reciclado: "))
            transporte = int(input("Transporte (1-6): "))
            cursor.execute("""
                UPDATE InfoSustentáveis
                SET Litros_Agua = %s, Kwh = %s, KG = %s, Porcent_KG = %s, Transporte = %s
                WHERE Nome = %s AND Dia = %s
            """, (litros, kwh, kg, porcent, transporte, nome, data))
            conn.commit()
            print("Registro atualizado com sucesso.")
        else:
            print("Registro não encontrado.")
    except mysql.connector.Error as err:
        print("Erro ao atualizar:", err)
    finally:
        cursor.close()
        conn.close()

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Incluir Registro")
        print("2. Buscar Registro")
        print("3. Deletar Registro")
        print("4. Alterar Registro")
        print("5. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            incluir_registro()
        elif op == "2":
            buscar_registros()
        elif op == "3":
            deletar_registro()
        elif op == "4":
            alterar_registro()
        elif op == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()