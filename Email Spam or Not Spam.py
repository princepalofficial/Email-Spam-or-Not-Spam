import numpy as np
import pandas as pd
# 1. Create Email Dataset
data = {
    "Email":[
        "Congratulations! You won a free prize",
        "Win cash now, click this link",
        "You have won a lottery",
        "Claim Your free gift now",
        "Urgent! Get free money",
        "Free offer, click now",
        "You won a cash prize",
        "Limited time lottery offer",
        "Please attend the meeting tomorrow",
        "Your project report is ready",
        "Can you send me the assignment?",
        "Meeting is scheduled at 10 AM",
        "Please call me when you are free",
        "Your class starts at 9 AM",
        "Let's discuss the project",
        "please send the document"
    ]
}
df = pd.DataFrame(data)

# 2. Spam Keywords
spam_words = np.array([
    "free",
    "win",
    "won",
    "prize",
    "money",
    "lottery",
    "click",
    "urgent",
    "gift",
    "cash"
])

# 3. Spam Detection Function
def predict_spam(email):
    email = email.lower()
    count = np.sum([
        word in email
        for word in spam_words
    ])
    if count >= 2:
        return "Spam"
    else:
        return "Not Spam"

# 4. Prediction
df["Prediction"] = df["Email"].apply(predict_spam)

# 5. Display Result
print("***** Email Spam Detection *****")
print(f"{'Email':<45}{'Prediction':<12}")
print("-" * 60)
for _, row in df.iterrows():
    print(f"{row['Email']:<45}{row['Prediction']:<12}")

# 6. Count Spam / Not Spam
print("\n***** Email Count ******")
print(df["Prediction"].value_counts())

# 7. New Email
new_email = pd.DataFrame({"Email": ["Congratulations! You won Free money",
                                    "Please send me the Project report"]})
new_email["Prediction"] = new_email["Email"].apply(predict_spam)

print("\n***** New Email ******")
print(new_email)
