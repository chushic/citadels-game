import pygame as pg
import os


from components import Game, Player, Assassin

g = Game()
p = g.get_player(0)
p.role = Assassin()
p.role.use_bility()

print("done")



        


    