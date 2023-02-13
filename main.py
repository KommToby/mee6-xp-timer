# Import Libs
import time
import ctypes
import winsound

# Stopwatch
def stopwatch():
    start_time = time.time()
    while True:
        time.sleep(0.01)
        elapsed_time = time.time() - start_time
        print("\rElapsed time: %.2f seconds" % elapsed_time, end="")
        if ctypes.windll.user32.GetAsyncKeyState(0x0D) != 0: # 0x0D is the virtual key code for the Enter key
            print("\nStopwatch reset.")
            start_time = time.time()
        # Play sound after 60 seconds
        if int(elapsed_time) % 60 == 0:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

if __name__ == "__main__":
    stopwatch()
