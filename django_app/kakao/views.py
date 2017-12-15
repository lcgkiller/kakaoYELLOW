from django.shortcuts import render

# Create your views here.
def keyboard(request):
    return JsonResponse({
       'type' : 'buttons',
       'buttons' : ['썸톡번역기','맛집 찾기','SomeTip', 'Q&A', '개발자의 한마디']
    })

