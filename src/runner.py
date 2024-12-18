'''import sys

print(sys.argv)
import math as m

print(m.sqrt(12))

print(m.factorial(5))
'''


class studentdatabase:
    def _init_(self):
        self.students={}
    def create(self,id,department,rollno,name):
        if id in self.students:
            print("student id already exits")
        else:
            self.students[id]={'name':name,'department':department,'roll number':rollno}
            print("student id created successfully👍")
    def delete(self,id):
        if id in self.students:
            del self.students[id]
            print("student id deleted successfully")
        else:
            print("id cannot be  found")
    def update(self,id,name='None',department='None',rollno='None'):
        if id in self.students:
            if name:
                self.students[id]['name']=name
            if department:
                self.students[id]['department']=department
            if rollno:
                self.students[id]['rollno']=rollno
            print("updated successfully")
        else:
            print("student id not found")
    def veiwbyname(self,name):
        g= False
        for id,details in self.students.items():
           if details['name']==name:
               print(f"ID: {id}, Name: {details['name']}, Department: {details['department']}")
               g=True
        if not g:
            print("invalid name")
    def veiwbydept(self,department):
        f=False
        for id, details in self.students.items():
            if details['department'] == department:
                print(f"ID: {id}, Name: {details['name']}, Department: {details['department']}")
                f=True
        if not f:
            print("invalid entry")
def main():
    a=studentdatabase()
    while True:
        print("\nStudent Database Management System")
        print("1. Create Student Record")
        print("2. Delete Student Record")
        print("3. Update Student Record")
        print("4. View by Name")
        print("5. View by Department")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            rollno=input("Enter roll number")
            a.create(id,department,rollno,name)
        elif choice == '2':
            id = input("Enter Student ID to delete: ")
            a.delete(id)
        elif choice == '3':
            id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            department = input("Enter new Department (leave blank to keep unchanged): ")
            rollno = input("Enter roll number")
            a.update(id, name if name else None, department if department else None,rollno if rollno else None )
        elif choice == '4':
            name = input("Enter Name to search: ")
            a.veiwbyname(name)
        elif choice == '5':
            department = input("Enter Department to search: ")
            a.veiwbydept(department)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
c=main()