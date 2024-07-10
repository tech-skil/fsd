from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def chatPage(request, *args, **kwargs):
    context = {}
    return render(request, "chat/chatPage.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("chat-page")
    return render(request, "chat/LoginPage.html")