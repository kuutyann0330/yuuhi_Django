from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    # メソッドがGETになっているので画面を表示している
    def get(self, request):
        return render(request, "diary/index.html")
    
index = IndexView.as_view()