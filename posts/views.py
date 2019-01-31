from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Post

#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def post_list(request):
#    return render(request, 'posts/post_list.html', {})

def index(request):
  # return HttpResponse("Hello World! このページは投稿のインデックスです。")
  posts = Post.objects.order_by('-published')
  return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request,post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'posts/post_detail.html', {'post' :post})

#class IndexView(generic.ListView):
#	"""docstring for IndexView"""
#	template_name = 'posts/index.html'
#	context_object_name = 'latest_post_list'

#	def get_queryset(self):
#		#return Post.objects.order_by('-pub_date')[:]
#		return Post.objects.order_by('-published')[:5]

#class DetailView(generic.DetailView):
#	"""docstring for DetailView"""
#	model = Post
#	template_name = 'posts/detail.html'
