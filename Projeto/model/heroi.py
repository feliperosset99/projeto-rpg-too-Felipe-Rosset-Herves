from model.personagem import Personagem   # Importa a classe pai
from model.enums import ClasseHeroi       # Importa o enum com as classes de herói

# Herói é um tipo de Personagem (herança)
class Heroi(Personagem):    
    def __init__(self, nome, classe, vida, vida_maxima, ataque, defesa): 
        super().__init__(nome, vida, vida_maxima, ataque, defesa)  # Inicializa os atributos herdados
        if not isinstance(classe, ClasseHeroi):                    # Valida se a classe é do tipo ClasseHeroi
            raise TypeError("Classe precisa ser da ClasseHeroi")   # Erro se for outro tipo
        self.__classe = classe                                     # Guarda a classe (atributo privado)

    # Getter: permite ler a classe do herói
    @property
    def classe(self):
        return self.__classe
    

    # Sobrescreve exibir_dados para incluir informações do herói
    def exibir_dados(self):
        # Usa os dados da classe pai e acrescenta o tipo (classe) do herói
        msg = f'''Status do Herói:
{super().exibir_dados()}
Classe: {self.classe.value}'''
        return msg

    # Representação em texto do objeto (mostra todos os atributos)
    def __str__(self):
        return f"\nHeroi: {self.__dict__}"