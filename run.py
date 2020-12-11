from nnf import Var
from lib204 import Encoding
import random

#Creation of Token object to hold token variables
#This represents the Resistance and Spies variable in the report
class Token(object):
    def __init__(self, GameToken):
        self.GameToken = GameToken
    def __hash__(self):
        return hash(self.GameToken)
    def __str__(self):
        return self.GameToken
    def __eq__(self, other):
        return self.GameToken == other.GameToken
    def __repr__(self):
        return str(self)

#Creation of Vote Tracker object to hold Vote variables
#In the report this is the Z variable
class VoteTracker(object):
    def __init__(self, VoteTrack):
        self.VoteTrack = VoteTrack
    def __hash__(self):
        return hash(self.VoteTrack)
    def __str__(self):
        return self.VoteTrack
    def __eq__(self, other):
        return self.VoteTrack == other.VoteTrack
    def __repr__(self):
        return str(self)

#Creation of Mission object to hold Mission variables
#In the report this is the X variable
class Missions(object):
    def __init__(self, mission):
        self.mission = mission
    def __hash__(self):
        return hash(self.mission)
    def __str__(self):
        return self.mission
    def __eq__(self, other):
        return self.mission == other.mission
    def __repr__(self):
        return str(self)

''''
Variables: 16 Total.
We need to prove there exists a winning model for each of these that comes to True (only did some so far on this code)

RR RRR RRR -> TRUE
RR RRS RRR RRRR -> TRUE
RR RRS RRR RRRS RRRR -> TRUE
RR RRS RRR RRRS RRRS
RR RRS RRS RRRR RRRR -> TRUE
RR RRS RRS RRRS

SS RRS RRR RRRR RRRR -> TRUE
SS RRR RRR RRRR  -> TRUE
SS RRR RRR RRRS RRRR -> TRUE

RS RRR RRR RRRR -> TRUE
RS RRR RRR RRRS RRRR -> TRUE
RS RRR RRR RRRS RRRS
RS RRS RRS
RS RRS RRR RRRS
RS RRS RRR RRRR RRRR -> TRUE
RS RSS RRR RRRR RRRR -> TRUE
'''

#Creating a list of Resistance Tokens
ResistanceTokens=[(Token("R1")),(Token("R2")),(Token("R3")),(Token("R4"))]
#Creating a list of Spy Tokens
SpyTokens=[(Token("S1")),(Token("S2")),(Token("S3"))]

#Creating a conjoined list of all player tokens
PlayerTokens= ResistanceTokens + SpyTokens

#Pre_models list will hold the pre-model of the game
pre_models=[]
#It will then be converted to variable types and stored in post models
post_models=[]

''' Each mission will be allocated the corrosponding PlayerTokens based on round (X in the report)'''

MissionOne=[]
MissionTwo=[]
MissionThree=[]
MissionFour=[]
MissionFive=[]

Missions=[(Missions("Mission One")), (Missions("Mission Two")),(Missions("Mission Three")),(Missions("Mission Four")),(Missions("Mission Five"))]
FinalMissions=[]

#this list holds the total number of ways to win each mission based on calculation
MissionWinTotals=[6.0,4.0,2.0,8.0,7.0]
''' The 5 players on the board will choose whether they can approve or reject a mission Y and Z in the report'''

VoteTracking = [(VoteTracker("Z1")), (VoteTracker("Z2")),(VoteTracker("Z3")),(VoteTracker("Z4")),(VoteTracker("Z5"))]

#This will keep track of the votes throughout the game
FinalVotes=[]

''' For the first round 2 Tokens are chosen'''
def StartingRound():

    for i in range(2):
        Select = random.choice(PlayerTokens)
        MissionOne.append(Select)
        PlayerTokens.remove(Select)

'''Starting from round two are the strategies to maximize winnings'''

