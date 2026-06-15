#---------------------------------------------
#Regex
#----------------------------------------------
import re

print("MODULE 6: REGEX DEMO")
print("-" * 50)

# --------------------------------------------------
# 1. BASIC PATTERN MATCHING
# --------------------------------------------------
print("\n1. BASIC PATTERN MATCHING")

text = "Python is powerful. Python is easy."

result = re.findall("Python", text)
print("Matches for 'Python':", result)


# --------------------------------------------------
# 2. SIMPLE PATTERNS
# --------------------------------------------------
print("\n2. SIMPLE PATTERNS")

text = "My number is 9876543210"

digits = re.findall(r"\d", text)
print("All digits:", digits)

full_number = re.findall(r"\d{10}", text)
print("10-digit number:", full_number)


# --------------------------------------------------
# 3. EMAIL VALIDATION
# --------------------------------------------------
print("\n3. EMAIL VALIDATION")

email_text = "Contact us at support@test.com or admin@company.org"

emails = re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+", email_text)
print("Extracted Emails:", emails)


# --------------------------------------------------
# 4. SEARCH AND REPLACE
# --------------------------------------------------
print("\n4. SEARCH AND REPLACE")

text = "Python is good"

new_text = re.sub("good", "awesome", text)
print("Updated text:", new_text)


# --------------------------------------------------
# 5. SPLITTING TEXT
# --------------------------------------------------
print("\n5. SPLITTING TEXT")

data = "apple,banana;orange|grapes"

split_data = re.split(r"[,;|]", data)
print("Split result:", split_data)


# --------------------------------------------------
# 6. PRACTICAL VALIDATION
# --------------------------------------------------
print("\n6. PRACTICAL VALIDATION")

phone = "9876543210"

if re.match(r"\d{10}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


print("\nDemo completed successfully.")

