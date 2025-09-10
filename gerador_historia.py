"""
gerador_historia.py
-------------------
Script principal do projeto Gerador de Histórias.
Gera histórias curtas e aleatórias com base em temas escolhidos pelo usuário.
"""
import random

# Listas de elementos para cada tema
TEMAS = {
    "fantasia": {
        "personagens": ["um corajoso cavaleiro", "uma fada travessa", "um dragão vegetariano", "uma princesa inventora"],
        "lugares": ["num castelo mal-assombrado", "na floresta encantada", "no reino das nuvens", "no lago mágico"],
        "acoes": ["encontrou um mapa secreto", "lutou contra um monstro de gelatina", "descobriu uma passagem secreta", "ganhou um concurso de dança"],
        "objetos": ["uma espada mágica", "um livro de feitiços", "um amuleto brilhante", "um chapéu invisível"],
        "desfechos": ["e todos viveram felizes para sempre.", "e o reino foi salvo por uma receita de bolo.", "e a magia voltou à floresta.", "e o dragão virou amigo de todos."]
    },
    "ficcao": {
        "personagens": ["uma gata astronauta", "um robô cozinheiro", "um alienígena curioso", "um cientista maluco"],
        "lugares": ["em uma nave espacial de chocolate", "numa cozinha do futuro", "no planeta dos doces", "na estação lunar"],
        "acoes": ["descobriu uma nova galáxia", "resolveu o mistério do pudim desaparecido", "inventou um teletransporte de pizza", "ganhou um concurso intergaláctico"],
        "objetos": ["um capacete de brigadeiro", "uma colher de pau falante", "um chip de memória infinita", "um foguete de marshmallow"],
        "desfechos": ["e a galáxia foi salva com uma receita de bolo.", "e o robô se tornou o chef mais famoso do universo.", "e todos voltaram para casa com doces.", "e a nave virou uma confeitaria espacial."]
    },
    "misterio": {
        "personagens": ["uma detetive de chiclete", "um cachorro farejador", "um fantasma tímido", "um bibliotecário curioso"],
        "lugares": ["na cidade de Docelândia", "na mansão dos enigmas", "no museu do sorvete", "no parque dos mistérios"],
        "acoes": ["resolveu o mistério do pudim desaparecido", "descobriu uma pista secreta", "desvendou um código antigo", "encontrou um mapa misterioso"],
        "objetos": ["uma lupa de açúcar", "um diário secreto", "um chaveiro mágico", "um chiclete colorido"],
        "desfechos": ["e a cidade voltou a ter suas sobremesas em paz.", "e todos descobriram o segredo do sorvete infinito.", "e o fantasma fez novos amigos.", "e o mistério foi resolvido com um sorriso."]
    }
}

def gerar_historia(tema):
    """
    Gera uma história aleatória baseada no tema escolhido.
    Parâmetro:
        tema (str): Tema da história ('fantasia', 'ficcao', 'misterio')
    Retorno:
        str: História gerada
    """
    if tema not in TEMAS:
        raise ValueError("Tema inválido. Escolha entre: fantasia, ficcao, misterio.")
    elementos = TEMAS[tema]
    personagem = random.choice(elementos["personagens"])
    lugar = random.choice(elementos["lugares"])
    acao = random.choice(elementos["acoes"])
    objeto = random.choice(elementos["objetos"])
    desfecho = random.choice(elementos["desfechos"])
    historia = f"Era uma vez {personagem} que, {lugar}, {acao} com a ajuda de {objeto}, {desfecho}"
    return historia

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Histórias!")
    print("Temas disponíveis: fantasia, ficcao, misterio")
    tema = input("Escolha um tema para a sua história: ").strip().lower()
    try:
        historia = gerar_historia(tema)
        print("\nSua história gerada:")
        print(historia)
    except ValueError as e:
        print(e)