def StartMissionTwo(MissionOneOption):

    #If both players are in the resistance in round one, then keep these two players and add in a random third player since 3 people are needed for round one.
    #This would also be considered a win for the resistance
    if (MissionOneOption[0] in ResistanceTokens) & (MissionOneOption[1] in ResistanceTokens):
        SelectTwo = random.choice(PlayerTokens)
        for i in range(2):
            MissionTwo.append(MissionOneOption[i])
        MissionTwo.append(SelectTwo)
        PlayerTokens.remove(SelectTwo)

    #If One player is in the resistance in round one, keep only that player and add two random players instead.
    if (MissionOneOption[0] in ResistanceTokens) & (MissionOneOption[1] in SpyTokens):
        MissionTwo.append(MissionOneOption[0])
        for i in range(2):
            SelectThree = random.choice(PlayerTokens)
            MissionTwo.append(SelectThree)
            PlayerTokens.remove(SelectThree)

    if (MissionOneOption[0] in SpyTokens) & (MissionOneOption[1] in ResistanceTokens):
        MissionTwo.append(MissionOneOption[1])
        for i in range(2):
            SelectFour = random.choice(PlayerTokens)
            MissionTwo.append(SelectFour)
            PlayerTokens.remove(SelectFour)

    #If no player is in the resistance in round one, remove all these players and add in 3 random players instead.
    if (MissionOneOption[0] in SpyTokens) & (MissionOneOption[1] in SpyTokens):
        for i in range(3):
            SelectFive = random.choice(PlayerTokens)
            MissionTwo.append(SelectFive)
            PlayerTokens.remove(SelectFive)

def StartMissionThree(MissionTwoOption):

    #If all players are in the resistance in round two, then keep all the players (3 players) and add one random one for the next round
    #This would also be considered a win for the resistance
    if (MissionTwoOption[0] in ResistanceTokens) & (MissionTwoOption[1] in ResistanceTokens) & (MissionTwoOption[2] in ResistanceTokens):
        for i in MissionTwoOption:
            MissionThree.append(i)
    else:
        for i in range(len(MissionTwoOption)):
            if MissionTwoOption[i] in ResistanceTokens:
                MissionThree.append(MissionTwoOption[i])
            else:
                SelectionSix=random.choice(PlayerTokens)
                PlayerTokens.remove(SelectionSix)
                MissionThree.append(SelectionSix)


def StartMissionFour(MissionThreeOption):

    if (MissionThreeOption[0] in ResistanceTokens) & (MissionThreeOption[1] in ResistanceTokens) & (MissionThreeOption[2] in ResistanceTokens):
        for i in MissionThreeOption:
            MissionFour.append(i)
        SelectionSeven=random.choice(PlayerTokens)
        PlayerTokens.remove(SelectionSeven)
        MissionFour.append(SelectionSeven)
    else:
        for i in range(len(MissionThreeOption)):
            PlaceHolder=0
            if MissionThreeOption[i] in ResistanceTokens:
                MissionFour.append(MissionThreeOption[i])
                PlaceHolder+1
                if PlaceHolder==3:
                    SelectionSeven=random.choice(PlayerTokens)
                    PlayerTokens.remove(SelectionSeven)
                    MissionFour.append(SelectionSeven)
                if len(MissionFour)==2:
                    SelectionSeven=random.choice(PlayerTokens)
                    PlayerTokens.remove(SelectionSeven)
                    SelectionEight=random.choice(PlayerTokens)
                    PlayerTokens.remove(SelectionEight)
                    MissionFour.append(SelectionSeven)
                    MissionFour.append(SelectionEight)


def StartMissionFive(MissionFourOption):
    for i in range(4):
        if MissionFourOption[i] in ResistanceTokens:
            MissionFive.append(MissionFourOption[i])
        else:
            FinalSelect= random.choice(PlayerTokens)
            MissionFive.append(FinalSelect)
            PlayerTokens.remove(FinalSelect)


'''For the sake of the model this function will generate a random voting list'''
def vote(votes):
    for i in range(len(pre_models)):
        FinalVotes.append(random.choice(votes))

'''For the sake of the model this function will track the current mission'''
def missiontracker():
    for i in range(len(pre_models)):
        FinalMissions.append(Missions[i])

''' This function determines if there is a win for the resistance, the resistance need to have atleast 3 points to win
The win is determined by checking the variables inside each allocated mission List MissionOne, MissionTwo etc if it Satisfies all R then it's a win this repesents V in the report document'''

