
## Maquina de vendas Antony V B
ModoMaquina = 0
produtos = ['Vazio','Coca','Pepsi','Monster','Café','Redbull']
precos = [0,3.75,3.67,9.95,1.25,13.99]
estoque = [0,2,5,1,100,2]
produtoEscolhido = 0
valorRecebido = 0
valorProdutoAtual = 0
troco = 0
emUso = 1
notasMoedas = [0,5,1,0.2,0.1,0.01]
estoqueNotasDinheiroMaquina = [[0,100,100,100,100,100],[631]]
subtrairDinheiroMaquina = 0
ListaTroco = []
emEstoque = 1
edição = 0
editor = 0
estoqueOuPreco = 0
excluido = 0
ModoMaquina = 0

def validarEstoque():
    global emEstoque
    if estoque[produtoEscolhido] <= 0:
        print('Estoque esgotado')
        emEstoque = 0
    else:
        emEstoque =1

def trocoF(valorTroco):
    global ListaTroco, estoqueNotasDinheiroMaquina
    for i in range(1,len(notasMoedas)):
        notasUtilizadas = 0
        if estoqueNotasDinheiroMaquina[1][0] >= valorTroco:
            while (valorTroco + 0.0001) >= notasMoedas[i] and estoqueNotasDinheiroMaquina[0][i] > 0:
                valorTroco -= notasMoedas[i]
                notasUtilizadas +=1
                subtrairDinheiroMaquina = estoqueNotasDinheiroMaquina[1][0]
                subtrairDinheiroMaquina -= notasMoedas[i]
                estoqueNotasDinheiroMaquina[1][0] = subtrairDinheiroMaquina
                estoqueNotasDinheiroMaquina[0][i] -= 1
            ListaTroco.append(notasUtilizadas)

ModoMaquina = int(input('Digite 1 para entra no modo normal e 0 para entrar no modo administrativo: '))
while ModoMaquina > 1 or ModoMaquina < 0:
    ModoMaquina = int(input('Digite 1 para entra no modo normal e 0 para entrar no modo administrativo: '))
while ModoMaquina ==0:
    edição = int(input('No que gostaria de mexer:\n1 Para adicionar itens na maquina\n2 Para editar o preço e estoque de um produto\n3 Para remover um produto\n4 Para sair deste modo e entrar no normal\n'))
    while edição > 4 or edição < 1:
        edição = int(input('No que gostaria de mexer:\n1 Para adicionar itens na maquina\n2 Para editar o preço e estoque de um produto\n3 Para remover um produto\n4 Para sair deste modo e entrar no normal\n'))
    if edição == 1:
        produtos.append(str(input('Digite o produto que deseja adicionar: ')))
        precos.append(int(input('digite o valor deste produto(use ponto não vírgula): ')))
        estoque.append(int(input('Digite quantos tem no estoque: ')))
    elif edição ==2:
        print("Produtos atuais: ")
        for i in range(1,len(produtos)):
            print(f"{produtos[i]} {[i]}")
        editor = int(input('Digite o numero do produto que deseja alterar: '))
        while editor > len(produtos) or editor < 1:
            editor = int(input('Digite o numero do produto que deseja alterar: '))
            estoqueOuPreco = int(input('Digite 1 para mexer no estoque do produto e 2 para mexer no preço: '))
        while estoqueOuPreco < 1 or estoqueOuPreco > 2:
            estoqueOuPreco = int(input('Digite 1 para mexer no estoque do produto e 2 para mexer no preço: '))
        if estoqueOuPreco == 1:
            estoque[editor] = int(input('Digite a nova quantidade do estoque: '))
        else:
            precos[editor] = int(input('Digite o novo preço: '))
    elif edição == 3:
        print("produtos atuais: ")
        for i in range(1,len(produtos)):
            print(f"{produtos[i]} {[i]}")
        excluido = int(input('Digite o numero do produto que será excluido: '))
        while excluido < 1 or excluido > len(produtos):
            excluido = int(input('Digite o numero do produto que será excluido: '))
        produtos.pop(excluido)
        precos.pop(excluido)
        estoque.pop(excluido)
    else:
        ModoMaquina = 1

while ModoMaquina == 1:
    print('Digite o codigo do produto a ser comprado: ')
    for i in range(1,len(produtos)):
        print(f"{produtos[i]} ({precos[i]} 'Reais') Digite: {i}")
    produtoEscolhido = int(input())
    while produtoEscolhido<1 or produtoEscolhido> len(produtos):
        produtoEscolhido = int(input('Digite o codigo do produto a ser comprado: '))
    while produtoEscolhido > len(produtos) or produtoEscolhido<=0:
        produtoEscolhido = int(input('Erro digite novamente: '))
    valorProdutoAtual = precos[produtoEscolhido]
    validarEstoque()
    if emEstoque == 1:
        print(f"O valor a ser pago é {valorProdutoAtual}")
        valorRecebido = float(input(f'Digite o valor que você vai inserir(use pontos não vírgula): '))
    while valorRecebido < valorProdutoAtual:
        valorRecebido = float(input(f'Valor insulficiente.\nDigite o valor que você vai inserir(use pontos não vírgula): '))
    valorRecebido -= precos[produtoEscolhido]
    trocoF(valorRecebido)
    print('Este é o seu troco: ')
    if len(ListaTroco) == 0:
        print('Sem troco, a maquina não tem notas ou moedas os suficiente. Compra cancelada ')
    else:
        for i in range((len(notasMoedas))-1):
            print(f'De {notasMoedas[i+1]} reais foram {ListaTroco[i]} ')
        estoque[produtoEscolhido] -=1
    ListaTroco.clear()

