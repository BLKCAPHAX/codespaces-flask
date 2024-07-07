from flask import Flask, render_template
import time

app = Flask(__name__)

def generator():
    yield "{ \"answer\" : \"".encode("utf-8")
    for i in range(0, 999999):
        yield (str(i) + " ").encode("utf-8")
        time.sleep(0.3)
    yield "\"}".encode("utf-8")

@app.route("/v4/search", methods=["GET"])
def search():
    return generator(), {"Content-Type" : "application/json"}
