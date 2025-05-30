from collections import defaultdict
from typing import List


day1 = ["Raman", "Bobby", "Chahat"]
day2 = ["Raman", "David"]
day3 = ["Bobby", "Chahat", "David"]
all_days = [day1, day2, day3]


def track_attendance(days: List[List[str]]) -> dict:
    """
    Goes through a list of daily attendance lists and counts appearances.

    Args:
        days (List[List[str]]): Each sublist represents a single day's attendance.

    Returns:
        dict: Mapping of student names to the number of times they appeared.
    """
    attendance = defaultdict(int)
    for day in days:
        for student in day:
            attendance[student] += 1
    return dict(attendance)


attendance_summary = track_attendance(all_days)

print("Attendance Summary:")
print(attendance_summary)
