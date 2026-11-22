from decimal import Decimal, ROUND_DOWN

from utilitarios import arredondar, formatar_moeda


class TaxaContratual:
    VALOR = Decimal("2000.00")
    MAX_PARCELAS = 5

    def __init__(self, num_parcelas=1):
        if not 1 <= num_parcelas <= self.MAX_PARCELAS:
            raise ValueError("A taxa pode ser paga em 1 a 5 parcelas.")
        self.num_parcelas = num_parcelas

    def parcelas(self):  
        valor_base = (self.VALOR / self.num_parcelas).quantize(
            Decimal("0.01"), rounding=ROUND_DOWN)
        lista = [valor_base] * (self.num_parcelas - 1)
        lista.append(self.VALOR - valor_base * (self.num_parcelas - 1))
        return lista


class Orcamento:

    MESES = 12
    LARGURA = 52

    def __init__(self, imovel, taxa):
        self.imovel = imovel
        self.taxa = taxa

    def _linha(self, texto, valor):
        valor_txt = formatar_moeda(valor)
        pontos = self.LARGURA - len(texto) - len(valor_txt)
        return f"{texto} {'.' * max(pontos - 2, 2)} {valor_txt}"

    def resumo(self):
        imovel = self.imovel
        linhas = ["=" * self.LARGURA,
                  "ORÇAMENTO RENTSMART - R.M IMÓVEIS".center(self.LARGURA),
                  "=" * self.LARGURA,
                  f"Imóvel: {imovel.descricao()}",
                  "",
                  "ALUGUEL MENSAL",
                  self._linha("Aluguel-base", imovel.ALUGUEL_BASE)]
        for descricao, valor in imovel.adicionais():
            linhas.append(self._linha(f"+ {descricao}", valor))
        linhas.append(self._linha("Subtotal", imovel.subtotal()))
        if imovel.desconto() > 0:
            linhas.append(self._linha(f"- {imovel.rotulo_desconto()}",
                                      imovel.desconto()))
        linhas.append(self._linha("VALOR MENSAL DO ALUGUEL",
                                  imovel.aluguel_mensal()))
        parcelas = self.taxa.parcelas()
        linhas += ["",
                   "TAXA CONTRATUAL (cobrada à parte)",
                   self._linha("Valor da taxa", TaxaContratual.VALOR),
                   f"Pagamento: {self.taxa.num_parcelas}x "
                   f"de {formatar_moeda(parcelas[0])}"
                   + (" (última parcela ajustada)"
                      if parcelas[-1] != parcelas[0] else ""),
                   "",
                   self._linha("TOTAL NOS 12 PRIMEIROS MESES",
                               self.total_primeiro_ano()),
                   "=" * self.LARGURA]
        return "\n".join(linhas)

    def total_primeiro_ano(self):
        return self.imovel.aluguel_mensal() * self.MESES + TaxaContratual.VALOR

    def projecao_12_meses(self):
        aluguel = self.imovel.aluguel_mensal()
        parcelas = self.taxa.parcelas()
        projecao = []
        acumulado = Decimal("0.00")
        for mes in range(1, self.MESES + 1):
            parcela = parcelas[mes - 1] if mes <= len(parcelas) else Decimal("0.00")
            total_mes = arredondar(aluguel + parcela)
            acumulado += total_mes
            projecao.append({"mes": mes,
                             "aluguel": aluguel,
                             "parcela_taxa": parcela,
                             "total_mes": total_mes,
                             "acumulado": acumulado})
        return projecao

    def __str__(self):
        return self.resumo()
