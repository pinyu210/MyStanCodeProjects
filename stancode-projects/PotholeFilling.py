"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is at the(2,1)
    post-condition:Karel is at the (2,7)
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East
    post-condition:Karel is in the pot hole,facing South
    """
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()

def go_out():
    """
    pre-condition: Karel is in the pothole,facing South
    post-condition:Karel is at the upper left of the pothole,facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
