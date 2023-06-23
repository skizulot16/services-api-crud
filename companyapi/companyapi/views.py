from django.http import HttpResponse,JsonResponse
def home(request):
    print('home page requested')
    people=['new','mew']
    return JsonResponse(people,safe=False)