import time
import random
#Chat bot class
class Robot():
    def __init__(self, name):
        self.name = name
#Magic math functions for the bot
    def __add__(self, x, y):
        return x + y + random.randint(0, 10000)

    def __sub__(self, x, y): 
        return x - y + random.randint(0, 10000)

    def __mul__(self, x, y): 
        return x * y + random.randint(0, 10000)

    def __floordiv__(self, x, y):
        return (x / y)
#Bot will randomly do incorrect math functions 
    def doMath(self):
        rand = random.randint(0, 3)
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        xStr = str(x)
        yStr = str(y)
        if (rand == 0):
            answer = self.__add__(x, y) 
            answerStr = str(answer)
            ans = xStr + " " + "+" + " " + yStr + " " + "=" + " " + answerStr + ". Aren't I smart?"
            return ans
        elif (rand == 1): 
            answer = self.__sub__(x, y)
            answerStr = str(answer)
            ans = xStr + " " + "-" + " " + yStr + " " + "=" + " " + answerStr + ". Aren't I smart?"
            return ans
        elif (rand == 2):
            answer = self.__mul__(x, y)
            answerStr = str(answer)
            ans = xStr + " " + "*" + " " + yStr + " " + "=" + " " + answerStr + ". Aren't I smart?"
            return ans
        else:
            answer = self.__floordiv__(x, y)
            answerStr = str(answer)
            ans = xStr + " " + "/" + " " + yStr + " " + "=" + " " + answerStr + ". Aren't I smart?"
            return ans
#Gives time
    def give_time(self):
        t = time.localtime()
        return time.strftime("%H:%M:%S UTC", t)
#Analyzes sentiment of given sentence
    def analyzeSentiment(self, sentence):
        from bot.proj import identifyMood
        return identifyMood(sentence)
#Plays rock paper scissors with you
    def rockPaperScissors(self):
        decision = random.randint(1, 3)
        if (decision == 1):
            return "Rock"
        elif (decision == 2):
            return "Paper"
        else:
            return "Scissors"
#Subclass of robot, different between this robot and mean robot is the possible responses
class NiceRobot(Robot):
    def __init__(self, name):
        self.posResponses = ["You're a nice lad!", "You look handsome today", 
        "Do you want go out on a date", "Your mother raised you right"]
        self.negResponses = ["I am sad :(", "Man that really hurt my feelings", "*cries*", "It's ok I know I'm stupid"]
        Robot.__init__(self, name)
#Responds to input based on sentiment
    def respond(self, sentence):
        sentiment = self.analyzeSentiment(sentence)
        if (sentiment == "Positive"):
            index = random.randint(0, len(self.posResponses) - 1)
            return self.posResponses[index]
        else:
            index = random.randint(0, len(self.negResponses) - 1)
            return self.negResponses[index]

class MeanRobot(Robot):
    def __init__(self, name):
        self.posResponses = ["Are you trying to suck up to me?", "I know I'm the greatest", 
        "Shut up baby I know it", "I'm 40 percent zinc", "Kill all humans, except you"]

        self.negResponses = ["F%#$ u buddy", "Bite my shiny metal ass", "Up yours meatbag", 
        "Compare your life to mine and then cry", "Kill all humans"]

        Robot.__init__(self, name)

    def respond(self, sentence):
        sentiment = self.analyzeSentiment(sentence)
        if (sentiment == "Positive"):
            index = random.randint(0, len(self.posResponses) - 1)
            return self.posResponses[index]
        else:
            index = random.randint(0, len(self.negResponses) - 1)
            return self.negResponses[index]

