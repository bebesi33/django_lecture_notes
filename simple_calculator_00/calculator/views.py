from django.shortcuts import render

# Create your views here.
def calculator_home(request):
    return render(request, 'main.html')


# Approach 1: separate page
def addition(request):
    value_1 = request.GET['num1']
    value_2 = request.GET['num2']
    try:
        value_1_int = int(value_1)
    except ValueError:
        value_1_int = 0
    try:
        value_2_int = int(value_2)
    except ValueError:
        value_2_int = 0

    res = value_1_int + value_2_int
    return render(request, 'result.html', {'calc_result': res})
