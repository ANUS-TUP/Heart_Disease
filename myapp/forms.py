from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[(0, 'Female'), (1, 'Male')])
    cp = forms.IntegerField(label="Chest Pain Type (0-3)")
    trestbps = forms.IntegerField(label="Resting Blood Pressure")
    chol = forms.IntegerField(label="Serum Cholestoral (mg/dl)")
    fbs = forms.ChoiceField(choices=[(0, 'False'), (1, 'True')], label="Fasting Blood Sugar > 120 mg/dl")
    restecg = forms.IntegerField(label="Resting ECG results (0-2)")
    thalach = forms.IntegerField(label="Max Heart Rate Achieved")
    exang = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Exercise Induced Angina")
    oldpeak = forms.FloatField(label="ST depression")
    slope = forms.IntegerField(label="Slope of ST segment (0-2)")
    ca = forms.IntegerField(label="Number of major vessels (0-3)")
    thal = forms.IntegerField(label="Thalassemia (0-3)")
