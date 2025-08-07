studentrecords= {'sandeep':99,'deep':60,'sandy':70}
inputvalue = input("Enter the student's Name: ").strip().lower()

if inputvalue in studentrecords:
    print(f"{inputvalue.capitalize()}'s marks: {studentrecords[inputvalue]}")
else:
    print("Student not found.")