def ResistanceWin():
    #The game win condition starts out as a false
    #The counter increases anytime a Resistance mission is a success
    counter = 0
    win = False
    StartingRound()
    if (MissionOne[0] in ResistanceTokens) and (MissionOne[1] in ResistanceTokens):
        counter +=1
    if counter <=3:
        pre_models.append(MissionOne)
        StartMissionTwo(MissionOne)
        if (MissionTwo[0] in ResistanceTokens) and (MissionTwo[1] in ResistanceTokens) and  (MissionTwo[2] in ResistanceTokens):
            counter +=1
        if counter <=3:
            pre_models.append(MissionTwo)
            StartMissionThree(MissionTwo)
            if (MissionThree[0] in ResistanceTokens) and (MissionThree[1] in ResistanceTokens) and  (MissionThree[2] in ResistanceTokens):
                counter +=1
            if counter <= 3:
                pre_models.append(MissionThree)
                StartMissionFour(MissionThree)
                if (MissionFour[0] in ResistanceTokens) and (MissionFour[1] in ResistanceTokens) and  (MissionFour[2] in ResistanceTokens) and (MissionFour[3] in ResistanceTokens):
                    counter +=1
                if counter <= 3:
                    pre_models.append(MissionFour)
                    StartMissionFive(MissionFour)
                    if (MissionFive[0] in ResistanceTokens) and (MissionFive[1] in ResistanceTokens) and  (MissionFive[2] in ResistanceTokens) and (MissionFive[3] in ResistanceTokens):
                        counter +=1
                        pre_models.append(MissionFive)
    if counter >=3:
        win = True

    return win


GameWon = ResistanceWin()
print("Did the Resistance Win:")
print(GameWon)
print("")

vote(VoteTracking)
missiontracker()


for i in range(len(pre_models)):
    post_models.append([Var(s) for s in pre_models[i]])

print("Current game model:")
print(post_models)
print("")


print("Current Vote Tracking per Round:")
print(FinalVotes)

SpyTokensVariable = [Var(i) for i in SpyTokens]
ResistanceTokensVariable = [Var(i) for i in ResistanceTokens]
MissionVariables=[Var(i) for i in FinalMissions]


def game_theory():
    E = Encoding()
    #Constraint is to check if a mission is won or lost based upon if NO spy tokens are played in the current mission or the current mission's vote tracker didn't reach z5
    for x in range(len(post_models)):
        if post_models[x]:
          if len(post_models[x]) == 2:
            if FinalVotes[x] == VoteTracking[4]:
              E.add_constraint(MissionVariables[x].negate())
            elif ((post_models[x][0] not in SpyTokensVariable) and (post_models[x][1] not in SpyTokensVariable)):
              E.add_constraint(MissionVariables[x])
            else:
              E.add_constraint(MissionVariables[x].negate())
          elif len(post_models[x]) == 3:
            if FinalVotes[x] == VoteTracking[4]:
              E.add_constraint(MissionVariables[x].negate())
            elif ((post_models[x][0] not in SpyTokensVariable) and (post_models[x][1] not in SpyTokensVariable) and (post_models[x][2] not in SpyTokensVariable)):
              E.add_constraint(MissionVariables[x]) 
            else:
              E.add_constraint(MissionVariables[x].negate())
          elif len(post_models[x]) == 4:
            if FinalVotes[x] == VoteTracking[4]:
              E.add_constraint(MissionVariables[x].negate())
            elif ((post_models[x][0] not in SpyTokensVariable) and (post_models[x][1] not in SpyTokensVariable) and (post_models[x][2] not in SpyTokensVariable) and (post_models[x][3] not in SpyTokensVariable)):
              E.add_constraint(MissionVariables[x])           
            else:
              E.add_constraint(MissionVariables[x].negate())

    return E

def token_theory():
  S= Encoding()
  #Constraint to check if the tokens played where a success or fail
  for missions in post_models:
    for tokens in missions:
      if tokens in SpyTokensVariable:
        S.add_constraint(tokens.negate())
      else:
        S.add_constraint(tokens)
  return S


if __name__ == "__main__":

    T = game_theory()
    S = token_theory()

    satisfiable = T.is_satisfiable()
    if not GameWon:
      satisfiable = False

    print("\nSatisfiable: %s" % satisfiable)
    print("   Solution: %s" % S.solve())
    print("   Solution: %s" % T.solve())
    print("")
    print("Mission Won Likelihood:")
    for v,vn,x in zip(MissionVariables,post_models,MissionWinTotals):
      print(" %s: %.2f" % (vn, T.likelihood(v)/x))

    