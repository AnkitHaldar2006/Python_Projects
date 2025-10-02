questions = {
    "What is the capital of France?": "Paris",
    "Who wrote '1984'?": "George Orwell",
    "What is 9 * 6?": "54"
}

score = 0
for q, a in questions.items():
    user_ans = input(q + " ")
    if user_ans.strip().lower() == a.lower():
        score += 1

print(f"Your score: {score}/{len(questions)}")