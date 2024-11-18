class No:
    """
    Classe que representa um nó de uma estrutura encadeada.
    Cada nó contém um valor e uma referência para o próximo nó.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó (inicialmente None)


class Hibrida:
    """
    Classe que implementa uma estrutura híbrida, funcionando como:
    - Pilha (LIFO - Last In, First Out)
    - Fila (FIFO - First In, First Out)
    """
    def __init__(self, tipo):
        """
        Inicializa a estrutura híbrida.

        Parâmetro:
        - tipo: Deve ser "fila" ou "pilha", indicando o comportamento desejado.
        """
        self.tipo = tipo  # Define se a estrutura é uma pilha ou uma fila
        if tipo not in ["fila", "pilha"]:
            raise ValueError("Erro: o tipo deve ser 'fila' ou 'pilha'.")
        
        self.frente = None  # Referência ao primeiro elemento da estrutura
        self.tras = None  # Referência ao último elemento (usado apenas na fila)
        
        if self.tipo == "pilha":
            self.tamanho = 0  # Usado apenas na pilha para rastrear o tamanho

    def colocar(self, valor):
        """
        Adiciona um novo elemento à estrutura.

        Parâmetro:
        - valor: O valor a ser adicionado.
        """
        novo_no = No(valor)  # Cria um novo nó com o valor fornecido
        if self.tipo == "pilha":  # Comportamento da pilha (LIFO)
            novo_no.proximo = self.frente  # O próximo nó do novo nó será o topo atual
            self.frente = novo_no  # Atualiza o topo para o novo nó
            self.tamanho += 1  # Incrementa o tamanho da pilha
        else:  # Comportamento da fila (FIFO)
            if self.esta_vazia():  # Caso especial: fila vazia
                self.frente = novo_no  # O novo nó será o primeiro nó
                self.tras = novo_no  # O novo nó também será o último nó
            else:
                self.tras.proximo = novo_no  # Adiciona o novo nó ao final da fila
                self.tras = novo_no  # Atualiza a referência para o último nó

    def tirar(self):
        """
        Remove e retorna o elemento na frente da estrutura.

        Retorno:
        - Valor removido ou None se a estrutura estiver vazia.
        """
        if self.esta_vazia():  # Verifica se a estrutura está vazia
            return None
        
        valor_removido = self.frente.valor  # Armazena o valor do elemento a ser removido
        self.frente = self.frente.proximo  # Move a referência da frente para o próximo nó

        if self.tipo == "pilha":  # Comportamento da pilha (LIFO)
            self.tamanho -= 1  # Decrementa o tamanho da pilha
            return valor_removido
        else:  # Comportamento da fila (FIFO)
            if self.frente is None:  # Caso especial: fila fica vazia após a remoção
                self.tras = None  # Remove a referência ao último nó
            return valor_removido

    def esta_vazia(self):
        """
        Verifica se a estrutura está vazia.

        Retorno:
        - True se a estrutura estiver vazia, False caso contrário.
        """
        return self.frente is None

    def ver_primeiro_elemento(self):
        """
        Retorna o elemento no topo (pilha) ou na frente (fila) sem removê-lo.

        Retorno:
        - Valor do primeiro elemento ou mensagem informativa se estiver vazia.
        """
        if self.esta_vazia():  # Verifica se a estrutura está vazia
            return "Não há nenhum elemento."
        return self.frente.valor  # Retorna o valor do elemento na frente


# Exemplo de uso como PILHA
hibrida = Hibrida("pilha")  # Cria uma estrutura do tipo pilha
hibrida.colocar(1)  # Adiciona o elemento 1 ao topo da pilha
hibrida.colocar(2)  # Adiciona o elemento 2 ao topo da pilha
hibrida.colocar(3)  # Adiciona o elemento 3 ao topo da pilha
hibrida.tirar()  # Remove o elemento do topo (3)
hibrida.tirar()  # Remove o elemento do topo (2)
print(f"Pilha: o elemento do topo é {hibrida.ver_primeiro_elemento()}")  # Mostra o elemento restante no topo (1)

# Exemplo de uso como FILA
hibrida = Hibrida("fila")  # Cria uma estrutura do tipo fila
hibrida.colocar(1)  # Adiciona o elemento 1 à fila
hibrida.colocar(2)  # Adiciona o elemento 2 à fila
hibrida.colocar(3)  # Adiciona o elemento 3 à fila
hibrida.tirar()  # Remove o elemento na frente da fila (1)
hibrida.tirar()  # Remove o próximo elemento na frente da fila (2)
print(f"Fila: o elemento da frente é {hibrida.ver_primeiro_elemento()}")  # Mostra o elemento restante na frente (3)
