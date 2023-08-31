import random
from prettytable import PrettyTable

class ChessPlayer():
    def __init__(self,p_name,Age,ELO,Tenacity,isboring):
        self.name = p_name
        self.age = Age
        self.Elo = ELO
        self.tenacity = Tenacity
        self.isBoring = isboring
        self.Points = 0

    def __str__(self):
        return f"{self.name}"
    
    def simulateMatch(a,b):
        EloDiff = abs(a.Elo-b.Elo)
        a.TourneyScore=0
        b.TourneyScore=0
        Draw = False

        if (a.isBoring == True or b.isBoring == True) and EloDiff<=100:
            Draw=True
        elif EloDiff>100:
            a.TourneyScore+=1
        elif EloDiff>50 and EloDiff<100:
            winning_factor = b.tenacity*random.randint(0,10)
            if a.Elo>winning_factor:
                a.TourneyScore+=1
            else:
                b.TourneyScore+=1
        else:
            if a.tenacity>b.tenacity:
                a.TourneyScore+=1
            else:
                b.TourneyScore+=1
        
        if a.TourneyScore>b.TourneyScore:
            return 1
        elif Draw == True:
            return 0.5
        else:
            return 0

            

    
#initialising players
Courage = ChessPlayer("Courage the Cowardly Dog",25,1000.39,1000,False,)
PrincessPeach = ChessPlayer("Princess Peach",23,945.65,50,True)
WalterWhite = ChessPlayer("Walter White",50,1650.73,750,False)
RoryGilmore = ChessPlayer("Rory Gilmore",16,1700.87,500,False)
AnthonyFantano = ChessPlayer("Anthony Fantano",37,1400.45,400,True)
BethHarmon = ChessPlayer("Beth Harmon",20,2500.34,150,False)

my_list = [Courage,PrincessPeach,WalterWhite,RoryGilmore,AnthonyFantano,BethHarmon]

for i in my_list:
    for j in my_list:
        if i==j:
            pass
        else:
            if i.Elo > j.Elo:
                x = ChessPlayer.simulateMatch(i,j)
                if x==1:
                    i.Points+=x
                elif x==0.5:
                    i.Points+=x
                    j.Points+=0.5
                else:
                    j.Points+=1
            else:
                x = ChessPlayer.simulateMatch(j,i)
                if x==1:
                    j.Points+=x
                elif x==0.5:
                    i.Points+=x
                    j.Points+=0.5
                else:
                    i.Points+=1

mytable = PrettyTable(["Player Name" , "Score"])
for i in my_list:
    mytable.add_row([i,int(i.Points)])

print(mytable)

