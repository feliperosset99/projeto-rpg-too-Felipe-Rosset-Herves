from model.missao import Missao   # Importa a classe pai

# Missão de entrega: herda de Missao e acrescenta a mercadoria a entregar e um bônus
class MissaoEntrega(Missao):
    def __init__(self, nome, descricao, recompensa, mercadoria): 
        super().__init__(nome, descricao, recompensa)   # Inicializa os atributos herdados
        self.__mercadoria = mercadoria                  # Mercadoria a ser entregue (privado)
        self.__bonus = 30 # Valor fixo para missões de entrega

    # Getter: permite ler a mercadoria
    @property
    def mercadoria(self):
        return self.__mercadoria
    
    # Getter: permite ler o bônus
    @property
    def bonus(self):
        return self.__bonus

    # Sobrescreve o cálculo da recompensa somando o bônus de entrega
    def calcular_recompensa(self):
        recompensa = super().calcular_recompensa()   # Recompensa base (0 se não estiver concluída)
        if recompensa > 0:                           # Só soma o bônus se houver recompensa
            recompensa += self.bonus
        return recompensa
    
    # Sobrescreve exibir_dados para incluir a mercadoria
    def exibir_dados(self):
        # Usa os dados da classe e acrescenta a mercadoria
        msg = f'''
Dados da missão de entrega:
{super().exibir_dados()}
Mercadoria: {self.mercadoria}
'''
        return msg

    # Representação em texto do objeto (mostra todos os atributos)
    def __str__(self): 
        return f"\nMissaoEntrega: {self.__dict__}"