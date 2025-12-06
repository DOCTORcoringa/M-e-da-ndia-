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
# ESCOLHA DE QUANTIDADE (NOVA)
# ============================
def escolher_quantidade():
    print(caixa("QUANTIDADE", [
        "1 - 100",
        "2 - 250",
        "3 - 500",
        "4 - 1000",
        "5 - Digitar quantidade manualmente"
    ]))

    while True:
        opc = input(RED + f"{PAINEL} | Escolha: " + RESET).strip()

        if opc == "1":
            return 100
        elif opc == "2":
            return 250
        elif opc == "3":
            return 500
        elif opc == "4":
            return 1000
        elif opc == "5":
            custom = input(RED + f"{PAINEL} | Digite a quantidade: " + RESET).strip()
            if custom.isdigit():
                return int(custom)
            print(caixa("ERRO", ["Quantidade inválida."]))
        else:
            print(caixa("ERRO", ["Opção inválida."]))

# ============================
# BARRA DE CARREGAMENTO
# ============================
def barra_carregamento(acao, qtd):
    os.system(CLEAR)
    print(RED + f"╭┄┄┄┄┄┄❲ PROCESSANDO {acao.upper()} ❳┄┄┄┄┄┄╮")
    print(RED + "│ Executando...")
    print(RED + "│")

    tempo = 0.1 * qtd / 10

    for _ in tqdm(range(qtd), bar_format=RED + "│ {l_bar}{bar}{r_bar}"):
        time.sleep(tempo)

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

    print(caixa("AÇÃO INICIADA", [
        f"Ação Selecionada: {tipo}",
        "Use apenas em ambiente autorizado"
    ]))

    ddi = escolher_ddi()
    numero_local = input(RED + f"{PAINEL} | Número local: " + RESET)
    numero = ddi + numero_local

    if not validar_ddi(numero):
        print(caixa("ERRO", ["DDI não permitido."]))
        input(RED + "ENTER..." + RESET)
        return

    qtd = escolher_quantidade()
    barra_carregamento(tipo, qtd)

    print(caixa("RELATÓRIO FINAL", [
        f"Número: {numero}",
        f"Ação realizada: {tipo}",
        f"Quantidade executada: {qtd}",
        "Status: Concluído"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# EXECUÇÃO — MODO MULTI
# ============================
def executar_multi(tipo):
    os.system(CLEAR)

    print(caixa("AÇÃO INICIADA", [
        f"Ação Selecionada: {tipo}",
        "Modo múltiplos números"
    ]))

    ddi = escolher_ddi()
    nums = input(RED + f"{PAINEL} | Números (vírgula): " + RESET)
    lista = [ddi + n.strip() for n in nums.split(",") if n.strip()]

    if len(lista) < 2:
        print(caixa("ERRO", ["É necessário no mínimo 2 números!"]))
        input(RED + "ENTER..." + RESET)
        return

    for n in lista:
        if not validar_ddi(n):
            print(caixa("ERRO", [f"Número inválido: {n}"]))
            input(RED + "ENTER..." + RESET)
            return

    qtd = escolher_quantidade()
    total = len(lista) * qtd
    barra_carregamento(tipo, total)

    print(caixa("RELATÓRIO FINAL", [
        f"Números processados: {len(lista)}",
        f"Ação realizada: {tipo}",
        f"Quantidade total: {total}",
        "Status: Concluído"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# MENU
# ============================
def menu():
    os.system(CLEAR)

    banner = """███╗░░██╗██╗██╗░░██╗
████╗░██║██║╚██╗██╔╝
██╔██╗██║██║░╚███╔╝░
██║╚████║██║░██╔██╗░
██║░╚███║██║██╔╝╚██╗
╚═╝░░╚══╝╚═╝░░╚═╝░░╚═╝

██████╗░░█████╗░██╗███╗░░██╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██║████╗░██║██║░░██║██╔══██╗
██████╔╝███████║██║██╔██╗██║███████║███████║
██╔══██╗██╔══██║██║██║╚████║██╔══██║██╔══██║
██║░░██║██║░░██║██║██║░╚███║██║░░██║██║░░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝"""

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
