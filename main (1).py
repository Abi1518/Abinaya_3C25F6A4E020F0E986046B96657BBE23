#defining class player
class Player:
    def play(self):
       print("The player is playing cricket.")
#defining class batsman
class Batsman(Player):
    def play(self) :
       print("The batsman is batting.")
#defining class bowler
class Bowler(Player):
    def play(self) :
       print("The bowler is bowling.")
#creating an instance of the class
batsman=Batsman()
bowler=Bowler()
 
batsman.play()
bowler.play()