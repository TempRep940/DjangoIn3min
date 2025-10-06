This is a Django-based interactive quiz web application. The application displays a series of questions, each with multiple-choice options, and a countdown timer for every question. Each question is shown for three seconds, and the timer changes color to indicate the remaining time (black for 3, dark red for 2, bright red for 1 ).

Users can click on one of the four options:

If the selected option is correct, the question is removed from the rotation.

If the option is incorrect, the question remains and a new question is displayed.

Once all questions are answered correctly, an “Again” button appears, allowing users to restart the quiz with all questions. The application uses JavaScript on the frontend to handle question rotation, countdown, user interaction, and dynamic updates without page reloads. The backend is built with Django, passing the question data as JSON to the template for rendering.

The entire project was generated using AI-Prompt Engineer-Tester workflow.
