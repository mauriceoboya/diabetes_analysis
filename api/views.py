from django.shortcuts import render
from .models import Diabetes
from .forms import DiabetesSerializer
#from . import logistic_model
import joblib
# Create your views here.
def home(request):
    pred=None
    diabetes=Diabetes.objects.all()
    model=joblib.load('api/logistic_model.joblib')
    if request.method=='POST':
        form=DiabetesSerializer(request.POST)
        if form.is_valid():
            field_list = [
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['bloodpressure'],
                form.cleaned_data['skinthickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['diabetespedigreefunction'],
                form.cleaned_data['age'],
                ]
            single_prediction = [int(value) if value.isdigit() else float(value) for value in field_list]
            single_input=[single_prediction]
            pred=model.predict(single_input)


    else:
        form=DiabetesSerializer()

    context={
        'diabetes':diabetes,
        'form':form,
        'logistic':model,
        'pred':pred
    }
    return render(request,'app/index.html',context)
