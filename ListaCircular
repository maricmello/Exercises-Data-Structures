class No:
    """
    Classe que representa um nó em uma lista circular.
    Cada nó contém um valor (dado) e uma referência para o próximo nó.
    """
    def __init__(self, dado):
        self.dado = dado  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó


class ListaCircular:
    """
    Classe que implementa uma lista encadeada circular.
    Permite operações como adicionar, remover, buscar e exibir elementos.
    """
    def __init__(self):
        self.cabeca = None  # Referência para o primeiro nó da lista

    def esta_vazia(self):
        """
        Verifica se a lista está vazia.
        Retorna True se estiver vazia, caso contrário, False.
        """
        return self.cabeca is None

    def adicionar(self, dado):
        """
        Adiciona um elemento ao final da lista.
        Caso a lista esteja vazia, o novo nó se referencia como próximo (tornando-se circular).
        """
        novo_no = No(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca  # Aponta para si mesmo, criando a circularidade
        else:
            no_atual = self.cabeca
            while no_atual.proximo != self.cabeca:  # Navega até o último nó
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no  # Conecta o último nó ao novo nó
            novo_no.proximo = self.cabeca  # Fecha o ciclo

    def adicionar_inicio(self, dado):
        """
        Adiciona um elemento no início da lista.
        Atualiza a referência da cabeça e ajusta os nós para manter a circularidade.
        """
        novo_no = No(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
        else:
            novo_no.proximo = self.cabeca  # O novo nó aponta para o início atual
            no_atual = self.cabeca
            while no_atual.proximo != self.cabeca:  # Navega até o último nó
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no  # O último nó aponta para o novo nó
            self.cabeca = novo_no  # Atualiza a cabeça para o novo nó

    def remover_ultimo(self):
        """
        Remove o último elemento da lista.
        Caso a lista tenha apenas um elemento, ela será esvaziada.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        if self.cabeca.proximo == self.cabeca:  # Caso especial: apenas um elemento
            print(f"Elemento {self.cabeca.dado} removido.")
            self.cabeca = None
            return

        atual = self.cabeca
        anterior = None

        while atual.proximo != self.cabeca:  # Navega até o último nó
            anterior = atual
            atual = atual.proximo

        anterior.proximo = self.cabeca  # Remove a referência para o último nó
        print(f"Elemento {atual.dado} removido.")

    def remover_primeiro(self):
        """
        Remove o primeiro elemento da lista.
        Caso a lista tenha apenas um elemento, ela será esvaziada.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        if self.cabeca.proximo == self.cabeca:  # Caso especial: apenas um elemento
            print(f"Elemento {self.cabeca.dado} removido.")
            self.cabeca = None
            return

        print(f"Elemento {self.cabeca.dado} removido.")
        ultimo = self.cabeca
        while ultimo.proximo != self.cabeca:  # Navega até o último nó
            ultimo = ultimo.proximo
        self.cabeca = self.cabeca.proximo  # Atualiza a cabeça para o próximo nó
        ultimo.proximo = self.cabeca  # Fecha o ciclo com a nova cabeça

    def buscar(self, dado):
        """
        Busca um elemento na lista.
        Retorna True se o elemento for encontrado, caso contrário, False.
        """
        if self.esta_vazia():
            return False
        atual = self.cabeca
        while True:
            if atual.dado == dado:  # Verifica o valor atual
                return True
            atual = atual.proximo
            if atual == self.cabeca:  # Retorna ao início, encerra a busca
                break
        return False

    def tamanho(self):
        """
        Calcula e retorna o número de elementos na lista.
        """
        if self.esta_vazia():
            return 0
        contador = 0
        atual = self.cabeca
        while True:
            contador += 1
            atual = atual.proximo
            if atual == self.cabeca:  # Retorna ao início, encerra a contagem
                break
        return contador

    def exibir_lista(self):
        """
        Exibe todos os elementos da lista circular.
        Mostra que a lista é circular exibindo o primeiro elemento ao final.
        """
        if self.esta_vazia():
            print('A lista está vazia.')
            return

        atual = self.cabeca
        print(atual.dado, end=' -> ')  # Exibe o dado do primeiro nó
        atual = atual.proximo

        while atual != self.cabeca:  # Continua até retornar ao primeiro nó
            print(atual.dado, end=' -> ')
            atual = atual.proximo

        print(f'({self.cabeca.dado})')  # Mostra o primeiro elemento para indicar a circularidade


# Testando a Lista Circular
lista = ListaCircular()

# Adicionando elementos
lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(30)
print("Lista após adições:")
lista.exibir_lista()

# Adicionando um elemento no início
lista.adicionar_inicio(5)
print("\nLista após adicionar 5 no início:")
lista.exibir_lista()

# Removendo o último elemento
lista.remover_ultimo()
print("\nLista após remover o último elemento:")
lista.exibir_lista()

# Removendo o primeiro elemento
lista.remover_primeiro()
print("\nLista após remover o primeiro elemento:")
lista.exibir_lista()

# Removendo todos os elementos
lista.remover_primeiro()
lista.remover_primeiro()
print("\nLista após remover todos os elementos:")
lista.exibir_lista()
