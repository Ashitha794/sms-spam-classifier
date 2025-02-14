import pandas as pd

# Define exactly 100 ham messages
ham_messages = [
    "Hey, how are you?", "Are we still meeting today?", "Don't forget to bring the documents.",
    "Can you send me the report?", "Looking forward to your feedback.", 
    "Your appointment is scheduled for tomorrow.", "I hope you have a great day!",
    "Let me know if you need anything.", "I'm on my way!", "Thanks for your help.",
    "Let's catch up soon.", "Can we reschedule our meeting?", "How about dinner tomorrow?",
    "Your package has been shipped!", "Your subscription is confirmed.",
    "Reminder: Meeting at 10 AM tomorrow.", "Don't miss the deadline!",
    "Please review the attached document.", "I hope this email finds you well.",
    "Have you checked the new updates?", "We're excited to announce our new product!",
    "Can you confirm your attendance?", "We're offering a special discount!",
    "You have a new follower!", "Congratulations on your achievement!",
    "Your feedback is important to us.", "Looking forward to hearing from you.",
    "We're here to help you with any queries.", "Your account has been successfully created.",
    "Thanks for being a loyal customer.", "Important: Update your account details.",
    "You're invited to our exclusive webinar!", "Check out our latest blog post!",
    "You have a message from customer support.", "Can we discuss this over coffee?",
    "Your order has been dispatched!", "Thank you for your support.",
    "You have a new message!", "This is a friendly reminder.",
    "Your opinion matters to us!", "Let's make plans for the weekend.",
    "You're eligible for a special offer!", "This is an automated message.",
    "We've updated our privacy policy.", "Can you help me with this task?",
    "Thank you for your feedback!", "We're looking forward to your response.",
    "This message contains important information.", "Don't forget to RSVP.",
    "Your invoice is ready.", "You have a new message!",
    "Join us for a free trial!", "Your feedback helps us improve.",
    "We appreciate your business!", "Your account has been activated.",
    "We value your input!", "Here's a special offer for you!",
    "We're excited to share our new updates.", "Your package will arrive soon.",
    "You have a new comment on your post!", "Thanks for your prompt reply.",
    "We are reaching out to inform you about our latest updates.",
    "Your appointment is confirmed.", "We're having a sale this weekend!",
    "Your new password has been set.", "Check out our upcoming events!",
    "This is a limited time offer!", "Congratulations! You've won a prize!",
    "Your membership has been renewed.", "You're invited to join our community!",
    "Don't miss out on this opportunity!", "We have a surprise for you!",
    "You have an important message from HR.", "Let's collaborate on this project.",
    "Thank you for your subscription!", "Your order has been confirmed!",
    "We are here to assist you.", "You're receiving this message because you opted in.",
    "Don't forget to check your email.", "Your feedback is valuable to us.",
    "We're hosting a contest, join now!", "You have been selected for a survey!",
    "This is not a spam message, we promise!", "Meet me at the coffee shop.",
    "Looking forward to our meeting.", "We appreciate your loyalty.",
    "You are receiving this message as part of our newsletter.",
    "This is a promotional message.", "We value your opinion!",
    "Join our webinar for more insights!", "You have a new connection on LinkedIn!",
    "We're excited to have you on board!", "Thank you for being a part of our community.",
    "We have something special just for you!", "Your review is appreciated.",
    "Your application is under review.", "Congratulations on your new job!",
    "You have an invitation to our event!", "We're happy to inform you that...",
    "Your feedback helps us to serve you better.", "Thank you for your inquiry.",
    "You're a valued member of our community!", "We are glad to have you with us.",
    "Here's a reminder for your appointment.", "We're here to make your experience better!"
]

