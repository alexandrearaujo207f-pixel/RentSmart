# RentSmart - Sistema de Orçamento de Locação (R.M Imóveis)

Aplicação em **Python** (com **Programação Orientada a Objetos**) que calcula o
orçamento de locação de apartamentos, casas e estúdios da R.M Imóveis, mostra um
resumo detalhado na tela e gera um arquivo **CSV com a projeção dos 12 primeiros meses**.

Trabalho da disciplina *Algorithmic Thinking & Introduction to Object-Oriented Programming*.

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas a biblioteca padrão: `csv` e `decimal`)

## Como executar

```bash
git clone <LINK-DO-SEU-REPOSITORIO>
cd rentsmart
python main.py
```

(Em alguns sistemas o comando é `python3 main.py`.)

O programa faz as perguntas no terminal, valida as respostas, mostra o orçamento
e cria o arquivo `projecao_12_meses.csv` na mesma pasta.

## Regras de negócio

| Item | Valor |
|---|---|
| Apartamento 1 quarto (aluguel-base) | R$ 700,00 |
| Casa 1 quarto (aluguel-base) | R$ 900,00 |
| Estúdio (aluguel-base) | R$ 1.200,00 |
| 2º quarto - apartamento | + R$ 200,00 / mês |
| 2º quarto - casa | + R$ 250,00 / mês |
| Vaga de garagem (casa e apartamento) | + R$ 300,00 / mês |
| Estúdio - pacote inicial de 2 vagas | + R$ 250,00 / mês |
| Estúdio - vaga adicional | + R$ 60,00 por vaga / mês |
| Apartamento sem crianças | 5% de desconto sobre o aluguel (após os adicionais) |
| Taxa contratual | R$ 2.000,00 em 1 a 5 parcelas (apresentada à parte) |

### Decisões tomadas onde o enunciado deixa margem

- O estacionamento do estúdio é opcional. Se o cliente quiser, o mínimo é 2 vagas (pacote de R$ 250,00); cada vaga acima de 2 custa R$ 60,00.
- O desconto de 5% incide sobre aluguel-base + adicionais (2º quarto e garagem).
- A taxa contratual não recebe desconto e é dividida em parcelas iguais, cobradas a partir do mês 1. Se a divisão não for exata, a diferença de centavos fica na última parcela (a soma sempre fecha R$ 2.000,00).

## Estrutura do projeto

| Arquivo | O que contém |
|---|---|
| `main.py` | Ponto de entrada: conduz as perguntas e chama as demais partes |
| `imoveis.py` | Classes `Imovel`, `Apartamento`, `Casa` e `Estudio` |
| `orcamento.py` | Classes `TaxaContratual` e `Orcamento` (resumo e projeção de 12 meses) |
| `entrada.py` | Funções de leitura com validação (`ler_opcao`, `ler_sim_nao`, `ler_inteiro`) |
| `projecao.py` | Função `salvar_csv` |
| `utilitarios.py` | Arredondamento e formatação de moeda |
| `exemplo_projecao_12_meses.csv` | Exemplo de arquivo gerado |

### Classes

- `Imovel` guarda o que é comum (aluguel-base, adicionais, desconto, aluguel mensal).
- `Apartamento`, `Casa` e `Estudio` herdam de `Imovel` e só definem o que muda
  (valores, desconto do apartamento, estacionamento do estúdio).
- `TaxaContratual` calcula as parcelas da taxa.
- `Orcamento` recebe um imóvel e uma taxa, monta o resumo e a projeção.

## Exemplo

Apartamento, 2 quartos, com garagem, sem crianças, taxa em 4 parcelas:

```
Aluguel-base ............ R$ 700,00
+ Segundo quarto ........ R$ 200,00
+ Vaga de garagem ....... R$ 300,00
Subtotal ............... R$ 1.200,00
- Desconto de 5% ........ R$ 60,00
VALOR MENSAL ........... R$ 1.140,00
Taxa contratual: 4x de R$ 500,00
```

## Sobre o CSV

O arquivo usa `;` como separador, vírgula decimal e codificação UTF-8 com BOM,
para abrir corretamente no Excel em português. Colunas: mês, aluguel,
parcela da taxa, total do mês e acumulado.

## Testes manuais realizados

| Cenário | Aluguel mensal | Taxa | Total em 12 meses |
|---|---|---|---|
| Apto, 2 quartos, garagem, sem crianças, 4x | R$ 1.140,00 | 4 x R$ 500,00 | R$ 15.680,00 |
| Casa, 2 quartos, garagem, 5x | R$ 1.450,00 | 5 x R$ 400,00 | R$ 19.400,00 |
| Estúdio, 4 vagas, 3x | R$ 1.570,00 | 666,66 / 666,66 / 666,68 | R$ 20.840,00 |
| Apto, 1 quarto, sem garagem, com crianças, 1x | R$ 700,00 | R$ 2.000,00 | R$ 10.400,00 |
