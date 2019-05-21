from django.shortcuts import render
from random import randint

def main_page(request):
    return render(request, 'pitstop_app/main_page.html', {})


def jopa(request):
    if request.method == 'POST':
        #print(request.POST)
        if validate(request.POST):
            prediction = get_prediction(request.POST)
            #print(prediction)
            return render(request, 'pitstop_app/results.html', prediction)
        else:
            error_info = {"ERROR" : "Invalid data"}
            return render(request, 'pitstop_app/404.html', error_info)
    else:
        return render(request, 'pitstop_app/404.html', {})


def error(request):
    return render(request, 'pitstop_app/404.html', {})


def get_prediction(data):
    value = 0.
    value += 3. if data["weather"] == "rainy" else 2.
    value += abs((float(data["temperature"]) - 21) / 2.)
    value += len(data["car-model"]) / 10.
    value += int(data["track-id"]) / 10.
    value += randint(1, 5)
    value = round(value)
    
    return {'prediction' : value}


def validate(data):
    validator = True
    try:
        float(data['temperature'])
        int(data['track-id'])
    except ValueError:
        validator = False
    return validator



