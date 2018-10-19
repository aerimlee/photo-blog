from django.shortcuts import render

def post_list(request):
    return render(request, 'photos/post_list.html', {})