from django.db import models
from sorl.thumbnail import ImageField

class Foto(models.Model):
	TATUAZH_TYPE = (		
		('Br', 'Brovi'),
		('Gu', 'Gubi'),
		('Gl', 'Glaza'),
	)
	title = models.CharField(max_length=300)
	comment_first = models.CharField(max_length=300)
	comment_second = models.CharField(max_length=300)
	type = models.CharField(max_length=2, default='Br', choices=TATUAZH_TYPE)
	image_location = models.ImageField(upload_to="images/", help_text='Please upload your photos here')
	date = models.DateTimeField(auto_now_add=True)