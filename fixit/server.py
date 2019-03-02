"""Handles http requests from front-end"""

import json

from flask import Flask, request

from fix_it import FixItGame
from Lobby import Lobby

app = Flask(__name__)

game = FixItGame()
lobby = Lobby()

### Handle things in the lobby ###


@app.route('/lobby/ready')
def is_ready():
    """triggered when a player is ready to go into the game"""
    lobby.num_ready += 1
    if lobby.players and lobby.num_ready == len(lobby.players):
        lobby.start_game(game)

    return get_lobby()


@app.route('/lobby/leave', methods=["GET", "PUT"])
def delete_player_lobby():
    """takes player out of lobby"""
    if request.method == "PUT":
        data = request.get_json()
        name = data['name']

        lobby.delete(name)
        lobby.last_deleted = name

    return get_lobby()


@app.route('/lobby/join', methods=["GET", "PUT"])
def add_player_lobby():
    """Adds a player to the lobby"""
    if request.method == "PUT":
        data = request.get_json()
        name = data['name']
        ip = data['ip']

        lobby.add(name, ip)
        lobby.last_added = name

    return get_lobby()


@app.route('/lobby')
def get_lobby():
    "Get all the players currently in the lobby"
    response = app.response_class(
        response=json.dumps(lobby.players_names),
        status=200,
        mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


### Handle orders made within the game ###


@app.route('/orders/<player>', methods=["GET", "PUT"])
def modify_orders(player):
    """Either adds or deletes an order for a certain player"""
    if request.method == "PUT":
        data = request.get_json()
        value = data['value']
        order_type = data['type']
        task = data['task']

        if task == "ADD":
            game.add_order(player, int(value), order_type)
        elif task == "DELETE":
            game.delete_order(player, int(value), order_type)

    response = app.response_class(
        response=json.dumps(game.accounting.players[player].to_dict()),
        status=200,
        mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    app.run(debug=False)
