import os 

restaurantes = [{'nome':'Pizza hut', 'categoria':'Pizzaria', 'ativo':False}, 
                    {'nome':'Braza burguer', 'categoria':'Hamburgueria', 'ativo':True},
                    {'nome':'Portal da picanha', 'categoria':'Carne', 'ativo':False}]


def exibir_nome_do_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. sair\n")

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    print("Opcao Invalida!")
    input("Insira uma tecla para volta ao menu: ")
    main()

def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que voce deseja cadastrar: ")
    categoria = input(f"Informe a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante,"categoria": categoria,"ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O nome restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("insira uma tecla para voltar pro menu principal: ")
    main()

def listar_restaurantes():
    os.system("cls")
    print("Listando os restaurantes\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    input("insira uma tecla para voltar pro menu principal: ")
    main()
def alternar_estado_restaurante():
    os.system("cls")
    print("Alternando o estado do restaurante")
    nome_restaurante = input("Informe o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False 

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O Restaurante {nome_restaurante}, foi atividado com sucesso!" if restaurante["ativo"] else f"O Restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print("O Restaurante nao foi encontrado!")

    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app() 
        else :
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__":
    main()

