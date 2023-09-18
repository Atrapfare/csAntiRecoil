from pynput.mouse import Listener, Controller

mouse = Controller()


def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        while True:
            mouse.move(0, 5)
            if not mouse.get_pressed(mouse.Button.left):
                break


with Listener(on_click=on_click) as listener:
    listener.join()
