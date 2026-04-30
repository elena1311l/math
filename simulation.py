import random
import json
class SlotMachine:
    def __init__(self, name, config):
        self.name = name     
        self.config = config 
        self.history = []
        self.reels= [
            ["Seven"] * 1 + ["Cherry"] * 3 + ["Lemon"] * 6,
            ["Seven"] * 1 + ["Cherry"] * 2 + ["Lemon"] * 7,
            ["Seven"] * 1 + ["Cherry"] * 1 + ["Lemon"] * 8]

    def run_simulation(self, spins):
        res_sum = 0
        for _ in range(spins):
            result1=random.choice(self.reels[0])
            result2=random.choice(self.reels[1])
            result3=random.choice(self.reels[2])
            if result1==result2==result3=="Seven":
                res_sum+=self.config["seven_win"]
            elif result1==result2==result3=="Cherry":
                res_sum+=self.config["cherry_win"]
            elif result1==result2==result3=="Lemon":
                res_sum+=self.config["lemon_win"]
            else:
                res_sum+=0
        self.history.append(res_sum/ spins)
        return res_sum/ spins
        
    def save_report(self):
        data_to_save={
            "game_name":self.name,
            "results":self.history,
            "settings":self.config
        }

        with open('final.json', 'w') as fl:
            json.dump(data_to_save, fl, indent=2)

try:
    with open('config.json', 'r') as file:
        data=json.load(file)
except FileNotFoundError:
    print("Error: The file was not found")
    data = {"seven_win": 100, "cherry_win": 10, "lemon_win": 2}

my_game = SlotMachine("Fruit Paradise", data) 
result_rtp=my_game.run_simulation(100000)
my_game.run_simulation(50000)
my_game.run_simulation(150000)
my_game.run_simulation(950000)
my_game.save_report()

print(f'Name of game {my_game.name}')
print(f"Result is {result_rtp} ")
print(f"History is: {my_game.history}")