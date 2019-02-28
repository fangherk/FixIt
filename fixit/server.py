import json

from flask import Flask, request

from fixit.fix_it import FixItGame

app = Flask(__name__)

game = FixItGame()
game.new_game()


@app.route('/orders/<player>', methods=["GET", "PUT"])
def modify_orders(player):
    player_json = game.accounting.players[player].to_dict()
    if request.method == "GET":
        return json.dumps(player_json)
    elif request.method == "PUT":
        data = request.get_json()
        value = data['value']
        order_type = data['type']
        task = data['task']

        if task == "ADD":
            game.add_order(player, int(value), order_type)
        elif task == "DELETE":
            game.delete_order(player, int(value), order_type)

        return json.dumps(game.accounting.players[player].to_dict())


if __name__ == "__main__":
    app.run(debug=False, port=5000)
