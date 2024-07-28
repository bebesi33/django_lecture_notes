from django.db import models


class DiscountCondition(models.Model):
    bank = models.CharField(max_length=25, verbose_name="Commerical Bank")
    discount_name = models.CharField(primary_key=True, max_length=250, unique=True, verbose_name="Interest rate discount name")
    money_transfer_condition = models.IntegerField(blank=True, null=True)
    payment_condition = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_condition'
        verbose_name = 'Interest rate discount condition'
        verbose_name_plural = 'Interest rate discount conditions'
    
    def __str__(self):
        return self.name


class DiscountValue(models.Model):
    discount_rate_id = models.CharField(max_length=250, unique=True)
    discount_name = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, verbose_name="Interest rate discount name")
    loan_type = models.CharField(max_length=25)
    term_trh_low = models.IntegerField()
    term_trh_upper = models.IntegerField()
    discount_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'discount_value'


class IncomeTrh(models.Model):
    income_rule_id = models.IntegerField()
    interest_period_min = models.IntegerField(blank=True, null=True)
    interest_period_max = models.FloatField(blank=True, null=True)
    income_min = models.IntegerField(blank=True, null=True)
    income_max = models.FloatField(blank=True, null=True)
    upper_limit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'income_trh'


class Insurance(models.Model):
    insurance_rate_id = models.CharField(primary_key=True, max_length=250, unique=True)
    bank = models.CharField(max_length=25, verbose_name="Commerical Bank")
    loan_type = models.CharField(max_length=25)
    insurance_coverage_type = models.CharField(max_length=25)
    insurance_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'insurance'


class Loan(models.Model):
    bank = models.CharField(max_length=25, verbose_name="Commerical Bank")
    loan_type = models.CharField(max_length=25)
    bank = models.CharField(max_length=25, verbose_name="Commerical Bank")
    loan_name = models.CharField(max_length=25, primary_key=True)
    term_min = models.IntegerField()
    term_max = models.IntegerField()
    interest_rate = models.FloatField()
    interest_period = models.IntegerField()
    total_loan_fee_ind = models.FloatField()
    discount_eligible = models.CharField(max_length=3)
    insurance_possible = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'loan'
