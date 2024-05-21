from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import Dogs
from django.utils import timezone  

# Create your views here.

def add_dogs(request):
    if request.method == 'POST':
        name = request.POST['dogName']
        breed = request.POST['dogBreed']
        image = request.FILES['dogImage']
        dog = Dogs(name=name, breed=breed, image=image)
        dog.save()
        return HttpResponse("Dog saved successfully 😁")
    return render(request, 'add_dogs.html')

def view_dogs(request):
    dogs = Dogs.objects.all()
    return render(request, 'view_dogs.html', {'dogs':dogs})
    

def master_dog(request, dog_id):
    dog = get_object_or_404(Dogs, pk=dog_id)
    return render(request, 'master_dog.html', {'dog':dog})

def delete_dogs(request, dog_id):
    Dogs.objects.filter(pk=dog_id).delete()
    #return HttpResponse("Deleted dog successfully 😒")
    return redirect('view_dogs')  

# Import the timezone module

def dog_update(request, dog_id):
    dog = get_object_or_404(Dogs, pk=dog_id)

    if request.method == 'POST':
        # Retrieve form data
        name = request.POST['name']
        age = request.POST['age']
        breed = request.POST['breed']
        dog_image = request.FILES['image'] if 'image' in request.FILES else None  # Handle if no image is provided

        # Update dog model fields
        dog.name = name
        dog.age = age
        dog.breed = breed
        
        if dog_image:
            dog.image = dog_image
       
        dog.updated_at = timezone.now()

        # Save the changes
        dog.save()
       
    return render(request, 'master_dog.html', {'dog':dog})
