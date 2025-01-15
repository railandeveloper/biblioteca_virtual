'''Descrição do Projeto: Gerenciador de Biblioteca Virtual
Um sistema que permite gerenciar livros em uma biblioteca virtual. O sistema deve permitir:

Cadastrar Livros: Título, autor, ano de publicação e gênero.
Listar Livros: Exibir todos os livros cadastrados.
Procurar Livros: Buscar por título ou autor.
Remover Livros: Remover um livro específico pelo índice.
Salvar e Carregar Dados: Salvar os dados em um arquivo JSON e carregar automaticamente ao iniciar.
Limpar o Terminal: Opção para limpar a tela.
Sair do Sistema: Finalizar a execução.
Estrutura do Projeto
plaintext
Copiar código
biblioteca_virtual/
├── main.py          # Arquivo principal que executa o programa
├── modulo.py        # Contém funções auxiliares (menu, validações, exibição)
├── biblioteca.json  # Arquivo JSON para armazenar os livros
└── README.md        # Documentação do projeto
Funcionalidades e Dicas
Classe Livro:

Crie uma classe Livro para representar os livros.
A classe deve ter atributos como título, autor, ano e gênero.
Classe Biblioteca:

Crie uma classe Biblioteca para gerenciar a lista de livros.
Métodos:
adicionar_livro
remover_livro
listar_livros
procurar_livro
salvar_dados
carregar_dados
Arquivo modulo.py:

Crie funções para exibir menus e realizar validações de entrada (como validar se o ano é numérico ou se o título contém apenas letras).
Arquivo main.py:

Implemente a lógica principal com um loop para o menu.
Chame os métodos da classe Biblioteca conforme a opção escolhida.
'''