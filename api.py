from flask import Flask, json
from main import Draw

app = Flask()

@app.get("/api/v1/get_last_sorteo")
def get_last_sorteo():
    return Draw.get_last_draw()


if __name__ == "__main__":
    app.run(debug=True)
