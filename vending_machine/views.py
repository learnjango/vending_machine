from django.shortcuts import render
  
def sandwiches(request):
    return render(request, "sandwiches.html")
def salads(request):
    return render(request, 'salads.html')
def snacks(request):
    return render(request, 'snacks.html')
def drinks(request):
    return render(request, 'drinks.html')
def sweets(request):
    return render(request, 'sweets.html')