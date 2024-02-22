import os

dir_path = r'/home/mahmoud/Desktop/DSAI03/Valeriia Neganova_359185_assignsubmission_file_/'

res = []

class Student_Submission:

    def __init__(self, first_student, second_student, cosine):
        self.first_student = first_student
        self.second_student = second_student
        self.cosine = cosine

    def display(self):
        return self.first_student + " | " + self.second_student + " | " + str(self.cosine)

def file_Name_Generator(file_name):
    splited_file_name = file_name.split("_")
    student_submission = Student_Submission(splited_file_name[0],
    splited_file_name[1], 50)
    return student_submission

for file_path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_path)) and (".pdf" in file_path):
        for file in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file_path)) and (".pdf" in
            file) and (file != file_path):
                res.append(file_Name_Generator(file_path))
                res.append(file_Name_Generator(file))
for i in res:
    print(i.display())
