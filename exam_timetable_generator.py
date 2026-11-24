# Project No. 76 - Examination Timetable Generator
# Language: Python 3
# Concepts: Lists, Dictionaries, Scheduling, Constraints

from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"


def parse_date(text):
    """Convert 'DD-MM-YYYY' text to a datetime. Return None if invalid."""
    text = text.strip()
    if len(text) != 10:
        return None
    try:
        return datetime.strptime(text, DATE_FORMAT)
    except ValueError:
        return None


def parse_subjects(text):
    """Convert 'DAA, DBMS, OOP' into a list ['DAA', 'DBMS', 'OOP']."""
    subjects = []
    for item in text.split(","):
        item = item.strip()
        if item != "":
            subjects.append(item)
    return subjects


def check_subjects(subjects):
    """Return an error message if the subject list is wrong, else None."""
    if len(subjects) == 0:
        return "At least one subject is required."
    seen = []
    for subject in subjects:
        if subject.lower() in seen:
            return "Duplicate subject: " + subject + "."
        seen.append(subject.lower())
    return None


def parse_holidays(text):
    """Return (list_of_holiday_dates, error_message)."""
    holidays = []
    text = text.strip()
    if text == "" or text.lower() == "none":
        return holidays, None
    for item in text.split(","):
        date = parse_date(item)
        if date is None:
            return [], "Invalid holiday date. Please enter the date as DD-MM-YYYY."
        holidays.append(date)
    return holidays, None


def generate_timetable(subjects, start_date, holidays):
    """One exam per day, in the given order. Skip Sundays and holidays.
    Returns a dictionary: {subject: date}"""
    timetable = {}
    current = start_date
    for subject in subjects:
        while current.weekday() == 6 or current in holidays:  # 6 = Sunday
            current = current + timedelta(days=1)
        timetable[subject] = current
        current = current + timedelta(days=1)
    return timetable


def run(subjects_text, start_text, holidays_text):
    """Validate input, build the timetable and print it."""
    subjects = parse_subjects(subjects_text)
    error = check_subjects(subjects)
    if error:
        print(error)
        return

    start_date = parse_date(start_text)
    if start_date is None:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    holidays, error = parse_holidays(holidays_text)
    if error:
        print(error)
        return

    timetable = generate_timetable(subjects, start_date, holidays)
    for subject in timetable:
        date = timetable[subject]
        print(subject + " : " + date.strftime(DATE_FORMAT) + " (" + date.strftime("%A") + ")")


def run_test_cases():
    """The 4 test cases from the problem statement."""
    tests = [
        ("Test Case 1: Normal Input",
         "DAA, DBMS, OOP, Maths, CSA", "12-10-2026", "14-10-2026"),
        ("Test Case 2: Boundary / Minimum Input",
         "DAA", "18-10-2026", "none"),
        ("Test Case 3(a): Invalid Input - bad date",
         "DAA, DBMS", "32-10-2026", "none"),
        ("Test Case 3(b): Invalid Input - no subjects",
         "", "12-10-2026", "none"),
        ("Test Case 3(c): Invalid Input - duplicate subject",
         "DAA, DAA", "12-10-2026", "none"),
        ("Test Case 4: Different Valid Scenario",
         "DAA, DBMS, OOP, Maths, CSA, DM, Java", "12-10-2026", "none"),
    ]
    for name, subjects, start, holidays in tests:
        print("\n" + name)
        print("Subjects: " + subjects + " | Start: " + start + " | Holidays: " + holidays)
        print("-" * 40)
        run(subjects, start, holidays)


def main():
    print("===== Examination Timetable Generator =====")
    print("1. Enter my own input")
    print("2. Run all test cases")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "2":
        run_test_cases()
    else:
        subjects_text = input("Enter subjects (comma separated): ")
        start_text = input("Enter start date (DD-MM-YYYY): ")
        holidays_text = input("Enter holidays (DD-MM-YYYY, comma separated, or 'none'): ")
        print("\n----- Exam Timetable -----")
        run(subjects_text, start_text, holidays_text)


main()
