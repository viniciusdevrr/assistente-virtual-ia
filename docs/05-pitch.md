# Etapa 6 — Pitch

## Roteiro sugerido — aproximadamente 3 minutos

Olá, meu nome é Vinícius Rodrigues Rocha e este é o DataGuide, um assistente
virtual desenvolvido para o desafio de Inteligência Artificial da DIO.

O problema que identifiquei é que pessoas que estão começando em análise de dados
frequentemente encontram conceitos como KPI, DAX, Power Query e indicadores, mas
nem sempre conseguem entender rapidamente o significado e a aplicação desses
termos.

A proposta do DataGuide é oferecer uma forma simples e interativa de consultar
esses conceitos.

O projeto foi construído em Python utilizando Streamlit para a interface,
Pandas para trabalhar com os dados e Ollama para executar uma LLM localmente.

Um dos principais pontos do projeto é a base de conhecimento. Em vez de deixar
o modelo responder livremente, eu organizei informações em arquivos JSON e CSV
e utilizei essas informações como contexto do agente.

Também defini regras de comportamento. O DataGuide deve responder em português,
ser didático e, principalmente, não inventar informações. Quando uma pergunta
não possui resposta na base, o agente deve reconhecer essa limitação.

Para avaliar o projeto, criei casos de teste envolvendo perguntas conhecidas,
perguntas sobre indicadores e perguntas propositalmente fora da base.

Como próximos passos, a solução poderia receber uma base maior, novos conteúdos
de Excel e Power BI, mecanismos de busca semântica e uma camada de avaliação
automática das respostas.

Esse projeto me permitiu praticar documentação de agentes, engenharia de
prompts, organização de dados, integração com LLM e construção de uma aplicação
funcional.
