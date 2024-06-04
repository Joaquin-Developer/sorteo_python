"""Flask API"""
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS  # , cross_origin

from main import Draw
from logic.utils import DrawNotFoundException


ENV = os.getenv("environment") or "prod"
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# permit all origins
CORS(app)


@app.get("/")
def index():
    return """
        <h1>Index</h1><hr />
        <p>Visit: <a href="/api/v1/get_last_draw">/api/v1/get_last_draw</a>
        for get last draw in json format. </p>
    """


@app.get("/api/v1/get_last_draw")
def get_last_draw():
    try:
        return Draw.main()
    except DrawNotFoundException:
        return jsonify({"message": "No historical information found"}), 404


@app.post("/api/v1/run_draw_by_metadata")
def run_by_metadata():
    if not request.json:
        return jsonify({"error": "Invalid input"}), 400

    req = request.json()
    logging.info(req)
    metadata_info = req
    groups_draw = Draw.main(True, True, None, metadata_info)

    return jsonify(groups_draw), 200


if __name__ == "__main__":
    app.run(debug=(ENV != "prod"))
