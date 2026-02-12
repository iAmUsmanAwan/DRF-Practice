from django.db import models



class Transaction(models.Model):
    title = models.CharField(max_length=255)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    TRANSACTION_TYPES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )
    
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPES)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def save(self, *args, **kwargs):
        if self.transaction_type == 'credit':
            self.amount = abs(self.amount) # Force positive
        elif self.transaction_type == 'debit':
            self.amount = -abs(self.amount) # Force negative
        super().save(*args, **kwargs)