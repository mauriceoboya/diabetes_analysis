from django.forms import ModelForm
from .models import Diabetes

class DiabetesSerializer(ModelForm):
    class Meta:
        model=Diabetes
        fields='__all__'

    def create(self,validated_data):
        return Diabetes.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.pregnance=validated_data.get('pregnancies',instance.pregnance)
        instance.Glucose=validated_data.get('Glucose',instance.Glucose)
        instance.Bloodpressure=validated_data.get('Bloodpressure',instance.Bloodpressure)
        instance.Skinthickness=validated_data.get('Skinthickness',instance.Skinthickness)
        instance.Insulin=validated_data.get('Insulin',instance.Insulin)
        instance.Bmi=validated_data.get('Bmi',instance.Bmi)
        instance.Diabetespedigreefunction=validated_data.get('Diabetespedigreefunction',instance.Diabetespedigreefunction)


        instance.save()
        return instance
    
