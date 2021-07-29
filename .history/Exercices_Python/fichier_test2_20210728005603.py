from _typeshed import Self


class Student:
    def __init__(self, student_id, marks,age):
       self.student_id=student_id
       self.marks=marks
       self.age=age

    def validate_age(self):
        if self.age >20:
            return True
        else:
            return False
    def validate_marks(self):
        if self.marks>0 and self.marks<100:
            return True
        else:
            return False
    def check_qualification(self):
        if (validate_age)==True and if(validate_marks)==True:
            if self.marks>65:
                return True
            else:
                return False
    def set(self,x):
        self.__student_id=x

    def get(self):
        if (check_qualification==True):
            return True
        else:
            return False

print(Student)