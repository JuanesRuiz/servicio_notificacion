from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notificar', methods=['POST'])
def notificar():
    # Verifica si el Content-Type es application/json
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 400
    
    try:
        data = request.json
        nombre = data.get("nombre", "desconocido")
        print(f"Notificando a {nombre}...")
        return jsonify({"Notificacion": f"Se notificó a {nombre} exitosamente."})
    except Exception as e:
        return jsonify({"error": f"Error procesando la solicitud: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
