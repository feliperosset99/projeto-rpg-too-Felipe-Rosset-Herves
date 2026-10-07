# Criei um setter para o atributo status, que garante que a missão só possa passar de PENDENTE para EM_ANDAMENTO e depois para CONCLUIDA, sem pular etapas.

from model.enums import StatusMissao   # Importa o enum com os status possíveis da missão

# Classe base para todos os tipos de missão
class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome                        # Nome da missão (privado)
        self.__descricao = descricao              # Descrição/objetivo da missão (privado)
        self.__recompensa = recompensa            # XP base concedido ao concluir (privado)
        self.__status = StatusMissao.PENDENTE     # Toda missão começa como pendente

    #permite ler o nome
    @property
    def nome(self): 
        return self.__nome
    
    #permite ler a descrição
    @property
    def descricao(self): 
        return self.__descricao
    
    #permite ler a recompensa base
    @property
    def recompensa(self): 
        return self.__recompensa

    #permite ler o status atual
    @property
    def status(self): 
        return self.__status

    # Setter do status: só permite a sequência PENDENTE -> EM_ANDAMENTO -> CONCLUIDA
    @status.setter
    def status(self, stat):
        # Não permite "alterar" para o mesmo status que já está
        if stat == self.__status:
            raise ValueError(f"O status da missão já é '{self.__status.value}'.")

        # Garante que o novo valor seja um item do enum StatusMissao
        elif not isinstance(stat, StatusMissao):
            raise TypeError("Você precisa selecionar o ENUM 'StatusMissao'. Outro tipo de dado é inválido.")
        
        # Se está pendente, só pode ir para "em andamento"
        elif self.__status == StatusMissao.PENDENTE:
            if stat != StatusMissao.EM_ANDAMENTO:
                raise ValueError(f"A missão está '{StatusMissao.PENDENTE.value}', seu status só pode ser alterado para '{StatusMissao.EM_ANDAMENTO.value}'.")
             
        # Se está em andamento, só pode ir para "concluída"
        elif self.__status == StatusMissao.EM_ANDAMENTO:
            if stat != StatusMissao.CONCLUIDA:
                raise ValueError(f"A missão está '{StatusMissao.EM_ANDAMENTO.value}', seu status só pode ser alterado para '{StatusMissao.CONCLUIDA.value}'.")
            
        # Se já está concluída, o status não pode mais mudar
        elif self.__status == StatusMissao.CONCLUIDA:
            raise ValueError(f"A missão já está '{StatusMissao.CONCLUIDA.value}', não pode ter seu status alterado.")
        
        # Se passou por todas as validações, atualiza o status
        self.__status = stat

    # Inicia a missão (muda de PENDENTE para EM_ANDAMENTO)
    def iniciar_missao(self):
        if self.status == StatusMissao.PENDENTE:
            self.status = StatusMissao.EM_ANDAMENTO    # Atualiza o status via setter
            return f"A missão {self.nome} começou! O objetivo é {self.descricao}."
        else:
            return f'A missão {self.nome} já foi iniciada!!!'   # Já tinha sido iniciada

    # Calcula a recompensa: só há recompensa se a missão estiver concluída
    def calcular_recompensa(self):
        if self.status is not StatusMissao.CONCLUIDA:
            return 0               # Missão não concluída não dá recompensa
        return self.recompensa     # Missão concluída retorna a recompensa base

    # Conclui a missão e entrega o XP ao herói
    def concluir_missao(self, heroi):
        # Impede concluir (e receber a recompensa) mais de uma vez
        if self.status == StatusMissao.CONCLUIDA:
            raise ValueError(f"A missão já está '{StatusMissao.CONCLUIDA.value}', não receberá a recompensa novamente.")
    
        self.status = StatusMissao.CONCLUIDA                # Marca como concluída (setter valida a transição)
        heroi.ganhar_experiencia(self.calcular_recompensa())   # Dá o XP ao herói
        print(f"Missão '{self.nome}' concluída. {heroi.nome} obteve a recompensa e ganhou o xp.\n")
    
    # Retorna um texto com os dados da missão
    def exibir_dados(self):
        # __class__.__name__ mostra o nome da classe real (Missao, MissaoCaca, etc.)
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.value}'''

        return msg

    # Representação em texto resumida da missão
    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status}'