import random

def load_songs_from_file(filename):
    songs = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    songs.append({"hint": parts[0], "answer": parts[1]})
    except FileNotFoundError:
        print(f"❌ Error: Could not find file '{filename}'")
    return songs

def choose_language():
    print("🌍 Select language:")
    print("1 - English")
    print("2 - 中文")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            return "en"
        elif choice == '2':
            return "cn"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def choose_difficulty():
    print("🎼 Select difficulty level:")
    print("1 - Easy")
    print("2 - Hard")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            return "easy"
        elif choice == '2':
            return "hard"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_filename(language, difficulty):
    return f"songs_{difficulty}_{language}.txt"

def is_guess_correct(guess, correct_answer):
    # no input or all spaces are wrong
    if not guess:
        return False
    # ignore case + fuzzy matching
    return guess == correct_answer or correct_answer in guess or guess in correct_answer

def play_game(song_list, num_questions=5):
    if len(song_list) < num_questions:
        print("⚠️ Not enough songs in the database!")
        return

    selected_songs = random.sample(song_list, num_questions)
    score = 0

    for i, song in enumerate(selected_songs):
        print(f"\n🎵 Question {i + 1}:")
        print("Hint:", song["hint"])
        correct_answer = song["answer"].strip().lower()

        # First try
        guess = input("Your guess: ").strip().lower()
        if is_guess_correct(guess, correct_answer):
            print("✅ Correct!")
            score += 1
            continue

        # Second hint
        words = correct_answer.split()
        print("❗Not quite. Here's another hint:")
        print(f"   ➤ Answer has {len(words)} word(s), starts with: '{correct_answer[0].upper()}'")
        second_guess = input("Try again: ").strip().lower()
        if is_guess_correct(second_guess, correct_answer):
            print("✅ Correct (second attempt)!")
            score += 1
        else:
            print(f"❌ Still wrong. The correct answer was: {song['answer']}")

    print(f"\n🎉 Game Over! You scored {score}/{num_questions} points.")

    if score == num_questions:
        print("🏆 Perfect! You're a music master!")
    elif score >= num_questions // 2:
        print("👍 Good job! Keep practicing!")
    else:
        print("🎧 Don't worry, try again!")

def main():
    while True:
        lang = choose_language()
        diff = choose_difficulty()
        filename = get_filename(lang, diff)
        songs = load_songs_from_file(filename)
        play_game(songs, num_questions=5)
        again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! 🎶 Goodbye.")
            break

if __name__ == "__main__":
    main()
