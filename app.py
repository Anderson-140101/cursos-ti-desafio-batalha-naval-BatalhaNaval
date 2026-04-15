import streamlit as st

st.set_page_config(page_title="Curso de Python Básico", page_icon="🐍", layout="wide")

st.sidebar.title("🐍 Curso de Python Básico")
st.sidebar.markdown("Do absoluto zero até a criação de Inteligências Artificiais!")

modulo_escolhido = st.sidebar.selectbox(
    "📚 Escolha o Módulo do Curso:",
    ["📘 Módulo 1: Python Básico", "🚀 Módulo 2: Python A Evolução"]
)

if modulo_escolhido == "📘 Módulo 1: Python Básico":
    menu = [
        "1. Introdução",
        "2. Variáveis",
        "3. Sinais e Operadores",
        "4. Aspas (Strings)",
        "5. Parênteses, Colchetes e Chaves",
        "6. Tomando Decisões (If/Else)",
        "7. Repetições (For e While)",
        "8. Funções (def)",
        "9. Tratamento de Erros (Try/Except)",
        "10. Módulos e Bibliotecas (Import)",
        "11. Projeto Final: Estágio (Ao Vivo!)"
    ]
    escolha = st.sidebar.radio("Navegação:", menu)
else:
    menu = [
        "Aula 1: Python Power Up",
        "Aula 2: Python Insights",
        "Aula 3: Python IA",
        "Aula 4: Python Dev"
    ]
    escolha = st.sidebar.radio("Aulas Avançadas:", menu)

st.title("Bem-vindo à Formação em Python! 🐍🚀")

