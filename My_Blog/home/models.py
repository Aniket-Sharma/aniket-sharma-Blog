from django.db import models
#
# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
#
# class Post(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250,
#                             unique_for_date='publish')
#     author = models.ForeignKey(User,
#                                related_name='blog_posts',
#                                on_delete='CASCADE')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10,
#                               choices=STATUS_CHOICES,
#                               default='draft')
#
#     def __str__(self):
#         return self.title

# About Section

class Experience(models.Model):
    PRIVACY_OPTIONS = (
        ('public', 'Public'),
        ('mid', 'Email-Identification-Required'),
        ('high', 'Admin-Permission-Required'),
        ('private', 'Private'),
    )
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=500)
    summary = models.TextField()
    story = models.TextField()
    bg_img = models.ImageField(upload_to='content/media/Images/Experience/bg_imgs/', null=True, blank=True)
    img = models.ImageField(upload_to='content/media/Images/Experience/', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    privacy = models.CharField(max_length=100, choices=PRIVACY_OPTIONS, default='public')
    status = models.CharField(max_length=100, choices=STATUS, default='published')

    def __str__(self):
        return self.title

class Personal_Detail(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    position = models.SmallIntegerField()

    def __str__(self):
        return self.title

# About Section Ends here

# Interests
class Interest(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    bg_img = models.ImageField(upload_to='content/media/Images/Interests/')
    link = models.URLField(verbose_name='URL to the Interests Page')

    def __str__(self):
        return self.title

# Projects
class Project(models.Model):
    category = models.ForeignKey(Interest, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    summary = models.TextField()

    upload_url = 'contents/media/Projects/'
    upload_url += str(title)
    upload_url += '/'

    image = models.ImageField(upload_to=upload_url)
    ved = models.FileField(upload_to=upload_url)
    other_stuff = models.FileField(upload_to=upload_url)

    blog = models.URLField()

    def __str__(self):
        return self.title

# Project Blog
class Project_Blog(models.Model):
    blog = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    title = Project.title
    start_summary = models.TextField()
    end_summary = models.TextField()

    def __str__(self):
        return self.title

# Project Blog Posts
class Project_Blog_Post(models.Model):
    blog = models.ForeignKey(Project, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    post = models.TextField()

    def __str__(self):
        return self.posted_at

# Personal Blog
class Personal_Blog(models.Model):
    CATEGORIES = (
        ('update', 'Update'),
        ('graffiti', 'Graffiti'),
        ('one_liner', 'One Liner'),
        ('dream', 'Dream'),
        ('political', 'Political'),
        ('plan', 'Plan'),
        ('goal', 'Goal'),
        ('super-optimistic-dream', 'Super Optimistic Dream'),
        ('story', 'Story'),
        ('real-story', 'Real Story'),
        ('bizarre_idea', 'Bizarre Idea'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=200)
    summary = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
    privacy = models.CharField(max_length=100, choices=Experience.PRIVACY_OPTIONS)

    posted_at = models.DateTimeField(auto_now_add=True)
    post = models.TextField()

    file = models.FileField(upload_to='content/media/Personal_Blog/', null=True, blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='content/media/Site-Data/Images/')


class File(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='content/media/Site-Data/Images/')

