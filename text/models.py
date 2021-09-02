from django.db import models

# Create your models here.

class SendEmail(models.Model):
	email = models.TextField(max_length = 500)

	def __str__(self):
		return self.email
