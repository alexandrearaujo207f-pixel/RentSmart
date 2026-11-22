import csv

COLUNAS = ["mes", "aluguel", "parcela_taxa", "total_mes", "acumulado"]
CABECALHO = ["Mês", "Aluguel (R$)", "Parcela da taxa (R$)",
             "Total do mês (R$)", "Acumulado (R$)"]


def _numero_br(valor):
    return f"{valor:.2f}".replace(".", ",")


def salvar_csv(projecao, caminho="projecao_12_meses.csv"):
    with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(CABECALHO)
        for linha in projecao:
            escritor.writerow([linha["mes"]] +
                              [_numero_br(linha[c]) for c in COLUNAS[1:]])
    return caminho
