import json
class Doctor:

    def __init__(self):
        self.data=dict()
        with open("Doctors.json") as json_file:
            self.data=json.load(json_file)

        
    def searchDoctors(self):
        while True:
            print("Search the doctor:")
            print("1:Using Availability")
            print("2:Using Specialization")
            print("3:Using ID")
            print("4:Using Name")
            print("5:Exit")

            userInput=int(input("Please Enter your choice:"))
            if userInput == 1:
                print("your option :\n1:Am\n2:Pm\n3:Af\n4:Both")
                time = input("Enter the time:")
                for availability in self.data["Doctors"]:
                    if availability["Availability"] == time:
                        print(availability)

            elif userInput == 2:
                special = input("Enter the Specialization:")
                for specialization in self.data["Doctors"]:
                    if specialization["Specialization"] == special:
                        print(specialization)

            elif userInput == 3:
                iD = int(input("Enter the ID from (99,1,2,3,6,12234,54)"))
                for identification in self.data["Doctors"]:
                    if int(identification["ID"]) == iD:
                        print(identification)
                        
            elif userInput == 4:
                name = input("Enter the name from (DR.joshi,DR.Pooja,DR.Vivek,DR.prach,DR.teja,DR.prasad)")
                for doctorName in self.data["Doctors"]:
                    if doctorName["Name"] == name:
                        print(doctorName)

            elif userInput == 5:
                break

    def appointDoctor(self):
        user_Name = input("please Enter your name")
        doctor_Name = input("please Enter Doctor name which you want to appoint:")
        date = input("please Enter the date")
        for appoint in self.data["Doctors"]:
            if appoint['Name'] == doctor_Name:
                self.data['Doctors']['appointment'].append({'name':user_Name,'doctor_Name':doctor_Name,'date':date})
        print(self.data)


    def doctorReport(self):
        doctor_Report=json.dump(self.data)
        print(doctor_Report)
                

            

        

        