# Define exactly 100 spam messages
spam_messages = [
    "Congratulations! You've won a lottery!", "Click here to claim your prize now!",
    "Free trial for a limited time!", "Call now for amazing offers!",
    "Get paid to work from home!", "You have a new message from your bank.",
    "Your account has been compromised!", "Limited time offer! Act now!",
    "You're eligible for a loan! Click to apply.", "Claim your free gift today!",
    "Congratulations! You've been selected!", "Act now and get a discount!",
    "Get rich quick!", "Earn money from home!",
    "You've been chosen for a special offer!", "This is your last chance to win big!",
    "You have a limited-time offer!", "You are a lucky winner!",
    "Click here to get your free gift!", "Don't miss this opportunity!",
    "Urgent: Update your payment information.", "This is a spam message!",
    "Get paid while you sleep!", "Your account will be suspended unless you act now!",
    "Congratulations! You are a finalist!", "You have a special offer waiting for you!",
    "Claim your cash prize!", "This is a one-time opportunity!",
    "You have won a free vacation!", "Your entry has been received!",
    "Don't delete this email!", "Your order has been shipped!",
    "You've been selected for a free gift!", "Hurry, offer ends soon!",
    "You're eligible for a refund!", "Congratulations! You've been chosen!",
    "You have an important message!", "You are one click away from a huge reward!",
    "Important: Your account is at risk!", "Your subscription is confirmed. Get your free gift!",
    "You have a new alert from your account!", "Don't miss out on this amazing offer!",
    "Act fast! Limited time offer!", "This is not a spam message.",
    "Your winnings await you!", "Congratulations! You've won!",
    "Get paid to click ads!", "Free money waiting for you!",
    "Your account has been credited!", "Your email address has won!",
    "You have an important notification from our team!",
    "This message contains exclusive offers!", "You've been selected for a survey!",
    "Claim your prize before it's too late!", "Important: You've been selected for a special deal!",
    "You are a winner! Click to claim your prize!",
    "You have a chance to earn cash!",
    "You've been pre-approved for a credit card!",
    "You have a new message from our marketing team!",
    "Get paid for your opinion!",
    "This is your final notice!",
    "Congratulations! You've won a gift card!",
    "Get started with a free trial today!",
    "You have an exclusive offer waiting!",
    "You have a new notification from our company!",
    "Don't let this opportunity pass you by!",
    "Congratulations! You've been selected for an exclusive offer!",
    "You're invited to our free seminar!",
    "This is a limited time offer, act fast!",
    "You've been chosen to receive a special gift!",
    "You are eligible for a special promotion!",
    "Claim your free trial today!",
    "Your account has been successfully activated!",
    "Act now for amazing discounts!",
    "Congratulations! You've been selected for a free service!",
    "You are a lucky winner!",
    "Get rich quick! Sign up now!",
    "You've won a cash prize!",
    "This is your chance to earn money from home!",
    "You've been selected for a special reward!",
    "Get paid to take surveys!",
    "Your account is at risk! Act now!",
    "You've been chosen for an exclusive invitation!",
    "Claim your special offer today!",
    "You've won a free cruise!",
    "Congratulations! You've been selected for a free gift card!"
    "Congratulations! You've won a $1000 gift card!"
    "Act now! Click here to claim your prize!"
    "Earn money from home with no experience required!"
    "Your account has been compromised. Verify your information immediately!"
    "You have a chance to win a free vacation to the Bahamas!"
    "Limited time offer! Get rich quick!"
    "Congratulations! You've been selected for a free gift!"
    "Your payment is due! Click to pay now."
    "This is not spam! You have a special offer waiting for you."
    "Click here to see your exclusive rewards!"
    "Your subscription has been confirmed! Enjoy your free trial!"
    "You have won a brand new iPhone! Click to claim!"
    "Don't miss out on this once-in-a-lifetime opportunity!"
    "You've been chosen to receive a cash bonus!"
]

# Create a dictionary with the messages
data = {
    'label': ['ham'] * 100 + ['spam'] * 100,  # 100 ham and 100 spam
    'message': ham_messages + spam_messages  # Combine both lists
}

# Create a DataFrame
df = pd.DataFrame(data)

# Check lengths of ham and spam messages
ham_length = len(df[df['label'] == 'ham'])
spam_length = len(df[df['label'] == 'spam'])

# Print lengths for debugging
print(f"Length of ham messages: {ham_length}")
print(f"Length of spam messages: {spam_length}")

# Save the DataFrame to a CSV file named spam.csv
if ham_length == 100 and spam_length == 100:
    df.to_csv('spam.csv', index=False, encoding='utf-8')
    print("Dataset saved as 'spam.csv'")
else:
    print("Error: Ham and spam message lists must each contain exactly 100 messages.")
