from django.shortcuts import render
import random
import markdown2
import string
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries() })

def title(request,title):
    return render(request, "encyclopedia/view.html",{"entries": util.list_entries(), "title_id":title, "content":markdown2.markdown(util.get_entry(title))} )

def Random(request):
    return render(request,"encyclopedia/view.html",{"title_id":random.choice(util.list_entries()),"content":markdown2.markdown(util.get_entry(random.choice(util.list_entries())))})

def create(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
            return HttpResponseRedirect("/wiki")

        
    return render(request, "encyclopedia/create.html",{"form":NewTaskForm()})



def search(request):
    if request.method == "POST":
        query = request.POST['q']
        entries = util.list_entries()
        l= list()
        for entry in entries:
            if query == entry:
                return render(request, "encyclopedia/view.html",{"entries": util.list_entries(), "title_id":query, "content":markdown2.markdown(util.get_entry(query))} )
            elif query.lower() in entry.lower():
                l.append(entry)
                return render(request,"encyclopedia/search.html",{"list_items":l})
            
            ## incomplete
           
def edit(request):
    if request.method == "POST":
        title1 = request.POST['entry_title']
        content = util.get_entry(title1)
        return render(request, "encyclopedia/edit.html",{"title":title1, "content":content})

def save_edit(request):
    if request.method == "POST":
        title= request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title,content)
    return render(request, "encyclopedia/view.html",{"entries": util.list_entries(), "title_id":title, "content":markdown2.markdown(util.get_entry(title))} )


class NewTaskForm(forms.Form):
    title= forms.CharField(label="Title")
    content= forms.CharField(widget=forms.Textarea(attrs={'name':'content', 'rows':'3', 'cols':'5'}))



