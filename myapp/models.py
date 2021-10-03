from django.db import models

# Create your models here.

class Twitter(models.Model):
    """
    All lesson data is stored in this model
    """
    
    description = models.TextField(
        _("Description of the lesson"), blank=True, null=True, max_length=10000)
    no_of_participants = models.IntegerField(
        _('No of participants'), default=1)
    language = models.JSONField(default=list)
    lesson_type = models.CharField(
        _("Type of lesson"), null=True, choices=LessonTypes.choices, max_length=10)
    pay_type = models.CharField(_("Pay Type"), choices=LessonDataPayChoices.choices,
        default=LessonDataPayChoices.PAID, max_length=10)
    session_type = models.CharField(
        _("Type of lesson"), choices=SessionTypes.choices, max_length=10)
    meeting_type = models.CharField(
        _("Type of Meeting"), choices=MeetingTypes.choices, max_length=20)
    price = models.JSONField(default=dict)
    timezone = models.CharField(
        _("Timezone of the lesson"), null=True, max_length=100)
    meeting_info = models.JSONField(default=dict)
    meeting_link = models.URLField(max_length=200, null=True, blank=True)
    lesson_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    is_private = models.BooleanField(_('Lesson Privacy'), default=False)
    cover_image = models.ImageField(
        _("Lesson Cover image"), upload_to=upload_lesson_image_path, blank=True, null=True)
    intro_video = models.URLField(max_length=200, null=True, blank=True)
    learnings = models.JSONField(default=list)
    requirements = models.JSONField(default=list)
    notes = models.JSONField(default=list)
    status = models.CharField(_("Lesson Status"), null=True, choices=LessonStatuses.choices, max_length=7,
                              help_text="Lesson status", default=LessonStatuses.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LessonDataManager()

    def __str__(self):
        return str(self.id)
class TweetAccount(models.Model):
    pass


class Tweet(models.Model):

    hastags = 
    passs