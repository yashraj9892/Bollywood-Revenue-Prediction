from django.shortcuts import render,redirect
from predict.forms import Myform
from . import preprocess
from . import model_loader
from . import model_loader2
# Create your views here.

def index(request):
    if request.method == "POST":
        movie_form = Myform(data=request.POST)
        if movie_form.is_valid():
            form = movie_form.save(commit=False)
            print(form.movie_name,form.genre,form.star_cast,form.director,form.year,form.budget,form.runtime)
            answer = preprocess.classify(form.movie_name,form.genre,form.star_cast,form.director,form.year,form.budget,form.runtime)
            print(answer)
            revenue =  preprocess.revenue(form.budget,answer[1])
            revenue= round(revenue[0],2)
            
            return render(request,'predict/verdict.html',{'movie_name':form.movie_name,'Verdict':answer[0],'Revenue':revenue})
        else:
            print(movie_form.errors)
    else:
        movie_form = Myform()
    return render(request,'predict/movie.html',{'movie_form':movie_form})

