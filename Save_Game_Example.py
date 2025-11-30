def save_score(score, filename="highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(score))
    print(f"High score saved to {filename}")

def load_score(filename="highscore.txt"):
    try:
        with open(filename, "r") as f:
            score = int(f.read())
        return score
    except FileNotFoundError:
        print(f"No high score file found at {filename}")
        return 0

# Example usage
currentScore = 502

loadedScore = load_score()

if currentScore > loadedScore:
    save_score(currentScore)
print(f"Current high score: {load_score()}")