import helper


if __name__ == "__main__":
    participants_list = []
    while True:
        user_input = input(
            "insert 'reg' To enroll, 'info' To get your Info," +
            " 'admin' To enter to the Administrator Panel: ").lower()
        if user_input == "reg":
            while True:
                prof_check = input(
                    "Are you Participate as Lecturer?(yes or no): ").lower()
                if prof_check == "yes":
                    lecturer = helper.get_lecturer_info()
                    helper.save_participant(participants_list, lecturer)
                    break
                elif prof_check == "no":
                    student = helper.get_student_info()
                    helper.save_participant(participants_list, student)
                    break
                else:
                    print("Please Choose yes or no as option!")
        elif user_input == "info":
            while True:
                user_code = input(
                    "Please enter your Code(enter 'back' to exit): ").lower()
                if user_code == "back":
                    break
                for item in participants_list:
                    if item.code == user_code:
                        item.show_info()
                        break
                else:
                    print(
                        "Your code is not correct or You're not register in our list.")
        elif user_input == "admin":
            while True:
                admin_code = input(
                    "Please enter your Administrator code: ")
                if admin_code == "0000":
                    helper.create_csv(participants_list)
                    helper.create_json(participants_list)
                    print("Your files has been created")
                    break
                else:
                    print("Wrong Code!")
                    break
        else:
            print("Wrong Option!")
