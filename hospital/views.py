from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def doctors(request):
    Doctors=[
        {
            "name":"Dr.fida",
            "specialization":"Cardiology",
            "experience":10

        },{
            "name":"Dr.shamna",
            "specialization":"Neurologist",
            "experience":5
        },
         {
            'name': 'Dr. Sara',
            'specialization': 'Dermatologist',
            'experience': 5
        },
         {
            'name': 'Dr. Rahul',
            'specialization': 'Neurologist',
            'experience': 8
        },
         {
            'name': 'Dr. Arun',
            'specialization': 'Cardiologist',
            'experience': 10
        },
    ]
    context={"doctor":Doctors}

    
    return render(request,"doctors.html",context)
def patients(request):
     patient_list = [
        {
            "name": "Fathima",
            "age": 22,
            "gender": "Female",
            "disease": "Fever",
            "phone": "9876543210"
        },
        {
            "name": "Shamna",
            "age": 25,
            "gender": "Female",
            "disease": "Diabetes",
            "phone": "9876543211"
        },
        {
            "name": "Arun",
            "age": 30,
            "gender": "Male",
            "disease": "Headache",
            "phone": "9876543212"
        },
        {
            "name": "Rahul",
            "age": 35,
            "gender": "Male",
            "disease": "Asthma",
            "phone": "9876543213"
        }
    ]
     context={
         "patients":patient_list
    }
 
     return render(request,"patients.html",context)