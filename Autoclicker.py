import tkinter as tk
import time
import pyautogui
import threading
go = False
clicking_thread = None

def STPressed():
    global go, clicking_thread
    go = True
    if clicking_thread is None or not clicking_thread.is_alive():
        clicking_thread = threading.Thread(target=click_loop, daemon=True)
        clicking_thread.start()

def click_loop():
    global go
    while go == True:
        pyautogui.click()
        time.sleep(60)

def STOP():
    global go
    go = False

window = tk.Tk()
window.title("Centered's Crappy Autoclicker")
window.geometry("600x400")
label = tk.Label(window, text="Hello, this is an autoclicker specified for MC!")
start = tk.Button(window, text="Start", command = STPressed)
stop = tk.Button(window, text = "Stop", command = STOP)
label.pack()
start.pack(side=tk.LEFT, padx = 125, pady = 5)
stop.pack(side=tk.LEFT, padx = 100, pady = 5)

window.mainloop()