if escolha == "1. Introdução":
    st.header("1. Introdução ao Python")
    st.write('''
    O Python é uma linguagem de programação muito popular, fácil de ler e de aprender.
    Ela é usada para criar sites, analisar dados, inteligência artificial e muito mais!
    ''')
    st.info("💡 **Dica:** O Python lê o código de cima para baixo, linha por linha.")

    st.subheader("Como mostrar algo na tela?")
    st.write("Usamos a função `print()` para escrever algo na tela do computador.")
    st.code('print("Olá, Mundo!")', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q1 = st.radio("Qual comando usamos para escrever algo na tela no Python?", ("mostrar()", "print()", "escrever()", "tela()"), index=None)
    if q1 == "print()":
        st.success("Exato! Você aprendeu a primeira função do Python.")
    elif q1 != None:
        st.error("Ops! Tente novamente. Lembre-se do inglês para 'imprimir'.")

elif escolha == "2. Variáveis":
    st.header("2. O que são Variáveis?")
    st.write('''
    Variáveis são como "caixinhas" ou "etiquetas" que usamos para guardar informações no computador.
    Para criar uma variável no Python, você escolhe um nome e usa o sinal de igual `=` para colocar algo dentro dela.
    ''')

    st.subheader("Exemplos de Variáveis:")
    st.code('''
nome = "João"      # Guarda um texto (String)
idade = 25         # Guarda um número inteiro (Integer)
altura = 1.75      # Guarda um número quebrado/decimal (Float)
gosta_de_python = True  # Guarda Verdadeiro ou Falso (Boolean)

print(nome)
print(idade)
    ''', language='python')

    st.warning('''
    ⚠️ **Regras para nomes de variáveis:**
    - Não podem ter espaços (use `_` como em `nome_completo`).
    - Não podem começar com números.
    - Não use acentos ou cedilha (preferencialmente).
    ''')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q2 = st.radio("Qual das opções abaixo é um nome VÁLIDO para uma variável no Python?", ("1_nome", "nome completo", "nome_completo", "nome-completo"), index=None)
    if q2 == "nome_completo":
        st.success("Correto! Não podemos usar espaços, traços ou começar com números.")
    elif q2 != None:
        st.error("Incorreto! Reveja a caixinha amarela de 'Regras'.")

elif escolha == "3. Sinais e Operadores":
    st.header("3. Sinais e Operadores Matemáticos")
    st.write("No Python, usamos sinais matemáticos para fazer contas, parecidos com a matemática da escola.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Operadores Matemáticos")
        st.markdown('''
        * `+` : Soma
        * `-` : Subtração
        * `*` : Multiplicação (não é um 'x', é um asterisco)
        * `/` : Divisão
        ''')
        st.code('''
soma = 10 + 5       # 15
subtracao = 10 - 5  # 5
multiplicacao = 10 * 5 # 50
divisao = 10 / 2    # 5.0
        ''', language='python')

    with col2:
        st.subheader("Operadores de Comparação")
        st.markdown('''
        Usamos para comparar coisas. Eles respondem `True` (Verdadeiro) ou `False` (Falso).
        * `==` : Igual a (Note que são DOIS sinais de igual. Um `=` só serve para guardar valor).
        * `!=` : Diferente de
        * `>` e `<` : Maior que e Menor que
        ''')
        st.code('''
print(10 == 10)  # True (10 é igual a 10)
print(5 > 10)    # False (5 não é maior que 10)
        ''', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q3 = st.radio("Qual a diferença entre `=` e `==` no Python?", ("São a mesma coisa.", "`=` guarda um valor e `==` compara se duas coisas são iguais.", "`==` guarda um valor e `=` compara.", "Nenhuma das anteriores."), index=None)
    if q3 == "`=` guarda um valor e `==` compara se duas coisas são iguais.":
        st.success("Perfeito! Um `=` é atribuição, dois `==` é comparação.")
    elif q3 != None:
        st.error("Quase lá! Leia novamente a sessão de Operadores de Comparação.")

elif escolha == "4. Aspas (Strings)":
    st.header("4. Onde colocar as Aspas?")
    st.write('''
    As aspas servem para dizer ao Python: **"Isto é um texto, não é um comando ou um número"**.
    Textos no Python são chamados de **Strings**.
    ''')

    st.subheader("Aspas Simples (' ') vs Aspas Duplas (\" \")")
    st.write("Você pode usar qualquer uma das duas, o resultado é o mesmo!")
    st.code('''
nome1 = 'Maria'  # Aspas simples
nome2 = "Maria"  # Aspas duplas
# As duas formas estão corretas!
    ''', language='python')

    st.subheader("Quando usar três aspas? (''' ''')")
    st.write("Usamos três aspas quando queremos escrever um texto que pula linhas (texto longo).")
    st.code('''
texto_longo = """
Este é um texto gigante.
Ele pode pular linhas facilmente.
Basta colocar entre três aspas.
"""
print(texto_longo)
    ''', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q4 = st.radio("Para que servem as 3 aspas (''' ou \"\"\")?", ("Para destacar um texto.", "Para textos curtos.", "Para textos longos que pulam linhas.", "Para fazer contas."), index=None)
    if q4 == "Para textos longos que pulam linhas.":
        st.success("Exatamente! Elas permitem a quebra de linha natural (multi-line).")
    elif q4 != None:
        st.error("Ainda não. Tente a opção que fala sobre pular linhas.")

elif escolha == "5. Parênteses, Colchetes e Chaves":
    st.header("5. Sinais Especiais: (), [], {}")
    st.write("Cada um desses sinais tem uma função muito específica e importante no Python.")

    st.subheader("1. Parênteses `( )` - Funções e Tuplas")
    st.write("Eles 'abraçam' as informações que vamos enviar para uma função, ou servem para organizar cálculos.")
    st.code('''
# Em funções:
print("Olá")  # O parênteses guarda o que o print vai mostrar na tela

# Em cálculos matemáticos:
conta = (10 + 5) * 2  # Dá prioridade para a soma
    ''', language='python')

    st.subheader("2. Colchetes `[ ]` - Listas")
    st.write("Eles servem para criar **Listas**. Uma lista guarda vários valores juntos em uma única variável.")
    st.code('''
frutas = ["Maçã", "Banana", "Laranja"]
numeros = [10, 20, 30, 40]

print(frutas[0]) # Mostra "Maçã" (no Python, a contagem começa do zero!)
    ''', language='python')

    st.subheader("3. Chaves `{ }` - Dicionários")
    st.write("Eles servem para criar **Dicionários**. Eles guardam valores no formato Chave/Valor.")
    st.code('''
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

print(pessoa["nome"]) # Mostra "Carlos"
    ''', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q5 = st.radio("Qual sinal usamos para criar uma **Lista** que guarda vários itens (como frutas)?", ("Parênteses ( )", "Colchetes [ ]", "Chaves { }", "Aspas \" \""), index=None)
    if q5 == "Colchetes [ ]":
        st.success("Muito bem! Colchetes são usados para listas.")
    elif q5 != None:
        st.error("Ops! Dê uma olhada novamente na seção 2.")

elif escolha == "6. Tomando Decisões (If/Else)":
    st.header("6. Ensinando o Computador a Tomar Decisões")
    st.write('''
    Até agora, nossos códigos rodavam direto, do começo ao fim. Mas e se a gente quiser que o código faça algo **apenas SE** uma condição for verdadeira?
    É aí que entram o **If** (Se), o **Else** (Se não) e o **Elif** (Se não, se).
    ''')

    st.subheader("O comando If e Else")
    st.write("Imagine que você está programando a entrada de um cinema. A pessoa só pode entrar se for maior de idade.")
    st.code('''
idade = 20

if idade >= 18:
    print("Você pode entrar no cinema!")
else:
    print("Você não pode entrar, volte para casa.")
    ''', language='python')

    st.warning('''
    ⚠️ **ATENÇÃO À IDENTAÇÃO (Os espaços antes do código):**
    Olhe para o código acima. Percebeu que o `print` não está colado no canto esquerdo? Ele tem uns espaços antes.

    No Python, **esses espaços (geralmente 4 espaços ou 1 'Tab') são obrigatórios!**
    Eles avisam ao Python: *"Ei, esse comando print faz parte do bloco If"*. Se você não colocar os espaços, o código vai dar erro.
    Outra coisa muito importante: Repare no sinal de dois pontos `:` no final do `if` e do `else`. Não esqueça deles!
    ''')

    st.subheader("Usando o Elif (Para mais de duas opções)")
    st.write("E se a gente tiver 3 regras? Por exemplo, um sinaleiro/semáforo:")
    st.code('''
cor = "Amarelo"

if cor == "Verde":
    print("Pode passar!")
elif cor == "Amarelo":
    print("Atenção, diminua a velocidade.")
else:
    print("Pare imediatamente!")
    ''', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q6 = st.radio("Por que os espaços (identação) antes do `print` dentro do `if` são importantes?", ("Apenas por estética.", "Para o código ficar colorido.", "Eles são obrigatórios para dizer ao Python que aquele comando faz parte do If.", "Não são importantes, o código roda sem eles."), index=None)
    if q6 == "Eles são obrigatórios para dizer ao Python que aquele comando faz parte do If.":
        st.success("Acertou em cheio! A identação é o que define os blocos de código no Python.")
    elif q6 != None:
        st.error("Cuidado! Leia a caixa amarela de atenção sobre a Identação.")

elif escolha == "7. Repetições (For e While)":
    st.header("7. Laços de Repetição (Loops)")
    st.write('''
    Imagine que você precisa escrever "Bom dia!" na tela 100 vezes.
    Você copiaria e colaria o comando `print` 100 vezes? Claro que não!
    Para isso usamos os **Laços de Repetição**, também chamados de *Loops*.
    ''')

    st.subheader("1. O comando `for` (Para)")
    st.write("Usamos o `for` quando sabemos exatamente quantas vezes queremos repetir ou quando queremos percorrer uma Lista.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Contando de 0 a 4:**")
        st.code('''
# range(5) significa "repita 5 vezes" (0, 1, 2, 3, 4)
for numero in range(5):
    print(numero)
        ''', language='python')

    with col2:
        st.markdown("**Percorrendo uma lista:**")
        st.code('''
frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print("Eu gosto de " + fruta)
        ''', language='python')

    st.subheader("2. O comando `while` (Enquanto)")
    st.write('''
    Usamos o `while` quando **NÃO** sabemos quantas vezes o código vai repetir, mas queremos que ele continue repetindo **ENQUANTO** uma condição for verdadeira.
    ''')
    st.code('''
contador = 1

while contador <= 3:
    print("Contagem: ", contador)
    contador = contador + 1 # Aumenta 1 para não rodar para sempre!

print("Fim da contagem!")
    ''', language='python')

    st.error('''
    🛑 **Cuidado com o Loop Infinito!**
    Se no código acima a gente esquecesse a linha `contador = contador + 1`, a condição seria sempre verdadeira (1 sempre será menor que 3), e o computador ficaria escrevendo "Contagem: 1" para sempre até travar!
    ''')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q7 = st.radio("O que acontece se esquecermos de atualizar a condição dentro de um `while`?", ("Ele roda uma vez e para.", "Ele causa um Loop Infinito, travando o programa.", "Ele pula para a próxima linha.", "O Python corrige sozinho."), index=None)
    if q7 == "Ele causa um Loop Infinito, travando o programa.":
        st.success("Exatamente! É o pesadelo de todo programador! 😅")
    elif q7 != None:
        st.error("Erro. Lembre-se do aviso vermelho no final da lição!")

elif escolha == "8. Funções (def)":
    st.header("8. Criando suas próprias Funções (`def`)")
    st.write('''
    Até agora, usamos funções que já vieram prontas no Python, como o `print()`.
    Mas você também pode **criar os seus próprios comandos (funções)**!
    Isso é ótimo para não ter que repetir o mesmo código várias vezes.
    ''')

    st.subheader("Como criar uma função?")
    st.write("Usamos a palavra-chave `def` (de *define*). Vamos criar uma função que dá bom dia:")
    st.code('''
# 1. CRIANDO A FUNÇÃO (Ela não faz nada até ser chamada)
def dar_bom_dia():
    print("Bom dia! Seja muito bem-vindo ao sistema!")
    print("------------------------------------------")

# 2. USANDO A FUNÇÃO
dar_bom_dia()
dar_bom_dia() # Posso usar quantas vezes quiser!
    ''', language='python')

    st.subheader("Funções que recebem informações (Parâmetros)")
    st.write('''
    As funções podem receber informações dentro dos parênteses `( )` para ficarem mais inteligentes.
    Vamos criar uma função que soma dois números:
    ''')
    st.code('''
def somar(numero1, numero2):
    resultado = numero1 + numero2
    print("A soma deu:", resultado)

somar(10, 5)   # Vai mostrar "A soma deu: 15"
somar(50, 50)  # Vai mostrar "A soma deu: 100"
    ''', language='python')

    st.success('''
    ✅ **Parabéns!**
    Com as Funções, você acaba de concluir a base essencial da programação em Python.
    Você já tem o conhecimento necessário para começar a criar os seus próprios projetinhos!
    ''')

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q8 = st.radio("Qual palavra usamos para começar a criar nossa própria função no Python?", ("function", "criar", "def", "fun"), index=None)
    if q8 == "def":
        st.success("Correto! `def` vem de 'define' (definir função).")
    elif q8 != None:
        st.error("Tente de novo! Olha o código de exemplo lá em cima.")

elif escolha == "9. Tratamento de Erros (Try/Except)":
    st.header("9. Tratamento de Erros (`try` e `except`)")
    st.write('''
    Você já notou que, às vezes, o Python mostra um erro gigante em vermelho na tela e o seu programa simplesmente fecha (crasha)?
    Como bons programadores, precisamos **prever** que erros podem acontecer e ensinar o programa a lidar com eles de forma elegante, sem "quebrar" na cara do usuário.
    ''')

    st.subheader("O que é o Try e o Except?")
    st.markdown('''
    * **`try` (Tentar):** Você pede para o Python *tentar* executar um bloco de código perigoso (que pode dar erro).
    * **`except` (Exceto/Se der erro):** Se o código der errado, o Python não trava! Ele pula para o bloco do Except e executa o que você mandar.
    ''')

    st.subheader("Exemplo Clássico: Divisão por Zero")
    st.write("Na matemática, não podemos dividir um número por zero. Se você tentar fazer isso no Python, ele quebra. Veja como consertar:")

    st.code('''
# Tente executar isso:
try:
    numero = 10
    divisor = 0
    resultado = numero / divisor
    print("O resultado é:", resultado)

# Se der um erro de "Divisão por Zero", faça isso em vez de travar:
except ZeroDivisionError:
    print("Opa! Você tentou dividir por zero. Isso não é permitido na matemática!")
    ''', language='python')

    st.subheader("Outro Exemplo: Erro de Digitação do Usuário")
    st.write("Imagine que você pede para a pessoa digitar a idade (um número), mas ela digita 'vinte' (um texto). O programa daria erro, mas com o Try/Except:")

    st.code('''
try:
    idade = int(input("Digite sua idade em números: "))
    print("Você tem", idade, "anos.")
except ValueError:
    print("Erro! Por favor, digite apenas números, não palavras.")
    ''', language='python')

    st.info("💡 **Dica de Ouro:** Usar `try` e `except` é o que diferencia um programa amador (que trava o tempo todo) de um programa profissional e seguro!")

    st.markdown("---")
    st.subheader("🧠 Quiz Rápido!")
    q9 = st.radio("Para que serve o bloco `except`?", ("Para tentar executar um código perigoso.", "Para executar algo SOMENTE quando um erro acontecer, evitando que o programa feche.", "Para encerrar o programa de propósito.", "Para acelerar o código."), index=None)
    if q9 == "Para executar algo SOMENTE quando um erro acontecer, evitando que o programa feche.":
        st.success("Você acertou! Ele é a 'rede de segurança' do seu programa!")
    elif q9 != None:
        st.error("Pense um pouco mais na tradução de 'Exceto' (se der erro).")

elif escolha == "10. Módulos e Bibliotecas (Import)":
    st.header("10. Módulos e Bibliotecas (`import`)")
    st.write('''
    Você sabia que não precisa programar tudo do zero? O Python possui um "arsenal" gigantesco de códigos prontos criados por outras pessoas que você pode usar de graça!
    Para trazer essas ferramentas extras para o seu programa, usamos a palavra mágica **`import`**.
    ''')

    st.subheader("Exemplo: A Biblioteca Matemática")
    st.write("O Python sabe somar e multiplicar, mas se você precisar calcular a raiz quadrada? Basta importar a biblioteca `math`!")
    st.code('''
import math # Trazendo a caixa de ferramentas de matemática

raiz = math.sqrt(25) # sqrt = square root (raiz quadrada)
print(raiz) # O resultado será 5.0
    ''', language='python')

    st.subheader("Exemplo: Sorteios com a biblioteca `random`")
    st.write("Criar códigos que geram coisas aleatórias é muito difícil. Mas graças à biblioteca `random` (aleatório), podemos fazer sorteios em 2 linhas!")
    st.code('''
import random

# Sorteando um número de 1 a 10:
numero_da_sorte = random.randint(1, 10)
print("Seu número da sorte é:", numero_da_sorte)

# Sorteando um vencedor de uma lista:
alunos = ["Ana", "Bruno", "Carlos", "Diana"]
vencedor = random.choice(alunos)
print("O grande vencedor do sorteio foi:", vencedor)
    ''', language='python')

    st.info("💡 **Curiosidade:** O próprio aplicativo que você está usando agora mesmo para ler este curso foi criado importando uma biblioteca famosa chamada `streamlit`!")

    st.markdown("---")
    st.subheader("🎯 Exercício Interativo!")
    st.write("Clique no botão abaixo para testar a biblioteca `random` aqui mesmo e sortear um número de 1 a 100:")

    import random # Importamos a biblioteca real aqui no código do aplicativo!
    if st.button("Sortear Número!"):
        sorteio = random.randint(1, 100)
        st.success(f"O número sorteado foi: **{sorteio}**!")

    st.markdown("---")
    st.subheader("🧠 Quiz Final!")
    q10 = st.radio("Qual é a palavra mágica que usamos para trazer bibliotecas e códigos prontos para dentro do nosso programa?", ("include", "bring", "import", "get"), index=None)
    if q10 == "import":
        st.success("Exatamente! Importar é o grande poder do Python! 🎈🎉")
    elif q10 != None:
        st.error("Erro! Dê uma olhadinha lá no título desta aula.")

elif escolha == "11. Projeto Final: Estágio (Ao Vivo!)":
    st.header("11. 💼 Seu 1º Dia de Estágio na TechCorp")
    st.write('''
    Chegou a hora de juntar tudo o que você aprendeu! Imagine que hoje é o seu primeiro dia de estágio em uma grande empresa de tecnologia focada em vendas.
    Seu chefe, o Sr. Tech, te mandou um e-mail com a sua primeira tarefa do dia.
    ''')

    st.info('''
    📧 **E-mail do Chefe:**
    "Olá estagiário, bem-vindo à equipe!
    Nós extraímos do nosso banco de dados uma lista com a idade dos nossos últimos 5 clientes. A lista é esta: `idades = [15, 22, 17, 30, 45]`.
    Sua missão é criar um programa usando um laço **for** para olhar cada idade. Se a idade for maior ou igual a 18, dê um `print` dizendo 'Cliente Adulto'. Se for menor, dê um `print` dizendo 'Cliente Menor de idade'. Confio em você!"
    ''')

    st.write("---")
    st.subheader("💻 Terminal de Programação em Tempo Real")
    st.write("Digite o seu código na caixa de texto abaixo e clique em 'Executar Código'. O resultado vai aparecer na caixinha verde ao lado!")

    col_codigo, col_resultado = st.columns([1.5, 1])

    with col_codigo:
        codigo_aluno = st.text_area(
            "Digite seu código Python aqui:",
            height=250,
            value="idades = [15, 22, 17, 30, 45]\n\n# Apague esta linha e comece a escrever seu For e If aqui!"
        )
        botao_rodar = st.button("▶️ Executar Código")

    with col_resultado:
        st.write("**Resultado na Tela (Terminal):**")
        if botao_rodar:
            # Sistema anti-RCE e de avaliação guiada
            codigo = codigo_aluno.lower()

            # Verificando as estruturas obrigatórias
            if "for " not in codigo:
                st.error("❌ Erro: Seu código precisa de um laço 'for' para percorrer a lista de idades.")
            elif "if " not in codigo:
                st.error("❌ Erro: Você esqueceu de usar o 'if' para verificar se a pessoa é maior de 18 anos.")
            elif "print(" not in codigo:
                st.error("❌ Erro: Você precisa imprimir (print) o resultado na tela conforme as instruções do chefe.")
            elif ">=" not in codigo and "> 17" not in codigo and "<" not in codigo:
                st.error("❌ Erro: Verifique os seus operadores lógicos (maior, menor, igual).")
            else:
                # Simulação de sucesso se os requisitos básicos forem preenchidos
                if ("adulto" in codigo and "menor" in codigo) or ("maior" in codigo and "menor" in codigo):
                    st.success('''
Cliente Menor de idade
Cliente Adulto
Cliente Menor de idade
Cliente Adulto
Cliente Adulto
                    ''')
                    st.balloons()
                    st.markdown("🏆 **Chefe:** Excelente trabalho estagiário! O código funcionou perfeitamente e imprimiu todos os clientes. Você acaba de ser promovido!")
                else:
                    st.warning("Seu código tem a estrutura correta, mas você não escreveu os textos de impressão exatamente como o Chefe pediu. Tente usar 'Adulto' e 'Menor' nos seus prints.")


elif escolha == "Aula 1: Python Power Up":
    st.header("⚡ Aula 1 - Python Power Up")
    st.write("Bem-vindo à primeira aula da **Evolução Python**. Hoje você deixará de ser um 'digitador de código' para se tornar um **Criador de Robôs**.")

    st.subheader("a. Automação de Tarefas")
    st.write('''
    Sabe aquela tarefa chata e repetitiva que você faz no trabalho? Preencher planilhas, baixar relatórios, enviar e-mails todo dia no mesmo horário?
    O Python consegue assumir o controle do seu computador e fazer isso para você em segundos. Chamamos isso de **RPA (Robotic Process Automation)**.
    ''')

    st.subheader("b. Criação de Bots & c. Controle de Mouse e Teclado")
    st.write("Para criar nosso primeiro Bot, usamos uma biblioteca superpoderosa chamada **`pyautogui`**. Ela simula um ser humano controlando o computador.")
    st.markdown('''
    - `pyautogui.click()`: Clica na tela.
    - `pyautogui.write('texto')`: Digita no teclado.
    - `pyautogui.press('enter')`: Aperta uma tecla.
    ''')

    st.subheader("d. Seu 1º projeto em Python partindo do zero")
    st.write("Vamos criar um Bot que abre o Bloco de Notas sozinho, digita uma mensagem e salva o arquivo.")
    st.code('''
# Passo 1: Instale a biblioteca (No terminal: pip install pyautogui)
import pyautogui
import time

# Passo 2: Damos uma pausa de 2 segundos para dar tempo de olhar a tela
time.sleep(2)

# Passo 3: O Bot aperta a tecla do Windows e pesquisa o bloco de notas
pyautogui.press("win")
time.sleep(1)
pyautogui.write("bloco de notas")
pyautogui.press("enter")
time.sleep(2)

# Passo 4: O Bot escreve a mensagem como se fosse você digitando!
pyautogui.write("Ola chefe! Eu sou um robo criado em Python e ja terminei o relatorio.")

# Passo 5: Salvar o arquivo
pyautogui.hotkey("ctrl", "s") # Aperta duas teclas juntas
time.sleep(1)
pyautogui.write("relatorio_bot")
pyautogui.press("enter")
    ''', language='python')

    st.info("⚠️ **Dica Importante:** Para parar um bot descontrolado do PyAutoGUI, arraste o seu mouse com força para qualquer um dos 4 cantos extremos da sua tela (Fail-Safe)!")

    st.markdown("---")
    st.subheader("🧠 Quiz Power Up")
    qa1 = st.radio("Se eu quiser que o meu Bot aperte a tecla 'Espaço' do meu teclado, qual comando do PyAutoGUI eu uso?", ("pyautogui.click('espaço')", "pyautogui.press('space')", "pyautogui.write('espaço')", "pyautogui.botao('space')"), index=None)
    if qa1 == "pyautogui.press('space')":
        st.success("Perfeito! `press()` é usado para apertar teclas específicas!")
    elif qa1 != None:
        st.error("Tente de novo! Lembre-se do inglês para 'Pressionar' uma tecla.")


elif escolha == "Aula 2: Python Insights":
    st.header("📊 Aula 2 - Python Insights")
    st.write("Hoje você vai aprender por que as empresas amam tanto o Python. Vamos transformar dados puros em **Ouro (Informação de valor)** usando Análise de Dados e Inteligência de Negócios.")

    st.subheader("a. Análise de Dados e c. Tratamento de Dados")
    st.write('''
    No mercado de trabalho, você não vai analisar 5 clientes no olho, vai analisar planilhas com 5 milhões de linhas!
    Para isso usamos a biblioteca **`pandas`**. Ela funciona como um 'Excel com super poderes'. O tratamento de dados envolve ler essa planilha e remover valores vazios, erros ou dados duplicados antes de analisar.
    ''')
    st.code('''
import pandas as pd

# 1. Lê uma base de dados inteira em 1 segundo
tabela = pd.read_csv("vendas_empresa.csv")

# 2. Tratamento: Joga fora linhas vazias (limpeza)
tabela = tabela.dropna()

# 3. Análise: Quanto a empresa faturou por loja?
faturamento = tabela.groupby('Loja')['Valor Final'].sum()
print(faturamento)
    ''', language='python')

    st.subheader("b. Gráficos e Dashboards & d. Relatórios que Impressionam")
    st.write("De nada adianta descobrir os dados se o seu chefe não entender nada. Você precisa apresentar visualmente! Para gerar relatórios e Dashboards (painéis interativos) que impressionam, usamos o próprio `streamlit` com o Pandas!")

    # Gerando um gráfico real na tela do usuário
    st.write("Veja este exemplo **REAL** gerado agora mesmo pelo seu aplicativo:")
    import pandas as pd
    import numpy as np

    # Criando dados falsos para demonstração
    dados_grafico = pd.DataFrame({
        "Meses": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Vendas": [1500, 2200, 1800, 3100, 4500, 5200]
    })

    st.bar_chart(dados_grafico, x="Meses", y="Vendas", color="#1f77b4")
    st.caption("Gráfico: Faturamento do 1º Semestre")

    st.markdown("---")
    st.subheader("🧠 Quiz Insights")
    qa2 = st.radio("Qual é a principal biblioteca do Python para trabalhar com grande quantidade de dados e tabelas (O 'Excel do Python')?", ("pyautogui", "streamlit", "pandas", "math"), index=None)
    if qa2 == "pandas":
        st.success("Exatamente! O Pandas é o rei dos dados no Python!")
    elif qa2 != None:
        st.error("Ops! Dê uma lida novamente na sessão 'Análise de Dados'!")

elif escolha == "Aula 3: Python IA":
    st.header("🤖 Aula 3 - Python IA")
    st.write("Chegamos ao topo da tecnologia atual! O Python é a principal linguagem do mundo para criar Inteligências Artificiais, como o ChatGPT, geradores de imagens e sistemas de previsão.")

    st.subheader("a. Criação de Inteligência Artificial e b. Previsões")
    st.write('''
    A Inteligência Artificial (IA) em Python geralmente usa um ramo chamado **Machine Learning (Aprendizado de Máquina)**.
    A ideia é simples: em vez de você escrever o código com as regras (os `Ifs` e `Elses`), você passa **Dados Históricos** para o Python e ele aprende as regras sozinho!
    ''')

    st.info("💡 **Exemplo prático:** Você dá para a IA os dados de 1.000 clientes (idade, salário, se comprou ou não). A IA estuda isso e consegue **prever** se o cliente de número 1.001 vai comprar o seu produto ou não!")

    st.write("Uma das bibliotecas mais usadas para previsões e machine learning é a `scikit-learn`.")
    st.code('''
from sklearn.ensemble import RandomForestClassifier

# 1. Cria a Inteligência Artificial (O cérebro)
ia = RandomForestClassifier()

# 2. Treina a IA com os dados históricos que você tem
ia.fit(dados_dos_clientes, compras_passadas)

# 3. Faz a previsão do futuro!
previsao = ia.predict(novo_cliente)
print(previsao)
    ''', language='python')

    st.subheader("c. A Nova Onda do Mercado de Trabalho")
    st.write('''
    O mundo mudou. Profissionais que apenas "usam" o computador estão sendo substituídos. Profissionais que **criam soluções e controlam IAs** estão sendo os mais disputados e bem pagos do mercado!
    Entender de Python, Machine Learning e automação é o seu "passaporte" para não ficar obsoleto nessa nova onda tecnológica.
    ''')

    st.markdown("---")
    st.subheader("🧠 Quiz IA")
    qa3 = st.radio("Como a maioria das Inteligências Artificiais no Python (Machine Learning) aprendem a fazer previsões?", ("O programador escreve milhares de regras no If e Else.", "A IA estuda um grande volume de Dados Históricos e aprende os padrões sozinha.", "A IA pesquisa no Google a resposta no momento da previsão.", "A IA adivinha chutando aleatoriamente."), index=None)
    if qa3 == "A IA estuda um grande volume de Dados Históricos e aprende os padrões sozinha.":
        st.success("Exato! Os dados são o 'combustível' que alimenta a Inteligência Artificial!")
    elif qa3 != None:
        st.error("Incorreto! Lembre-se, a IA moderna não usa regras manuais ou Google, ela usa Aprendizado de Máquina.")

elif escolha == "Aula 4: Python Dev":
    st.header("🌐 Aula 4 - Python Dev (Web & Apps)")
    st.write("A área de Desenvolvimento ('Dev') é focada em criar produtos digitais! O Python é muito famoso no backend (a parte invisível do servidor que faz as contas e salva os dados) usando ferramentas como **Django** e **Flask**.")

    st.subheader("a. Criação de Sites e Apps")
    st.write('''
    Hoje em dia, criar aplicativos e sites não exige que você saiba 5 linguagens de programação diferentes.
    Linguagens como o Python evoluíram tanto que você pode usar *Frameworks* (caixas de ferramentas de desenvolvimento) que cuidam de toda a lógica do servidor para você.

    Tudo o que você viu neste curso foi criado 100% em Python com o Framework **Streamlit**! Nós criamos menus, textos, botões e até gráficos sem escrever uma única linha de HTML ou CSS.
    ''')

    st.subheader("b. Desenvolvimento de um Chat ao Vivo")
    st.write("Sabe o WhatsApp, Discord ou Chat de Suporte? Eles utilizam estruturas que mantêm o Histórico e enviam novas mensagens instantaneamente. Veja a lógica básica de como se programa o cérebro de um Chat em Python:")
    st.code('''
# 1. O servidor guarda o histórico de mensagens (numa Lista)
historico_chat = []

# 2. Quando um usuário digita algo e clica em enviar (Função)
def enviar_mensagem(nome_usuario, texto_mensagem):
    # Formata a mensagem
    nova_mensagem = nome_usuario + " disse: " + texto_mensagem

    # Salva no Histórico do servidor
    historico_chat.append(nova_mensagem)

    # Atualiza a tela de todo mundo mostrando a mensagem nova
    print(nova_mensagem)

# 3. Simulando a conversa:
enviar_mensagem("Carlos", "Olá, alguém aí?")
enviar_mensagem("Maria", "Oi Carlos! Tudo bem?")
    ''', language='python')

    st.markdown("---")
    st.subheader("🧠 Quiz Final Dev")
    qa4 = st.radio("Qual o papel principal do Python na construção tradicional de sites e aplicativos complexos?", ("O Python cria as cores, fontes e animações bonitas da página.", "O Python roda no Back-End, cuidando das regras de negócio, cálculos e conexão com banco de dados.", "O Python fabrica as peças de hardware do celular.", "Nenhuma das alternativas."), index=None)
    if qa4 == "O Python roda no Back-End, cuidando das regras de negócio, cálculos e conexão com banco de dados.":
        st.success("Exatamente! Ele é o 'Cérebro' ou 'Motor' invisível dos grandes sites. Você concluiu a Evolução! 🎈🎉")
        st.balloons()
    elif qa4 != None:
        st.error("Ops! Tente novamente. Lembre-se do papel do Python no servidor (backend).")

st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido para transformar você em um Programador Profissional!")
