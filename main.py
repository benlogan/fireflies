strip1on = False 
strip2on = False

random1 = 0
score = 0
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip2 = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)
basic.show_number(score)

def on_forever():
    global random1
    random1 = randint(0, 3000)
    basic.pause(random1)
    strip2.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    global strip2on
    strip2on = True
    print("STRIP 2 TRUE")
    basic.pause(750)
    strip2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    global strip2on
    strip2on = False
basic.forever(on_forever)

def on_forever2():
    print("CHECKING FOR MATCH strip1on : " + strip1on + " strip2on : " + strip2on)
    if strip1on and strip2on:
        global score
        score = score + 1
        basic.show_number(score)
        print("MATCH new score : " + str(score))
    else:
        pass
basic.forever(on_forever2)

def on_every_interval():
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    global strip1on
    strip1on = True
    print("STRIP 1 TRUE")
    basic.pause(750)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    global strip1on
    strip1on = False
loops.every_interval(5000, on_every_interval)
