# projeto_integrador
Sistema sustentável de projeto integrador

O código apresentado tem o objetivo de avaliar o impacto ambiental do usuário cadastrado no sistema, tendo como base o seu consumo pessoal de energia elétrica, água, geração de resíduos e o meio de transporte utilizado.

1. Validação de data: o primeiro bloco do código pede ao usuário que insira primeiramente o dia atual, o mês e o ano, todos em formato numérico. Para isso, o programa garante que as entradas estejam corretas:

    a. solicitando ao usuário qual o dia do mês, garantindo que o número esteja entre 1 e 31.
    b. solicitando o mês e garantindo que esteja entre 1 e 12.
    c. verificando se o dia fornecido pelo usuário está de acordo com a quantidade de dias daquele mês digitado.
    d. solicitando ao usuário o ano e verificando se está entre o intervalo de 1900 e 3000.
    e. garantindo que caso o usuário insira dia 29 no mês fevereiro em um ano que é bissexto, essa data será rejeitada.

Quando o usuário fornecer a data correta em todos os padrões, ela será formatada e printada no formato DD/MM/AAAA.

2. Avaliação do consumo de água: o segundo bloco do código irá avaliar o consumo de água do usuário e classificando sua sustentabilidade de acordo com:
    a. a quantidade de água utilizada no dia, verificando se a entrada é válida (ou seja, se é numérica).
    b. caso o usuário coloque um número negativo, o programa retorna uma mensagem de erro.
    c. com base no consumo inserido, o código vai categorizar a sustentabilidade em:
            Menos de 150 litros: "Alta sustentabilidade" (🟢)
            Entre 150 e 200 litros: "Sustentabilidade moderada" (🟡)
            Mais de 200 litros: "Baixa sustentabilidade" (🔴)

3. Consumo de Energia Elétrica: o primeiro bloco de código solicita ao usuário que insira o consumo de energia elétrica em kWh. Para garantir que o valor inserido seja válido:
    a. O programa verifica se o dado digitado é um número.
    b. Caso o usuário insira um valor inválido (como uma string ou um número negativo), uma mensagem de erro é exibida.
    c. Com base no consumo informado, o usuário recebe um feedback sobre seu nível de sustentabilidade:
            Menos de 5 kWh: "Alta sustentabilidade" (indicada por 🟢).
            Entre 5 e 10 kWh: "Moderada sustentabilidade" (🟡).
            Mais de 10 kWh: "Baixa sustentabilidade" (🔴).

4. Geração de Resíduos Não Recicláveis: o segundo bloco do código pede ao usuário para inserir a quantidade de resíduos não recicláveis gerados (em kg). O programa:
    a. Verifica se a entrada é um número.
    b. Caso o usuário insira um valor negativo, uma mensagem de erro é exibida.

5. Percentual de Reciclagem: o terceiro bloco do código solicita que o usuário informe a porcentagem de resíduos reciclados. O programa:
    
    a. Verifica se a entrada é um número inteiro entre 0 e 100.
    b. Com base na porcentagem informada, avalia a sustentabilidade do usuário:
            Mais de 50%: "Alta sustentabilidade" (🟢).
            Entre 20% e 50%: "Moderada sustentabilidade" (🟡).
            Abaixo de 20%: "Baixa sustentabilidade" (🔴).

6. Escolha do Meio de Transporte: o quarto bloco pede ao usuário que informe o meio de transporte utilizado no dia. As opções disponíveis são:
            Transporte público (🛸)
            Bicicleta (🚲)
            Caminhada (🚶)
            Carro a gasolina (🚗)
            Carro elétrico (💡)
            Carona compartilhada (👥)

Com base na escolha, o programa classifica o meio de transporte em:
            Alta sustentabilidade" (🟢) para bicicleta, caminhada e carro elétrico.
            "Moderada sustentabilidade" (🟡) para carona compartilhada e transporte público.
            "Baixa sustentabilidade" (🔴) para carro a gasolina.

            