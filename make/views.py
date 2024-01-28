import io
from django.http import FileResponse 
from django.shortcuts import render 
import pyqrcode 

# Create your views here.

def index(request): 
    return(render(request, "make/index.html")) 

def make(request, url): 
    url = url.replace("^", "/") 
    if (url[0:7] != "http://" or url[0:8] != "https://"): 
        url = "https://" + url 
    qr_code = pyqrcode.create(url)
    b = io.BytesIO() 
    qr_code.png(b, scale=8) 
    b.seek(0)  
    response = FileResponse(b, content_type="image/png") 
    response["Content-Disposition"] = f"inline; filename={url}.png" 
    return response 

def get(request, info): 
    qr_code = pyqrcode.create(info)
    b = io.BytesIO() 
    qr_code.png(b, scale=8) 
    b.seek(0)  
    response = FileResponse(b, content_type="image/png") 
    response["Content-Disposition"] = f"inline; filename={info}.png" 
    return response 
