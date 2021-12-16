from flask import Flask, json
from main import Draw

app = Flask(__name__)

@app.get("/api/v1/get_last_sorteo")
def get_last_sorteo():
    # return Draw.get_last_draw()
    return Draw.main()


if __name__ == "__main__":
    app.run(debug=True)
