from django.shortcuts import redirect, render


def main(request):
    return render(request, "main.html", {})


def upload(request):
    return redirect(request, "post/upload.html")
