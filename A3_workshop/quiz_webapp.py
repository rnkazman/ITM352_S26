from flask import Flask, redirect, render_template, request, url_for

score = 0  # Initialize score variable
question_number = 0  # Initialize question number variable
#    questions = load_questions('quiz_questions.json')
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris", "Pittsburgh"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Saturn", "Mars", "Fig Newton"]
    }
]
max_questions = len(questions)  # Get the total number of questions
app = Flask(__name__)


@app.route("/")
def home():
    global score
    score = 0  # Reset score when returning to home page
    question_number = 0  # Reset question number when returning to home page
    return render_template("index.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score  # Use the global variables
    global question_number 
    global max_questions
    global questions
    
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        answer = request.form.get('answer') 
        
        if answer == questions[question_number]['options'][3]:  # Check if the answer is correct
            score += 1
        question_number += 1

        if question_number < max_questions:
            # Not done. Display the next question and options.
            return render_template('quiz.html', 
                                   question=questions[question_number]['question'], 
                                   question_number=question_number,
                                   options=questions[question_number]['options']  ) 
        else:            
            return render_template('result.html', 
                                   score=score, 
                                   max_questions=max_questions)  # Display the result page with the score
    else:
        # Load the question and options to display
        question_number = 0    # Reset question number for each quiz attempt
        # Display the question and options
        return render_template('quiz.html', 
                               question=questions[question_number]['question'], 
                               question_number=question_number,
                               options=questions[question_number]['options']  )  

@app.route('/result')
def result():
    # Display the user's score
    global score
    return render_template('result.html', score=score)

def main():
   app.run(debug=True)

if __name__ == "__main__":
   main()
