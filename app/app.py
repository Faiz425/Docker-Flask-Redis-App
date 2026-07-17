from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


@app.route("/")
def home():
    return "Welcome to Flask Redis App"


@app.route("/count")
def count():
    visits = r.incr("visits")
    return f"Visit count: {visits}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)