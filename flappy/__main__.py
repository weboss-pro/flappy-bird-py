import pyglet
from pyglet.window import key

# Create the window
window = pyglet.window.Window(300,500)

# Get the sprites set up
bird_image = pyglet.resource.image('assets/sprites/sheet.png')
bird_sprite = pyglet.sprite.Sprite(bird_image)
bird_sprite.x = 10

# Handle the keypress
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        print 'The SPACE key was pressed.'

@window.event
def on_draw():
    window.clear()
    #bird_image.blit(30,20)
    bird_sprite.draw()

pyglet.app.run()
