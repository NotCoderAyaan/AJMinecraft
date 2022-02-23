from ursina import *    # pip install ursina
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

ground = load_texture('11635-v7.jpg')
randombL = load_texture('54.png')
nether = load_texture('96.png')
gold = load_texture('1234.jpg')
wood = load_texture('3456.jpg')
plank = load_texture('7890.png')

skyland = load_texture('download.jpg')

cureentTx = ground

def update():
    global cureentTx
    if held_keys['1']: cureentTx = ground
    if held_keys['2']: cureentTx = wood
    if held_keys['3']: cureentTx = plank
    if held_keys['4']: cureentTx = gold
    if held_keys['5']: cureentTx = nether
    if held_keys['6']: cureentTx = randombL




class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model= 'sphere',
            scale= 150,
            texture = skyland,
            double_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.2,0.3),
            color=color.white,
            rotation=Vec3(150, -10, 0 ),
            position=Vec2(0.4, -0.4)
        )


class Volex(Button):
    def __init__(self, position = (0,0,0) , texture = ground):
        super().__init__(
            parent = scene,
            model='cube',
            color=color.white,
            highlight_color = color.lime,
            texture=texture,
            position=position,
            original_y=0.5
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                volex = Volex(position=self.position + mouse.normal, texture=cureentTx )
            if key == 'right mouse down':
                destroy(self)



for z in range(15):
    for x in range(15):
        volex = Volex((x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()
