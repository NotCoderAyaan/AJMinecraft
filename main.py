from ursina import *
from psdtools3 import



app = Ursina()


box = Entity(mode='cube', texture='white_cube', color=color.blue, position=(2,2) , scale = (1,1))


app.run()