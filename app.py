from flask import Flask, send_from_directory, send_file, jsonify

app = Flask(__name__, static_folder='static')

@app.route("/")
def read_root():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/control")
def read_control():
    return send_from_directory(app.static_folder, 'control.html')

@app.route("/map")
def read_map():
    return send_from_directory(app.static_folder, 'map.html')

@app.route("/up")
def up():
    print("1")
    return jsonify(message="up")

@app.route("/down")
def down():
    print("2")
    return jsonify(message="down")

@app.route("/right")
def right():
    print("3")
    return jsonify(message="right")

@app.route("/left")
def left():
    print("4")
    return jsonify(message="left")

@app.route("/mapping")
def mapping():
    print("5")
    return jsonify(message="mapping")

app.run(host='0.0.0.0', port=8000)