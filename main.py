# Upgrade: Função para tratar erros de entrada quando o usuário digita um valor não inteiro.
def leia_int(texto): 
    try:
        return int(input(texto))
    except ValueError:
        # Upgrade: cores ao terminal para destacar mensagens de erro e sucesso.
        print('\033[31mDIGITE UM NÚMERO INTEIRO\033[m') 
        return leia_int(texto)

# Upgrade: Função para melhorar a formatação e legibilidade do terminal.
def linha(): 
    print('-' * 50)

# Upgrade: arquivo de texto para armazenar as informações dos livros de forma que não se perca ao encerrar a execução.
def gravar_dados(livro, arquivo):
    try:
        with open(arquivo, 'a') as file:
            for valor in livro:
                file.write(f'{valor[0]},{valor[1]},{valor[2]}\n')
    except:
        print('\033[31mOCORREU UM ERRO AO GRAVAR DADOS\033[m')

# Calcular media dos anos
def calcular_media(anos):
    total = sum(anos)
    return total / len(anos)

# Exibir os dados dos alunos
def exibir_dados(arquivo):
    menorAno = 2025
    maisRecente = 0
    anoLivros = []
    print('BIBLIOTECA'.center(50))
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
    for i, linha in enumerate(linhas, start=1):
        livro = linha.split(',')
        anoLivros.append(int(livro[2]))
        if int(livro[2]) < menorAno:
            menorAno = int(livro[2])
            livroMenorAno = ((livro[0],int(livro[2])))
        if int(livro[2]) >= 2020:
            maisRecente += 1

        print(f'LIVRO {i}: Nome: {livro[0]} | Autor: {livro[1]} | Ano: {livro[2]}'.strip())
    print(f'\nLivro mais antigo: {livroMenorAno[0]} ({livroMenorAno[1]}) ')
    print(f'Livros publicados após 2020: {maisRecente}')
    mediaAnos = calcular_media(anoLivros)
    print(f'Média do ano de publicação dos livros: {mediaAnos:.2f}')


# Variaveis
arquivo = 'biblioteca.txt' 

# Entrada de dados
# Upgrade: loop infinito para cadastrar vários livros enquanto o usuário não escolhe parar a execução
while True:
    linha()
    # Upgrade: Menu para selecionar se quer cadastrar livro ou exibir livros cadastrados e informações adicionais
    print('MENU'.center(50)) 
    print('1 - Cadastrar novo livro')
    print('2 - Mostrar biblioteca')
    print('3 - Sair')
    opcao = leia_int('\nDigite a opção: ')
    linha()
    
    if opcao == 1:
        livro = []
        nome = str(input('Digite o nome do livro: ')).strip().title()
        autor = str(input('Digite o nome do autor do livro: ')).strip().title()
        ano = leia_int('Digite o ano de publicação do livro: ')
        livro.append((nome, autor, ano))
        gravar_dados(livro, arquivo)
        linha()
        print('\033[32mDADOS GRAVADOS\033[m'.center(50))
    elif opcao == 2:
        exibir_dados(arquivo)
    elif opcao == 3:
        print('SAINDO...'.center(50))
        linha()
        break
    else:
        print('\033[31mOPÇÃO INVALIDA\033[m')
        print('Digite uma das opções do menu!')
        