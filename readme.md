---

# Resolvendo Códigos em Python com GitHub Copilot (ou ChatGPT!)

Olá! Neste repositório, você encontrará exemplos de resoluções de códigos em **Python** utilizando o **GitHub Copilot**, uma ferramenta de inteligência artificial que sugere trechos de código enquanto você digita, facilitando o desenvolvimento.

> ⚠️ **Não tem acesso ao GitHub Copilot?**  
> Sem problemas! Você pode usar o **ChatGPT** como seu copiloto de estudos e obter as mesmas ideias e sugestões. O importante é aprender praticando!

---

## 📘 Conteúdo

### 1. Concatenando Dados

**Descrição:**  
Recebemos dois dados diferentes do usuário e os concatenamos em uma única string.

**O que você vai aprender:**
- Manipulação de strings (`str`)
- Concatenação de strings
- Entrada de dados com `input()`
- Utilização eficiente do GitHub Copilot ou ChatGPT para sugerir soluções

---

### 2. Repetindo Textos

**Descrição:**  
Solicitamos uma string e um número inteiro como entrada. O programa retorna a string repetida o número de vezes informado.

**O que você vai aprender:**
- Manipulação de strings (`str`)
- Tipos numéricos inteiros (`int`)
- Repetição de strings com operadores
- Entrada de dados com `input()`
- Como aproveitar sugestões de ferramentas de IA para resolver problemas

---

### 3. Operações Matemáticas Simples

**Descrição:**  
Resolvemos operações matemáticas básicas com dados fornecidos pelo usuário.

**O que você vai aprender:**
- Operações matemáticas básicas (`+`, `-`, `*`, `/`)
- Conversão de tipos
- Entrada e saída de dados
- Uso de ferramentas de IA para acelerar a escrita de código

---

## 🤖 Dica de Estudo

Experimente escrever o início do código e veja como o GitHub Copilot ou o ChatGPT sugerem o restante. Analisar essas sugestões é uma ótima forma de aprender boas práticas e descobrir soluções que talvez você ainda não conheça.

---

Um exemplo visual de como o repositório poderia ser estruturado. Deseja isso?

📁 resolvendo-codigos-python-copilot
├── README.md
├── 📁 exemplos
│   ├── 1_concatenando_dados.py
│   ├── 2_repetindo_textos.py
│   └── 3_operacoes_matematicas.py
├── 📁 imagens
│   └── exemplo_sugestao_copilot.png  (opcional, se quiser ilustrar)
└── .gitignore


1_concatenando_dados.py

# Solicita dois dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatena os dados
resultado = dado1 + " " + dado2

# Exibe o resultado
print("Resultado da concatenação:", resultado)


2_repetindo_textos.py

# Solicita dois dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatena os dados
resultado = dado1 + " " + dado2

# Exibe o resultado
print("Resultado da concatenação:", resultado)


3_operacoes_matematicas.py

# Solicita dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza operações básicas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"

# Exibe os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

Essa organização ajuda os visitantes a explorarem cada parte do projeto com clareza.