import locale
import config

def moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def cor(texto, codigo):
    if not config.USAR_CORES:
        return texto
    return f'\033[{codigo}m{texto}\033[m'