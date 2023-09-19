import json

from django.shortcuts import render
import requests

from modules_app.forms import UploadJSONForm
from config.settings import BACKEND_URL


def upload_json(request):
    if request.method == 'POST':
        form = UploadJSONForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            data = json.load(json_file)

            # Этот запрос должен уходить с фронтенда, но я поковырялся в JS и
            # получилось так себе, поэтому обращаюсь к апи методу тут =)
            response = requests.post(
                url=BACKEND_URL + 'json/',
                json=data,
            )
            context_data = {
                'title': 'Успех',
                'result': response.text,
            }
            if response.status_code != 200:
                context_data['title'] = 'Ошибка'

            return render(request,
                          template_name='after_upload.html',
                          context=context_data)

    else:
        form = UploadJSONForm()

    return render(request,
                  template_name='upload_json.html',
                  context={'title': 'Upload JSON File', 'form': form})
