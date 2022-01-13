
# Person#start_conversation(friend, topic): accept two arguments, the friend to start a conversation with and the topic of conversation.

# If the topic is politics, both people get sadder (their happiness decreases by 2) and the method returns "blah blah partisan blah lobbyist".
# If the topic is weather, both people get a little happier (their happiness increases by 1) and the method returns "blah blah sun blah rain".
# If the topic is not politics or weather, their happiness points don't change and the method returns "blah blah blah blah blah".


class Person:
    all = []

    def __init__(self, name, bank_account=0, happiness=8, hygiene=8):
        self.name = name
        self.bank_account = bank_account
        self.happiness = happiness
        self.hygiene = hygiene
        self.all.append(self)

    def displayPerson(self):
        # print(
        #     f'Name: {self.name}, money: {self.bank_account}, happiness: {self.happiness}, hygiene: {self.hygiene}')
        print("Name: %s\t money: %s\t happiness: %s\t hygiene: %s\t" %
              (self.name, self.bank_account, self.happiness, self.hygiene))

    @classmethod
    def displayAll(cls):  # send in cls instead of self
        for current in cls.all:
            current.displayPerson()

    def setHygiene(self, value):  # self can technically be named anything
        if (value > 10):
            self.hygiene = 10
        elif (value < 0):
            self.hygiene = 0
        else:
            self.hygiene = value

    def setHappiness(self, value):
        if (value > 10):
            self.happiness = 10
        elif (value < 0):
            self.happiness = 0
        else:
            self.happiness = value

    def isClean(self):
        return self.hygiene > 7

    def isHappy(self):
        return self.happiness > 7

    def getPaid(self, amount):
        # no error handling rn
        self.bank_account += amount
        print("money is now: %s" % self.bank_account)

    def takeBath(self):
        self.setHygiene(self.hygiene + 4)
        print("bath taken")

    def workout(self):
        self.setHappiness(self.happiness + 2)
        self.setHygiene(self.hygiene - 3)
        print("queen shit")

    def callFriend(self, friend):
        self.setHappiness(self.happiness + 3)
        friend.setHappiness(friend.happiness + 3)
        print("Hi %s! It's %s. How are you?" % (self.name, friend.name))

    def startConvo(self, friend, topic):
        if topic == "politics":
            self.setHappiness(self.happiness - 2)
            friend.setHappiness(friend.happiness - 2)
            print("rvb")
        elif topic == "weather":
            self.setHappiness(self.happiness + 1)
            friend.setHappiness(friend.happiness + 1)
            print("sunny day")
        else:
            print("blah blah blah")

# end class


# ! TEST
print("TESTING\n")
phil = Person("phil")
jill = Person("jill")
phil.bank_account = 100
print(phil.bank_account)
phil.setHappiness(-1000)
phil.setHygiene(-1000)
# phil.displayPerson()
Person.displayAll()
print(phil.isClean())
print(phil.isHappy())
phil.getPaid(100)
phil.takeBath()
phil.displayPerson()
phil.workout()
phil.displayPerson()
jill.setHappiness(-1000)
phil.callFriend(jill)
Person.displayAll()
phil.startConvo(jill, "politics")
jill.startConvo(phil, "weather")
phil.startConvo(jill, "butts")
Person.displayAll()
