# Trabalho 02 - Programação Funcional
# Tema: Mercado de Carbono (créditos, emissões, compensação)
# Aluno: Lucas Gilmar da Silva e Felipe José Sens

# Obs: Programa simples em Python que calcula as emissões totais de atividades,
# aplica créditos de carbono e mostra custo ou receita final.

def validar_numero(valor):
    try:
        v = float(valor)
        if v < 0:
            return None
        return v
    except:
        return None


def calcular_emissao_total(atividade):
    # emissões por unidade * número de unidades
    return atividade["emissao_por_unidade"] * atividade["unidades"]


def aplicar_creditos(atividades, creditos):
    # aplica os créditos nas emissões, na ordem das atividades
    restante = creditos
    resultado = []
    for a in atividades:
        total = a["emissao_total"]
        aplicado = total if total <= restante else restante
        liquida = total - aplicado
        restante -= aplicado
        resultado.append({
            "nome": a["nome"],
            "emissao_total": total,
            "credito_aplicado": aplicado,
            "emissao_liquida": liquida
        })
    return resultado, restante


def custo_ou_receita(emissao_liquida_total, credito_restante, preco):
    # se ainda restar emissão líquida, precisa comprar crédito
    if emissao_liquida_total > 0:
        return emissao_liquida_total * preco  # custo
    # se sobrou crédito, pode vender
    elif credito_restante > 0:
        return -credito_restante * preco  # receita
    else:
        return 0.0


def main():
    print("=== Mercado de Carbono ===")
    preco = None
    while preco is None:
        p = input("Preço por tonelada (R$): ")
        preco = validar_numero(p)
        if preco is None:
            print("Valor inválido!")

    creditos = None
    while creditos is None:
        c = input("Créditos comprados/gerados (toneladas): ")
        creditos = validar_numero(c)
        if creditos is None:
            print("Valor inválido!")

    # atividades
    atividades = []
    qtd = None
    while qtd is None:
        q = input("Quantas atividades deseja registrar? ")
        qv = validar_numero(q)
        if qv is None or int(qv) != qv:
            print("Digite um número inteiro válido.")
        else:
            qtd = int(qv)

    for i in range(qtd):
        print(f"\nAtividade {i+1}:")
        nome = input("Nome da atividade: ") or f"Atividade{i+1}"
        emis = None
        while emis is None:
            e = input("Emissões por unidade (t): ")
            emis = validar_numero(e)
            if emis is None:
                print("Valor inválido!")
        uni = None
        while uni is None:
            u = input("Quantidade de unidades: ")
            uni = validar_numero(u)
            if uni is None:
                print("Valor inválido!")
        atividades.append({
            "nome": nome,
            "emissao_por_unidade": emis,
            "unidades": uni
        })

    # cálculo total por atividade
    for a in atividades:
        a["emissao_total"] = calcular_emissao_total(a)

    # aplica créditos
    ajustadas, credito_restante = aplicar_creditos(atividades, creditos)

    # emissão líquida total
    emissao_liquida_total = sum(a["emissao_liquida"] for a in ajustadas)

    # custo/receita
    resultado = custo_ou_receita(emissao_liquida_total, credito_restante, preco)

    # saída
    print("\n--- Relatório ---")
    for a in ajustadas:
        print(f"{a['nome']}:")
        print(f"  Emissão total: {a['emissao_total']:.2f}")
        print(f"  Crédito aplicado: {a['credito_aplicado']:.2f}")
        print(f"  Emissão líquida: {a['emissao_liquida']:.2f}")
    print("----------------------")
    print(f"Emissão líquida total: {emissao_liquida_total:.2f} tCO2")
    if resultado > 0:
        print(f"Custo total (compra de créditos): R$ {resultado:.2f}")
    elif resultado < 0:
        print(f"Receita (venda de créditos): R$ {-resultado:.2f}")
    else:
        print("Sem custo ou receita.")
    print("----------------------")


if __name__ == "__main__":
    main()
