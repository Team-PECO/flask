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
    print("up")
    return jsonify(message="up")

@app.route("/down")
def down():
    print("down")
    return jsonify(message="down")

@app.route("/right")
def right():
    print("right")
    return jsonify(message="right")

@app.route("/left")
def left():
    print("left")
    return jsonify(message="left")

# IP 주소를 저장한 파일을 보내주는 엔드포인트
@app.route("/get-ip")
def get_ip():
    try:
        # static 폴더 내에 있는 ip.txt 파일을 클라이언트에 전송
        return send_file('static/ip.txt')
    except FileNotFoundError:
        return jsonify(error="IP file not found"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
