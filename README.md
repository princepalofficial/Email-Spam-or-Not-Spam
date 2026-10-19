Email Spam or Not Spam 📧

About the Project

This is a simple Python project that checks whether an email is Spam or Not Spam.

The program looks for specific words in an email message and counts how many spam-related keywords are found. Based on the count, it gives a result.

I created this project to practice Python and understand the basics of text processing.

Tools Used

- Python
- Pandas
- NumPy

How It Works

1. The program takes email text as input.
2. It converts the text into lowercase.
3. It checks for predefined spam-related words.
4. It counts the matching words.
5. If two or more spam keywords are found, the email is marked as Spam.
6. Otherwise, it is marked as Not Spam.

Project Files

- "Email Spam or Not Spam.py" — Main Python code
- "README.md" — Project information

How to Run

First, clone the repository:

git clone https://github.com/princepalofficial/Email-Spam-or-Not-Spam.git

Open the project folder:

cd Email-Spam-or-Not-Spam

Install the required libraries:

pip install pandas numpy

Run the Python file:

python "Email Spam or Not Spam.py"

What I Learned

- Working with strings in Python
- Converting text to lowercase
- Searching for specific keywords
- Using conditions to classify text
- Understanding basic email filtering

Current Limitations

This project uses predefined keywords instead of a trained Machine Learning model. Therefore, it may sometimes classify an email incorrectly.

Future Improvements

- Use a real email dataset.
- Train a Machine Learning model.
- Improve text preprocessing.
- Evaluate the model using Precision, Recall and F1-score.
- Create a simple web application.

Author

Prince Pal

GitHub: https://github.com/princepalofficial
