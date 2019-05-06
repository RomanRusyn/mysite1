from django.shortcuts import render


# Create your views here.
def index12(request):
    # return render(request, 'mainApp/homepage.html')
    return render(request, 'C:\\Users\\roman\\mysite\\mainApp\\templates\\mainApp\\homepage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values ': ['Якщо у вас є запитання, то задавайте їх по телефону', '+3-800-456-23-45']})
