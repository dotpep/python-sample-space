from django.http import HttpResponse

numbers = [x for x in range(1, 7)]

def display_even_numbers(request):
    response = ""
    for i in numbers:
        remainder = i % 2
        if remainder == 0:
            response += str(i) + "<br/>"
    return HttpResponse(response)

def display_odd_numbers(request):
    response = ""
    for i in numbers:
        if i % 2 == 1:
            response += str(i) + "<br/>"
    return HttpResponse(response)