class Character(object):
    def __init__(self):
        super(self, Character).__init__()
        self.state = {
            "assassinated": False,
            "stolen": False,
        }

class Assassin(Character):
    def __init__(self):
        super.__init__()
        self.ranking = 1

    def use_ability(self, target_ranking, char_pool: list[Character], crank_to_pid: dict):
        for character in char_pool:
            if character.ranking == target_ranking:
                character.state["assassinated"] = True

class Thief(Character):
    def __init__(self):
        super.__init__()
        self.ranking = 2

    def use_ability(self, target_ranking, char_pool: list[Character], crank_to_pid: dict):
        for character in char_pool:
            if character.ranking == target_ranking:
                character.state["stolen"] = True

class Magician(Character):
    def __init__(self):
        super().__init__()
        self.ranking = 3

    # def use_ability(type: str, exchange_target=-1, n_discard=-1, crank_to_pid: dict):
    #     # if type == "exchange":
    #     #     exchanger = 
    #     pass 
            

class Player(object):
    def __init__(self, id):
        self.id = id
        self.role = None
        self.score = 0
        self.field = []
        self.gold = 0
        self.hand = []

    
    def calculate_score(self):
        self.score = 0



class Game(object):
    def __init__(self, n_player = 6) -> None:
        self.terminated = False
        self.n_player = n_player
        self.players = [Player(i) for i in range(self.n_player)]
        self.deck = []


    def get_player_by_pid(self, id:int) -> Player:
        for p in self.players:
            if p.id == id:
                return p
        return None
    
    def get_player_by_crank(self, crank:int) -> Player:
        for p in self.players:
            if p.role.ranking == crank:
                return p
        return None


    def __check_termination(self) -> None:
        pass

    def round(self) -> None:
        # assign roles 
        self.selection_phase()
        # players act
        for i in range(self.n_player):
            self.turn_phase(i)


    def selection_phase(self) -> dict:
        """
        Let players select character for each round by assigning player.role
        and return a list of character for this round
        """


        crank_to_pid = {}
        return crank_to_pid

    def turn_phase(self, player: Player) -> None:
        """
        1. check status 
        2. character ability
        3. **must** gather resources, pick one of two approaches
        4. **may** build districts, limited to one
        5. check if the game meets the termination critierra
        """ 
        


        self.__check_termination()

    def get_scores(self):
        for player in self.players:
            pass 




    def main_game(self):
        while not self.terminated:
            self.round()

        self.get_scores()
