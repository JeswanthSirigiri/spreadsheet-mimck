from django.db import models
from django.core.exceptions import ValidationError

class Spreadsheetapp(models.Model):
    name = models.CharField(max_length=255, unique=True)
    data = models.JSONField()  # Stores the spreadsheet grid as JSON

    def clean(self):
        """Ensure JSONField does not contain deeply nested recursion."""
        import json
        try:
            json.dumps(self.data)  # Attempt to serialize
        except (TypeError, ValueError):
            raise ValidationError("Invalid JSON data")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
class Spreadsheet(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title