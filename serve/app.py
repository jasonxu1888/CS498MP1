from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def get_num():
    import socket

    return socket.gethostbyname()


@app.post("/")
def post_num():
    import subprocess

    subprocess.Popen(["python3", "stress_cpu.py"])


if __name__ == "__main__":
    app.run()