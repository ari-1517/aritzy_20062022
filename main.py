basic.show_string("aritzy")
basic.show_number(0)
basic.show_icon(IconNames.NO)
basic.show_number(3 + 18)
basic.show_icon(IconNames.TSHIRT)
basic.show_number(100 - 200)
basic.show_icon(IconNames.STICK_FIGURE)
basic.show_number(500 * 25)
basic.show_icon(IconNames.EIGTH_NOTE)
basic.show_number(Math.sqrt(37))
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
