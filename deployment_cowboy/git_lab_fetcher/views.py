from django.http import HttpResponse
from django.shortcuts import render
import subprocess

# Create your views here.

def index(request):
    p = subprocess.run(['scripts/pull.sh'], capture_output=True, text=True)
    return HttpResponse(f"@fetch index: {p.stdout}")