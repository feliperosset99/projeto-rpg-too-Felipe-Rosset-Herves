from enum import Enum  # Importa a classe base para criar enumerações (conjuntos fixos de valores)

# Define as classes possíveis de um herói
class ClasseHeroi(Enum):
    GUERREIRO = "Guerreiro"  # Classe guerreiro; o valor é o texto exibido ao usuário
    MAGO = "Mago"            # Classe mago
    ARQUEIRO = "Arqueiro"    # Classe arqueiro


# Define os tipos possíveis de inimigo
class TipoInimigo(Enum):
    ORC = "Orc"          # Inimigo do tipo orc
    GOBLIN = 'Goblin'    # Inimigo do tipo goblin
    DRAGAO = 'Dragão'    # Inimigo do tipo dragão

# Define os estados possíveis de uma missão
class StatusMissao(Enum):
    PENDENTE = 'Pendente'              # Missão criada, mas ainda não iniciada
    EM_ANDAMENTO = 'Em andamento'      # Missão já iniciada
    CONCLUIDA = 'Concluída'            # Missão finalizada