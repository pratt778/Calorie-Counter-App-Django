from django.shortcuts import render
import requests
import json

# Create your views here.
#T1uN7OALfaESgxfLpV5pkQ==0vj9zYPV6EsMfdYR
def home(request):
    if request.method =='GET':
        query = request.GET.get('food')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'T1uN7OALfaESgxfLpV5pkQ==0vj9zYPV6EsMfdYR'})
        if response.status_code == requests.codes.ok:
            res = json.loads(response.content)
            print(response.content)
            data = {'res':res}
            return render(request,'home.html',data) 
        else:
            print("Error:", response.status_code, response.text)
    return render(request,'home.html')