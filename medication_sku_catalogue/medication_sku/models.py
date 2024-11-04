from django.conf import settings
from django.db import models

class MedicationSKU(models.Model):
    medication_name = models.CharField(max_length=100, unique=True)
    presentation = models.CharField(max_length=50)
    dose = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust max_digits and decimal_places as needed
    unit = models.CharField(max_length=20)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='medications'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('medication_name', 'presentation', 'dose', 'unit')
        verbose_name = 'Medication SKU'
        verbose_name_plural = 'Medication SKUs'

    def __str__(self):
        return f"{self.medication_name} - {self.presentation} - {self.dose}{self.unit}"
