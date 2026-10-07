# Classe base para qualquer personagem do jogo (Herói e Inimigo herdam dela)
class Personagem: 
    # Construtor: recebe os dados básicos do personagem
    def __init__(self, nome, vida, vida_maxima, ataque, defesa): 
            self.__nome = nome                  # Nome do personagem (atributo privado)
            self.__vida = vida                  # Vida atual (privado)
            self.__vida_maxima = vida_maxima    # Limite máximo de vida (privado)
            self.__ataque = ataque              # Poder de ataque (privado)
            self.__defesa = defesa              # Poder de defesa (privado)
            self.__nivel = 1                    # Todo personagem começa no nível 1
            self.__xp = 0                       # E com 0 de experiência

    # Getter: permite ler o nível, mas não alterá-lo diretamente
    @property
    def nivel(self): 
        return self.__nivel
    
    # Getter: permite ler o xp atual
    @property
    def xp(self): 
        return self.__xp 

    # Getter: permite ler o nome
    @property
    def nome(self):
        return self.__nome

    # Getter: permite ler a vida atual
    @property
    def vida(self):
        return self.__vida

    # Getter: permite ler a vida máxima
    @property
    def vida_maxima(self):
        return self.__vida_maxima

    # Getter: permite ler o ataque
    @property
    def ataque(self):
        return self.__ataque

    # Getter: permite ler a defesa
    @property
    def defesa(self):
        return self.__defesa

    # Setter da vida: garante que ela fique entre 0 e a vida máxima
    @vida.setter
    def vida(self, valor):
        if valor < 0:                          # Vida não pode ficar negativa
            self.__vida = 0
        elif valor > self.__vida_maxima:       # Vida não pode ultrapassar o máximo
            self.__vida = self.__vida_maxima
        else:                                  # Valor válido: apenas atribui
            self.__vida = valor

    # Setter do ataque: impede valores negativos
    @ataque.setter
    def ataque(self, valor):
        if valor < 0:
            self.__ataque = 0
        else:
            self.__ataque = valor

    # Setter da defesa: impede valores negativos
    @defesa.setter
    def defesa(self, valor):
        if valor < 0:
            self.__defesa = 0
        else:
            self.__defesa = valor

    # Adiciona experiência ao personagem e sobe de nível quando atinge o necessário
    def ganhar_experiencia(self, quantidade):
        if quantidade <= 0:                    # Ignora quantidades zero ou negativas
            return
        self.__xp += quantidade                # Soma o xp ganho
        # Enquanto houver xp suficiente (nível x 100), sobe de nível (pode subir vários de uma vez)
        while self.__xp >= self.__nivel * 100:
            self.__xp -= self.__nivel * 100    # Desconta o xp gasto no nível
            self.__nivel += 1                  # Aumenta o nível
            self._aumentar_atributos()         # Melhora os atributos do personagem
            print(f'{self.nome} subiu para o nível {self.nivel}!\n')  # Avisa a subida de nível

    # Método protegido: bônus aplicado a cada nível ganho
    def _aumentar_atributos(self):
        self.__vida_maxima += 10          # +10 na vida máxima
        self.ataque = self.ataque + 2     # +2 no ataque (usa o setter)
        self.defesa = self.defesa + 1     # +1 na defesa (usa o setter)
        self.vida = self.vida_maxima      # Recupera toda a vida

    # Retorna True se o personagem ainda tem vida
    def esta_vivo(self):
        return self.__vida > 0

    # Método protegido: reduz a vida de acordo com o dano recebido
    def _receber_dano(self, valor):
        self.__vida = self.__vida - valor     # Subtrai o dano da vida
        if self.__vida < 0:                   # Evita vida negativa
                    self.__vida = 0

    # Ataca outro personagem
    def atacar(self, alvo):
        dano = self.calcular_dano_contra(alvo)    # Calcula o dano considerando a defesa do alvo
        alvo._receber_dano(dano)                  # Aplica o dano no alvo
        print(f'{self.__nome} atacou {alvo.nome} causando {dano} de dano')  # Mostra o resultado

    # Calcula o dano: ataque do atacante menos a defesa do alvo
    def calcular_dano_contra(self, alvo):
        dano =  self.__ataque - alvo.defesa
        if dano > 0:          # Se o dano for positivo, retorna ele
            return dano
        else:                 # Caso contrário, o dano mínimo é 1
            return 1   

    # Retorna um texto com os dados do personagem
    def exibir_dados(self):
        # Texto multilinha formatado com os atributos atuais
        msg = f'''
Nome: {self.nome}
Vida: {self.vida}
Ataque: {self.ataque}
Defesa: {self.defesa}
Nível: {self.nivel}
Experiência: {self.xp}'''
        return msg