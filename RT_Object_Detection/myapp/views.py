from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse
import cv2
from .forms import Object_DataForm

# Create your views here.


def home (request):
    form = Object_DataForm
    if request.method == 'POST' :
        print(request.POST)
        form = Object_DataForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "home.html", context)

def stream():
    
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
    

# Nesne tespiti kodunu kullanarak görüntü akışı döndürün
def video_feed(request):
    return StreamingHttpResponse(stream(), content_type="multipart/x-mixed-replace; boundary=frame")