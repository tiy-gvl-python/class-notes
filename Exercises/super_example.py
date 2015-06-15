class Person: # Super Class

    walking = False

    def talk(self):
        return "talking"

    def move(self):
        self.walking = True
        print("base walking called")
        return "walking"


class SlowPerson(Person): # Sub Class

    walking = True

    def blink(self):
        return

    def move(self):
        super().move()
        self.walking = True
        return "slowly walking"


joel = Person()
sarah = SlowPerson()

print(joel.move())
print('---- beautiful silence =====')
print(sarah.walking)
print(sarah.move())
print(sarah.walking)