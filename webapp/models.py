from django.db import models

class Track(models.Model):
	ArtistId = models.IntegerField()
	ArtistName = models.CharField(max_length=30)
	TrackName = models.CharField(max_length=100)
	Country = models.CharField(max_length=30)
	GenreName = models.CharField(max_length=30)
	ReleaseDate= models.DateTimeField(auto_now=False, auto_now_add=False)
	
	def __str__(self):
		return self.TrackName