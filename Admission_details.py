print("Techspace Admission Form :")

print("\nStudent Details:")

while True:
    name = input("Enter your full name: ")
    if name == "" or " " not in name or not name.replace(" ", "").isalpha():
        print("Invalid name. Enter full name using letters only.")
    else:
        break

while True:
    age = input("Enter your age: ")

    if not age.isdigit():
        print("Invalid age (numbers only)")
    else:
        age = int(age)
        if age <= 0 or age > 50:
            print("Invalid age (must be between 1 and 50)")
        else:
            break

while True:
    mobile = input("Mobile Number: ")
    if not mobile.isdigit() or len(mobile) != 10:
        print("Invalid mobile. Enter 10 digits.")
    else:
        break

while True:
    alt_mobile = input("Enter Alternative Mobile Number (10 digits): ")

    if not alt_mobile.isdigit() or len(alt_mobile) != 10:
        print("Invalid number. Only digits are allowed.")
    else:
        break

from datetime import datetime
while True:
    dob = input("Date of Birth (DD-MM-YYYY): ")
    try:
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        if dob_date.year > 2025:
            print("Invalid DOB. Future date not allowed.")
        else:
            break
    except:
        print("Invalid DOB. Use DD-MM-YYYY format.")

while True:
    email = input("Email ID: ")
    if not email.endswith("@gmail.com"):
        print("Invalid email. Must end with @gmail.com.")
    else:
        local = email.split("@")[0]
        if local == "" or not local.replace(".", "").replace("_","").isalnum():
            print("Invalid email. Check characters before @.")
        elif email != email.lower():
            print("Invalid email. Use lowercase only.")
        else:
            break

while True:
    aadhar = input("Aadhar Number (12 digits): ")
    if not aadhar.isdigit() or len(aadhar) != 12:
        print("Invalid Aadhar. Enter 12 digits.")
    else:
        break

while True:
    pan = input("PAN Number : ").upper()

    if len(pan) != 10:
        print("Invalid PAN. PAN must be exactly 10 characters.")

    elif pan.isdigit():
        print("Invalid PAN. PAN cannot be only numbers.")

    elif not pan[0:5].isalpha():
        print("Invalid PAN. First 5 characters must be letters.")

    elif not pan[5:9].isdigit():
        print("Invalid PAN. Characters 6 to 9 must be digits.")

    elif not pan[9].isalpha():
        print("Invalid PAN. Last character must be a letter.")

    else:
        print("PAN accepted ")
        break

while True:
    qual = input("Current Qualification: ")
    if qual == "" or not qual.replace(" ", "").isalpha():
        print("Invalid qualification. Letters only.")
    else:
        break

while True:
    year = input("Year of study: ")
    if not year.isdigit():
        print("Invalid year. Enter numbers only.")
    else:
        break

while True:
    hobbies = input("Enter your hobbies (comma separated): ")
    valid_hobby = True
    for char in hobbies:
        if char.isdigit():
            valid_hobby = False
            break
    if hobbies == "" or not valid_hobby:
        print("Invalid hobbies. Letters only.")
    else:
        break

while True:
    skills = input("Enter skill  (letters only): ")
    if skills == "" or not skills.isalpha():
        print("Invalid skill. Letters only.")
    else:
        break

address = input("Enter your address: ")
if address == "":
    print("Address cannot be empty")
    exit()

while True:
    city = input("Enter your city: ")
    if city == "":
        print("City cannot be empty")
    elif not city.replace(" ", "").isalpha():
        print("City must contain only letters")
    else:
        break

while True:
    pin = input("Enter 6-digit PIN code: ")
    if not pin.isdigit():
        print("PIN code must contain only numbers")
    elif len(pin) != 6:
        print("PIN code must be exactly 6 digits")
    else:
        break

print("Address, City and PIN code accepted successfully ")
    
while True:
    marks10 = input("Enter 10th Marks (%): ")

    if marks10.replace(".", "", 1).isdigit():
        marks10 = float(marks10)
        if marks10 >= 0 and marks10 <= 100:
            break
        else:
            print("Invalid marks (0 to 100 only)")
    else:
        print("Invalid marks (enter percentage)")

