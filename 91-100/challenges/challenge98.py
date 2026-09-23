# check_grade(mark)

# 80+ → A
# 60–79 → B
# 40–59 → C
# Below 40 → F

def check_grade(mark):
    if mark < 40:
        return "F"
    elif mark < 60:
        return "C"
    elif mark < 80:
        return "B"
    else:
        return 'A'

print(check_grade(30))
print(check_grade(48))
print(check_grade(68))
print(check_grade(88))

