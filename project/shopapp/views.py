# from itertools import product
# from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
# def index(request):
# 	return render(request, 'index.html')

def allProduct(request,c_slug=None):
	c_page=None
	products_list=None
	if c_slug!=None:
		c_page=get_object_or_404(Category,slug=c_slug)
		products_list=Product.objects.all().filter(category=c_page,available=True)
	else:
		products_list=Product.objects.all().filter(available=True)
	pagenator=Paginator(products_list,6)
	try:
		page=int(request.GET.get('page','1'))
	except:
		page=1
	try:
		products=pagenator.page(page)
	except   (EmptyPage,InvalidPage):
		products=pagenator.page(pagenator.num_pages)

	print(products.object_list[0].image.url)
	
	return render(request,"category.html",{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
	try:
		product=Product.objects.get(category__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'product.html',{'product':product})