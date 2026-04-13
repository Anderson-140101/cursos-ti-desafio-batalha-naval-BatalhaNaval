import streamlit as st

st.set_page_config(page_title="Curso de Python Básico", page_icon="🐍", layout="wide")

st.sidebar.title("🐍 Curso de Python Básico")
st.sidebar.markdown("Aprenda os conceitos básicos do Python passo a passo!")

menu = ["1. Introdução", "2. Variáveis", "3. Sinais e Operadores", "4. Aspas (Strings)", "5. Parênteses, Colchetes e Chaves"]
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

st.sidebar.markdown("---")
st.sidebar.info("Este aplicativo foi criado para ajudar você a entender os fundamentos do Python!")
