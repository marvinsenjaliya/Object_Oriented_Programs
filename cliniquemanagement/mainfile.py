import json
from Doctors import Doctor
from patient import Patient



if __name__ ==  "__main__":

    doctor=Doctor()
    patient=Patient()
    while True:
        user=int(input("please Enter what are you looking for:\n1:Doctors\n2:Patients\n3:Exit"))
        if user == 1:
            while True:
                user_Doctors=int(input("please Enter your Choice:\n1:Search for Doctors\n2:appoint doctor\n3:report doctor\n4:exit"))
                if user_Doctors == 1:
                    doctor.searchDoctors()
                elif user_Doctors ==2:
                    doctor.appointDoctor()
                elif user_Doctors ==3:
                    doctor.appointDoctor()
                elif user_Doctors == 4:
                    break

        elif user == 2:
            while True:
                user_Patient=int(input("please Enter your Choice:\n1:patientSearch\n2:patient report\n3:exit"))
                if user_Patient == 1:
                    patient.patientSearch()
                elif user_Patient == 2:
                    patient.patientReport()
                elif user_Patient == 3:
                    break

        elif user == 3:
            break




