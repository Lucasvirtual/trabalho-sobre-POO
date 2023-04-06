from Categoria import Categoria

class Produto:
    def __init__(self, nome, custo, categoria):
        self._nome = nome.upper()
        self._custo = custo
        self.qtd_estoque = 0
        self.categoria = categoria


    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.upper()

    @property
    def custo(self):
        return self._custo

    @nome.setter
    def custo(self, novo_custo):
        self._custo = novo_custo()



    def __str__(self):
        return f"NOME: {self._nome}, CATEGORIA: {self.categoria}, ESTOQUE: {self.qtd_estoque} PREÇO VENDA: R${self.preco_venda():.2f}"



    @staticmethod
    def cadastrar_produtos(lista_produtos,categorias):
        try:
            nomeProd = str(input("Informe o nome: "))
            _custo = float(input("Informe o preço do produto: "))

            for i, item in enumerate(categorias):
                print(f"{i} - NOME: {item}")

            categorias = categorias[int(input("Escolha uma categoria: "))]
            prod = Produto(nomeProd, _custo, categorias)
            lista_produtos.append(prod)
            produtos = lista_produtos

            print("PRODUTO CADASTRADO")
            for i, produto in enumerate(produtos):
                print(produto)

            return produtos

        except:
            print('Deve ser digitado o indice da categoria')



    @staticmethod
    def adicionar_estoque(lista_produtos):
        for i, item in enumerate(lista_produtos):
            print(f"{i + 1}, {item}")

        escolha = int(input("Qual produto você quer adicionar estoque ? "))

        novoEstoque = int(input("Quantos você quer adicionar ? "))

        escolhaProduto = lista_produtos[escolha - 1]
        escolhaProduto.qtd_estoque += novoEstoque

        print(f"Estoque atualizado: {escolhaProduto}")



    @staticmethod
    def remover_estoque(produtos):
        print("Escolha o produto que deseja remover do estoque:")
        for i, produto in enumerate(produtos):
            print(f"{i + 1} - {produto}")

        escolha = int(input("Digite o número correspondente ao produto: "))
        produto = produtos[escolha - 1]

        while True:
            qtd_remover = int(input(f"Digite a quantidade de {produto._nome} a ser removida do estoque: "))
            if qtd_remover > produto.qtd_estoque:
                print(
                    f"Não é possível remover {qtd_remover} unidades do estoque. Apenas {produto.qtd_estoque} unidades estão disponíveis.")
            else:
                break

        produto.qtd_estoque -= qtd_remover
        print(f"{qtd_remover} unidades de {produto._nome} foram removidas do estoque.\n{produto}")



    @staticmethod
    def excluir_produto(lista_produtos):

            for produto in lista_produtos:
                print(produto)
            nome_produto = input("Digite o nome do produto a ser excluído: ").upper()

            if produto._nome == nome_produto:
                lista_produtos.remove(produto)
                print("Produto excluído com sucesso!")
                return
            print("Produto não encontrado na lista de produtos ou digite o nome exatamente como mostra")


    def preco_venda(self):
        return self._custo * (1 + self.categoria.perc_lucro / 100)