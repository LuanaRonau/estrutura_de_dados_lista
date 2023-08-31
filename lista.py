#lista

class Elemento:
    def __init__(self, val, prox=None):
        self.__valor = val
        self.__prox = prox

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self, prox):
        self.__prox = prox

class Lista:
    def __init__(self):
        self.__lista = []
        self.__inicio = None
        self.__fim = None
    
    def inserirComoPrimeiro(self, novo):
        novo_elem = Elemento(novo)
        if self.__inicio is not None:
            novo_elem.prox = self.__inicio
        self.__lista.insert(0, novo_elem) #
        self.__inicio = novo_elem
        if self.__fim is None:
            self.__fim = novo_elem        
    
    def inserirComoUltimo(self, novo):
        novo_elem = Elemento(novo)
        if self.__fim is not None:
            self.__fim.prox = novo_elem
        self.__fim = novo_elem
        self.__lista.append(novo_elem) #
        if self.__inicio is None:
            self.__inicio = novo_elem

        #print("Método chamado")
        #for i in self.__lista:
        #    if i.prox is None:
        #        print(f"valor: {i.valor}, prox: {i.prox}")
        #    else:
        #        print(f"valor: {i.valor}, prox: {i.prox.valor}")
        #print(self.__inicio.valor)
        #print(self.__fim.valor)
    
    def removerElemento(self, valor):
        iterador = self.__inicio
        while iterador.prox.valor != valor:
            if iterador.prox is None:
                break
            iterador = iterador.prox
        iterador = iterador.prox.valor

        confere = self.__inicio
        while confere.prox is not None:
            print(f"valor: {confere.valor}, prox: {confere.prox.valor}")
            confere = confere.prox
        

teste = Lista()
teste.inserirComoPrimeiro('camila')
teste.inserirComoPrimeiro('berto')
teste.inserirComoPrimeiro('amanda')
teste.inserirComoUltimo('dante')
teste.inserirComoUltimo('emily')
teste.removerElemento('dante')
