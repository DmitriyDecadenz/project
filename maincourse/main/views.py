from django.shortcuts import render
def index(request):
	data = {
		'title':'Главная страница',
		'values':['some', 'hello','wss'],
		'obj':{
			'car':'Bmw',
			"age":18,
			'hobby':'Footbal',

		}
	}
	return render(request, 'main/index.html', data)

def about(request):
	return render(request, 'main/about.html')
