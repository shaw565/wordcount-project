from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')

def count(request):
	var1=request.GET['fulltext']
	wordtxt= var1.split()

	dict1={}

	for word in wordtxt:
		if word in dict1:
			dict1[word] +=1

		else:
			dict1[word] =1

	all_values = dict1.values()
	max_value = max(all_values)

	sortedwords = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)

	return render(request,'count.html',{'fulltext':var1,'countofwords':len(wordtxt),'dict1':dict1.items(),'max1':max_value,'sortedwords':sortedwords})


def about(request):
	return render(request,'about.html')