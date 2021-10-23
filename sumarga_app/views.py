from django.shortcuts import render
from .models import post, images,Feature,picks,logo,news,contacts,newrelease,status

# Create your views here.
def index(request):
    stat=status.objects.all()
    posts = post.objects.all()
    bg_img = images.objects.all()
    book_details = Feature.objects.all()
    newrel=newrelease.objects.all()
    pick=picks.objects.all()
    logos=logo.objects.all()
    new=news.objects.all()
    cont = contacts.objects.all()
    return render(request,'index.html',{'post':posts, 'bgimage':bg_img,'status':stat, 'features':book_details,'newrelease':newrel, 'picks':pick,'logo':logos,'news':new,'contact':cont})

def about(request):
    bg_img=images.about_us_img
    return render(request,'about.html',{'bg_img': bg_img})

def contact(request):
    return render(request,'contact.html')

def article(request,myid):
    article=post.objects.filter(id=myid)

    return render(request,'article.html',{'post':article[0]})

def featured_book(request):
    book_details=Feature.objects.all()
    return render(request,'index.html',{'features':book_details})
