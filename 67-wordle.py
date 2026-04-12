from collections import Counter

GREEN = "G"
YELLOW = "Y"
GRAY = "X"


def evaluate(guess, answer):
    """Return Wordle pattern for guess vs answer."""
    result = [""] * 5
    answer_count = Counter(answer)

    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = GREEN
            answer_count[guess[i]] -= 1

    for i in range(5):
        if result[i] == "":
            if answer_count[guess[i]] > 0:
                result[i] = YELLOW
                answer_count[guess[i]] -= 1
            else:
                result[i] = GRAY

    return "".join(result)


def convert_pattern(p):
    """Convert user symbols to internal format."""
    return (
        p.replace("✅", "G")
         .replace("🟨", "Y")
         .replace("☑️", "X")
         .replace(" ", "")
    )


def find_word_for_pattern(pattern, answer, word_list):
    """Find any word matching the pattern."""
    for word in word_list:
        if evaluate(word, answer) == pattern:
            return word
    return None


def solve_templates(patterns, answer, word_list):
    results = []

    for p in patterns:
        target = convert_pattern(p)
        match = find_word_for_pattern(target, answer, word_list)

        if match:
            results.append(match)
        else:
            results.append(p)

    return results


# config

answer = "elfin"

patterns = [
    "☑️🟨🟨☑️☑️",
    "🟨☑️☑️✅✅",
    "🟨🟨☑️☑️✅",
    "🟨☑️🟨☑️✅",
    "☑️🟨☑️☑️✅",
]

# Load word list
with open("words.txt") as f:
    word_list = [w.strip().lower() for w in f if len(w.strip()) == 5]

output = solve_templates(patterns, answer, word_list)

for o in output:
    print(o)