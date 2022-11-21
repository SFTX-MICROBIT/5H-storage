def on_gesture_tilt_left():
    蛇.change(LedSpriteProperty.X, -1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_received_number(receivedNumber):
    while True:
        for index in range(4):
            music.play_melody("F A G F B A G A ", 500)
        for index2 in range(4):
            music.play_melody("G B A G C5 B A B ", 500)
radio.on_received_number(on_received_number)

def on_gesture_logo_down():
    蛇.change(LedSpriteProperty.Y, -1)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    蛇.change(LedSpriteProperty.Y, 2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    蛇.change(LedSpriteProperty.Y, 1)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_received_string(receivedString):
    while True:
        for index3 in range(4):
            music.play_melody("C E D C F E D E ", 500)
        for index4 in range(4):
            music.play_melody("D F E D G F E F ", 500)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    蛇.change(LedSpriteProperty.Y, -2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    蛇.change(LedSpriteProperty.X, 1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

蛇: game.LedSprite = None
radio.send_number(0)
radio.send_string("hello!")
game.set_score(0)
蛇 = game.create_sprite(2, 2)
苹果 = game.create_sprite(randint(0, 4), randint(0, 4))

def on_forever():
    global 苹果
    if 蛇.is_touching(苹果):
        game.add_score(1)
        苹果.delete()
        basic.pause(100)
        苹果 = game.create_sprite(randint(0, 4), randint(0, 4))
    if game.score() == 15:
        basic.clear_screen()
        basic.show_string("You win！")
        basic.show_string("score：15/15")
        basic.show_string("Congratulations！")
        if True:
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # . # . #
                                # . . . #
                                . . . . .
            """)
            basic.pause(2000)
            basic.show_icon(IconNames.TSHIRT)
            basic.pause(2000)
            basic.show_leds("""
                . # # # .
                                . # # # .
                                . # . # .
                                . # . # .
                                . # . # .
            """)
            basic.pause(2000)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # . # .
                                . # . # .
                                # # . # #
            """)
            basic.pause(2000)
basic.forever(on_forever)
