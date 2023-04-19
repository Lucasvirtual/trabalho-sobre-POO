# trabalho-sobre-POO
Contexto:
A empresa Kratos Store realiza a venda uma variedade de produtos que são
distribuídos em 3 categorias:
➔ Tecnologia - Notebooks, mouses, teclados, dispositivos de armazenamento de
dados, PCs, entre outros.
➔ Acessórios - Canecas, garrafas, chaveiros, porta-copos, entre outros.
➔ Papelaria - Papel, caneta, lápis, pilotos de quadro, entre outros.
O valor da venda de cada produto é calculado a partir do custo de compra do
produto acrescido de uma porcentagem do valor do custo, que representa o lucro esperado
pelo produto daquela categoria. Exemplos:
Notebook ASUS M515DA
Custo: R$ 2000,00
Porcentagem de lucro da categoria Tecnologia: 25%
Valor da venda: R$ 2500,00
Caneca Estampa Floral
Custo: R$ 10,00
Porcentagem de lucro da categoria Acessórios : 20%
Valor da venda: R$ 12,00
Caneta BIC azul
Custo: R$ 1,00
Porcentagem de lucro da categoria Papelaria : 18%
Valor da venda: R$ 1,18
Você foi chamado para criar um programa capaz registrar a entrada de produtos em
estoque e orientar os funcionários sobre os preços destes produtos. Siga as orientações a
seguir para a elaboração do programa.
Orientações iniciais

● Você precisará criar uma Classe chamada Categoria.
  ○ Uma Categoria possui um nome e uma porcentagem de lucro.
  ○ Crie os atributos e aplique o encapsulamento neles, gerando métodos para
manipular e visualizar os atributos que julgar necessário.
  ○ Crie um método construtor que receberá como parâmetros, os dados
necessários para instanciar uma Categoria.
  ○ Crie uma sobrecarga no método __str__, para que ele retorne apenas o
nome da Categoria.

● Você precisará criar uma classe chamada Produto.
  ○ Um Produto possui um nome, um custo de compra, uma quantidade em
estoque e uma Categoria.
  ○ Crie os atributos e aplique o encapsulamento neles, gerando métodos para
manipular e visualizar os atributos que julgar necessário.
  ○ Crie um método construtor que receberá como parâmetros, os dados
necessários para instanciar um Produto.
  ○ Crie um método preco_venda() que deverá calcular e retornar qual o preço
da venda do produto, com base na porcentagem de lucro definida pela
categoria dele.
  ○ Crie uma sobrecarga no método __str__, para que ele retorne uma string no
seguinte formato:
“Produto nome_produto, categoria nome_categoria, qtd_Estoque em
estoque, preço de venda R$ valor_venda”
Obs.: O nome_categoria deve ser exibido através do método toString da
categoria.
Obs.: O valor_venda deve ser exibido através do retorno do método
preco_venda(), que deve calcular qual o valor pelo qual o produto deve ser
vendido, com base na categoria do produto.

● No programa principal (main), deve existir uma lista de Produtos e uma Lista de
Categorias, onde serão guardados os produtos e as categorias cadastradas pelo
sistema.

● Crie um menu para controlar as ações do seu programa. Esse menu deve ser
exibido em loop pelo seu programa, até que a opção 8 seja informada.
○ MENU PRINCIPAL
1 - Cadastrar Categoria
2 - Excluir Categoria
3 - Cadastrar Produto
4 - Excluir Produto
5 - Exibir Produtos Cadastrados
6 - Adicionar Estoque a Produto
7 - Remover Estoque de Produto
8 - Sair

Orientações sobre as operações do programa

● As classes Categoria e Produto possuirão métodos estáticos necessários para
manipular as operações do programa (cadastro, exclusão, edição), além dos demais
métodos necessários para os objetos instanciados.

● Realizar o cadastro de categorias de produtos.
  ○ Para realizar o cadastro da categoria, crie um método estático na Classe
Categoria , que será chamado pelo método main para solicitar ao usuário, os
dados para a criação da categoria (além de realizar as validações
necessárias).
  ○ O programa só deve permitir o cadastro de até 5 categorias. Caso o usuário
tente cadastrar uma sexta, ele deve ser advertido e o programa deve retornar
ao menu inicial.
  ○ Para cadastrar uma categoria, deve-se informar o nome dela e o valor da
porcentagem de lucro desta categoria.
  ○ O registro do nome da categoria deve ser armazenado todo em caixa alta,
mesmo que o usuário informe um nome com letras minúsculas. (recomendo
que faça no construtor da classe Categoria)

● Realizar a exclusão de categorias de produtos.
  ○ Para realizar a exclusão da Categoria, crie um método estático na Classe
Categoria, que será chamado pelo método main para solicitar ao usuário, os
dados para a exclusão da Categoria (além de realizar as validações
necessárias).
  ○ A exclusão deve ser feita informando o nome da categoria, e deve funcionar
independente de o usuário informar nomes com letras maiúsculas ou
minúsculas.
  ○ Uma Categoria só pode ser excluída se não houver produtos cadastrados
utilizando a categoria. Caso uma categoria tente ser removida, ainda com
produtos em estoque vinculados a ela, o programa deve informar quais
produtos estão vinculados à categoria, e retornar ao menu inicial.

● Realizar o cadastro de um produto.
  ○ Para realizar o cadastro de um Produto, crie um método estático na Classe
Produto, que será chamado pelo método main para solicitar ao usuário, os
dados para o cadastro do Produto(além de realizar as validações
necessárias).
  ○ Para cadastrar um produto, deve informar o nome do produto, o preço e a
sua categoria (que deve estar previamente cadastrada no programa). Por
padrão, a quantidade de um produto em estoque deve ser iniciada sempre
com o valor 0.
  ○ O registro do nome do produto deve ser armazenado todo em caixa alta,
mesmo que o usuário informe um nome com letras minúsculas.

● Realizar a exclusão de um produto.
  ○ Para realizar a exclusão de um Produto, crie um método estático na Classe
Produto, que será chamado pelo método main para solicitar ao usuário, os
dados para a exclusão do Produto(além de realizar as validações
necessárias).
  ○ A exclusão deve ser feita informando o nome do produto, independente de o
usuário informar nomes com letras maiúsculas ou minúsculas.

● Exibir produtos cadastrados.
  ○ Crie um método estático na Classe Produto, que será chamado pelo método
main para exibir o método __str__ de cada produto cadastrado.
  ○ Obs: Para exibir o __str__ de um objeto, basta printar o próprio objeto.

● Adicionar estoque ao produto.
  ○ Crie um método estático na Classe Produto, que será chamado pelo método
main para adicionar uma quantidade ao estoque de um produto informado
pelo usuário.

● Remover o produto do estoque.
  ○ Crie um método estático na Classe Produto, que será chamado pelo método
main para remover uma quantidade do estoque de um produto informado
pelo usuário.
  ○ O estoque de um produto não pode ficar negativo. Caso o usuário informe
um valor para remoção que deixe o estoque negativo, ele deve ser advertido,
e o dado deve ser solicitado novamente.
Regras gerais

● Seu programa deve ser desenvolvido com base nos conceitos de POO.

● Todas as Classes e métodos devem possuir uma Docstring. Oriente-se pela PEP
257: https://peps.python.org/pep-0257
