import time
import ctypes
import winsound
import tkinter as tk

def stopwatch():
    start_time = time.time()
    while True:
        time.sleep(0.01)
        elapsed_time = time.time() - start_time
        label["text"] = "Elapsed time: %.2f seconds" % elapsed_time
        root.update()
        if ctypes.windll.user32.GetAsyncKeyState(0x0D) != 0: # 0x0D is the virtual key code for the Enter key
            label["text"] = "Stopwatch reset."
            start_time = time.time()
        if int(elapsed_time) % 60 == 0:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Stopwatch")
label = tk.Label(root, text="")
label.pack(pady=20)
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=20)

if __name__ == "__main__":
    stopwatch()
    root.mainloop()

root.withdraw()