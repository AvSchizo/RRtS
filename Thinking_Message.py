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
print(f"{spellMessage(". . .")}", end="")
time.sleep(0.5)
print("\r              ", end="\r")
print(f"{spellMessage(". . .")}")