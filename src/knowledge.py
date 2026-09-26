from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

def load_knowledge():
    with open(DATA_DIR / "base_conhecimento.json", "r", encoding="utf-8") as f:
        knowledge = json.load(f)

    indicators = pd.read_csv(DATA_DIR / "indicadores.csv")
    return knowledge, indicators

def build_context():
    knowledge, indicators = load_knowledge()

    context = []
    context.append("INFORMAÇÕES SOBRE O AGENTE:")
    context.append(json.dumps(knowledge["sobre"], ensure_ascii=False, indent=2))

    context.append("\nCONCEITOS DISPONÍVEIS:")
    for item in knowledge["conceitos"]:
        context.append(
            f"- Tema: {item['tema']}\n"
            f"  Pergunta: {item['pergunta']}\n"
            f"  Resposta-base: {item['resposta']}"
        )

    context.append("\nINDICADORES DISPONÍVEIS:")
    for _, row in indicators.iterrows():
        context.append(
            f"- {row['indicador']} ({row['area']}): {row['descricao']}"
        )

    context.append("\nREGRAS:")
    context.extend(f"- {rule}" for rule in knowledge["regras"])

    return "\n".join(context)
