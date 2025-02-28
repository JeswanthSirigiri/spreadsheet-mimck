# from django.db import models
#
# class Spreadsheet(models.Model):
#     name = models.CharField(max_length=255)
#     #data = models.JSONField()  # Store grid data as JSON
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
# class Cell(models.Model):
#     spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE, related_name='cells')
#     row = models.IntegerField()
#     col = models.IntegerField()
#     value = models.CharField(max_length=255, blank=True, null=True)
#     formula = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         unique_together = ('spreadsheet', 'row', 'col')
#
#     def __str__(self):
#         return f"Cell ({self.row}, {self.col}) in {self.spreadsheet.name}"