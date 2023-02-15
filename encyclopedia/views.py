from markdown2 import Markdown
from django.shortcuts import render
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def markdownconv(foo):
    markdowner = Markdown()
    check = util.get_entry(foo)
    if check:
        return markdowner.convert(check)
    else:
        return None    

def entry(request, strname):
    
        convertedname = markdownconv(strname)
        if not convertedname:
                return render(request, "encyclopedia/ErrorPage.html", {
                "title": "Wrong Entry name"
        })
        else:
            return render(request, "encyclopedia/markdownconverter.html", {
            "title": strname,
            "mdconverted": convertedname
        })


def query(request):
    if request.method == "POST":
        postname = request.POST['q']
        convpostname = markdownconv(postname)
        if convpostname:
            return render(request, "encyclopedia/markdownconverter.html", {
                "title": postname,
                "mdconverted": convpostname})
        else:
            ListOfEntries = util.list_entries()
            FoundEntries = []
            for entry in ListOfEntries:
                if postname.upper() in entry.upper():
                    FoundEntries.append(entry)
            return render(request, "encyclopedia/SearchEntry.html", {
                    "FoundEntries": FoundEntries
                    })

def NewPage(request):

    return render(request, "encyclopedia/NewPage.html")


def AddNewPage(request):
    if request.method == "POST":
        NewEntryName = request.POST['t']
        NewEntryMD = request.POST['a']
        AllEntries = util.list_entries()
        if NewEntryName in AllEntries:
            return render(request, "encyclopedia/ErrorPage.html",
                    {"title": "Entry with this name already exists"})
        else:
                util.save_entry(NewEntryName, NewEntryMD)
                ConvertedEntry = markdownconv(NewEntryName)
                return render(request, "encyclopedia/NewlyAddedPage.html", { 
                    "title": NewEntryName, 
                    "mdconverted": ConvertedEntry })

def EditPage(request):
    if request.method == "POST":
        EntryName = request.POST['ET']
        EntryContent = util.get_entry(EntryName)


    return render(request, "encyclopedia/EditPage.html", {
        "ET": EntryName,
        "MDContent": EntryContent
    })

def EditedPage(request):
    if request.method == "POST":
        NewEntryName = request.POST['NewName']
        NewMDContent = request.POST['NewMDContent']
        util.save_entry(NewEntryName, NewMDContent)
        ConvNewEntry = markdownconv(NewEntryName)
    return render(request, "encyclopedia/markdownconverter.html", {
        "title": NewEntryName,
        "mdconverted": ConvNewEntry
    })

def RandomPicker(request):
    WholeList = util.list_entries()
    PopulatedList = []
    for entry in WholeList:
        PopulatedList.append(entry)
    RandomPick = random.choice(PopulatedList)
    ConvRandomPick = markdownconv(RandomPick)


    return render(request, "encyclopedia/markdownconverter.html", {
        "title": RandomPick,
        "mdconverted": ConvRandomPick
    })