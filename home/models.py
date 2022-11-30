from django.db import models
from django.utils import timezone
VIDEO_CATEGORY_CHOICES = (
    ("Sports", "Sports"),
    ("Movies", "Movies"),
    ("Webseries", "Webseries"),
    ("Kids", "Kids"),
)
FREE_OR_PREMIUM_CHOICE = (
    ('free','free'),
    ('premium','premium'),
)
class Genre(models.Model):
    genre_type=models.CharField(max_length=20)
    
    def __str__(self):
        return self.genre_type

class Video(models.Model):
    video_clip = models.FileField(upload_to='videos/')
    director = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,choices=VIDEO_CATEGORY_CHOICES)
    slug = models.SlugField(null=True,blank=True)
    content_language=models.CharField(max_length=50)
    summary = models.TextField()
    uploaded = models.DateTimeField(default=timezone.localtime().now)
    free_or_premium = models.CharField(max_length=20,choices=FREE_OR_PREMIUM_CHOICE)
    genre = models.ManyToManyField(Genre, related_name="videos")

    def __str__(self):
        return self.slug




    #  imagef = base64.b64encode(imagefile.read())
    #     imagedecoded=base64.b64decode(imagef)  this is used to extract meta data of any file object
    #     imagedecoded=BytesIO(imagedecoded)  type, length, quality
    #     metadata = exifread.process_file(imagedecoded)