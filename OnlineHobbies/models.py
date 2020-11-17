from django.db import models

# for online enrollment status
from User.models import User


# Create your models here.
from django.utils import timezone

# this models registers the list of hobbies in the online hobby page
class OnlineClass(models.Model):
    online_class_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="User/images")
    # get_started = models.CharField(max_length=100)
    #
    #
    # class_video_links=models.
    # created_date = models.DateTimeField(
    #  default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.online_class_name)


# this model enrolls the current user for an online class using enroll button in UI - Apr 9 2020
class OnlineClassEnroll(models.Model):
    online_class_name=models.ForeignKey(OnlineClass, on_delete=models.CASCADE, related_name='OnlineClassEnroll', default=3)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    enrollment_status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{0} enrolled by \t {1}  on the date  {2}'.format(self.online_class_name,self.username,self.created_date)

    def created(self):
        self.created_date = timezone.now()
        self.save()


# this model provides the admin/instructor to register new class with below fields - Apr 9 2020
class OnlineClassVideoPage(models.Model):
    online_class_name=models.ForeignKey(OnlineClass, on_delete=models.CASCADE, related_name='OnlineClassVideoPage')
    class_title = models.CharField(max_length=100)
    class_subtitle=models.CharField(max_length=100)
    class_requirements=models.TextField(max_length=2500)
    class_goal = models.TextField(max_length=2500)
    class_video_links = models.CharField(max_length=25)

    def __str__(self):
        return str(self.class_title)


