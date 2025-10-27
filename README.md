# Trabalho 02 - Programação Funcional

**Tema:** Mercado de Carbono (créditos, emissões, compensação)  
**Aluno:** [Seu nome aqui]

---

## 🧠 Descrição
Programa simples em Python que calcula:
- As emissões totais por atividade;
- A compensação com créditos de carbono;
- E o custo ou receita final, dependendo se o usuário precisa comprar ou pode vender créditos.

Feito para a disciplina de **Programação Funcional**, aplicando conceitos básicos de funções puras e separação de responsabilidades, mas de forma simples e prática.

---

## ⚙️ Como Executar

### 1. Pré-requisitos
- Python instalado (versão 3.8 ou superior).  
  Caso ainda não tenha, baixe em [python.org/downloads](https://www.python.org/downloads/).

### 2. Execução
No terminal do VS Code ou Prompt de Comando, vá até a pasta onde está o arquivo:
```bash
cd caminho\da\pasta

python mercado_carbono.py

py mercado_carbono.py

💬 Entradas
O programa pede:

1. Preço por tonelada (em R$);
2. Quantidade total de créditos disponíveis (em toneladas);
3. Quantas atividades serão registradas;
4. Para cada atividade:
    • Nome;
    • Emissões por unidade (em toneladas);
    • Quantidade de unidades.

📊 Saída

O programa exibe um relatório contendo:
    • Emissão total por atividade;
    • Créditos aplicados;
    • Emissão líquida (após compensação);
    • Emissão líquida total;
    • Custo ou receita final do período.