import pyglet

# Get the sprites set up
bird_image = pyglet.resource.image('assets/sprites/sheet.png')
bird_sprite = pyglet.sprite.Sprite(bird_image)
bird_sprite.x = 10

title_image = pyglet.resource.image('assets/sprites/title.png')
title_sprite = pyglet.sprite.Sprite(title_image)
title_sprite.set_position(0, 0)

instructions_image = pyglet.resource.image('assets/sprites/instructions.png')
instructions_sprite = pyglet.sprite.Sprite(instructions_image)
instructions_sprite.set_position(0, 0)

downflap_image = pyglet.resource.image('assets/sprites/downflap.png')
upflap_image = pyglet.resource.image('assets/sprites/upflap.png')
middleflap_image = pyglet.resource.image('assets/sprites/middleflap.png')

bird_images = [
    downflap_image,
    middleflap_image,
    upflap_image
]

bird_animation = pyglet.image.Animation.from_image_sequence(bird_images, .500, loop=True)
bird_sprite = pyglet.sprite.Sprite(bird_animation)
bird_sprite.set_position(50, 50)
