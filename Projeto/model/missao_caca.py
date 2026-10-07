from model.missao import Missao        # Importa a classe pai
from model.enums import TipoInimigo    # Importa o enum com os tipos de inimigo

# Missão de caça: herda de Missao e acrescenta o inimigo caçado e um bônus
class MissaoCaca(Missao):
    def __init__(self, nome, descricao, recompensa, inimigo_cacado): 
        super().__init__(nome, descricao, recompensa)   # Inicializa os atributos herdados
        if not isinstance(inimigo_cacado, TipoInimigo):             # Valida se o inimigo é um TipoInimigo
            raise TypeError('Inimigo caçado precisa ser um TipoInimigo')  # Erro se for outro tipo
        self.__inimigo_cacado = inimigo_cacado          # Tipo de inimigo que deve ser caçado (privado)
        self.__bonus = 10 # Valor fixo para missões de caça

    # Getter: permite ler o inimigo caçado
    @property
    def inimigo_cacado(self):
        return self.__inimigo_cacado

    # Getter: permite ler o bônus
    @property
    def bonus(self):
        return self.__bonus

    # Sobrescreve o cálculo da recompensa somando o bônus de caça
    def calcular_recompensa(self):
        recompensa = super().calcular_recompensa()   # Recompensa base (0 se não estiver concluída)
        if recompensa > 0:                           # Só soma o bônus se houver recompensa
            recompensa += self.bonus
        return recompensa
    
    # Sobrescreve exibir_dados para incluir o inimigo
    def exibir_dados(self):
        # Usa os dados da classe e acrescenta o inimigo caçado
        msg = f'''
Dados da missão de caça:
{super().exibir_dados()}
Inimigo: {self.inimigo_cacado.value}
'''
        return msg

    # Representação em texto do objeto (mostra todos os atributos)
    def __str__(self): 
        return f"\nMissaoCaca: {self.__dict__}"