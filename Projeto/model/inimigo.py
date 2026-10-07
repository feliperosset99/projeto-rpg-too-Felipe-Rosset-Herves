from model.personagem import Personagem   # Importa a classe pai
from model.enums import TipoInimigo       # Importa o enum com os tipos de inimigo

# Inimigo é um tipo de Personagem (herança)
class Inimigo(Personagem):
    def __init__(self, nome, tipo, vida, vida_maxima, ataque, defesa): 
        super().__init__(nome, vida, vida_maxima, ataque, defesa)  # Inicializa os atributos herdados
        if not isinstance(tipo, TipoInimigo):                      # Valida se o tipo é um TipoInimigo
            raise TypeError('Tipo precisa ser um TipoInimigo')     # Erro se for outro tipo
        self.__tipo = tipo                                         # Guarda o tipo (atributo privado)

    # Getter: permite ler o tipo do inimigo
    @property
    def tipo(self):
        return self.__tipo

    # Sobrescreve exibir_dados para incluir informações do inimigo
    def exibir_dados(self):
        # Usa os dados da classe pai e acrescenta o tipo do inimigo
        msg = f'''
Dados do Inimigo:
{super().exibir_dados()}
Tipo: {self.tipo.value}

'''
        return msg

    # Representação em texto do objeto (mostra todos os atributos)
    def __str__(self): 
        return f"\nInimigo: {self.__dict__}"