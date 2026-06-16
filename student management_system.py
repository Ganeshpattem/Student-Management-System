print('student management system')
class Student:
    student_dictionary = {}

    def __init__(self):
        self.rollno = self._get_roll_number()
        self.name = input('\tenter the student name: ')
        self.phone = input('\tenter the student phone number: ')
        self.address = input('\tenter the student address: ')
        self.email = input('\tenter the student email: ')
        self.course = input('\tenter the student course: ')
        self.year = int(input('\tenter the student year: '))
        self.semester = int(input('\tenter the student semester: '))
        Student.student_dictionary[self.rollno] = self
        print('student information added successfully')
        self.get_student_information()

    @staticmethod
    def _get_roll_number():
        while True:
            try:
                return int(input('\tenter the student roll number: '))
            except ValueError:
                print('invalid roll number, please enter a number')

    def get_student_information(self):
        print('student information:')
        print('\tstudent roll number:', self.rollno)
        print('\tstudent name:', self.name)
        print('\tstudent phone number:', self.phone)
        print('\tstudent address:', self.address)
        print('\tstudent email:', self.email)
        print('\tstudent course:', self.course)
        print('\tstudent year:', self.year)
        print('\tstudent semester:', self.semester)

    def update_information(self):
        print('update student information (leave blank to keep current value)')
        name = input(f'\tenter the student name [{self.name}]: ').strip()
        if name:
            self.name = name
        phone = input(f'\tenter the student phone number [{self.phone}]: ').strip()
        if phone:
            self.phone = phone
        address = input(f'\tenter the student address [{self.address}]: ').strip()
        if address:
            self.address = address
        email = input(f'\tenter the student email [{self.email}]: ').strip()
        if email:
            self.email = email
        course = input(f'\tenter the student course [{self.course}]: ').strip()
        if course:
            self.course = course
        year = input(f'\tenter the student year [{self.year}]: ').strip()
        if year:
            self.year = int(year)
        semester = input(f'\tenter the student semester [{self.semester}]: ').strip()
        if semester:
            self.semester = int(semester)
        print('student information updated successfully')
        self.get_student_information()


def functions():
    while True:
        print()
        print('welcome to GPIT college')
        print('welcome to student management system')
        print('\t1. get student information')
        print('\t2. add student information')
        print('\t3. delete student information')
        print('\t4. update student information')
        print('\t5. get number of students in the college')
        print('\t6. exit')

        options = input('please enter your choice: ').strip()
        print()
        print('your chosen option:', options)

        if options == '1':
            try:
                rollno = int(input('enter the student roll number:'))
                Student.student_dictionary[rollno].get_student_information()
            except (ValueError, KeyError):
                print('you have entered the wrong roll number, please try again')

        elif options == '2':
            Student()
            print('you have chosen to add student information')

        elif options == '3':
            try:
                rollno = int(input('enter the student roll number:  '))
                Student.student_dictionary.pop(rollno)
                print('you have chosen to delete student information')
                print('student information deleted successfully for roll number:', rollno)
            except ValueError:
                print('invalid input, please enter a valid roll number')
            except KeyError:
                print('you have entered the wrong roll number, please try again')

        elif options == '4':
            try:
                rollno = int(input('enter student roll number:'))
                student = Student.student_dictionary[rollno]
            except (ValueError, KeyError):
                print('you have entered the wrong roll number, please try again')
            else:
                print('you have chosen to update student information')
                student.update_information()

        elif options == '5':
            total = len(Student.student_dictionary)
            print('you have chosen to get number of students in the college')
            print('total students:', total)

        elif options == '6':
            print('you have chosen to exit')
            break

        else:
            print('invalid choice, please enter a number between 1 and 6')


if __name__ == '__main__':
    functions()
    