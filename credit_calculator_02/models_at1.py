# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DiscountCondition(models.Model):
    bank = models.TextField(blank=True, null=True)
    discount_name = models.TextField(blank=True, null=True)
    money_transfer_condition = models.IntegerField(blank=True, null=True)
    payment_condition = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_condition'


class DiscountValue(models.Model):
    discount_name = models.TextField(blank=True, null=True)
    loan_type = models.TextField(blank=True, null=True)
    term_trh_low = models.IntegerField(blank=True, null=True)
    term_trh_upper = models.IntegerField(blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_value'


class IncomeTrh(models.Model):
    interest_period_min = models.IntegerField(blank=True, null=True)
    interest_period_max = models.FloatField(blank=True, null=True)
    income_min = models.IntegerField(blank=True, null=True)
    income_max = models.FloatField(blank=True, null=True)
    upper_limit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income_trh'


class Insurance(models.Model):
    bank = models.TextField(blank=True, null=True)
    loan_type = models.TextField(blank=True, null=True)
    insurance_coverage_type = models.TextField(blank=True, null=True)
    insurance_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance'


class Loan(models.Model):
    bank = models.TextField(blank=True, null=True)
    loan_name = models.TextField(blank=True, null=True)
    term_min = models.IntegerField(blank=True, null=True)
    term_max = models.IntegerField(blank=True, null=True)
    interest_rate = models.FloatField(blank=True, null=True)
    interest_period = models.IntegerField(blank=True, null=True)
    total_loan_fee_ind = models.FloatField(blank=True, null=True)
    field_discount_eligible = models.TextField(db_column=' discount_eligible', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    loan_type = models.TextField(blank=True, null=True)
    insurance_possible = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan'
