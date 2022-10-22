"""
 facing forward
 o
/|\
/ \

left hand to head
 o)
/|
/ \

left hand to hip
 o
/|>
/ \

left hand to start
 o
/|\
/ \

right leg in
 o
/|\
< \

right leg out"
 o
/|\
/ \

1
19
say Hokey Pokey
say You put your right foot in
right leg in
say You put your right foot out
right leg out
say You put your right foot in
right leg in
say Shake it all about
left hand to head
right hand to hip
left hand to hip
right hand to head
say You do the hokey pokey and you turn yourself around
turn
turn
say That's what it's all about!
right leg out
right hand to start
left hand to start
"""
import fileinput
import sys
from enum import Enum, auto


class Leg(Enum):
    IN = auto()
    OUT = auto()

class Hand(Enum):
    HIP = auto()
    HEAD = auto()
    START = auto()



class StickMan:
    def __init__(self):
        self.facing_forward = True
        self.right_leg = Leg.OUT
        self.left_leg = Leg.OUT
        self.right_hand = Hand.START
        self.left_hand = Hand.START

    def say_something(self, str):
        print(str)

    def draw(self):
        # Hackathon-level spagetti
        head = ""
        body = ""
        legs = ""
        if not self.facing_forward:
            head += "(" if self.left_hand == Hand.HEAD else " "
            head += "o"
            head += ")" if self.right_hand == Hand.HEAD else " "

            if self.left_hand == Hand.START:
                body += "/"
            elif self.left_hand == Hand.HIP:
                body += "<"
            else:
                body += " "
            body += "|"
            if self.right_hand == Hand.START:
                body += "\\"
            elif self.right_hand == Hand.HIP:
                body += ">"
            else:
                body += " "

            legs += "/" if self.left_leg == Leg.OUT else "<"
            legs += " "
            legs += "\\" if self.right_leg == Hand.START else ">"
        else:
            head += "(" if self.right_hand == Hand.HEAD else " "
            head += "o"
            head += ")" if self.left_hand == Hand.HEAD else " "

            if self.right_hand == Hand.START:
                body += "/"
            elif self.right_hand == Hand.HIP:
                body += "<"
            else:
                body += " "
            body += "|"
            if self.left_hand == Hand.START:
                body += "\\"
            elif self.left_hand == Hand.HIP:
                body += ">"
            else:
                body += " "

            legs += "/" if self.right_leg == Leg.OUT else "<"
            legs += " "
            legs += "\\" if self.left_leg == Leg.OUT else ">"
        print(head)
        print(body)
        print(legs)

    def turn(self):
        self.facing_forward = not self.facing_forward
        self.draw()

test_cases = int(input().rstrip())

for test_case in range(test_cases):
    stick_man = StickMan()
    number_of_commands = int(input().rstrip())
    for _command in range(number_of_commands):
        command = input().rstrip()
        if command.startswith("say "):
            stick_man.say_something(command[4:])
        elif command == "left hand to head":
            stick_man.left_hand = Hand.HEAD
            stick_man.draw()
        elif command == "left hand to hip":
            stick_man.left_hand = Hand.HIP
            stick_man.draw()
        elif command == "left hand to start":
            stick_man.left_hand = Hand.START
            stick_man.draw()
        elif command == "left leg in":
            stick_man.left_leg = Leg.IN
            stick_man.draw()
        elif command == "left leg out":
            stick_man.left_leg = Leg.OUT
            stick_man.draw()
        elif command == "right hand to head":
            stick_man.right_hand = Hand.HEAD
            stick_man.draw()
        elif command == "right hand to hip":
            stick_man.right_hand = Hand.HIP
            stick_man.draw()
        elif command == "right hand to start":
            stick_man.right_hand = Hand.START
            stick_man.draw()
        elif command == "right leg in":
            stick_man.right_leg = Leg.IN
            stick_man.draw()
        elif command == "right leg out":
            stick_man.right_leg = Leg.OUT
            stick_man.draw()
        elif command == "turn":
            stick_man.turn()
        else:
            print(f"Unrecognized command: {command}")




