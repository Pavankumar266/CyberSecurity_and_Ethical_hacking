print("========================================")
print("       PHISHING EMAIL SIMULATOR")
print("========================================")

score = 0
total = 5

questions = [
    {
        "email": """
From: bank-security@example.com
Subject: Urgent Account Alert

Your account needs verification immediately.
Please check your account using the link provided.
""",
        "answer": "p",
        "reason": "The message creates urgency and asks you to use a link to verify your account."
    },

    {
        "email": """
From: college-office@college.edu
Subject: Class Schedule

Your class schedule for next week is attached.
Please check the official college portal for details.
""",
        "answer": "s",
        "reason": "This example does not contain the typical urgent request or suspicious link."
    },

    {
        "email": """
From: prize-winner@example.com
Subject: Congratulations! You Won!

You have won a large prize.
Send your personal information to claim your prize.
""",
        "answer": "p",
        "reason": "Unexpected prizes and requests for personal information are common phishing warning signs."
    },

    {
        "email": """
From: library@college.edu
Subject: Library Reminder

Your borrowed books are due next week.
Please visit the official college library website if you need more information.
""",
        "answer": "s",
        "reason": "The message directs the user to the official website rather than requesting sensitive information."
    },

    {
        "email": """
From: security-alert@example.com
Subject: Your Password Will Expire Today!

Your password will expire immediately.
Enter your password and personal details to continue.
""",
        "answer": "p",
        "reason": "Urgency and requests for passwords or personal information are major phishing warning signs."
    }
]

for i, question in enumerate(questions, 1):

    print("\n----------------------------------------")
    print("Email", i)
    print("----------------------------------------")
    print(question["email"])

    print("Is this email:")
    print("S - Safe")
    print("P - Phishing")

    choice = input("Enter S or P: ").lower()

    if choice == question["answer"]:
        print("Correct! ✓")
        score += 1
    else:
        print("Incorrect.")
    
    print("Why?")
    print(question["reason"])


print("\n========================================")
print("             FINAL RESULT")
print("========================================")

print("Your score:", score, "/", total)

if score == total:
    print("Excellent! You identified all the examples correctly.")

elif score >= 3:
    print("Good awareness! Review the warning signs you missed.")

else:
    print("Keep learning! Review common phishing warning signs.")

print("\nImportant phishing warning signs:")
print("1. Unexpected requests for passwords or personal information")
print("2. Urgent or threatening messages")
print("3. Suspicious sender addresses")
print("4. Unexpected prizes or offers")
print("5. Links asking you to log in")
