import random


class Enemy:

    def __init__(self, name="Enemy", hit_point=0, lives=1):
        self._name = name
        self._hit_point = hit_point
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_point = self._hit_point - damage
        if remaining_point >= 0:
            self._hit_point = remaining_point
            print(f"I took {damage} point(s), {self._hit_point} remaining.")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life. {self._lives} remaining.")
            else:
                self._alive = False
                print(f"{self._name} died.")

    def __str__(self):
        return (f"Name: {self._name}, Hit point: {self._hit_point}, Lives: "
                f"{self._lives}")


class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name, hit_point=23, lives=1)

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomps!")


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name, lives=3, hit_point=12)

    def dodge(self):
        dodged = random.randint(1, 3)
        if dodged == 3:
            print(f"===== {self._name} dodged ======")
            return True
        else:
            return False

    # take_damage method overriding
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage)
            

# vampire king class 
class VampireKing(Vampire):
    def __init__(self, name):
        super().__init__(name)
        self._hit_point = 140
    
    def take_damage(self, damage):
        super().take_damage(damage // 4)
           
    
