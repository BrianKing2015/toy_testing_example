from flask import Flask, jsonify, request
import database_creation

app = Flask(__name__)


@app.route('/artists', methods=["GET"])
def get_artists():
    artists = database_creation.get_artists()
    return jsonify(artists)


@app.route("/artists", methods=["POST"])
def insert_artist():
    artist_details = request.get_json()
    first_name = artist_details["first_name"]
    last_name = artist_details["last_name"]
    birth_year = artist_details["birth_year"]
    result = database_creation.insert_artist(first_name, last_name, birth_year)
    return jsonify(result)


@app.route("/artists", methods=["PUT"])
def update_artist():
    artist_details = request.get_json()
    user_id = artist_details["user_id"]
    first_name = artist_details["first_name"]
    last_name = artist_details["last_name"]
    birth_year = artist_details["birth_year"]
    result = database_creation.update_artist(user_id, first_name, last_name, birth_year)
    return jsonify(result)


@app.route("/artists/<user_id>", methods=["DELETE"])
def delete_artist(user_id: str):
    result = database_creation.delete_artist(user_id)
    return jsonify(result)


@app.route("/artists/<user_id>", methods=["GET"])
def get_artist_by_id(user_id: str):
    result = database_creation.get_by_id(user_id)
    return jsonify(result)


if __name__ == "__main__":
    database_creation.create_db_table()
    app.run(host='127.0.0.1', debug=True)
