from flask import Flask, request

app = Flask(__name__)

seed = 0


@app.get("/")
def get_num():
    return str(seed)


@app.post("/")
def post_num():
    global seed
    seed = request.json["num"]


if __name__ == "__main__":
    app.run()
