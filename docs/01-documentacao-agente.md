# Etapa 1 — Documentação do Agente

## 1. Identificação

**Nome:** DataGuide

**Tipo:** Assistente virtual educacional com Inteligência Artificial Generativa.

## 2. Problema

Pessoas que estão começando a estudar análise de dados frequentemente encontram
termos técnicos, ferramentas e indicadores sem saber exatamente o que significam
ou como são utilizados na prática.

O DataGuide foi criado para oferecer explicações simples e contextualizadas,
utilizando uma base de conhecimento controlada.

## 3. Público-alvo

- Estudantes de tecnologia;
- Pessoas iniciantes em análise de dados;
- Profissionais que desejam revisar conceitos de Excel e Power BI;
- Pessoas interessadas em automação de processos.

## 4. Objetivo

O agente deve explicar conceitos e indicar exemplos relacionados a:

- análise de dados;
- indicadores;
- Excel;
- Power BI;
- automação de processos.

## 5. Persona e tom de voz

O DataGuide possui comportamento:

- didático;
- objetivo;
- cordial;
- profissional;
- acessível para iniciantes.

Ele evita excesso de termos técnicos sem explicação.

## 6. Escopo

### O agente pode

- explicar conceitos presentes na base;
- comparar conceitos disponíveis;
- apresentar exemplos simples;
- consultar a lista de indicadores cadastrados;
- orientar estudos de forma educacional.

### O agente não pode

- inventar informações;
- afirmar dados que não estejam na base;
- realizar ações em sistemas externos;
- substituir profissionais especializados;
- apresentar informações externas como se estivessem na base.

## 7. Segurança e anti-alucinação

A aplicação fornece ao modelo uma base de conhecimento estruturada e instruções
explícitas para não inventar informações.

Quando não houver informação suficiente, o comportamento esperado é informar a
limitação ao usuário.

## 8. Arquitetura

```mermaid
flowchart TD
    A[Usuário] --> B[Interface Streamlit]
    B --> C[Prompt do Sistema]
    C --> D[Base de Conhecimento]
    C --> E[Ollama / LLM Local]
    E --> F[Resposta]
    F --> B
```

## 9. Fluxo

1. Usuário envia uma pergunta.
2. A aplicação recupera a base de conhecimento.
3. A base é inserida no contexto do agente.
4. O prompt define comportamento e restrições.
5. O Ollama processa a solicitação.
6. A resposta é exibida no Streamlit.
7. Caso o Ollama não esteja disponível, a aplicação utiliza o modo demonstração.

## 10. Limitações

A qualidade da resposta depende do modelo local utilizado e da qualidade da base
de conhecimento. A base atual é propositalmente pequena e educacional.
