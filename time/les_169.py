class ChristmasCharacter: # рождественский персонаж
    def deliver_gift(self): # доставка подарков
        return "🎁 подарок с любовью"
    
class FakeSanta(ChristmasCharacter): # подмена персонажа
    def deliver_gift(self): # доставка подарков
        return "😱 коробка с пауками"
    
class Christmas:
    def __init__(self, character):
        self.character = character

    def start(self):
        result = self.character.deliver_gift()
        if "подарок" in result and "любовью" in result:
            print("Рождество удалось!")
        else:
            print("Рождество испорчено...")
    

santa = Christmas(ChristmasCharacter())
jack = Christmas(FakeSanta())

santa.start()  # ✅ Рождество удалось!
jack.start()   # ❌ Рождество испорчено...