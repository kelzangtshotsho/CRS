from django.shortcuts import render, redirect
from .models import Photo, Rent
# Create your views here.
def index(request):
	# categories = Category.objects.all()
	photos = Photo.objects.all()
	context = {'photos': photos}
	return render(request, "index.html", context)

	
def viewPhoto(request, pk):
	photo = Photo.objects.get(id=pk)
	return render(request, 'photo.html', {'photo': photo})

def addPhoto(request):

	if request.method == 'POST':
		data = request.POST
		Image = request.FILES.get('Image')

		photo = Photo.objects.create(
			Image = Image,
			CID = data['CID'],
			Phone = data['Phone'],
			Account = data['Account'],
			Type = data['Type'],
			Name = data['Name'],
			Capacity = data['Capacity'],
			Rate = data['Rate'],
			PickLocation = data['PickLocation'],
			)
		return redirect('index')

		# print('data:', data)
		# print('Image:', Image)
		
	return render(request, 'add.html')

def rentcar(request):
	if request.method == 'POST':
		data = request.POST
		rent = Rent.objects.create(
			Owner = data['Owner'],
			CID = data['CID'],
			PickDate = data['PickDate'],
			DropDate = data['DropDate'],
			PickLocation = data['PickLocation'],
			DropLocation = data['DropLocation'],
			)

		# return redirect('photo')

	return render(request, 'rent.html')

def comfirm(request):
	return render(request, 'comfirm.html')





