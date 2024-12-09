from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Coordenadas do clique: ({x}, {y})')
        return False  # Para parar o listener após o primeiro clique

with mouse.Listener(on_click=on_click) as listener:
    listener.join()