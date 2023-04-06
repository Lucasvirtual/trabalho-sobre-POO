class Categoria:
    def __init__(self, nome: str, perc_lucro):
        self._nome = nome.upper()
        self._perc_lucro = perc_lucro


    def __str__(self):
        return f"{self._nome} - PORCENTAGEM: {self._perc_lucro}"


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.upper()

    @property
    def perc_lucro(self):
        return self._perc_lucro

    @perc_lucro.setter
    def perc_lucro(self, novo_perc_lucro):
        self._perc_lucro = novo_perc_lucro()



    @staticmethod
    def cadastrar_categoria(categorias):
        try:
            nome = str(input("Informe o nome: "))
            perc_lucro = float(input("Informe a porcentagem de lucro: "))
            if len(categorias) <= 4:

                categoria = Categoria(nome, perc_lucro)

                categorias.append(categoria)
                print("Categoria cadastrada com sucesso!")
                for categoria in categorias:
                    print(f"NOME: {categoria._nome} - PORCENTAGEM: {categoria.perc_lucro}%")
            else:
                print("Existe mais de 5 categorias")
        except ValueError as erro:
            print('O percentual de lucro deve ser um valor decimal!')


    @staticmethod
    def excluirCat(categorias,produtos):

        while True:
            existe_prod = False
            for categoria in categorias:
                print(f"NOME: {categoria._nome} - PORCENTAGEM: {categoria.perc_lucro}%")

            if len(categorias) == 0:
                break

            escolhaCat = str(input("Qual categoria você quer excluir ? ou digite sair ")).upper()
            if escolhaCat == "SAIR":
                break


            for i,item in enumerate(produtos):


                if item.categoria.nome == escolhaCat:
                    existe_prod = True
                    print("Existe produto nessa categoria")
                    print(f"Produto vinculado a {escolhaCat}: {item}")
                    break

            if existe_prod == False:
                for categoria in categorias:
                    if categoria._nome == escolhaCat:
                        categorias.remove(categoria)
                        print(f"Categoria '{categoria._nome}' excluída com sucesso!")
                        break
                    else:
                        print(f"Categoria '{escolhaCat}' não encontrada.")
                for categoria in categorias:
                    print(f"NOME: {categoria._nome} - PORCENTAGEM: {categoria.perc_lucro}%")

            else:
                print('Não foi possível excluir a categoria')