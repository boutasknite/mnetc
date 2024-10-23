from django.db import models


class Thrust(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='thrusts/')

    def __str__(self):
        return self.Name


class Member(models.Model):
    CHOICES = (
        ('governance', 'governance'),
        ('management', 'management'),
        ('member', 'member'),
    )
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200, blank=True, null=True)
    Phone_Number = models.CharField(max_length=100,blank=True, null=True)
    Affiliation = models.CharField(max_length=100)
    Research_Area = models.CharField(max_length=100, blank=True, null=True)
    Position = models.CharField(max_length=100, blank=True, null=True)
    CV = models.FileField(null=True, blank=True, upload_to='CV/')
    Motivation = models.TextField(default="", blank=True)
    Contribution = models.TextField(default="", blank=True)
    References = models.TextField(default="", blank=True)
    Biography = models.TextField(default="")
    Image = models.ImageField(upload_to='Members_Photos/', blank=True,  default='Members_Photos/default.jpg')
    Role = models.CharField(max_length=20, choices=CHOICES, default="member")
    User_Id = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.First_Name} {self.Second_Name}"


class Application(models.Model):
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=100)
    Affiliation = models.CharField(max_length=100)
    Research_Area = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    CV = models.FileField(upload_to='CV/')
    Image = models.ImageField(upload_to='Members_Photos/', default='Members_Photos/default.jpg')
    Biography = models.TextField(default="")
    Motivation = models.TextField(default="")
    Contribution = models.TextField(default="")
    References = models.TextField(default="")
    Status = models.CharField(max_length=100, default="In Process")

    def __str__(self):
        if f"{self.First_Name} {self.Second_Name}" != "":
            return f"{self.First_Name} {self.Second_Name}"
        return "Not defined"


class NewsEvent(models.Model):
    CHOICES = (
        ('News', 'News'),
        ('Event', 'Event'),
    )
    Type = models.CharField(max_length=20, choices=CHOICES, default="News")
    Title = models.CharField(max_length=300, default="")
    Date = models.DateField(blank=True, null=True)
    Place = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to='NewsEvent/', default='NewsEvent/default.png')

    def __str__(self):
        return self.Title


class NewsEventImage(models.Model):
    NewsEvent = models.ForeignKey(NewsEvent, related_name='images', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='NewsEvent/')

    def __str__(self):
        return f"Image for {self.NewsEvent.Title}"


class NewsEventParagraph(models.Model):
    NewsEvent = models.ForeignKey(NewsEvent, related_name='paragraphs', on_delete=models.CASCADE)
    Paragraph = models.TextField(default="")
    Title = models.CharField(max_length=300, default="")

    def __str__(self):
        return f"Image for {self.NewsEvent.Title}"


class Publication_Elearning(models.Model):
    CHOICES = (
        ('E-learning', 'E-learning'),
        ('Publication', 'Publication'),
    )
    Type = models.CharField(max_length=20, choices=CHOICES, default="E-learning")
    Title = models.CharField(max_length=300, default="")
    Date = models.DateField()
    File = models.FileField(upload_to='Publication_Elearning/')

    def __str__(self):
        return self.Title


class Seminars_Webinars_Podcast(models.Model):
    CHOICES = (
        ('Seminars & Webinars', 'Seminars & Webinars'),
        ('Podcast', 'Podcast'),
    )
    Type = models.CharField(max_length=20, choices=CHOICES, default="Seminars & Webinars")
    Title = models.CharField(max_length=300, default="")
    Date = models.DateField()
    Link = models.CharField(max_length=500)

    def __str__(self):
        return self.Title


class Pooling_Equipment(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Pooling Equipment/',  default='Pooling Equipment/default.png', blank=True, null=True)
    Description = models.TextField(default="")

    def __str__(self):
        return self.Name


