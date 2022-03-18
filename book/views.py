from django.shortcuts import render, redirect
from . models import Review, Book 
from . forms import ReviewForm 

def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html',{'books':books})


def rev(request, id):
    obj = Book.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        user = request.POST.get('user')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(user=user, stars = stars,  comment=comment , book=obj)
        review.save()
        return redirect('success')
    
    form = ReviewForm()
    context = {
        'form':form,
        'books': obj
    }
    return render(request, 'book/rev.html',context)

def success(request, id):
    obj = Book.objects.get(id=id)
    return render(request, 'book/success.html',{'books':obj})
def success(request):
    return render(request, 'book/success.html')