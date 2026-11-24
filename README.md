# PS 76 - Examination Timetable Generator

**Language:** Python 3
**Concepts:** Lists, Dictionaries, Scheduling, Constraints
**University:** Rungta International Skills University - B.Tech CSE, First Semester

## Problem Statement
Generate an exam date sheet from a list of subjects, a start date and optional holidays.
One exam is scheduled per day, in the given order. Sundays and holidays are skipped.
The `datetime` module is used to find dates and weekdays.

## How to Run
```
python exam_timetable_generator.py
```
Choose:
- `1` - enter your own subjects, start date (DD-MM-YYYY) and holidays
- `2` - run all 4 test cases from the problem statement automatically

## How It Works
1. Subjects are stored in a **list**.
2. Input is validated (date format, at least one subject, no duplicates).
3. Starting from the start date, each subject gets the next free day
   (not a Sunday, not a holiday).
4. The result is stored in a **dictionary** `{subject: date}` and printed with the weekday.

## Test Cases
| # | Input | Output |
|---|-------|--------|
| 1 | DAA, DBMS, OOP, Maths, CSA / 12-10-2026 / holiday 14-10-2026 | DAA 12 (Mon), DBMS 13 (Tue), OOP 15 (Thu), Maths 16 (Fri), CSA 17 (Sat) |
| 2 | DAA / 18-10-2026 (Sunday) / none | DAA 19-10-2026 (Monday) |
| 3a | DAA, DBMS / 32-10-2026 | Invalid date. Please enter the date as DD-MM-YYYY. |
| 3b | (no subjects) | At least one subject is required. |
| 3c | DAA, DAA | Duplicate subject: DAA. |
| 4 | DAA, DBMS, OOP, Maths, CSA, DM, Java / 12-10-2026 / none | DAA 12, DBMS 13, OOP 14, Maths 15, CSA 16, DM 17 (Sat), Java 19 (Mon) |

Screenshots of all test cases are in the `Testcases` folder.
