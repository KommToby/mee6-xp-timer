import time
import ctypes
import winsound
import tkinter as tk

# Main stopwatch loop
def stopwatch():
    start_time = time.time()
    alert_time = int(entry.get())
    while True:
        time.sleep(0.01)
        elapsed_time = time.time() - start_time
        label["text"] = "Elapsed time: %.2f seconds" % elapsed_time
        root.update()
        if ctypes.windll.user32.GetAsyncKeyState(0x0D) != 0: # 0x0D is the virtual key code for the Enter key
            label["text"] = "Stopwatch reset."
            start_time = time.time()
        if int(elapsed_time) % alert_time == 0:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) # Plays a Windows alert sound

def start_stopwatch():
    stopwatch()

def exit_program():
    root.destroy()

root = tk.Tk() # Creates the main window
root.geometry("250x140") # Sets the size of the main window
root.title("Mee6 XP Timer") # Sets the title of the main window
entry_label = tk.Label(root, text="Seconds:", font=("TkDefaultFont", 10), anchor="center") # Creates a label for the entry widget
entry_label.pack(pady=10) # Packs the label
entry = tk.Entry(root) # Creates an entry widget
entry.pack(pady=10) # Packs the entry widget
start_button = tk.Button(root, text="Start", command=start_stopwatch) # Creates a button that starts the stopwatch
exit_button = tk.Button(root, text="Exit", command=exit_program) # Creates a button that exits the program
start_button.pack(side="left", padx=10, pady=10) # Packs the buttons
exit_button.pack(side="right", padx=10, pady=10)
label = tk.Label(root, text="") # Creates a label for the stopwatch
label.pack(pady=20)

root.mainloop() # Starts the main loop

# notice there is no if __name__ == "__main__": here, because we don't want to run the stopwatch when we import the module