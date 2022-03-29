# courses = input("Enter students courses")










































































































students = dict()
n = int(input("Enter the number of students in class"))
for i in range(n):
        Sname = input("Enter the Students name:")
        IDs = []
        DoBs = []
        marks = []
        courses = []
        for j in range(1):
            ID = input("Enter students ID:")
            IDs.append(ID)
            DoB = input("Enter Date of Birth as d/m/y: ")
            DoBs.append(DoB)
            mark = int(input("Enter mark of students"))
            while (mark > 100):
                print ("please re-enter the mark")
                mark = int(input("Enter mark of students"))
            else:
                marks.append(mark)

            course = input("Enter courses of students:")
            courses.append(course)
            
        students[Sname] = IDs, marks, courses, DoBs
print ('Marks of students is:', students)

# students = {"Minh" : [89], "Long": [94], "Trang": [76], "Thao": [96]}
Name = input("Enter name of students")

if Name in students :
    print (students[Name])
else:
    print ("Student does not exist on list")