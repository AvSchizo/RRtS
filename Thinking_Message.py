import time
import sys

message = ". . ."

def spellMessage(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)
    return ""

print("thinking")
time.sleep(0.5)
print(f"{spellMessage(message)}", end="")
print("\r              ", end="\r")
time.sleep(0.5)
print(f"{spellMessage(message)}", end="")