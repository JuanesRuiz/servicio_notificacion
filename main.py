from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/notificar', methods=['POST'])
def notificar():
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 400
    data = request.json
    nombre = data.get("nombre", "desconocido")
    print(f"Notificando a {nombre}...")
    return jsonify({"Notificacion": f"Se notificó a {nombre} exitosamente."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
