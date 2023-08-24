import pandas as pd
import requests
import logging
import json
from io import StringIO
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST

from .models import Prediction

logger = logging.getLogger(__name__)

def homepage(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def index(request):
    latest_predictions_list = Prediction.objects.order_by("-created_at")[:5]
    template = loader.get_template("gex.html")
    context = {
        "latest_predictions_list": latest_predictions_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, prediction_id):
    response = "You're looking at the results of prediction %s."
    return HttpResponse(response % prediction_id)

def process_uploaded_file(data, index_col):
    content = data.read().decode('utf-8')
    csv = pd.read_csv(StringIO(content), index_col=index_col)
    return csv.to_json(orient='index')

@require_POST
def upload(request):
    if request.method == 'POST' and \
        request.FILES.get('gex') and \
            request.FILES.get('phenotype'):
        
        gex = process_uploaded_file(request.FILES['gex'], index_col="public_id")
        phenotype = process_uploaded_file(request.FILES['phenotype'], index_col="Sample SJ ID")

        # Define API endpoint URL
        api_endpoint = 'https://allium.serve.scilifelab.se/predict/'

        # Post JSON data to API endpoint
        response = requests.post(api_endpoint, json={'gex': gex, "pheno": phenotype})

        if response.status_code == 200: 
            response_json = json.loads(response.json())
            result = json.loads(response_json['result'])
            inference_df = pd.DataFrame.from_dict(result)
            return HttpResponse(inference_df.transpose().to_html(classes='table'))
        else:
            error = "Inference API returned error: %s."
            return HttpResponse(error % response.status_code)

        
