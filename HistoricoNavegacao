class No:
    """
    Representa um nó individual em uma estrutura de dados encadeada.
    Cada nó contém um valor e uma referência para o próximo nó na lista.
    """
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor (URL, neste caso)
        self.proximo = None  # Referência para o próximo nó (inicialmente é None)

class HistoricoNavegacao:
    """
    Implementa uma pilha para gerenciar o histórico de navegação.
    O comportamento é LIFO (Last In, First Out), típico de pilhas.
    """

    def __init__(self):
        """
        Inicializa o histórico de navegação.
        """
        self.topo = None  # Referência para o topo da pilha
        self.tamanho = 0  # Número de elementos na pilha

    def visitar_pagina(self, url):
        """
        Adiciona uma nova página ao histórico de navegação.
        
        Parâmetro:
        - url: A URL da página a ser adicionada.
        """
        novo_no = No(url)  # Cria um novo nó com a URL fornecida
        novo_no.proximo = self.topo  # O próximo nó do novo nó é o atual topo
        self.topo = novo_no  # Atualiza o topo para o novo nó
        self.tamanho += 1  # Incrementa o tamanho da pilha

    def voltar(self):
        """
        Remove e retorna a página atual do topo do histórico.
        Se não houver páginas, retorna uma mensagem informativa.
        
        Retorno:
        - URL da página removida ou mensagem se a pilha estiver vazia.
        """
        if self.esta_vazia():
            return "Não há mais páginas para voltar."
        valor_removido = self.topo.valor  # Armazena o valor do topo para retornar
        self.topo = self.topo.proximo  # Atualiza o topo para o próximo nó
        self.tamanho -= 1  # Decrementa o tamanho da pilha
        return valor_removido

    def esta_vazia(self):
        """
        Verifica se o histórico de navegação está vazio.
        
        Retorno:
        - True se estiver vazio, False caso contrário.
        """
        return self.topo is None

    def pagina_atual(self):
        """
        Retorna a página no topo do histórico sem removê-la.
        
        Retorno:
        - URL da página atual ou mensagem se a pilha estiver vazia.
        """
        if self.esta_vazia():
            return "Não há nenhuma página para ser visualizada."
        return self.topo.valor

    def exibir_historico(self):
        """
        Exibe todas as páginas no histórico, começando pela mais recente.
        """
        atual = self.topo  # Começa do topo da pilha
        while atual is not None:  # Itera enquanto houver nós na pilha
            print(atual.valor)  # Exibe o valor do nó atual
            atual = atual.proximo  # Move para o próximo nó
