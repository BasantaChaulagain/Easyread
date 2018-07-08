from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Matchtable(models.Model):
    SEMESTER_CHOICES = (
        (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'),
        (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth')
    )
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester = models. IntegerField(choices=SEMESTER_CHOICES, default=1)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    
    
class Book(models.Model):
    CONDITION_CHOICES = (
        ('GOOD', 'Good'), 
        ('BAD', 'Bad'), 
        ('FAIR', 'Fair'),
    )
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    matchtable = models.ForeignKey(Matchtable, on_delete=models.CASCADE, default='NULL')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default='NULL')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='NULL')
    condition = models. CharField(max_length=10, choices=CONDITION_CHOICES, default='GOOD')
    
    def __str__(self):
        return self.title