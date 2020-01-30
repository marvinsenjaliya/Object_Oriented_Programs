import json
class Patient:

    def __init__(self):
        self.data=dict()
        with open('patient.json') as patient_file:
            self.data=json.load(patient_file)

    def patientSearch(self):
        
        while True:
            print("Search the Patient:")
            print("1:Search by MobileNumber")
            print("2:Search by ID")
            print("3:Search by Name")
            print("4:exit")
            userInput=int(input("please enter your choice:"))
            
            if userInput == 1:
                patientmobilenumber = int(input("Enter the mobile number:"))
                for mobileNumber in self.data["Patients"]:
                    if mobileNumber["MobileNumber"] == patientmobilenumber:
                        print(mobileNumber)
             
            if userInput == 2:
                id = int(input("Enter the patient id:"))
                for identification in self.data["Patients"]:
                    if identification["ID"] == id:
                        print(identification)
                    
            if userInput == 3:
                name = input("Enter the patient name:")
                for patientname in self.data["Patients"]:
                    if patientname["Name"] == name:
                        print(patientname)

            if userInput == 4:
                break

    def patientReport(self):
        print(self.data)



