courseNumber = int(input("Enter course number: "))

def course(courseNumber):
    
    if courseNumber < 100:
        return "Not a course"
    if courseNumber >= 100 and courseNumber < 200:
        return "First Year Course"
    elif courseNumber >= 200 and courseNumber < 300:
        return "Second Year Course"
    elif courseNumber >= 300 and courseNumber < 400:
        return "Third Year Course"
    else:
        return "Graduate Course"

print(course(courseNumber))
