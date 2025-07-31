from flask import Flask, request, jsonify

app = Flask (__name__)

#Crear la ruta del endpoint
@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    nombre = data.get("nombre", "desconocido")
    print (f" notificando a {nombre}...")
    return jsonify({"Notificacion": f"Se notifico a {nombre} exitosamente."})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 10000)
