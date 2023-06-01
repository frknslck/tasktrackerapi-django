from django.db import models

class Todo(models.Model):

    PRIORITY = (
        (1, 'HIGH'),
        (2, 'MEDIUM'),
        (3, 'LOW')
    )

    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=2)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.title}" titled todo with level {self.priority} priority.'