while True:
    marks12 = input("Enter 12th Marks (%): ")

    if marks12.replace(".", "", 1).isdigit():
        marks12 = float(marks12)
        if marks12 >= 0 and marks12 <= 100:
            break
        else:
            print("Invalid marks (0 to 100 only)")
    else:
        print("Invalid marks (enter percentage)")
print("\nCollege Details:")

while True:
    college_name = input("Enter your college name: ")
    if college_name == "" or not college_name.replace(" ", "").isalpha():
        print("Invalid college name.")
    else:
        break

while True:
    branch = input("Enter your Branch: ")
    if branch == "" or not branch.replace(" ", "").isalpha():
        print("Invalid branch.")
    else:
        break

while True:
    university = input("Enter university name: ")
    if university == "" or not university.replace(" ", "").isalpha():
        print("Invalid university.")
    else:
        break

while True:
    city = input("Enter your city: ")
    if city == "" or not city.replace(" ", "").isalpha():
        print("Invalid city.")
    else:
        break

while True:
    state = input("Enter your state: ")
    if state == "" or not state.replace(" ", "").isalpha():
        print("Invalid state.")
    else:
        break

print("\nCourse Interest")
print("1. Data Science and AI/ML")
print("2. Full Stack Development")
print("3. Backend Development")
print("4. Frontend Development")
print("5. Other")

while True:
    choice = input("Choose your course (1-5): ")
    if choice in ["1","2","3","4","5"]:
        break
    else:
        print("Invalid choice.")

if choice == "1":
    course = "Data Science and AI/ML"
elif choice == "2":
    course = "Full Stack Development"
elif choice == "3":
    course = "Backend Development"
elif choice == "4":
    course = "Frontend Development"
else:
    course = input("Enter your preferred course: ")

print("Selected Course:", course)

while True:
    select = input("When do you plan to start? ")
    if select == "":
        print("Start time cannot be empty.")
    else:
        break

print("\nFeedback")
print("Lecture Rating: 1-Excellent 2-Good 3-Average")
while True:
    rating = input("Enter your choice (1-3): ")
    if rating in ["1","2","3"]:
        break
    else:
        print("Invalid choice.")

print("Clarity Rating: 1-Very Clear 2-Clear 3-Somewhat Clear 4-Improvement needed")
while True:
    clarity = input("Enter your choice (1-4): ")
    if clarity in ["1","2","3","4"]:
        break
    else:
        print("Invalid choice.")

while True:
    comment = input("Any comments/suggestions (max 100 words): ")
    if len(comment.split()) > 100:
        print("Word limit exceeded.")
    else:
        break

while True:
    suggestion = input("Enter your suggestion (max 100 words): ")
    if len(suggestion.split()) > 100:
        print("Word limit exceeded.")
    else:
        break

while True:
    consent = input("May we contact you? (yes/no): ")
    if consent not in ["yes","no"]:
        print("Invalid input.")
    else:
        break

print("\nForm submitted successfully! ")
print("\n--- Student Details Summary ---")
print("Name:", name)
print("Age:", age)
print("Mobile:", mobile)
print("DOB:", dob)
print("Email:", email)
print("Aadhar:", aadhar)
print("PAN:", pan)
print("Qualification:", qual)
print("Year of Study:", year)
print("Hobbies:", hobbies)
print("Skill Code:", skills)
print("Address:\n", address)
print("PIN Code:", pin)
print("10th Marks:", str(marks10)+"%")
print("12th Marks:", str(marks12)+"%")
print("College:", college_name)
print("Branch:", branch)
print("University:", university)
print("City:", city)
print("State:", state)
print("Selected Course:", course)
print("Start Time:", select)
print("Lecture Rating:", rating)
print("Clarity Rating:", clarity)
print("Comments:", comment)
print("Suggestion:", suggestion)
print("Consent:", consent)

print("\nForm Submitted Successfully! ")