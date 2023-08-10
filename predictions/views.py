from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST

from .models import Prediction

def index(request):
    latest_predictions_list = Prediction.objects.order_by("-created_at")[:5]
    template = loader.get_template("predictions/index.html")
    context = {
        "latest_predictions_list": latest_predictions_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, prediction_id):
    response = "You're looking at the results of prediction %s."
    return HttpResponse(response % prediction_id)

@require_POST
def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_size = uploaded_file.size
        return HttpResponse(file_size)
