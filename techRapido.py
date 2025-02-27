import os

restaurantes = [{'nome':'Molhuar', 'categoria':'Italiana', 'ativo':False}, 
                {'nome':'Melhor da região', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Datebayo', 'categoria':'Japonesa', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Resulta o nome do programa escolhido estilizado na tela '''
    print('''
████████╗███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░██╗██████╗░░█████╗░
╚══██╔══╝██╔════╝██╔══██╗██║░░██║  ██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗
░░░██║░░░█████╗░░██║░░╚═╝███████║  ██████╔╝███████║██████╔╝██║██║░░██║██║░░██║
░░░██║░░░██╔══╝░░██║░░██╗██╔══██║  ██╔══██╗██╔══██║██╔═══╝░██║██║░░██║██║░░██║
░░░██║░░░███████╗╚█████╔╝██║░░██║  ██║░░██║██║░░██║██║░░░░░██║██████╔╝╚█████╔╝
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░
''')

def exibir_opcoes():
    ''' Informa todas as opções disponíveis do menu principal '''
    print(' --------------- OPÇÕES ----------------')
    print('| 1. Cadastrar restaurante.             |')
    print('| 2. Lista restaurante.                 |')
    print('| 3. Alternar estado do restaurante.    |')
    print('| 4. Sair.                              |')
    print('|_______________________________________|\n')

def finalizar_programa():
    ''' Resulta uma mensagem de finalização do programa '''
    exibir_subtitulo('Finalizando o programa.')

def voltar_ao_menu_principal():
    ''' Realiza a solicitação  de pressionar um tecla para voltar ao menu '''
    input('Digite uma tecla para voltar ao menu principal. ')
    main()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Subtítulo estilizado na tela '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes.')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Realiza uma lista dos retaurantes presentes até o momento'''
    exibir_subtitulo('Listando restaurantes.')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja realizar a alteração de estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!\n' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso\n'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.\n')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você selecionou a opção {opcao_escolhida}.')
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()