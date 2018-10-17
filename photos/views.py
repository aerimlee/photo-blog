from django.shortcuts import render
from .models import Photo


def detail(request, pk):
    photo = Photo.objects.get(pk=pk)

    messages = (
        '<p>{pk}ss</p>'.format(pk=photo.pk),
        '<p>ss{url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))