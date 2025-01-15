# Contém funções auxiliares (menu, validações, exibição)
import json
import os


class Livro():
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

     # definindo como o objeto sera exibido
    def __str__(self):
        return f"Título: {self.titulo.title()}, Autor: {self.autor}, Ano: {self.ano}, Gênero: {self.genero.title()}"


class Biblioteca():
    def __init__(self):
        self.lista_de_livros = carregar_dados()

    def adicionar_livro(self):
        print('Digite os dados do livro: ')
        
        def validar_entrada_str(texto):
            entrada = texto.strip()
            if all(letra.isalpha() or letra.isspace() for letra in entrada):
                return entrada.lower()
            else:
                exibir_erro('A entrada aceita apenas caracteres de texto')
                return None
            
        while True:
            titulo = str(input('Titulo: ')).strip().lower()
            if not titulo:
                exibir_erro('O título não pode ser vazio')
            else:
                break
            
        while True:
            autor =  validar_entrada_str(input('Autor: '))
            if autor:
                break
            
        while True:
            try:
                ano = int(input('Ano: '))
                if ano > 0:
                    break
                else:
                    exibir_erro('O ano deve ser um numero positivo.')
            except:
                exibir_erro('O ano deve conter apenas números.')
                
        while True:            
            genero = validar_entrada_str(input('Genero: '))
            if genero:
                break
        # criando o objeto novo livro com os dados inseridos pelo usuario
        novo_livro = Livro(titulo, autor, ano, genero)
        self.lista_de_livros.append(novo_livro)
        salvar_dados(self.lista_de_livros)
        print(f"\033[92mLivro '{titulo.title()}' adicionado com sucesso!\033[0m")
        

    def remover_livro(self):
        if self.lista_de_livros:
            self.listar_livros()
            while True:    
                try:    
                   indice_a_remover = int(input('Qual o índice do livro que você gostaria de remover?: '))
                   if indice_a_remover >=0 and indice_a_remover < len(self.lista_de_livros):
                        livro_removido = self.lista_de_livros.pop(indice_a_remover)
                        salvar_dados(self.lista_de_livros)
                        print(f"\033[92mLivro '{livro_removido.titulo}' removido com sucesso!\033[0m")
                        break
                   else:
                       exibir_erro(f'o indice nao e valido, verifique os indices disponiveis')
                except ValueError:
                    exibir_erro('Erro: O índice deve ser um número inteiro válido.')
                except IndexError:
                    exibir_erro('Erro: Índice fora do intervalo. Escolha um índice válido.')
        else:
            exibir_erro('A biblioteca está vazia. Nenhum livro para remover.')


    def listar_livros(self):
        if not self.lista_de_livros:
            exibir_erro('A biblioteca está vazia. Nenhum livro cadastrado.')
        else:
            print("\033[92m\n=== Livros na Biblioteca ===\033[0m")
            for indice, conteudo in enumerate(self.lista_de_livros):
                print(f"{indice}. {conteudo}")


    def procurar_livros(self):
        if self.lista_de_livros:
            nome__livro_procurado = str(input(f'Qual o nome do livro que voce procura?: ')).strip().lower()
            encontrado = False 
            for livro in self.lista_de_livros:
                if nome__livro_procurado in livro.titulo.lower():
                    print("\033[92m=== Encontrado ===\033[0m")
                    print(f'{livro} ')
                    encontrado = True
            if not encontrado:
                exibir_erro('=== Nenhum livro encontrado. ===')
        else:
            exibir_erro('A biblioteca está vazia.') 
                       

def salvar_dados(lista_livros):
        with open('biblioteca.json', 'w') as arquivo:
            json.dump([livro.__dict__ for livro in lista_livros], arquivo, indent=4)
            

def carregar_dados():
    try:
        with open('biblioteca.json', 'r') as arquivo:
            lista_de_dicionarios = json.load(arquivo)
            # Converte cada dicionário em um objeto Livro
            return [Livro(**livro) for livro in lista_de_dicionarios]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def exibir_menu():
    print("\033[92m=== Suas Opcoes ===\033[0m")
    print("\033[92m1 - ADICIONAR LIVRO \033[0m")
    print("\033[92m2-  REMOVER LIVRO\033[0m")
    print("\033[92m3-  LISTAR LIVROS\033[0m")
    print("\033[92m4-  PROCURAR LIVRO\033[0m")
    print("\033[92m5-  LIMPAR TELA\033[0m")
    print("\033[92m6-  FECHAR PROGRAMA\033[0m")


def limpar_tela():
    os.system('cls')

    
def exibir_erro(msg):
      print(f"\033[91m{msg}.\033[0m")        