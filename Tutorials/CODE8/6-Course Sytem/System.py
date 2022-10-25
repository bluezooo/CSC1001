from Student import Student
from Staff import Staff
from Course import Course

#System class is a simulation of graphical interface of Course Selection System: 
#System class stores and allows updates for the information of all users(Student/Staff).
class System:
    def __init__(self):
        self.CourseDict={} #{course code:course object} for all the courses provided for students to select
        self.StudentDict={} #{student id:student object} for all students 
        self.StaffDict={}   #{staff id:staff object} for all staffs
        
    #def show(self) to simulate course selection process, showing the main menu for all courses     
    def show(self):
        while True:
            #courseList stores all the courses provided for students to choose, list allows order to appear the same for all students
            courseList=list(self.CourseDict.values())
            print('1:Student')
            print('2:Staff')
            print('3:Administrator')
            status=input('Please select your status:')
            if status=='1':
                ID=input('Please enter your student ID:')
                #student here is the student object corresponding to this ID
                student=self.StudentDict[ID]
                print('Hi,%s!Welcome!'%student.Name)
                #Use index 1,2,3,... to represent each course, just type the number to select a course
                index=0
                #The dictionary IndexDict {index:course object} is to correspond index the the relevant course
                IndexDict={}
                for course in courseList:
                    index+=1
                    print('%d:%s'%(index,course.Code))
                    IndexDict[index]=course
                #The list indexList stores the all indexes the student chooses, here eval('[%s]'%'1,2,3') for example turns the input to a list
                indexList=eval('[%s]'%input('Please select the course you want to add(Use comma to separate):\n').strip())
                for j in indexList:
                    #IndexDict[j] is the course object with index j, which has method addStudent() to add students to its data field self.StudentDice
                    IndexDict[j].addStudent(student)
                    student.selectCourse(IndexDict[j])
                print("You have chosen:")
                for course in student.CourseDict.values():
                    print(course)
                input("Press Enter to exit")
            elif status=='3':
                input("Press Enter to stop the program")
                break
            
    #def readStudentDict(self,file) to import information of all students from the student.txt file to the data fields self.StudentDict of System class           
    def readStudentDict(self,file):
        f=open(file,'r')
        studentInfoList=[]
        for line in f.readlines():
            studentInfoList.append(line.split())
        #Delete the first line which is desription 'ID    Name    Major'
        studentInfoList.pop(0)
        for Info in studentInfoList:
            ID=Info[0]
            name=Info[1]
            major=Info[2]
            student=Student()
            student.setID(ID)
            student.setName(name)
            student.setMajor(major)
            self.StudentDict[ID]=student
        f.close()
        
    #def readStaffDict(self,file) to import information of all staffs from the staff.txt file to the data fields self.StaffDict of System class
    def readStaffDict(self,file):
        f=open(file,'r')
        staffInfoList=[]
        for line in f.readlines():
            staffInfoList.append(line.split())
        #Delete the first line which is desription 'ID    Name    Course'
        staffInfoList.pop(0)
        for Info in staffInfoList:
            ID=Info[0]
            name=Info[1]
            code=Info[2]
            staff=Staff()
            course=Course()
            staff.setID(ID)
            staff.setName(name)
            course.setCode(code)
            course.setInstructor(staff)
            self.StaffDict[ID]=staff
            self.CourseDict[code]=course
        f.close()

    #def generateFile(self) to generate a file storing all information after the selection process       
    def generateFile(self):
        file=open('CourseSelection.txt','w')
        for course in self.CourseDict.values():
            file.write('-'*20+'\n')
            file.write('Course code:%s\n'%course.Code)
            file.write('Course instructor:Prof %s\n'%(course.Instructor.Name))
            file.write('Course student namelist:\n')
            for student in course.StudentDict.values():
                file.write(str(student)+'\n')
            file.write('-'*20+'\n')
        file.close()


