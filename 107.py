# Loop through a dictionary

student = {
    "name" : "Vivek Thakur",
    "age" : 27,
    "country" : "Nepal", 
}

# for key in student:  
#     print(key)                 # name, age, country

# for key in student:
#     print(student[key])   # Vivek Thakur, 27, Nepal


for key, value in student.items():
    print(key, ":", value)