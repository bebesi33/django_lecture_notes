from django.db import models


class CommonBankField(models.Model):
    bank = models.CharField(max_length=25, verbose_name="Commerical Bank")
    # this feature is suitable for created_at or updated_at datetime fields...

    class Meta:
        abstract = True

class CommonLoanType(models.Model):
    loan_type = models.CharField(max_length=25)

    class Meta:
        abstract = True



class DiscountCondition(CommonBankField):
    discount_name = models.CharField(
        primary_key=True,
        max_length=250,
        unique=True,
        verbose_name="Interest rate discount name",
    )
    money_transfer_condition = models.IntegerField(
        blank=True, null=True, verbose_name="Monthly money transfer condition"
    )
    payment_condition = models.FloatField(
        blank=True, null=True, verbose_name="Monthly payment condition"
    )

    class Meta:
        managed = False
        db_table = "discount_condition"
        verbose_name = "Interest rate discount condition"
        verbose_name_plural = "Interest rate discount conditions"

    def __str__(self):
        return self.name


class DiscountValue(CommonLoanType):
    discount_rate_id = models.CharField(max_length=250, unique=True, primary_key=True)
    discount_name = models.ForeignKey(
        DiscountCondition,
        on_delete=models.CASCADE,
        verbose_name="Interest rate discount name",
    )
    term_trh_low = models.IntegerField()
    term_trh_upper = models.IntegerField()
    discount_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = "discount_value"


class IncomeTrh(models.Model):
    income_rule_id = models.IntegerField(primary_key=True)
    interest_period_min = models.IntegerField(blank=True, null=True)
    interest_period_max = models.IntegerField(blank=True, null=True)
    income_min = models.IntegerField(blank=True, null=True)
    income_max = models.FloatField(blank=True, null=True)
    upper_limit = models.FloatField()

    class Meta:
        managed = False
        db_table = "income_trh"


class Insurance(CommonLoanType, CommonBankField):
    insurance_rate_id = models.CharField(primary_key=True, max_length=250, unique=True)
    insurance_coverage_type = models.CharField(max_length=25)
    insurance_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = "insurance"


class Loan(CommonBankField, CommonLoanType):
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
        db_table = "loan"
