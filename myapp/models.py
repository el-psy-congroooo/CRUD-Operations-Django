from django.db import models

Choices = [('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'),
           ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th'), ('11', '11th'), ('12', '12th')]


class PersonalInformation(models.Model):
    """
    This model is to store the personal information of the students. 
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    std = models.CharField(max_length=100, choices=Choices)
    roll = models.IntegerField()
    sub = models.TextField()

    def __str__(self):
        return self.name
