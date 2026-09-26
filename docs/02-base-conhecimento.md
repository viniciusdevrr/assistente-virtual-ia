# Etapa 2 — Base de Conhecimento

## Objetivo

A base de conhecimento fornece ao agente informações controladas para reduzir
respostas inventadas e manter o assistente dentro do seu escopo.

## Arquivos

### `base_conhecimento.json`

Contém:

- informações sobre o agente;
- conceitos;
- respostas-base;
- regras de comportamento.

### `indicadores.csv`

Contém exemplos de indicadores organizados por área.

Campos:

| Campo | Descrição |
|---|---|
| categoria | Categoria do indicador |
| indicador | Nome do indicador |
| descricao | Definição resumida |
| area | Área relacionada |

### `exemplos_perguntas.csv`

Contém perguntas usadas para planejar e avaliar o comportamento esperado.

## Estratégia

A aplicação carrega os arquivos no início e transforma seus conteúdos em um
contexto textual enviado ao agente.

A separação entre dados e código permite atualizar a base sem alterar a lógica
principal da aplicação.

## Segurança

A base utiliza apenas conteúdo educacional e dados fictícios. Não são utilizados
dados pessoais, bancários ou credenciais.

## Evolução futura

A base pode ser ampliada com:

- mais conceitos de Excel;
- funções DAX;
- indicadores de RH;
- exemplos de SQL;
- exemplos de tratamento de dados;
- documentos técnicos previamente revisados.
