class No:
    """
    Classe que representa um nó em uma lista encadeada.
    Cada nó contém um valor (dado) e uma referência para o próximo nó.
    """
    def __init__(self, dado):
        self.dado = dado  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó (inicialmente None)

class ListaEncadeada:
    """
    Classe que implementa uma lista encadeada.
    Permite operações como adicionar, remover, buscar e exibir elementos.
    """
    def __init__(self):
        self.cabeca = None  # Ponto inicial da lista (primeiro nó)

    def esta_vazia(self):
        """
        Verifica se a lista está vazia.
        Retorna True se estiver vazia, caso contrário, False.
        """
        return self.cabeca is None

    def adicionar(self, dado):
        """
        Adiciona um novo elemento ao final da lista.
        
        Parâmetro:
        - dado: Valor a ser adicionado à lista.
        """
        novo_no = No(dado)
        if not self.cabeca:  # Caso especial: lista vazia
            self.cabeca = novo_no
            return
        no_atual = self.cabeca
        while no_atual.proximo:  # Navega até o último nó
            no_atual = no_atual.proximo
        no_atual.proximo = novo_no  # Conecta o novo nó ao final da lista

    def adicionar_inicio(self, dado):
        """
        Adiciona um novo elemento ao início da lista.
        """
        novo_no = No(dado)
        novo_no.proximo = self.cabeca  # O novo nó aponta para o antigo início
        self.cabeca = novo_no  # Atualiza a cabeça para o novo nó

    def adicionar_posicao(self, dado, posicao):
        """
        Adiciona um novo elemento em uma posição específica.
        
        Parâmetros:
        - dado: Valor a ser adicionado.
        - posicao: Índice onde o elemento será inserido.
        """
        novo_no = No(dado)

        if posicao == 0:  # Caso especial: inserir no início
            self.adicionar_inicio(dado)
            return

        atual = self.cabeca
        contador = 0

        while atual is not None and contador < posicao - 1:
            atual = atual.proximo
            contador += 1

        if atual is not None:  # Insere na posição encontrada
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
        else:
            print(f'Posição {posicao} fora do intervalo.')

    def remover_ultimo(self):
        """
        Remove o último elemento da lista.
        """
        if self.esta_vazia():  # Caso especial: lista vazia
            print('A lista está vazia.')
            return

        atual = self.cabeca
        anterior = None

        while atual.proximo is not None:  # Navega até o último nó
            anterior = atual
            atual = atual.proximo

        if anterior is None:  # Caso especial: apenas um elemento na lista
            self.cabeca = None
        else:
            anterior.proximo = None  # Remove a referência para o último nó

        print(f'Elemento {atual.dado} removido.')

    def remover_primeiro(self):
        """
        Remove o primeiro elemento da lista.
        """
        if self.esta_vazia():  # Caso especial: lista vazia
            print('A lista está vazia.')
            return

        print(f'Elemento {self.cabeca.dado} removido.')
        self.cabeca = self.cabeca.proximo  # Atualiza a cabeça para o próximo nó

    def remover_posicao(self, posicao):
        """
        Remove o elemento em uma posição específica.
        
        Parâmetro:
        - posicao: Índice do elemento a ser removido.
        """
        if self.esta_vazia():  # Caso especial: lista vazia
            print('A lista está vazia.')
            return

        if posicao == 0:  # Caso especial: remover o primeiro elemento
            self.remover_primeiro()
            return

        atual = self.cabeca
        anterior = None
        contador = 0

        while atual is not None and contador < posicao:
            anterior = atual
            atual = atual.proximo
            contador += 1

        if atual is not None:  # Remove a referência para o nó na posição
            anterior.proximo = atual.proximo
            print(f'Elemento na posição {posicao} removido.')
        else:
            print(f'Posição {posicao} fora do intervalo.')

    def buscar(self, dado):
        """
        Busca um elemento na lista.
        
        Parâmetro:
        - dado: Valor a ser buscado.
        
        Retorna:
        - True se o elemento for encontrado, False caso contrário.
        """
        atual = self.cabeca
        while atual is not None:
            if atual.dado == dado:
                return True
            atual = atual.proximo
        return False

    def tamanho(self):
        """
        Retorna o tamanho da lista (número de elementos).
        """
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def buscar_posicao(self, posicao):
        """
        Retorna o elemento em uma posição específica.
        
        Parâmetro:
        - posicao: Índice do elemento.
        """
        atual = self.cabeca
        contador = 0

        while atual is not None and contador < posicao:
            atual = atual.proximo
            contador += 1

        if atual is not None:
            print(f'Elemento na posição {posicao}: {atual.dado}')
        else:
            print(f'Posição {posicao} fora do intervalo.')

    def exibir_lista(self):
        """
        Exibe todos os elementos da lista, separados por "->".
        """
        if self.esta_vazia():  # Caso especial: lista vazia
            print("A lista está vazia.")
        else:
            atual = self.cabeca
            while atual:
                print(atual.dado, end=' -> ')
                atual = atual.proximo
            print('None')  # Marca o fim da lista

    def __iter__(self):
        """
        Torna a lista iterável, permitindo uso em loops for.
        """
        atual = self.cabeca
        while atual is not None:
            yield atual.dado  # Retorna o valor do nó atual
            atual = atual.proximo


# Testando a Lista Encadeada
lista = ListaEncadeada()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)

for elemento in lista:  # Itera sobre os elementos usando __iter__
    print(elemento)
