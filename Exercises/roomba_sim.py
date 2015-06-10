
import random

class Room:
    """
    Responsibilities:
    - width
    - height
    - keeps track of what squares are clean
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cleaned_squares = []
        self.moves = []

    @property
    def report(self):
        return (len(self.moves), self.percent_cleaned)

    def clean_square(self, x, y):
        if (x, y) not in self.cleaned_squares:
            self.cleaned_squares.append((x, y))
        self.moves.append((x, y))

    def is_valid_move(self, x, y):
        is_right_of_x = x > self.width
        is_left_of_x = x <= 0
        is_up_of_y = y <= 0
        is_down_of_y = y > self.height
        return not any([is_right_of_x, is_left_of_x, is_up_of_y, is_down_of_y])

    @property
    def percent_cleaned(self):
        return len(self.cleaned_squares) / (self.width * self.height)



class Roomba:
    """
    Responsibilities:

    - location
    - know its current direction
    - respond to hitting a wall
    - give its relative x and y movement  ehhhhhh
    - speed of 1
    """

    def __init__(self, room):
        self.room = room
        self.spawn_in_room()

    def get_loc(self):
        return self.x, self.y

    def spawn_in_room(self):
        self.x = random.randint(1, self.room.width)
        self.y = random.randint(1, self.room.height)

    def clean_square(self):
        self.room.clean_square(self.x, self.y)

    def move(self):
        temp_x = self.x
        temp_y = self.y
        choices = [
            (temp_x, temp_y - 1),
            (temp_x + 1, temp_y),
            (temp_x, temp_y + 1),
            (temp_x - 1, temp_y),
            (temp_x - 1, temp_y - 1),
            (temp_x + 1, temp_y - 1),
            (temp_x + 1, temp_y + 1),
            (temp_x - 1, temp_y + 1)
        ]
        random_choice = random.choice(choices)
        random_x, random_y = random_choice
        if self.room.is_valid_move(random_x, random_y):
            self.x = random_x
            self.y = random_y
        self.clean_square()


class Simulation:
    """
    Responsibilities:
    - placing the Roomba
    - asking Roomba where it's moving
    - updating the room
    - iterating over turns
    - reporting data (current turn, percent complete)

    Collaborators:
    - Room
    - Roomba
    """

    def __init__(self, roomba):
        self.roomba = roomba
        self.room = self.roomba.room

    def run_simulation(self):
        half_done = 0
        while self.room.report[1] < .5:
            self.roomba.move()

        half_done = self.room.report[0]
        ninety_done = 0

        while self.room.report[1] < .9:
            self.roomba.move()

        ninety_done = self.room.report[0]

        all_done = 0

        while self.room.report[1] < 1:
            self.roomba.move()

        all_done = self.room.report[0]
        return (half_done, ninety_done, all_done)
