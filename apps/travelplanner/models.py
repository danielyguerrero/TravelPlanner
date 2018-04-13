from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class TripManager(models.Manager):
	def validate(self, form_data):
		errors = []
		destination = form_data['destination']
		description = form_data['description']
		travel_date_from = form_data['travel_date_from']
		travel_date_to = form_data['travel_date_to']

		if len(destination) == 0:
			errors.append("Please type a Destination!")
		if len(description) == 0:
			errors.append("Please type a Description!")
		if len(travel_date_from) == 0:
			errors.append("Please enter in a Date From!")
		if len(travel_date_to) == 0:
			errors.append("Please enter in a Date To!")

		return errors

	def add_trip(self, form_data, user_id):
		user = User.objects.get(id=user_id)
		trip = self.create(
		destination = form_data['destination'],
		description = form_data['description'],
		travel_date_from = form_data['travel_date_from'],
		travel_date_to = form_data['travel_date_to'],
		added_by = user
		)
		return trip

class Trip(models.Model):
	destination = models.CharField(max_length=45)
	description = models.CharField(max_length=45)
	travel_date_from = models.DateField(null=True, blank=True)
	travel_date_to = models.DateField(null=True, blank=True)
	added_by = models.ForeignKey(User, related_name="added_trips")
	joined_by = models.ManyToManyField(User, related_name="joined")
	objects = TripManager()

	def __unicode__(self):
		return "id: {}, destination: {}, description: {}, travel_date_from: {}, travel_date_to: {}, added_by: {}".format(self.id, self.destination, self.description, self.travel_date_from, self.travel_date_to, self.added_by)