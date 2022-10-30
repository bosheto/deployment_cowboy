import imp
from django.http import HttpResponse
from django.shortcuts import render
import subprocess
from gitlab_modules import artifact_downloader

# Create your views here.

def index(request):
    # p = subprocess.run(['scripts/pull.sh'], capture_output=True, text=True)
    artifact_downloader.compile()
    return HttpResponse(f"Job started`")