from django.shortcuts import HttpResponse, render
import subprocess
# Create your views here.

test = [

]


def build_jar(request):
    subprocess.Popen(["python", "gitlab_modules/artifact_downloader.py"])
    test.append({
        'author':'build complete',
    })
    return home(request)

def run_test(request):
    test.append({
        'author': 'test complete'
    })
    return home(request)

def clear_console_output(request):
    tests = []
    return home(request)

def home(request):
        
    context = {
        'posts': test,
    }
    return render(request, 'controller/home.html', context)

def about(request):
    return render(request, 'controller/about.html') 