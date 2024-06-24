# build class cha
class Person:
    def __init__(self, name: str, yob: int):
        self.__name = name
        self.__yob = yob

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    def set_name(self, name):
        self.__name = name

    def set_yob(self, yob):
        self.__yob = yob

# Tạo class job


class Student(Person):
    def __init__(self, name, yob, grade: int):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f'name:{self.get_name()}, yob:{self.get_yob()}, grade:{self._grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f'name:{self.get_name()}, yob:{self.get_yob()}, subject:{self._subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f'name:{self.get_name()}, yob:{self.get_yob()}, grade:{self._specialist}')

# Tạo Ward


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f'Ward name: {self.name}')
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.get_yob(), reverse=True)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return None
        return sum(teacher.get_yob() for teacher in teachers) / len(teachers)


student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()

teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

num_doctors = ward1.count_doctor()
print(f'Number of doctors in the ward: {num_doctors}')

print("\nAfter sorting Age of Ward1 people")
ward1 . sort_age()
ward1 . describe()


print(f"\nAverage year of birth (teachers): { ward1.compute_average()}")
