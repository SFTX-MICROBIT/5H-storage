input.onGesture(Gesture.TiltLeft, function () {
    蛇.change(LedSpriteProperty.X, -1)
})
input.onGesture(Gesture.LogoDown, function () {
    蛇.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.A, function () {
    蛇.change(LedSpriteProperty.Y, 2)
})
input.onGesture(Gesture.LogoUp, function () {
    蛇.change(LedSpriteProperty.Y, 1)
})
input.onButtonPressed(Button.B, function () {
    蛇.change(LedSpriteProperty.Y, -2)
})
input.onGesture(Gesture.TiltRight, function () {
    蛇.change(LedSpriteProperty.X, 1)
})
let 蛇: game.LedSprite = null
game.setScore(0)
蛇 = game.createSprite(2, 2)
let 苹果 = game.createSprite(randint(0, 4), randint(0, 4))
basic.forever(function () {
    if (蛇.isTouching(苹果)) {
        game.addScore(1)
        苹果.delete()
        basic.pause(100)
        苹果 = game.createSprite(randint(0, 4), randint(0, 4))
    }
    if (game.score() == 15) {
        if (true) {
            苹果.delete()
            蛇.delete()
            basic.showString("YOU WIN!")
            basic.showString("SCORE:15/15")
            basic.showString("CONGRATULATIONS!")
            while (true) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # . # . #
                    # . . . #
                    . . . . .
                    `)
                basic.pause(1000)
                basic.showIcon(IconNames.TShirt)
                basic.pause(1000)
                basic.showLeds(`
                    . # # # .
                    . # # # .
                    . # . # .
                    . # . # .
                    . # . # .
                    `)
                basic.pause(1000)
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . # . # .
                    . # . # .
                    # # . # #
                    `)
                basic.pause(1000)
            }
        }
    }
})
