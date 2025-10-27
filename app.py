import os

# Lista de restaurantes
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

# Exibe o nome estilizado do programa
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

# Exibe o menu de opções
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')
    print('Encerrando o programa. Obrigado por utilizar o Sabor Express!\n')

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('⚠️ Opção inválida!\n')
    voltar_ao_menu_principal()

# Formata subtítulos com separadores
def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

# Cadastra um novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

# Lista os restaurantes cadastrados
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f"{'Nome do restaurante':<22} | {'Categoria':<20} | Status")
    print('-' * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado ✅' if restaurante['ativo'] else 'Desativado ❌'
        print(f"{nome_restaurante:<22} | {categoria:<20} | {ativo}")
    voltar_ao_menu_principal()

# Alterna o estado (ativo/desativado) de um restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {nome_restaurante} foi {status} com sucesso!')
            break

    if not restaurante_encontrado:
        print('⚠️ Restaurante não encontrado!')

    voltar_ao_menu_principal()

# Escolhe a opção digitada pelo usuário
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

# Função principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
