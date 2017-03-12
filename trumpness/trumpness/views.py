from django.http import JsonResponse
from ml.classifier import final_classify

def base_page(request):
    sentence = request.GET.get('sentence') # get the 'org_id' passed as get request
    result = ''
    if sentence:
        result = final_classify(sentence)

    return JsonResponse({'result':result})