"""
Python V2 _ Chap 4 _ Exercise 4.5
"""

import turtle

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Tekent een Archimedeïsche spiraal die begint in de oorsprong.

    Args:
      t: de turtle die de spiraal tekent
      n: aantal lijnsegmenten om te tekenen
      length: hoe lang elk segment is
      a: hoe los de initiële spiraal begint (groter is loser)
      b: hoe los de spiraal gewikkeld is (groter is loser)
    """
    theta = 0.0

    for i in range(n):
        t.forward(length)
        dtheta = 1 / (a + b * theta)

        t.left(dtheta)
        theta += dtheta

# Maak de wereld en de turtle aan
screen = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)  # Maximaliseer de snelheid van de turtle
draw_spiral(bob, n=1000)

# Sluit het venster pas als de gebruiker dit vraagt
screen.exitonclick()
