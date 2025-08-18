import os
import pickle
from django.conf import settings
from django.shortcuts import render
import numpy as np

model_path = os.path.join(settings.BASE_DIR, 'myapp', 'rf_model.pkl')

with open(model_path, "rb") as file:
    model = pickle.load(file)

def home(request):
    return render(request, "myapp/predict.html")

def predict_heart(request):
    if request.method == "POST":
        try:
            age = int(request.POST.get("age"))
            sex = int(request.POST.get("sex"))
            trestbps = int(request.POST.get("trestbps"))
            chol = int(request.POST.get("chol"))
            exercise = int(request.POST.get("exercise"))
            smoking = int(request.POST.get("smoking"))
            family_hd = int(request.POST.get("family_heart_disease"))
            diabetes = int(request.POST.get("diabetes"))
            bmi = float(request.POST.get("bmi"))
            high_bp = int(request.POST.get("high_blood_pressure"))
            low_hdl = int(request.POST.get("low_hdl_cholesterol"))
            high_ldl = int(request.POST.get("high_ldl_cholesterol"))
            alcohol = int(request.POST.get("alcohol_consumption"))
            stress = int(request.POST.get("stress_level"))
            sleep = float(request.POST.get("sleep_hours"))
            sugar = int(request.POST.get("sugar_consumption"))
            triglyceride = int(request.POST.get("triglyceride_level"))
            fasting_bs = int(request.POST.get("fasting_blood_sugar"))
            crp = float(request.POST.get("crp_level"))
            homocysteine = float(request.POST.get("homocysteine_level"))
            heart_status = int(request.POST.get("heart_disease_status"))

       # Prepare input for prediction
            input_data = np.array([[age, sex, trestbps, chol, exercise, smoking,
                                    family_hd, diabetes, bmi, high_bp, low_hdl,
                                    high_ldl, alcohol, stress, sleep, sugar,
                                    triglyceride, fasting_bs, crp, homocysteine,
                                    heart_status]])

            prediction = model.predict(input_data)[0]

            result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
            return render(request, "result.html", {"result": result})

        except Exception as e:
            return render(request, "result.html", {"result": f"Error: {str(e)}"})

    return render(request, "predict.html")