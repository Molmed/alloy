from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the predictions index.")

def detail(request, prediction_id):
    response = "You're looking at the results of prediction %s."
    return HttpResponse(response % prediction_id)
