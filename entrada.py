def ler_opcao(pergunta, opcoes):   
    while True:
        print(pergunta)
        for chave, texto in opcoes.items():
            print(f"  {chave} - {texto}")
        escolha = input("Sua escolha: ").strip()
        if escolha in opcoes:
            return escolha
        print("Opção inválida. Tente novamente.\n")


def ler_sim_nao(pergunta):
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Responda apenas com 's' ou 'n'.")


def ler_inteiro(pergunta, minimo, maximo):
    while True:
        texto = input(f"{pergunta} ({minimo} a {maximo}): ").strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"O número deve estar entre {minimo} e {maximo}.")
