def riddle_solver():
    riddles = [
        {
            "question": "What has keys but can't open locks?",
            "answer": "keyboard"
        },
        {
            "question": "What can travel around the world while staying in the same corner?",
            "answer": "stamp"
        },
        {
            "question": "What has hands but can't clap?",
            "answer": "clock"
        }
    ]

    print("Welcome to the Riddle Solver!")
    score = 0

    for riddle in riddles:
        print("\nRiddle:")
        print(riddle["question"])
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == riddle["answer"]:
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Oops! The correct answer was: {riddle['answer']}")

    print(f"\nGame Over! You solved {score} out of {len(riddles)} riddles.")

# Run the game
riddle_solver()