import random


_TIPS = [
    "Ao minerar, sempre leve madeira extra para criar ferramentas e tochas conforme necessário.",
    "Explorar cavernas profundas é mais seguro com um balde de água para lidar com lava ou quedas.",
    "Construa uma fazenda de trigo e cenoura cedo para garantir comida sustentável.",
    "Use camas para marcar pontos de renascimento e evitar caminhar longas distâncias após morrer.",
    "Mantenha um escudo equipado para bloquear ataques de esqueletos e creepers.",
    "Aproveite vilas para trocar recursos e conseguir equipamentos encantados mais rapidamente.",
    "Coloque tochas ao redor da base para reduzir o surgimento de mobs hostis.",
    "Leve um mapa ou bússola ao explorar para facilitar o caminho de volta para casa.",
    "Combine elytra com foguetes de pólvora para viagens aéreas rápidas, mas leve um balde de água para pousos difíceis.",
    "Mesas de encantamento cercadas com 15 estantes garantem o nível máximo de encantamento.",
]


def get_random_tip() -> str:
    """Retorna uma dica aleatória sobre Minecraft."""
    return random.choice(_TIPS)

