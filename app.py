import streamlit as st

st.set_page_config(page_title="Curso de Python Básico", page_icon="🐍", layout="wide")

st.sidebar.title("🐍 Curso de Python Básico")
st.sidebar.markdown("Aprenda os conceitos básicos do Python passo a passo!")

menu = [
    "1. Introdução",
    "2. Variáveis",
    "3. Sinais e Operadores",
    "4. Aspas (Strings)",
    "5. Parênteses, Colchetes e Chaves",
    "6. Tomando Decisões (If/Else)",
    "7. Repetições (For e While)",
    "8. Funções (def)",
    "9. Tratamento de Erros (Try/Except)"
]
escolha = st.sidebar.radio("Navegação:", menu)

st.title("Bem-vindo ao Curso de Python! 🚀")

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
    st.subheader("🧠 Quiz Final!")
    q9 = st.radio("Para que serve o bloco `except`?", ("Para tentar executar um código perigoso.", "Para executar algo SOMENTE quando um erro acontecer, evitando que o programa feche.", "Para encerrar o programa de propósito.", "Para acelerar o código."), index=None)
    if q9 == "Para executar algo SOMENTE quando um erro acontecer, evitando que o programa feche.":
        st.success("Você acertou! Ele é a 'rede de segurança' do seu programa! 🎉")
        st.balloons()
    elif q9 != None:
        st.error("Pense um pouco mais na tradução de 'Exceto' (se der erro).")

st.sidebar.markdown("---")
st.sidebar.info("Este aplicativo foi criado para ajudar você a entender os fundamentos do Python!")
