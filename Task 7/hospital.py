class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        
    def show_record(self):
        return f"Record ID: {self.record_id}\nDiagnosis: {self.diagnosis}\nTreatment: {self.treatment}"
        
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_records = []
        
    def add_medical_record(self, record_id, diagnosis, treatment):
        record = MedicalRecord(record_id, diagnosis, treatment)
        self.medical_records.append(record)
        
    def show_records(self):
        for record in self.medical_records:
            print(record.show_record())
            
class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients = []
        
    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            
    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            
    def info(self):
        return f"Dr. {self.name} (Specialty: {self.specialty})"
    
class Department:
    def __init__(self, departmen_name):
        self.departmen_name = departmen_name
        self.doctors = []
        
    def add_doctor(self, doctor):
        if doctor not in self.doctors:
            self.doctors.append(doctor)
            
    def remove_doctor(self, doctor):
        if doctor in self.doctors:
            self.doctors.remove(doctor)
    
    def show_doctors(self):
        return f"Department: {self.departmen_name}, Doctors: {[doctor.name for doctor in self.doctors]}"
    
class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []
        
    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            
    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            
    def show_departments(self):
        return f"Hospital: {self.name}, Departments: {[department.departmen_name for department in self.departments]}"
    
# Example
hospital = Hospital("Mayzh Hospital")

dep1 = Department("Cardiology")
dep2 = Department("Neurology")

hospital.add_department(dep1)
hospital.add_department(dep2)

doc1 = Doctor(1, "Dr. Akmal Zaidan Ganteng", "Cardiology")
doc2 = Doctor(2, "Dr. Budi", "Neurology")

dep1.add_doctor(doc1)
dep2.add_doctor(doc2)

pat1 = Patient(1, "John Doe", 30)
pat2 = Patient(2, "Jane Doe", 25)

doc1.add_patient(pat1)
doc2.add_patient(pat2)

pat1.add_medical_record(1, "Fever", "Rest and fluids")
pat2.add_medical_record(2, "Headache", "Ibuprofen")

print(hospital.show_departments())
print(pat1.show_records())
print(pat2.show_records())
print(doc1.info())
print(doc2.info())
print(dep1.show_doctors())
