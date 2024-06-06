# models.py
from django.db import models
import shortuuid

class EmailSubscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email



def generate_feedback_id():
    return 'feed' + shortuuid.ShortUUID(alphabet="123456790").random(length=10)

class FeedBack(models.Model):
    id = models.CharField(
        primary_key=True, 
        max_length=25, 
        editable=False, 
        default=generate_feedback_id
    )
    feedback = models.CharField(max_length=1500)

    def __str__(self):
        return f"Feedback({self.id}): {self.feedback[:50]}..."

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
