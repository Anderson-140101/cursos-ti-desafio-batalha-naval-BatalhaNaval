from streamlit.testing.v1 import AppTest

def test_app_initial_state():
    """Test the initial state of the application when first loaded."""
    at = AppTest.from_file("app.py").run()

    # Ensure the app runs without exceptions
    assert not at.exception

    # Check sidebar elements
    assert at.sidebar.title[0].value == "🐍 Curso de Python Básico"
    assert "Aprenda os conceitos básicos do Python" in at.sidebar.markdown[0].value

    # Check main title
    assert at.title[0].value == "Bem-vindo ao Curso de Python! 🚀"

    # Check that it defaults to the first section (Introdução)
    assert at.header[0].value == "1. Introdução ao Python"

def test_app_navigation_introducao():
    """Test navigation to the 1. Introdução section explicitly."""
    at = AppTest.from_file("app.py").run()

    at.sidebar.radio[0].set_value("1. Introdução").run()
    assert not at.exception
    assert at.header[0].value == "1. Introdução ao Python"
    assert "Como mostrar algo na tela?" in at.subheader[0].value

def test_app_navigation_variaveis():
    """Test navigation to the 2. Variáveis section."""
    at = AppTest.from_file("app.py").run()

    # Change navigation to 2. Variáveis
    at.sidebar.radio[0].set_value("2. Variáveis").run()

    assert not at.exception
    assert at.header[0].value == "2. O que são Variáveis?"
    assert at.subheader[0].value == "Exemplos de Variáveis:"
    # Check that the code block and warning are present
    assert len(at.code) > 0
    assert len(at.warning) > 0

def test_app_navigation_sinais_operadores():
    """Test navigation to the 3. Sinais e Operadores section."""
    at = AppTest.from_file("app.py").run()

    at.sidebar.radio[0].set_value("3. Sinais e Operadores").run()
    assert not at.exception
    assert at.header[0].value == "3. Sinais e Operadores Matemáticos"

    # This section has columns and subheaders
    assert len(at.subheader) >= 2
    assert at.subheader[0].value == "Operadores Matemáticos"
    assert at.subheader[1].value == "Operadores de Comparação"

def test_app_navigation_aspas():
    """Test navigation to the 4. Aspas (Strings) section."""
    at = AppTest.from_file("app.py").run()

    at.sidebar.radio[0].set_value("4. Aspas (Strings)").run()
    assert not at.exception
    assert at.header[0].value == "4. Onde colocar as Aspas?"

    assert at.subheader[0].value == "Aspas Simples (' ') vs Aspas Duplas (\" \")"
    assert at.subheader[1].value == "Quando usar três aspas? (''' ''')"

def test_app_navigation_parenteses():
    """Test navigation to the 5. Parênteses, Colchetes e Chaves section."""
    at = AppTest.from_file("app.py").run()

    at.sidebar.radio[0].set_value("5. Parênteses, Colchetes e Chaves").run()
    assert not at.exception
    assert at.header[0].value == "5. Sinais Especiais: (), [], {}"

    # This section has three subheaders
    assert len(at.subheader) >= 3
    assert at.subheader[0].value == "1. Parênteses `( )` - Funções e Tuplas"
    assert at.subheader[1].value == "2. Colchetes `[ ]` - Listas"
    assert at.subheader[2].value == "3. Chaves `{ }` - Dicionários"
