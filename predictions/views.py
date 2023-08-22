import pandas as pd
import requests
import logging
from io import StringIO
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST

from .models import Prediction

logger = logging.getLogger(__name__)

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

        # Read CSV and convert to JSON
        # TODO: validation
        uploaded_content = uploaded_file.read().decode('utf-8')
        csv_data = pd.read_csv(StringIO(uploaded_content), index_col="public_id")
        pheno = pd.read_csv('/home/mariya/Development/allium/data/test_data/gex/pheno.csv', index_col="Sample SJ ID")

        # Define API endpoint URL
        api_endpoint = 'https://allium.serve.scilifelab.se/predict/'

        # Post JSON data to API endpoint
        response = requests.post(api_endpoint, json={'gex': csv_data.to_json(orient='index'), "pheno": pheno.to_json(orient='index')})

        logger.info('API Response: %s', response.content)

        
        #if response.status_code == 201:  # Assuming API responds with 201 Created
        #    return JsonResponse({'message': 'CSV data converted and posted successfully'}, status=201)
        #else:
        #    return JsonResponse({'error': 'Failed to post JSON data to the API'}, status=response.status_code)

        return HttpResponse(response.status_code)
