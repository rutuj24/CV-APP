from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def index(request):
	return render(request, 'index.html', {})

def screen(request):
	return render(request, 'screen.html', {})

def screen_result(request):
	resume = request.GET['res'].strip()
	requirement = request.GET['des'].strip()
	resume = resume.lower()
	requirement = requirement.lower()
	text = [resume, requirement]
	cv = CountVectorizer()
	count_matrix = cv.fit_transform(text)
	percentage = cosine_similarity(count_matrix)[0][1]*100
	if percentage > 20 :
		result = 'A'
	elif percentage > 15 :
		result = 'B'
	elif percentage > 10 :
		result = 'C'
	else :
		result = 'D'
		
	return render(request, 'screener.html', {'sol':result, 'res':resume, 'req':requirement})