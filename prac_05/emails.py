"""
Emails
Estimate: 30 minutes
Actual:   35 minutes
"""

def extract_name(email):
    """Extract name from email."""
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name

email_to_name = {}

email = input("Email: ")
while email != "":
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    if confirmation != "y" and confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
