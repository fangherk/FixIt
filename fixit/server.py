import json

from flask import Flask, request

from fixit.fix_it import FixItGame

app = Flask(__name__)
game = FixItGame()

try:
    num_players = 3  #int(input("How many players are there?\t"))
except:
    raise ValueError("Invalid number of players")
else:
    players = [str(x) for x in list(range(1, int(num_players) + 1))]
    game.set_up_game(players)


@app.route('/orders/<player>', methods=["GET", "PUT"])
def modify_orders(player):
    player_json = game.accounting.players[player].to_dict()
    if request.method == "GET":
        return json.dumps(player_json)
    elif request.method == "PUT":
        data = request.get_json()
        value = data['value']
        type = data['type']
        task = data['task']

        if task == "ADD":
            game.add_order(player, int(value), type)
        elif task == "DELETE":
            game.delete_order(player, int(value), type)

        return json.dumps(game.accounting.players[player].to_dict())


if __name__ == "__main__":
    app.run(debug=False, port=5000)
