import csv
import json
from pathlib import Path
from person import Student, Lecturer


def save_participant(participant_list, participant):
    participant_list.append(participant)


def get_lecturer_info():
    lect = Lecturer()
    code = input("Please enter your code: ")
    if code != "":
        lect.code = code
    name = input("Please enter your name: ")
    if name != "":
        lect.name = name
    family = input("Please enter your name: ")
    if name != "":
        lect.family = family
    lect.show_info()
    lect.greet()
    print("Your info has been saved")
    return lect


def get_student_info():
    stud = Student()
    code = input("Please enter your code: ")
    if code != "":
        stud.code = code
    name = input("Please enter your name: ")
    if name != "":
        stud.name = name
    family = input("Please enter your name: ")
    if name != "":
        stud.family = family
    stud.show_info()
    print("Your info has been saved")
    return stud


def create_json(lst):
    string = []
    for item in lst:
        obj = {}
        obj["code"] = item.code
        obj["name"] = item.name
        obj["family"] = item.family
        string.append(obj)
    data = json.dumps(string)
    print(data)
    Path("participants.json").write_text(data, encoding="utf-8")


def create_csv(lst):
    with open("participants.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Code", "Name", "Family"])
        for item in lst:
            writer.writerow([item.code, item.name, item.family])
