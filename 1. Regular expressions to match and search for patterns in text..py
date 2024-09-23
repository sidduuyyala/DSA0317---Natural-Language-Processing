import re
text = "Hello, my email is john.doe@example.com and phone number is 123-456-7890."
email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
email_match = re.search(email_pattern, text)
phone_match = re.search(phone_pattern, text)

if email_match:
    print("Email found:", email_match.group())
else:
    print("Email not found.")

if phone_match:
    print("Phone number found:", phone_match.group())
else:
    print("Phone number not found.")
all_emails = re.findall(email_pattern, text)
all_phone_numbers = re.findall(phone_pattern, text)
print("All emails:", all_emails)
print("All phone numbers:", all_phone_numbers)
