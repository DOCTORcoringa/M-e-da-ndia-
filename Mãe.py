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
# CAIXINHA PADRÃO
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
    print(RED + f"│ Ação: {acao}")
    print(RED + "│ Carregando...\n│")

    for i in tqdm(range(qtd), bar_format=RED + "│ {l_bar}{bar}{r_bar}"):
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
# FUNÇÃO DE ESCOLHA DE DDI
# ============================
def escolher_ddi():
    print(caixa("SELECIONE O DDI", [f"{codigo} - {pais}" for codigo, pais in DDIS_COMPLETOS.items()]))
    while True:
        ddi = input(RED + f"{PAINEL} | Escolha o DDI pelo código: " + RESET).strip()
        if ddi in DDIS_COMPLETOS:
            return ddi
        else:
            print(caixa("ERRO", [f"{PAINEL} | DDI inválido! Tente novamente."]))

# ============================
# VALIDAÇÃO DE DDIs
# ============================
def validar_ddi(numero):
    for ddi in DDIS_PERMITIDOS:
        if numero.startswith(ddi):
            return True
    return False

# ============================
# PROCESSAMENTO — MODO ÚNICO
# ============================
def executar_unico(tipo):
    os.system(CLEAR)

    print(caixa("INFORMAÇÕES", [
        f"{PAINEL} | Modo Selecionado: {tipo}",
        f"{PAINEL} | Uso restrito: apenas em ambiente controlado"
    ]))

    ddi = escolher_ddi()
    numero_local = input(RED + f"{PAINEL} | Digite o número local: " + RESET)
    numero = ddi + numero_local

    if not validar_ddi(numero):
        print(caixa("ERRO", [
            f"{PAINEL} | DDI não permitido",
            f"{PAINEL} | Use um dos DDIs permitidos: {', '.join(DDIS_PERMITIDOS)}"
        ]))
        input(RED + "ENTER..." + RESET)
        return

    qtd = int(input(RED + f"{PAINEL} | Quantidade: " + RESET))

    barra_carregamento(tipo, qtd)

    print(caixa("RELATÓRIO FINAL DETALHADO", [
        f"{PAINEL} | Número do Alvo: {numero}",
        f"{PAINEL} | Ação Executada: {tipo}",
        f"{PAINEL} | Quantidade: {qtd}",
        f"{PAINEL} | Tempo Estimado: {qtd * 0.2:.1f}s",
        f"{PAINEL} | Status: Concluído",
        f"{PAINEL} | Sistema: {PAINEL}"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# PROCESSAMENTO — MODO DUPLO (2+ NÚMEROS)
# ============================
def executar_duplo(tipo):
    os.system(CLEAR)

    print(caixa("INFORMAÇÕES", [
        f"{PAINEL} | Modo Selecionado: {tipo}",
        f"{PAINEL} | Uso restrito: apenas em ambiente controlado",
        f"{PAINEL} | Mínimo: 2 números"
    ]))

    ddi = escolher_ddi()
    numeros = input(RED + f"{PAINEL} | Digite vários números locais separados por vírgula: " + RESET)
    lista = [ddi + n.strip() for n in numeros.split(",") if n.strip()]

    if len(lista) < 2:
        print(caixa("ERRO", [
            f"{PAINEL} | É necessário pelo menos DOIS números.",
            f"{PAINEL} | Você colocou apenas {len(lista)}"
        ]))
        input(RED + "ENTER..." + RESET)
        return

    for n in lista:
        if not validar_ddi(n):
            print(caixa("ERRO", [
                f"{PAINEL} | Número inválido: {n}",
                f"{PAINEL} | Use DDIs permitidos: {', '.join(DDIS_PERMITIDOS)}"
            ]))
            input(RED + "ENTER..." + RESET)
            return

    qtd = len(lista)

    barra_carregamento(tipo, qtd)

    print(caixa("RELATÓRIO FINAL DETALHADO", [
        f"{PAINEL} | Total de Números: {qtd}",
        f"{PAINEL} | Ação Executada: {tipo}",
        f"{PAINEL} | Tempo Estimado: {qtd * 0.2:.1f}s",
        f"{PAINEL} | Status: Concluído",
        f"{PAINEL} | Sistema: {PAINEL}"
    ]))

    input(RED + "ENTER para voltar..." + RESET)

# ============================
# MENU PRINCIPAL
# ============================
def menu():
    os.system(CLEAR)

    banner = f"""███╗░░██╗██╗██╗░░██╗
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
        f"{PAINEL} | 1 Denúncia (1 número)",
        f"{PAINEL} | 2 Spam (1 número)",
        f"{PAINEL} | 3 Denúncia Dupla (2+ números)",
        f"{PAINEL} | 4 Spam Duplo (2+ números)",
        f"{PAINEL} | 5 Sair"
    ]

    print(caixa("MENU PRINCIPAL", opcoes))

    escolha = input(RED + f"{PAINEL} | Digite a opção: " + RESET)
    return escolha

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
        executar_duplo("Denúncia Dupla")
    elif opc == "4":
        executar_duplo("Spam Duplo")
    elif opc == "5":
        os.system(CLEAR)
        print(caixa("SAINDO", [f"{PAINEL} | Obrigado por usar o painel {PAINEL}"]))
        break
