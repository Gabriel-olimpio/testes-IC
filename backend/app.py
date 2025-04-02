from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

csv_path = "Relatorio_cadop.csv"
df = pd.read_csv(csv_path, encoding="utf-8", delimiter=";")

# Substituindo valores NaN por strings vazias
df.fillna("", inplace=True)

# Formatando os valores das colunas para minúsculas
df["Razao_Social"] = df["Razao_Social"].str.lower()
df["Nome_Fantasia"] = df["Nome_Fantasia"].str.lower()


# Rota de busca textual 
@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").lower()
    if not termo:
        return jsonify({"error": "Favor fornecer um termo para buscar."}), 400

    results = df[
        df["Razao_Social"].str.contains(termo, na=False) |
        df["Nome_Fantasia"].str.contains(termo, na=False)
    ]

    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)