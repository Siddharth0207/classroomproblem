from prob import load_data , save_json



l1 = load_data(r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\data\dataset.xlsx - Student requests.csv")
output_json_student = (r"C:\Users\siddh\OneDrive\文档\ML\digitalyz\json_data\student.json")
json_1  = save_json(l1,output_file=output_json_student)
    