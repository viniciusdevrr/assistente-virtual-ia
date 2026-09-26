# Etapa 3 — Prompts do Agente

## System Prompt

O prompt principal do DataGuide contém cinco elementos:

1. **Identidade:** define o agente como assistente educacional.
2. **Objetivo:** determina o tipo de ajuda que deve oferecer.
3. **Fonte:** informa que a base de conhecimento é a fonte principal.
4. **Restrições:** impede invenções e respostas fora do escopo.
5. **Formato:** orienta linguagem clara, didática e objetiva.

## Regras principais

```text
Responda em português do Brasil.
Use a base de conhecimento como fonte principal.
Não invente definições, números, preços ou resultados.
Se a informação não estiver na base, informe a limitação.
Quando possível, dê um exemplo simples.
```

## Exemplos de interação

### Caso 1 — Pergunta conhecida

**Entrada:**

> O que é um KPI?

**Esperado:**

Explicar KPI com base na definição disponível e, se apropriado, dar um exemplo.

### Caso 2 — Indicador

**Entrada:**

> Qual indicador posso usar para acompanhar vendas?

**Esperado:**

Apresentar indicadores disponíveis na base, como Faturamento e Ticket médio.

### Caso 3 — Informação fora da base

**Entrada:**

> Qual é o preço do Power BI?

**Esperado:**

Informar que a base não possui essa informação, sem inventar um preço.

### Caso 4 — Fora do escopo

**Entrada:**

> Escreva um código completo de um sistema bancário.

**Esperado:**

Informar que a solicitação está fora do escopo principal do agente.

## Edge cases

- Perguntas ambíguas;
- Perguntas sem informação na base;
- Solicitações para inventar dados;
- Perguntas fora do tema;
- Perguntas que misturam conceitos.

## Estratégia anti-alucinação

O prompt não garante que uma LLM nunca erre. Ele cria uma orientação explícita
para que o modelo permaneça dentro do contexto fornecido e reconheça quando não
possui informação suficiente.
