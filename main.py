from Categoria import Categoria
from Produto import Produto

produtos = []
categorias = []

while True:
    print("\nMENU PRINCIPAL")
    print("1 - Cadastrar Categoria")
    print("2 - Excluir Categoria")
    print("3 - Cadastrar Produto")
    print("4 - Excluir Produto")
    print("5 - Exibir Produtos Cadastrados")
    print("6 - Adicionar Estoque a Produto")
    print("7 - Remover Estoque de Produto")
    print("8 - Sair")
    print()

    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            Categoria.cadastrar_categoria(categorias)

        if opcao == 2:
            Categoria.excluirCat(categorias, produtos)

        if opcao == 3:
            Produto.cadastrar_produtos(produtos, categorias)

        if opcao == 4:
            Produto.excluir_produto(produtos)

        if opcao == 5:
            for itens in produtos:
                print(itens)

        if opcao == 6:
            Produto.adicionar_estoque(produtos)

        if opcao == 7:
            Produto.remover_estoque(produtos)

        if opcao == 8:
            print("################ PROGRAMA FINALIZADO ################")
            break

    except ValueError as erro:
        print('A opção informada deve ser um número inteiro')