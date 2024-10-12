# Simple_Web_Prototyping


## Flask Basic Web Application
This is a simple web application built using HTML, CSS, and Flask. The goal of the application is to demonstrate how to create a basic form, handle user input on the backend using Flask, and display the results back to the user. Additionally, the app features a basic quiz form where users can answer multiple-choice questions and receive a score based on their answers.

##Features
User input form with fields for Name and Email.
A basic quiz form with multiple-choice questions.
Backend processing using Flask.
Displays submitted form data and quiz results on a result page.
Simple CSS styling for a clean interface.
### Quiz Form
The quiz form allows users to answer multiple-choice questions. The form sends the user's responses to the backend for processing, where their score is calculated based on the correct answers. The result page displays the user's score along with a message indicating their performance.

### Quiz Flow:
User Input: The user answers a set of predefined questions with multiple-choice options.
Form Submission: The quiz form is submitted via the POST method to the Flask backend.
Processing: The Flask app checks the user's answers against the correct answers and calculates the score.
Results: The score is displayed along with the correct answers to give feedback to the user.
Prerequisites
Python 3.x installed on your system.
Flask library installed.
### How to Run the Application
Clone or download this repository:


git clone https://github.com/yourusername/flask-web-app.git
Navigate to the project directory:


cd flask-web-app
Run the Flask application:


flask run
Open your browser and visit http://127.0.0.1:5000/ to access the application.

### How It Works
The homepage (/) contains a form where users can enter their Name and Email.
Upon submission, the form data is sent to the /submit route using the POST method.
The Flask backend processes the data and renders a new page (/result) showing the submitted information.
The quiz form, located on another page (/quiz), allows users to answer multiple-choice questions.
Upon submitting the quiz, the user is redirected to the results page (/quiz_result), where their score and feedback are displayed.
Customization
CSS: You can modify the style.css file in the static folder to change the design.
HTML Forms: To add more input fields, edit the index.html or quiz.html file in the templates folder.
Backend Logic: You can extend the Flask app by adding more routes or handling more complex logic in the app.py file.
