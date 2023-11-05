import microbit

row_pins = [microbit.pin3, microbit.pin10, microbit.pin9, microbit.pin6]
col_pins = [microbit.pin4, microbit.pin2, microbit.pin7]

def keypadListen():
    key_code = -1
    for row, row_pin in enumerate(row_pins):
        row_pin.write_digital(1)
        for col, col_pin in enumerate(col_pins):
            if col_pin.read_digital():
                key_code = row*len(col_pins)+(col+1)
                break
        row_pin.write_digital(0)
    return key_code
