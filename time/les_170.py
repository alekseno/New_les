
class Christmas:
    def __init__(self, character):
        self.character = character

    def start(self):
        result = self.character.deliver_gift()

        if (not "червяк" in result and not "паук" in result) and "подарок" in result:
            print("Рождество удалось!")
        else:
            print("Рождество испорчено...")

class AnyCharacter():
    def deliver_gift(self):
        return  input().lower()

AnyCharac = Christmas(AnyCharacter())
AnyCharac.start()