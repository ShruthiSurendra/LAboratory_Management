from django.shortcuts import render
from .models import DoctorRegister
import pandas as pd
from .models import VitaminRegister
from .models import BloodRegister
from .models import HormoneRegister
from .models import SerologyRegister
from .models import CopdRegister


def index(request):
    return render(request, 'lab/index.html')

def register(request):
 if request.method == 'POST':
    print("Successfully registered")
    Name = request.POST['Name']
    Password = request.POST['Password']
    Gender = request.POST['gender']
    Email = request.POST['Email']

    Phone = request.POST['Phone']
    print("Name", Name)
    print("Password", Password)
    print("Gender", Gender)
    print("Email", Email)
    print("Phone", Phone)
    DoctorRegister(Name=Name, Password=Password, Gender=Gender, Email=Email, Phone=Phone).save()
    return render(request, 'lab/thanks.html')
 else:
    return render(request, 'lab/register.html')

def thanks(request):
    return render(request, 'lab/thanks.html')

def blood(request):
    return render(request, 'lab/blood.html')

def bloodr(request):
    if request.method == 'POST':
        print("Successfully registered")
        Name = request.POST['Name']
        Location = request.POST['Location']
        Number = request.POST['Number']
        Age = request.POST['Age']
        Test = request.POST['Test']
        Gender = request.POST['Gender']
        BloodRegister(Name=Name, Location=Location, Number=Number, Age=Age, Test=Test, Gender=Gender).save()
        return render(request, 'lab/thanks.html')
    else:
        return render(request, 'lab/br.html')

def vitamin(request):
    return render(request, 'lab/vitamin.html')

def vr(request):
    if request.method == 'POST':
        print("Successfully registered")
        Name = request.POST['Name']
        Location = request.POST['Location']
        Number = request.POST['Number']
        Age = request.POST['Age']
        Test = request.POST['Test']
        Gender = request.POST['Gender']
        VitaminRegister(Name=Name, Location=Location, Number=Number, Age=Age, Test=Test, Gender=Gender).save()
        return render(request, 'lab/thanks.html')
    else:
        return render(request, 'lab/vr.html')

def hormone(request):
    return render(request, 'lab/hormone.html')

def hr(request):
    if request.method == 'POST':
        print("Successfully registered")
        Name = request.POST['Name']
        Location = request.POST['Location']
        Number = request.POST['Number']
        Age = request.POST['Age']
        Test = request.POST['Test']
        Gender = request.POST['Gender']
        HormoneRegister(Name=Name, Location=Location, Number=Number, Age=Age, Test=Test, Gender=Gender).save()
        return render(request, 'lab/thanks.html')
    else:
        return render(request, 'lab/hr.html')

def serology(request):
    return render(request, 'lab/serology.html')

def sr(request):
    if request.method == 'POST':
        print("Successfully registered")
        Name = request.POST['Name']
        Location = request.POST['Location']
        Number = request.POST['Number']
        Age = request.POST['Age']
        Test = request.POST['Test']

        Gender = request.POST['Gender']




        SerologyRegister(Name=Name, Location=Location, Number=Number, Age=Age, Test=Test, Gender=Gender).save()

        return render(request, 'lab/thanks.html')
    else:
        return render(request, 'lab/sr.html')

def copd(request):
  if request.method == 'POST':
    print("Successfully registered")
    Name = request.POST['Name']
    Aadhar = request.POST['Aadhar']
    Email = request.POST['Email']
    Age = request.POST['Age']
    Gender = request.POST['Gender']
    Weight= request.POST['Weight']
    Lipcolour= request.POST['Lipcolour']
    Fev= request.POST['Fev']
    Intensity= request.POST['Intensity']
    Temperature= request.POST['Temperature']
    print("Name", Name)
    print("Aadhar", Aadhar)
    print("Email", Email)
    print("Age", Age)
    print("Gender", Gender)
    print("Weight", Weight)
    print("Lipcolour", Lipcolour)
    print("Fev", Fev)
    print("smoke intensity", Intensity)
    print("Temperature", Temperature)

    dataset = pd.read_excel('shru/copd dataset.xlsx')
    dataset = dataset.values
    X = dataset[0:, 1:8]
    Y = dataset[0:, 8:9]
    from sklearn.model_selection import train_test_split  # splitting data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)
    from sklearn.ensemble import RandomForestClassifier  # using random forest algorithm for prdediction and accuracy
    model3 = RandomForestClassifier()
    model3.fit(X_train, Y_train)
    Pred = model3.predict(X_test)
    print(model3.predict([[Age, Gender, Weight, Lipcolour, Fev, Intensity, Temperature]]))
    r=model3.predict([[Age, Gender, Weight, Lipcolour, Fev, Intensity, Temperature]])
    treat=''
    if r == 'severe':
      treat = '1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators,bullectomy,3.lung  transplant'
    elif  r == 'mild':
      treat = '1.quit smcoking,pulmonary rehab,2.short-acting bronchodilators '
    else:
      treat = '1.quit smoking,pulmonary rehab,2.short-acting bronchodilators,long-acting bronchodilators'

    from sklearn.metrics import accuracy_score
    print('Random forest accuracy', accuracy_score(Pred, Y_test) * 100)
    CopdRegister(Name=Name, Aadhar=Aadhar, Email=Email, Age=Age, Gender=Gender, Weight=Weight, Lipcolour=Lipcolour, Fev=Fev, Intensity=Intensity, Temperature=Temperature, Med=treat, Pred =r).save()
    return render(request, 'lab/report.html',{'name': Name, 'aadhar': Aadhar,'email': Email, 'age':Age, 'gender': Gender, 'weight': Weight, 'lipcolour':Lipcolour,'fev':Fev, 'smoke':Intensity,'temperature':Temperature,'med':treat,'pred':r})
  else:
   return render(request, 'lab/copd.html')

def report(request):
    return render(request, 'lab/report.html')

def login(request):
  if request.method == 'POST':
    print("successfuly logged in")
    Name = request.POST['Name']
    Password = request.POST['Password']
    print("Name", Name)
    print("Password", Password)
    data = DoctorRegister.objects.get(Name=Name)
    print(data)
    if (data.Password == Password):
      return render(request, 'lab/copd.html')
    else:
      return render(request, 'lab/fail.html')
  else:
    return render(request, 'lab/login.html')

def fail(request):
  return render(request, 'lab/fail.html')
