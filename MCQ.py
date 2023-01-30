questions = [
    { 
        "question": "What is the Capital of India?",
        "options" : [
            "Mumbai",
            "Chennai",
            "Pune",
            "New Delhi"
        ],
        "correct_ans":"New Delhi"
    },
    { 
        "question": "Who was India's first Prime Minister?",
        "options":[
            "Jawaharlal Nehru",
            "Indira Gandhi",
            "Mahatman Gandhi",
            "Vallabhbhai Patel"
        ],
        "correct_ans":"Jawaharlal Nehru"
    },
    {
        "question": "What is Python?", 
        "options": [
            "A programming language", 
            "A type of snake", 
            "A delicious dessert", 
            "A social media platform"
        ], 
        "correct_ans": "A programming language"
    },
    {
        "question": "The value of tan 45?", 
        "options": [
            "0", 
            "1", 
            "0.33", 
            "Infinity"
        ], 
        "correct_ans": "1"
    }, 
    {
        "question": "The valve of sin 45?", 
        "options": [
            "0", 
            "1", 
            "0.8509", 
            "0.5"
        ], 
        "correct_ans": "0.8509"
    }
]

score = 0
for i, question in enumerate(questions):
    print(f"Question {i + 1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"Option {j + 1}: {option}")
    user_answer = input("Enter your answer: ").lower()
    if user_answer == question["correct_ans"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
    print("\n")
print(f"Your score: {score}/{len(questions)}")



