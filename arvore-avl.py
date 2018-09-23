### Arvore AVL

from random import sample

### Classe nó
class Node(object):
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dire = None
        self.altura = 1

### Classe árvore

class Arvore(object):

    # Faz a inserção de um novo valor
    def insere(self, raiz, key):
        
        # Caso seja raíz
        if not raiz:
            return Node(key)
        elif key < raiz.valor:
            raiz.esq = self.insere(raiz.esq, key)
        elif key > raiz.valor:
            raiz.dire = self.insere(raiz.dire, key)
        
        # Atualiza a altura da raíz
        raiz.altura = 1 + max(self.getAltura(raiz.esq), self.getAltura(raiz.dire))

        # Recebe o Fator de Balanceamento
        fb = self.getFatorBalanceamento(raiz)

        # Verifica necessidade de balanceamento da árvore
        if fb > 1 and key < raiz.esq.valor:
            return self.rotDir(raiz)
        if fb < -1 and key > raiz.dire.valor:
            return self.rotEsq(raiz)
        if fb > 1 and key > raiz.esq.valor:
            raiz.esq = self.rotEsq(raiz.esq)
            return self.rotDir(raiz)
        if fb < -1 and key < raiz.dire.valor:
            raiz.dire = self.rotDir(raiz.dire)
            return self.rotEsq(raiz)

        return raiz

    # Faz a remoção de um valor específico
    def delete(self, raiz, key):
        
        if not raiz:
            return raiz
        elif key < raiz.valor:
            raiz.esq = self.delete(raiz.esq, key)
        elif key > raiz.valor:
            raiz.dire = self.delete(raiz.dire, key)
        else:
            if raiz.esq is None:
                aux = raiz.dire
                raiz = None
                return aux
            elif raiz.dire is None:
                aux = raiz.esq
                raiz = None
                return aux

            aux = self.getMenorValor(raiz.dire)
            raiz.valor = aux.valor
            raiz.dire = self.delete(raiz.dire, aux.valor)

    def rotEsq(self, a):

        aux = a
        b = a.dire
        c = b.esq

        a = b
        a.esq = aux
        aux.dire = c

        a.altura = 1 + max(self.getAltura(a.esq), self.getAltura(a.dire))
        b.altura = 1 + max(self.getAltura(b.esq), self.getAltura(b.dire))

        return a

    def rotDir(self, a):
        
        aux = a
        b = a.esq
        c = b.dire

        a = b
        a.dire = aux
        aux.esq = c

        a.altura = 1 + max(self.getAltura(a.esq), self.getAltura(a.dire))
        b.altura = 1 + max(self.getAltura(b.esq), self.getAltura(b.dire))

        return a

    def getAltura(self, raiz):

        if not raiz:
            return 0
        else:
            return raiz.altura    
    
    def getFatorBalanceamento(self, raiz):
        if not raiz:
            return 0
        else:
            return self.getAltura(raiz.esq) - self.getAltura(raiz.dire)
    
    def getMenorValor(self, raiz):
        if raiz is None or raiz.left is None:
            return raiz
        else:
            self.getMenorValor(raiz.left)
    
    def inOrder(self, raiz):
        if raiz == None:
            return
        else:
            self.inOrder(raiz.esq)
            print("{0} ".format(raiz.valor), end="")
            self.inOrder(raiz.dire)


# Inicia a árvore
avl = Arvore()
raiz = None

# Cria lista aleatória
lista = sample(range(10), 10)
print("Amostra inicial: " + str(lista))

for i in lista:
    raiz = avl.insere(raiz, i)

print("Impressão in Order: ")
avl.inOrder(raiz)
print()