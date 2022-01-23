from flask import Flask
from main import Draw

app = Flask(__name__)


@app.get("/")
def index():
    return """
        <h1>Index</h1><hr />
        <p>Visit: <a href="/api/v1/get_last_draw">/api/v1/get_last_draw</a>
        for get last draw in json format. </p>
    """


@app.get("/api/v1/get_last_draw")
def get_last_draw():
    return Draw.main()


if __name__ == "__main__":
    app.run(debug=True)
