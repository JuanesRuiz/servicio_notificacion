from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    nombre = data.get("nombre", "desconocido")
    print(f"📨 Notificando a {nombre}...")
    return jsonify({"notificacion": f"Se notificó a {nombre} exitosamente."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
