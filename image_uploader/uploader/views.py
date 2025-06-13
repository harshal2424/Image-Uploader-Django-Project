from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    images = Image.objects.all()
    return render(request, 'uploader/image_upload.html', {'form': form, 'images': images})

@csrf_exempt
def clear_history(request):
    if request.method == 'POST':
        Image.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)




























