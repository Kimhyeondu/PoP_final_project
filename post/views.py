from django.shortcuts import render, redirect
def main(request):
    return render(request, 'main.html',{})


def upload(request):
    return redirect(request, "post/upload.html")