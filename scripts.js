function validarNumero(valor) {
    const v = parseFloat(valor);
    return isNaN(v) || v < 0 ? null : v;
}

function calcularEmissaoTotal(a) {
    return a.emissao_por_unidade * a.unidades;
}

function aplicarCreditos(atividades, creditos) {
    let restante = creditos;
    return atividades.map(a => {
        const total = a.emissao_total;
        const aplicado = Math.min(total, restante);
        const liquida = total - aplicado;
        restante -= aplicado;
        return {
            nome: a.nome,
            emissao_total: total,
            credito_aplicado: aplicado,
            emissao_liquida: liquida
        };
    });
}

function custoOuReceita(emissaoLiquidaTotal, creditoRestante, preco) {
    if (emissaoLiquidaTotal > 0) return emissaoLiquidaTotal * preco;
    if (creditoRestante > 0) return -creditoRestante * preco;
    return 0;
}

document.getElementById("calcular").addEventListener("click", () => {
    const preco = validarNumero(document.getElementById("preco").value);
    const creditos = validarNumero(document.getElementById("creditos").value);
    const atividadesStr = document.getElementById("atividades").value;

    if (preco === null || creditos === null) {
        alert("Valores inválidos de preço ou crédito!");
        return;
    }

    let atividades;
    try {
        atividades = JSON.parse(atividadesStr);
    } catch {
        alert("Formato inválido de atividades (use JSON).");
        return;
    }

    const comEmissao = atividades.map(a => ({
        ...a,
        emissao_total: calcularEmissaoTotal(a)
    }));

    const ajustadas = aplicarCreditos(comEmissao, creditos);
    const emissaoLiquidaTotal = ajustadas.reduce((s, a) => s + a.emissao_liquida, 0);
    const creditoRestante = Math.max(0, creditos - comEmissao.reduce((s, a) => s + a.emissao_total, 0));
    const resultado = custoOuReceita(emissaoLiquidaTotal, creditoRestante, preco);

    let relatorio = "--- Relatório ---\n";
    ajustadas.forEach(a => {
        relatorio += `${a.nome}:\n`;
        relatorio += `  Emissão total: ${a.emissao_total.toFixed(2)}\n`;
        relatorio += `  Crédito aplicado: ${a.credito_aplicado.toFixed(2)}\n`;
        relatorio += `  Emissão líquida: ${a.emissao_liquida.toFixed(2)}\n`;
    });
    relatorio += `----------------------\n`;
    relatorio += `Emissão líquida total: ${emissaoLiquidaTotal.toFixed(2)} tCO₂\n`;
    if (resultado > 0)
        relatorio += `Custo total (compra de créditos): R$ ${resultado.toFixed(2)}\n`;
    else if (resultado < 0)
        relatorio += `Receita (venda de créditos): R$ ${(-resultado).toFixed(2)}\n`;
    else relatorio += `Sem custo ou receita.\n`;

    document.getElementById("resultado").textContent = relatorio;
});
