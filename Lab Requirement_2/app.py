from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the Welcome Page (Page 1)
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for the Quiz Page (Page 2)
@app.route('/quiz')
def quiz():
    return render_template('Quiz.html')  # Ensure this matches your template name

# Route for handling Quiz Submission and Score Calculation (Page 3)
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    # Correct answers for the quiz
    correct_answers = {
        'q1': 'Jane Austen',
        'q2': 'True',
        'q3': 'To Kill a Mockingbird',
        'q4': 'False',
        'q5': 'Herman Melville',
        'q6': 'True',
        'q7': 'The Hobbit',
        'q8': 'Harper Lee',
        'q9': 'False',
        'q10': 'The Great Gatsby'
    }
    
    # Calculate score
    score = 0
    for key in correct_answers:
        if request.form.get(key) == correct_answers[key]:
            score += 1
    
    return render_template('score_page.html', score=score)

# Main function to run the app
if __name__ == "__main__":
    app.run(debug=True)
