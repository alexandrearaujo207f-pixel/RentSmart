from entrada import ler_inteiro, ler_opcao, ler_sim_nao
from imoveis import Apartamento, Casa, Estudio
from orcamento import Orcamento, TaxaContratual
from projecao import salvar_csv

TIPOS = {"1": "Apartamento", "2": "Casa", "3": "Estúdio"}
MAX_VAGAS_ESTUDIO = 10


def montar_imovel():
    tipo = ler_opcao("Qual tipo de imóvel o cliente deseja?", TIPOS)

    if tipo == "3":
        vagas = 0
        if ler_sim_nao("Deseja estacionamento? (pacote inicial de 2 vagas)"):
            vagas = ler_inteiro("Quantas vagas no total", 2, MAX_VAGAS_ESTUDIO)
        return Estudio(vagas)

    quartos = ler_opcao("Quantos quartos?", {"1": "1 quarto", "2": "2 quartos"})
    garagem = ler_sim_nao("Deseja vaga de garagem?")
    if tipo == "1":
        tem_criancas = ler_sim_nao("O cliente possui crianças?")
        return Apartamento(quartos == "2", garagem, tem_criancas)
    return Casa(quartos == "2", garagem)


def main():
    print("=== RentSmart - R.M Imóveis ===\n")
    imovel = montar_imovel()
    parcelas = ler_inteiro("Em quantas parcelas pagar a taxa contratual",
                           1, TaxaContratual.MAX_PARCELAS)
    orcamento = Orcamento(imovel, TaxaContratual(parcelas))

    print()
    print(orcamento)

    arquivo = salvar_csv(orcamento.projecao_12_meses())
    print(f"\nProjeção dos 12 meses salva em: {arquivo}")


if __name__ == "__main__":
    main()
