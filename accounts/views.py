from django.shortcuts import render

# Create your views here.
def account_main(request):
	return render(request,'accounts/home.html')