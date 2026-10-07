from model.missao_caca import MissaoCaca        # Importa a missão de caça
from model.missao_coleta import MissaoColeta    # Importa a missão de coleta
from model.missao_entrega import MissaoEntrega  # Importa a missão de entrega
from model.enums import StatusMissao, ClasseHeroi, TipoInimigo  # Importa os enums de status, classe e tipo de inimigo
from model.heroi import Heroi                   # Importa a classe do herói

# Função principal que executa a simulação do jogo
def main():

    # Cria o herói: nome, classe, vida, vida máxima, ataque, defesa
    arqueiro = Heroi("Arqueiro", ClasseHeroi.ARQUEIRO, 80, 100, 15, 10)
    # Mostra os dados iniciais do herói
    print("\n!!! Começo do Jogo !!!\n")
    print(f"{arqueiro.exibir_dados()}\n")

    # Cria uma missão de cada tipo: nome, descrição, recompensa e o que tem que ser feito (inimigo, item ou entrega)
    missaoCaca = MissaoCaca("Caça", "Cace goblins para proteger a vila", 75, TipoInimigo.GOBLIN)
    missaoColeta = MissaoColeta("Coleta", "Colete uma erva medicinal rara", 80, "Erva medicinal")
    missaoEntrega = MissaoEntrega("Entrega", "Entregue uma carta para o rei", 92, "Carta")

    # Guarda as missões em uma lista (polimorfismo)
    listaMissoes = []
    listaMissoes.append(missaoCaca)
    listaMissoes.append(missaoColeta)
    listaMissoes.append(missaoEntrega)


    # Percorre cada missão da lista
    for missao in listaMissoes:
        print(f"{missao.iniciar_missao()}\n")              # Inicia a missão e mostra a mensagem
        try:
            missao.concluir_missao(arqueiro)        # Conclui a missão e dá o XP ao herói
        except ValueError as erro:                  # Captura erros de regra (ex.: missão já concluída)
            print (f"Não foi possível concluir a missão: {erro}")



    # Mostra os dados do herói após todas as missões (nível/XP atualizados)
    print("\n!!! Final Do Jogo !!!\n\n")
    print(f"{arqueiro.exibir_dados()}\n\n\n")

    # Teste proposital de erro: tenta voltar uma missão concluída para pendente
    print("!!! Teste de Erro !!!\n")
    try:
        missaoCaca.status = StatusMissao.PENDENTE   # O setter deve recusar essa alteração
    except ValueError as erro:                      # Transição de status inválida
        print(f"Não foi possível alterar os Dados: {erro}\n")
    except TypeError as erro:                       # Valor que não é do enum StatusMissao
        print(f"Não foi possível alterar os Dados: {erro}\n")


main()