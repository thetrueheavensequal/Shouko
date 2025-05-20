from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user_id = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from User {self.user_id}"