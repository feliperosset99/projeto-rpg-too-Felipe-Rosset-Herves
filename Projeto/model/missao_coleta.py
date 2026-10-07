from model.missao import Missao   # Importa a classe pai

# Missão de coleta: herda de Missao e acrescenta o item a coletar e um bônus
class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item): 
        super().__init__(nome, descricao, recompensa)   # Inicializa os atributos herdados
        self.__item = item                              # Item que deve ser coletado (privado)
        self.__bonus = 20 # Valor fixo para missões de coleta

    # Getter: permite ler o item
    @property
    def item(self):
        return self.__item
    
    # Getter: permite ler o bônus
    @property
    def bonus(self):
        return self.__bonus

    # Sobrescreve o cálculo da recompensa somando o bônus de coleta
    def calcular_recompensa(self):
        recompensa = super().calcular_recompensa()   # Recompensa base (0 se não estiver concluída)
        if recompensa > 0:                           # Só soma o bônus se houver recompensa
            recompensa += self.bonus
        return recompensa
    
    # Sobrescreve exibir_dados para incluir o item
    def exibir_dados(self):
        # Usa os dados da classe pai e acrescenta o item coletado
        msg = f'''
Dados da missão de coleta:
{super().exibir_dados()}
Item: {self.item}
'''
        return msg

    # Representação em texto do objeto (mostra todos os atributos)
    def __str__(self): 
        return f"\nMissaoColeta: {self.__dict__}"