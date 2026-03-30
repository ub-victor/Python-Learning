from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # For now (no database yet)
        print("Email:", email)
        print("Password:", password)

        # Later we will authenticate user
        return redirect('login')  # temporary

    return render(request, 'accounts/login.html')