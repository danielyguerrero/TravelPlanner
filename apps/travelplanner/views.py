from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Trip


# =================================================
# 						HELPERS
# =================================================
def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def user(request, id):
	context={
		'user': current_user(request),
	}
	return render(request, 'travelplanner/index.html')

# ==============================================================
# 						RENDER
# ==============================================================

def index(request):
	#CHECK IS THERE IS A USER_ID IN SESSION
	if 'user_id' not in request.session:

	# RETURN REDIRECT TO THE INDEX.HTML IF USER_ID NOT IN SESSION
	    return redirect('/')

	#ELSE SET VARIABLE "USER" TO EQUAL CURRENT_USER // FROM CURRENT_USER HELPER METHOD ABOVE
	user = current_user(request)

	#PASS VARIABLES THROUGH CONTEXT
	context = {
		'user': user,
		'joined_trips': user.joined.all(),
		'other_trips': Trip.objects.exclude(joined_by = user)
	}
	return render(request, 'travelplanner/index.html', context)

def travels(request):
	if 'user_id' not in request.session:
		return redirect('/')

	user = current_user(request)
	context = {
		'user': user,
		'joined_trips': user.joined.all(),
		'other_trips': Trip.objects.exclude(joined_by = user)
	}
	return render(request, 'travelplanner/index.html', context)

# =================================================
#                       PROCESS
# =================================================
def show_trip(request, trip_id):
	trip = Trip.objects.get(id = trip_id)
	context = {
		'users': trip.joined_by.all(),
		'trip': trip
	}
	return render(request, 'travelplanner/trip.html', context)

def add_trip(request):
	if request.method == "POST":
		errors = Trip.objects.validate(request.POST)

		if not errors:
			trip = Trip.objects.add_trip(request.POST, request.session["user_id"])
			trip.joined_by.add(current_user(request))
			print trip
			return redirect(reverse('dashboard'))

		flash_errors(request, errors)
		return redirect(reverse('add_trip'))
	else:
		return render(request, 'travelplanner/add.html')

def join_trip(request, trip_id):
	trip = Trip.objects.get(id=trip_id)
	trip.joined_by.add(current_user(request))
	return redirect(reverse('dashboard'))