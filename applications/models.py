from django.db import models
from django.contrib.auth.models import User

class InternshipApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    DOMAIN_CHOICES = [
        ('Software Development', 'Software Development'),
        ('Web Development', 'Web Development'),
        ('Data Analytics', 'Data Analytics'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Graphic Design', 'Graphic Design'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Networking', 'Networking'),
    ]
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    LEVEL_CHOICES = [
        ('HND 1', 'HND 1'), ('HND 2', 'HND 2'),
        ('Bachelor Year 1', 'Bachelor Year 1'),
        ('Bachelor Year 2', 'Bachelor Year 2'),
        ('Bachelor Year 3', 'Bachelor Year 3'),
        ('Master Year 1', 'Master Year 1'),
        ('Master Year 2', 'Master Year 2'),
        ('PhD', 'PhD'),
    ]

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    school_name = models.CharField(max_length=200)
    level_of_study = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    field_of_study = models.CharField(max_length=150)
    internship_domain = models.CharField(max_length=100, choices=DOMAIN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    cv = models.FileField(upload_to='documents/cv/')
    recommendation_letter = models.FileField(upload_to='documents/recommendations/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.internship_domain} ({self.status})"

    class Meta:
        ordering = ['-date_applied']