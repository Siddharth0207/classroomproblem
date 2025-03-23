from prob import load_data , save_json , structure_by_student





#Configuration for output files
output_json_student = (r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\json_data\student.json")
output_json_rooms = (r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\json_data\rooms.json")
output_json_courses = (r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\json_data\courses.json")
output_json_lectures = (r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\json_data\lectures.json")



records = load_data(r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\data\dataset.xlsx - Student requests.csv")
student_data = structure_by_student(records)    
save_json(student_data, output_json_student)

rooms = load_data(r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\data\dataset.xlsx - Rooms data.csv")
save_json(rooms, output_json_rooms)

courses = load_data(r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\data\dataset.xlsx - Course list.csv")
save_json(courses, output_json_courses)

lecture_details = load_data(r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\data\dataset.xlsx - Lecturer Details.csv")
save_json(lecture_details, output_json_lectures)

