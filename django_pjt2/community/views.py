from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request,'community/review_list.html',context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review = form.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form':form
    }
    return render(request,'community/form.html',context)




def detail(request,id):
    # review = Review.objects.get(id=id)
    review = get_object_or_404(Review,id=id)
    context = {
        'review':review
    }
    return render(request,'community/review_detail.html',context)



def update(request,id):
    review = get_object_or_404(Review,id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', id)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form':form
    }
    return render(request, 'community/form.html',context)


@require_POST
def delete(request,id):
    review = get_object_or_404(Review,id=id)
    review.delete()
    return redirect('community:index')