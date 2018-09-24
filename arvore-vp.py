BLACK = "BLACK"
RED = "RED"

class Node(object):
    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None

class Arvore(object):

    def insert(self, key):
        
        # Cria o novo nó
        node = Node(key)

        # Caso seja raiz
        if self.root == None:
            node.color = BLACK
            self.root = node
            return
        
        # Encontra o pai do nó
        currentNode = self.root
        while currentNode != None:
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        # Seta o pai do nó
        node.parent = potentialParent
        
        # Seta o lado no pai em que o nó será setado
        if node.key < node.parent.key:
            node.parent.left = node
        else:
            node.parent.right = node
        
        # Seta os nós filhos do novo como Nil (Testar código sem esta parte)
        node.left = None
        node.right = None

        # Chama o rebalanceamento da árvore
        self.fixTree(node)

    def fixTree(self, node):

        while node.parent.color == RED and node != self.root:

            # Caso o pai esteja a esquerda do avô
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                # Caso 3 - Pai e tio vermelhos
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent  # unknown

                else:
                    # Caso 4 - Pai vermelho e tio preto, peso interno
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    
                    # Caso 5 - Pai vermelho e tio preto, peso externo
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            
            # Caso o pai esteja a direita do avô
            else:
                uncle = node.parent.parent.right

                # Caso 3
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    # Caso 4
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    
                    # Caso 5
                    node.parent.color = BLACK
                    node.parent.parent.color = BLACK
                    self.left_rotate(node.parent.parent)

        self.root.color = BLACK

        def left_rotate(self, node):
            
            sibling = node.right
            node.right = sibling.left

            if sibling.left != None:
                sibling.left.parent = node
            
            sibling.parent = node.parent
            
            if node.parent == None:
                self.root = sibling
            else:
                if node == node.parent.left:
                    node.parent.left = sibling
                else:
                    node.parent.right = sibling

            sibling.left = node
            node.parent = sibling
        
        def right_rotate(self, node):
            
            sibling = node.left
            node.left = sibling.right

            if sibling.right != None:
                sibling.right.parent = node
            
            sibling.parent = node.parent
            
            if node.parent == None:
                self.root = sibling
            else:
                if node == node.parent.right:
                    node.parent.right = sibling
                else:
                    node.parent.left = sibling

            sibling.right = node
            node.parent = sibling

        def inOrder(self, raiz):
            if raiz == None:
                return
            else:
                self.inOrder(raiz.esq)
                print("{0} ".format(raiz.valor), end="")
                self.inOrder(raiz.dire)


rb = Arvore()
raiz = None

print("Amostra Inicial: ")
lista = [6, 8, 0, 7, 9, 1, 3, 4, 2, 5]

for i in lista:
    print("Insere:" + str(i))
    raiz = rb.insert(raiz, i)
    print(str(raiz.valor))

    print("Impressão in Order: ")
    avl.inOrder(raiz)
    print("\n")