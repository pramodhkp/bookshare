# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
# from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from submitbook.models import Feed
import logging

import datetime

def submit(request):
    return render(request, 'submit.html')

def feed(request):
	logging_format = (
	    '%(asctime)s - %(levelname)s - '
	    '%(filename)s:%(lineno)d - %(message)s'
	    )
	logging.basicConfig(level=logging.DEBUG, format=logging_format)
	error= False
	if not request.POST['update'] == "" and request.POST['update'] is not None:
		logging.debug(request.POST)
		user = request.user
		update = request.POST["update"]
		date = datetime.datetime.now()
		feedsave = Feed(username = user, date = date, message = update)
		feedsave.save()
		feed = Feed.objects.order_by('-date')
		# feeds_list = [feed.message for feed in feeds]
		return render(request, 'results.html', {"feed":feed, "user":user, "date":date, "message":update })
	else:
		error = True 
		feed = Feed.objects.order_by('-date')
		return render(request, 'results.html', {"error":error, "feed":feed})
	
		
	

	



# def myview(request):
#    posts = Post.objects.all()
#    post_body_list = [post.body for post in posts]
#    return render_to_response('mytemplate.html',
#                              {'post_list': post_body_list})


# def results(request):
# 	error = False
# 	if 'q' in request.GET:
# 	    q = request.GET['q']
# 	    tq = "https://www.googleapis.com/books/v1/volumes?q="+q+"&callback=handleResponse"
# 	    if not q:
# 	        error = True
# 	    else:
# 	    	#books = Book.objects.filter(title__icontains=q)
# 	        return render_to_response('results.html',
# 	                {'tq': tq})
# 	return render_to_response('submit.html',
# 	        {'error': error})

