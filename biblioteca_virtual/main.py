# Arquivo principal que executa o programa


import time
from modulo import exibir_menu, limpar_tela, Biblioteca


biblioteca = Biblioteca()


while True:
    exibir_menu()
    print()
    try:
        opcao = int(input('Digite sua opcao: ')) 
    except ValueError:
        print("\033[91mErro: Digite um número inteiro válido.\033[0m")
        continue 

    if opcao == 1:
        biblioteca.adicionar_livro()
               
    elif opcao == 2:
        biblioteca.remover_livro()
        
    elif opcao == 3:
        biblioteca.listar_livros()
        
    elif opcao == 4:
        biblioteca.procurar_livros()
        
    elif opcao == 5:
        limpar_tela()
    
    elif opcao == 6:
        print(f'Saindo do programa...')
        time.sleep(2)
        break            
        
    else:
        print("\033[91mOpcao invalida.\033[0m")                