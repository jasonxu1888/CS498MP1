from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def get_num():
    import socket

    return socket.gethostname()


@app.post("/")
def post_num():
    import subprocess

    subprocess.Popen(["python3", "stress_cpu.py"])

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
