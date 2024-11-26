from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')  # Garantindo que a pasta 'static' será usada para arquivos estáticos
CORS(app)

# Dados simulados
data = [
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Smith", "age": 30}
]

# Rota para obter dados (GET)
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Rota para adicionar novos dados (POST)
@app.route('/api/data', methods=['POST'])
def add_data():
    new_item = request.json
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify(data)  # Retorna toda a lista de itens após adicionar

# Rota para servir o arquivo HTML principal
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Rota para servir o arquivo JavaScript
@app.route('/script.js')
def serve_script():
    return send_from_directory('static', 'script.js')

if __name__ == '__main__':
    app.run(debug=True)
    