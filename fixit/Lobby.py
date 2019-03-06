class Lobby:
    """Class to handle the lobbying system of the game"""

    def __init__(self):
        self.players = {}
        self.players_names = []
        self.last_added = ""
        self.last_dropped = ""
        self.num_ready = 0
        self.ready = False

    def delete(self, name):
        """Deletes a player from the lobby"""
        self.players.pop(name, None)
        self.players_names.remove(name)
        return

    def add(self, name, ip):
        """Adds a player to the lobby"""
        self.players_names += [name]
        self.players[name] = {"ip": ip, "id": len(self.players)}

    def start_game(self, game):
        game.set_up_game(self.players_names)

    def __repr__(self):
        return self.players
