from django.shortcuts import render

def quiz_loop(request):
    # Sample questions array (you can replace with any questions)
    questions = [
        {"id": 1, "text": "What's 2 + 2?", "options": ["3", "4", "5", "22"], "correct": 1},
        {"id": 2, "text": "What color is the sky on a clear day?", "options": ["Blue", "Green", "Red", "Yellow"], "correct": 0},
        {"id": 3, "text": "Capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "correct": 2},
    ]
    # Pass the questions to the template; the template will read them using a JSON script
    return render(request, 'quiz/quiz.html', {'questions': questions})
