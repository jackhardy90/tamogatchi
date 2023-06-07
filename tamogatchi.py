import math
import time

class tamogatchi:
    def __init__(self):
        self.happiness = 100
        self.foodLevel = 100
        self.health = 100

    def happiness(self):
        return self.happiness
    
    def foodLevel(self):
        return self.foodLevel

    def health(self):
        return self.health

    def nextDay(self):
        self.happiness -= 2
        self.foodLevel -= 2
        self.health -= 2

    def gatchiDeath(self):
        if self.health <= 0:
            self.health = 0
            print ("Your tamogatchi died of old age.....!")
        if self.foodLevel <= 0:
            self.foodLevel = 0
            print ("Your tamogatchi died of hunger....")
        if self.happiness <= 0:
            self.happiness = 0
            print ("Your tamogatchi died of sadness....")
        else:
            raise Exception (
                print ("We don't know what happened, your tamogatchi just died......:(")
            )

    def __str__(self):
        return 'Your happiness score: ' + str(self.happiness) + '\n' + 'Your Food Level: ' + str(self.foodLevel) + '\n' + 'Your health level: ' + str(self.health)


#main program


gatchiFriend = tamogatchi()
while True:
    print ("Your Tamogatchi!")

#User input
    while True:
        print ('Happiness:', gatchiFriend.happiness, 'Hunger:', gatchiFriend.foodLevel, 'Health:', gatchiFriend.health)
        action = input ("What would you like to do? " '\n'
               '1. Play' '\n'
               '2. Feed' '\n'
               '3. Walk' '\n'
               '4. Quit' '\n')
        if gatchiFriend.health <= 0:
            gatchiFriend.gatchiDeath()
            break
        if action == '1':
            gatchiFriend.happiness += 5
            gatchiFriend.foodLevel -= 2
            gatchiFriend.health -= 3
            gatchiFriend.nextDay()
            break
        if action == '2':
            gatchiFriend.happiness += 5
            gatchiFriend.foodLevel += 3
            gatchiFriend.health += 2
            gatchiFriend.nextDay()
            break
        if action == '3':
            gatchiFriend.happiness += 3
            gatchiFriend.foodLevel -= 4
            gatchiFriend.health += 2
            gatchiFriend.nextDay()
            break
        if action == '4':
            print ("Thanks for playing!")
        else:
            raise TypeError(
                print ("Please only use single integers")
            
            )
        
            
