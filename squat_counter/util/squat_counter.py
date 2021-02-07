
SIT = 'SIT'
MIDDLE = 'MIDDLE'
STAND = 'STAND'
STAND_TEMPERATURE = 3
SIT_TEMPERATURE = 3



class SquatCounter:

    def __init__(self):
        self.init = True
        self.flag = True
        self.count = 0
        self.stand_temperature = 0
        self.sit_temperature = 0
    
    
    def update(self, posture):
        dictionary = {
            SIT: self.sit,
            STAND: self.stand,
            MIDDLE: self.middle,
        }
        dictionary[posture]()


    def stand(self):
        self.sit_temperature = 0
        self.stand_temperature += 1
        if self.stand_temperature > STAND_TEMPERATURE:
            self.__stand__()
    

    def __stand__(self):
        if self.init:
            self.init = False

        if not self.flag:
            self.count += 0.5
            self.flag = True


    def sit(self):
        self.stand_temperature = 0
        self.sit_temperature += 1
        if self.sit_temperature > SIT_TEMPERATURE:
            self.__sit__()


    def __sit__(self):
        if self.init:
            self.count -= 0.5
            self.init = False
        
        if self.flag:
            self.count += 0.5
            self.flag = False


    def middle(self):
        self.stand_temperature = 0
        self.sit_temperature = 0