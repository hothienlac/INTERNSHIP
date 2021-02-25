


class Counter:

    STAND_TEMPERATURE_THRESHOLD = 2
    SIT_TEMPERATURE_THRESHOLD = 2


    def __init__(self):
        self.init = True
        self.flag = True
        self.count = 0
        self.stand_temperature = 0
        self.sit_temperature = 0


    def update(self, posture, velocity):
        dictionary = [
            self.sit,
            self.middle,
            self.stand,
        ]
        dictionary[posture](velocity)


    def stand(self, velocity):
        self.sit_temperature = 0
        self.stand_temperature += 1
        if self.stand_temperature > self.STAND_TEMPERATURE_THRESHOLD:
            if self.init:
                self.__stand__()
                return
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
        if self.sit_temperature > self.SIT_TEMPERATURE_THRESHOLD:
            if self.init:
                self.__sit__()
                return
            if velocity > 0:
                self.__sit__()
                return


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

