# projeto_integrador
Sistema sustentável de projeto integrador

O código apresentado tem o objetivo de avaliar o impacto ambiental do usuário cadastrado no sistema, tendo como base o seu consumo pessoal de energia elétrica, água, geração de resíduos e o meio de transporte utilizado.

1. Consumo de Energia Elétrica: o primeiro bloco de código solicita ao usuário que insira o consumo de energia elétrica em kWh. Para garantir que o valor inserido seja válido:
    a. O programa verifica se o dado digitado é um número.
    b. Caso o usuário insira um valor inválido (como uma string ou um número negativo), uma mensagem de erro é exibida.
    c. Com base no consumo informado, o usuário recebe um feedback sobre seu nível de sustentabilidade:
            Menos de 5 kWh: "Alta sustentabilidade" (indicada por 🟢).
            Entre 5 e 10 kWh: "Moderada sustentabilidade" (🟡).
            Mais de 10 kWh: "Baixa sustentabilidade" (🔴).

2. Geração de Resíduos Não Recicláveis: o segundo bloco do código pede ao usuário para inserir a quantidade de resíduos não recicláveis gerados (em kg). O programa:
    a. Verifica se a entrada é um número.
    b. Caso o usuário insira um valor negativo, uma mensagem de erro é exibida.

3. Percentual de Reciclagem: o terceiro bloco do código solicita que o usuário informe a porcentagem de resíduos reciclados. O programa:
    a. Verifica se a entrada é um número inteiro entre 0 e 100.
    b. Com base na porcentagem informada, avalia a sustentabilidade do usuário:
            Mais de 50%: "Alta sustentabilidade" (🟢).
            Entre 20% e 50%: "Moderada sustentabilidade" (🟡).
            Abaixo de 20%: "Baixa sustentabilidade" (🔴).

4. Escolha do Meio de Transporte: o quarto bloco pede ao usuário que informe o meio de transporte utilizado no dia. As opções disponíveis são:
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


