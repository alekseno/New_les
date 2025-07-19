class HolidayTown:
    def celebrate(self):
        print("Этот праздник пока не определён...")

class HalloweenTown(HolidayTown):
    def celebrate(self):
        print("Монстры вышли на улицы! Ужас и веселье!")

class ChristmasTown(HolidayTown):
    def celebrate(self):
        print("Санта дарит подарки, всё сияет гирляндами!")
        
towns = [HalloweenTown(), ChristmasTown()]

for town in towns:
    town.celebrate()