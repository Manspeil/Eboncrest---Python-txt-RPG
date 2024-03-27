import time

def typewriter_effect(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("")
