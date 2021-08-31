import keyboard
import time

start_time = time.time()
seconds = 3600
while True:
    keyboard.write("love you.")
    keyboard.press('Enter')
    current_time = time. time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        break