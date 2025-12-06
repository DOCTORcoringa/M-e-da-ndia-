import time
import os
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

RED = Fore.RED
RESET = Style.RESET_ALL
CLEAR = "clear" if os.name != "nt" else "cls"
PAINEL = "NIX RAINHA"

# ============================
# CAIXA PADRÃO
# ============================
def caixa(titulo, linhas=[]):
    topo = f"{RED}╭┄┄┄┄┄┄❲ {PAINEL} | {titulo} ❳┄┄┄┄┄┄╮{RESET}"
    corpo = "\n".join([f"{RED}├┄┄┄❲ {linha} ❳{RESET}" for linha in linhas])
    baixo = f"{RED}╰┄┄┄┄┄┄┄┄┄┄┄╯{RESET}"
    return f"{topo}\n{corpo}\n{baixo}"

# ============================
# CAIXA DE BANNER
# ============================
def caixa_banner(banner):
    linhas = banner.split("\n")
    topo = f"{RED}╭┄┄┄┄┄┄❲ {PAINEL} | BANNER ❳┄┄┄┄┄┄╮{RESET}"
    corpo = "\n".join([f"{RED}│ {linha}{RESET}" for linha in linhas])
    baixo = f"{RED}╰┄┄┄┄┄┄┄┄┄┄┄╯{RESET}"
    return f"{topo}\n{corpo}\n{baixo}"

# ============================
# BARRA DE CARREGAMENTO
# ============================
def barra_carregamento(acao, qtd):
    print(RED + f"╭┄┄┄┄┄┄❲ {PAINEL} | PROCESSO ❳┄┄┄┄┄┄╮")
    print(RED + f"│ Executando: {acao}")
    print(RED + "│ Carregando...\n│")

    for _ in tqdm(range(qtd), bar_format=RED + "│ {l_bar}{bar}{r_bar}"):
        time.sleep(0.2)

    print(RED + "╰┄┄┄┄┄┄┄┄┄┄┄╯" + RESET)

# ============================
# DDIS PERMITIDOS
# ============================
DDIS_COMPLETOS = {
    "55": "Brasil",
    "1": "Estados Unidos / Canadá",
    "44": "Reino Unido",
    "33": "França",
    "351": "Portugal",
    "34": "Espanha",
    "39": "Itália",
    "49": "Alemanha",
    "61": "Austrália",
    "81": "Japão",
    "82": "Coreia do Sul",
    "86": "China",
    "90": "Turquia",
    "970": "Palestina",
    "972": "Israel"
}

DDIS_PERMITIDOS = list(DDIS_COMPLETOS.keys())

# ============================
# ESCOLHA DE DDI
# ============================
def escolher_ddi():
    print(caixa("SELECIONE O DDI", [
        f"{codigo} - {pais}" for codigo, pais in DDIS_COMPLETOS.items()
    ]))
    while True:
        ddi = input(RED + f"{PAINEL} | DDI: " + RESET).strip()
        if ddi in DDIS_COMPLETOS:
            return ddi
        print(caixa("ERRO", ["DDI inválido, tente novamente."]))

# ============================
# VALIDAÇÃO DE DDI
# ============================
def validar_ddi(numero):
    return any(numero.startswith(ddi) for ddi in DDIS_PERMITIDOS)

# ============================
# EXECUÇÃO — MODO ÚNICO
# ============================
def executar_unico(tipo):
    os.system(CLEAR)

    print(caixa("AÇÃO EM EXECUÇÃO", [
        f"Ação: {tipo}",
        "Uso restrito — Ambiente controlado"
    ]))

    ddi = escolher_ddi()
    numero_local = input(RED + f"{PAINEL} | Número local: " + RESET)
    numero = ddi + numero_local

    if not validar_ddi(numero):
        print(caixa("ERRO", ["DDI não permitido."]))
        input(RED + "ENTER..." + RESET)
        return

    barra_carregamento(tipo, 1)

    print(caixa("RELATÓRIO FINAL", [
        f"Número: {numero}",
        f"Ação: {tipo}",
        "Status: Concluído"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# EXECUÇÃO — MODO MULTI (2+ NÚMEROS)
# ============================
def executar_multi(tipo):
    os.system(CLEAR)

    print(caixa("AÇÃO EM EXECUÇÃO", [
        f"Ação: {tipo}",
        "Múltiplos números",
        "Uso restrito — Ambiente controlado"
    ]))

    ddi = escolher_ddi()
    nums = input(RED + f"{PAINEL} | Números locais (separados por vírgula): " + RESET)
    lista = [ddi + n.strip() for n in nums.split(",") if n.strip()]

    if len(lista) < 2:
        print(caixa("ERRO", ["Mínimo de 2 números!"]))
        input(RED + "ENTER..." + RESET)
        return

    for n in lista:
        if not validar_ddi(n):
            print(caixa("ERRO", [f"Número inválido: {n}"]))
            input(RED + "ENTER..." + RESET)
            return

    barra_carregamento(tipo, len(lista))

    print(caixa("RELATÓRIO FINAL", [
        f"Total: {len(lista)} números",
        f"Ação: {tipo}",
        "Status: Concluído"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# MENU
# ============================
def menu():
    os.system(CLEAR)

    banner = f\"""███╗░░██╗██╗██╗░░██╗
████╗░██║██║╚██╗██╔╝
██╔██╗██║██║░╚███╔╝░
██║╚████║██║░██╔██╗░
██║░╚███║██║██╔╝╚██╗
╚═╝░░╚══╝╚═╝╚═╝░░╚═╝

██████╗░░█████╗░██╗███╗░░██╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██║████╗░██║██║░░██║██╔══██╗
██████╔╝███████║██║██╔██╗██║███████║███████║
██╔══██╗██╔══██║██║██║╚████║██╔══██║██╔══██║
██║░░██║██║░░██║██║██║░╚███║██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝"""

    print(caixa_banner(banner))

    opcoes = [
        "1 - Denúncia",
        "2 - Spam",
        "3 - Denúncia (Múltiplos)",
        "4 - Spam (Múltiplos)",
        "5 - Sair"
    ]

    print(caixa("MENU PRINCIPAL", opcoes))

    return input(RED + f"{PAINEL} | Escolha: " + RESET)

# ============================
# LOOP PRINCIPAL
# ============================
while True:
    opc = menu()

    if opc == "1":
        executar_unico("Denúncia")
    elif opc == "2":
        executar_unico("Spam")
    elif opc == "3":
        executar_multi("Denúncia")
    elif opc == "4":
        executar_multi("Spam")
    elif opc == "5":
        os.system(CLEAR)
        print(caixa("SAINDO", [f"Obrigado por usar o painel {PAINEL}"]))
        break
