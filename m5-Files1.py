#---------------------------------------------
#File Handling 
#----------------------------------------------
import csv
import json
import xml.etree.ElementTree as ET
import zipfile
import os

print("MODULE 5 HANDS-ON: FILE PROCESSING SYSTEM")
print("-" * 55)

# --------------------------------------------------
# 1. TEXT FILE READING AND WRITING
# --------------------------------------------------
print("\n1. TEXT FILE READING AND WRITING")

report_file = "student_report.txt"

with open(report_file, "w") as file:
    file.write("Student Report\n")
    file.write("-------------\n")
    file.write("Rahul - 85\n")
    file.write("Anita - 90\n")
    file.write("John - 78\n")
    file.write("Priya - 88\n")

print("Text file created successfully.")

with open(report_file, "r") as file:
    content = file.read()
    print("\nContent of text file:")
    print(content)


# --------------------------------------------------
# 2. CSV HANDLING
# --------------------------------------------------
print("\n2. CSV HANDLING")

with open("../DATASET/students.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    print("CSV Data:")
    for row in csv_reader:
        print(row)


# --------------------------------------------------
# 3. JSON HANDLING
# --------------------------------------------------
print("\n3. JSON HANDLING")

with open("../DATASET/students.json", "r") as file:
    json_data = json.load(file)
    print("JSON Data:")
    for student in json_data:
        print(student)


# --------------------------------------------------
# 4. XML HANDLING
# --------------------------------------------------
# print("\n4. XML HANDLING")

# tree = ET.parse("../DATASET/students.xml")
# root = tree.getroot()
# <html>
#   <student>
#     <name>Marina</name>
#     <age>25</age>
#   </student>

# <student>
#     <name>Maria</name>
#     <age>20</age>
#   </student>
# </html>

print("XML Data:")
for student in root.findall("student"):
    student_id = student.find("id").text
    name = student.find("name").text
    marks = student.find("marks").text
    print({"id": student_id, "name": name, "marks": marks})


# --------------------------------------------------
# 5. COMPRESSION
# --------------------------------------------------
print("\n5. FILE COMPRESSION")

zip_file_name = "student_files.zip"

with zipfile.ZipFile(zip_file_name, "w") as zipf:
    zipf.write(report_file)
    zipf.write("../DATASET/students.csv", arcname="students.csv")
    zipf.write("../DATASET/students.json", arcname="students.json")
    zipf.write("../DATASET/students.xml", arcname="students.xml")

print("ZIP file created successfully.")


# --------------------------------------------------
# 6. DECOMPRESSION
# --------------------------------------------------
print("\n6. FILE DECOMPRESSION")

extract_folder = "extracted_files"

if not os.path.exists(extract_folder):
    os.mkdir(extract_folder)

with zipfile.ZipFile(zip_file_name, "r") as zipf:
    zipf.extractall(extract_folder)

print("ZIP file extracted successfully.")


# --------------------------------------------------
# 7. CONTEXT MANAGER CONFIRMATION
# --------------------------------------------------
print("\n7. CONTEXT MANAGER USAGE")
print("All files were handled safely using context managers.")

print("\nLab completed successfully.")
