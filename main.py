

# OBS: Uso de cores ANSI pode não funcionar em todos os terminais.  
# Use a flag USAR_CORES = False caso haja problemas de exibição.
#   ------------------
#  | CORES  | CÓDIGO  |
#   ---------  -------
#    Preto       30 
#    Vermelho    31   
#    Verde       32 
#    Amarelo     33 
#    Azul        34 
#    Magenta     35 
#    Ciano       36 
#    Branco      37 
#    Limpa       [m
#  -------------------
import config
from utils import cor, moeda
# importando as configuracoes de cores e padronização da moeda brasileira
# e dando a funcionalidade para o user desligar as cores no terminal caso
# seja necessário.


usar_cores = input('Deseja usar cores no terminal? [s/n]: ').strip().lower()
print()
# input para flag do uso de True ou False de cor no terminal.
config.USAR_CORES = usar_cores == 's'

saldo = 600
# Variavel que recebe valor do saldo sem estar hardcoded no codigo.

# titulo = cor('BEM VINDO AO CAIXA DO SEU','34').center(40) + cor('BANCO', '33').center(10) 
titulo = cor(' BEM VINDO AO CAIXA DO SEU ', '34')
nome_banco = cor('BANCO', '33') 
print((titulo + nome_banco).center(50)) 
# Uso de variaveis para ter o output centralizado. Não sei ainda outra solução mais
# limpa ou enxuta para ter os textos centralizados no output. Vizualmente penso ser
# mais agradável dessa forma mas talvez denescessário. Eventualmente o correto seria
# deixar essa solução visual para um possível frontend do programa. 
# Porém por enriquecer o código no portifolio optei dessa maneira e segui assim. 

print('INSIRA SEU CARTAO'.center(40))
# Brincadeira sem funcionalidade só para uso cosmetico e fantasioso
print(cor('-','33') *43) 
# Divisor cosmetico e organizacional do output.
print(f"SEU SALDO ATUAL: {cor(moeda(saldo), '33')}")
# Mostra o saldo atual do user. Variavel saldo pode ser alterada acima.
while True:
    try:
        saque = float(input('Digite o valor do saque (R$): '))
    except ValueError:
        print('Valor inválido')
        continue
    # Bloco que checa a condicional do user se digitar letras ao invés de números
    # retorna para o try caso seja digitado letras ao invés de números.
    if saque <= 0:
        print('Digite um valor válido (maior que zero)')
        continue
    # Condição que compara o valor da retirada com o total do saldo disponível.
    if saque > saldo:
        print(f"Seu saldo é {cor('insuficiente', '31')}! {cor(moeda(saldo), '33')}")
        continue
    saldo -= saque
    # Atualiza saldo após saque válido.
    print(f"O saldo atual é de {cor(moeda(saldo),'33')}")
    print(cor('-','33') *43)
    # output do saldo atual.
    if saldo == 0:
        print(f"Seu saldo foi {cor('ZERADO', '31')}")
        break
    # Se saldo atual for zero ele avisa e encerra o programa.
    while True:
        continuar = input("Deseja continuar com a operação? [s/n]: ").strip().upper()
        if continuar not in ('S','N'):
            print("Digite apenas s ou n")
        break
    if continuar == 'N':
        break
    # flag 'S', 'N' que pergunta e compara a condição caso o user decida 
    # continuar ou sair do programa.
print(f"Seu saldo atual é: {cor(moeda(saldo), '33')}")
# output final mostra o total restante do saldo do user.
print(cor('-','33') *43)
# Divisor cosmético e organizacional do output.
texto_desp = "TENHA UM BOM DIA"
linha = texto_desp.center(15)
linha_colorida = linha.replace("TENHA UM BOM DIA", cor("TENHA UM BOM DIA", "34"))
print(cor("TENHA UM BOM DIA", "34").center(49))
# Mensagem final cordial do programa. 
print(cor('-','33') *43)
# Divisor cosmético e organizacional do output.
texto_final = "ENTER PARA SAIR"
linha = texto_final.center(41)
linha_colorida = linha.replace("ENTER", cor("ENTER", "31"))
input(linha_colorida)
# Outro bloco de variaveis para tentar centralizar as linhas e usar cores no terminal. 
print(cor('-','33') *43)
# Divisor cosmético e organizacional do output.



