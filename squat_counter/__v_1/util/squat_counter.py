
SIT = 'SIT'
MIDDLE = 'MIDDLE'
STAND = 'STAND'
STAND_TEMPERATURE = 2
SIT_TEMPERATURE = 2



class SquatCounter:

    def __init__(self):
        self.init = True
        self.flag = True
        self.count = 0
        self.stand_temperature = 0
        self.sit_temperature = 0
    
    
    def update(self, posture, velocity):
        dictionary = {
            SIT: self.sit,
            STAND: self.stand,
            MIDDLE: self.middle,
        }
        dictionary[posture](velocity)


    def stand(self, velocity):
        self.sit_temperature = 0
        self.stand_temperature += 1
        if self.stand_temperature > STAND_TEMPERATURE:
            if velocity < 0:
                self.__stand__()
    

    def __stand__(self):
        if self.init:
            self.init = False

        if not self.flag:
            self.count += 0.5
            self.flag = True


    def sit(self, velocity):
        self.stand_temperature = 0
        self.sit_temperature += 1
        if self.sit_temperature > SIT_TEMPERATURE:
            if velocity > 0:
                self.__sit__()


    def __sit__(self):
        if self.init:
            self.count -= 0.5
            self.init = False
        
        if self.flag:
            self.count += 0.5
            self.flag = False


    def middle(self, velocity):
        self.stand_temperature = 0
        self.sit_temperature = 0