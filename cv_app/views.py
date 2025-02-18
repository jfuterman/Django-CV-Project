from django.shortcuts import render

# Create your views here.

# cv_app/views.py
from django.shortcuts import render

# View function for rendering CV
def cv_view(request):
    return render(request, 'cv_app/cv.html')

