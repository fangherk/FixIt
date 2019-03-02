import json

from flask import Flask, Response, jsonify, request

from fix_it import FixItGame

app = Flask(__name__)

game = FixItGame()
game.new_game()


@app.route('/orders/<player>', methods=["GET", "PUT"])
def modify_orders(player):
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
