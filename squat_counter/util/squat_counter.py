
SIT = 'SIT'
MIDDLE = 'MIDDLE'
STAND = 'STAND'
STAND_TEMPERATURE = 3
SIT_TEMPERATURE = 3



class SquatCounter:

    def __init__(self):
        self.curent_posture = STAND
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
        if self.curent_posture == SIT:
            self.count += 1
        self.curent_posture = STAND


    def sit(self):
        self.stand_temperature = 0
        self.sit_temperature += 1
        if self.sit_temperature > SIT_TEMPERATURE:
            self.__sit__()


    def __sit__(self):
        self.curent_posture = SIT


    def middle(self):
        self.stand_temperature = 0
        self.sit_temperature = 0