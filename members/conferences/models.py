# -*- coding: utf-8 -*-
import uuid
from tinymce import HTMLField

from django.db import models
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.postgres.fields import JSONField

from crm.utils import print_pdf


class ConferenceInterface(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default="")
    api_key = models.CharField(max_length=255, default="")
    private_key = models.CharField(max_length=255, default="")

    last_synced = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.name


class ConferenceRegistration(models.Model):
    PAYMENT_TYPE = (("paypal", "PayPal"), ("wire", "Wire Transfer"))

    interface = models.ForeignKey(ConferenceInterface, models.CASCADE)
    form_id = models.CharField(max_length=255)
    entry_id = models.CharField(max_length=255)
    entry_created = models.DateTimeField(null=True)

    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    organization = models.CharField(max_length=255, default="")
    billing_address = models.TextField(default="", blank=True)

    ticket_type = models.CharField(max_length=255)
    dinner_guest = models.CharField(max_length=255, default="", blank=True)
    dinner_guest_qty = models.IntegerField(default=0)

    conference_dinner = models.CharField(max_length=255, default="", blank=True)
    reception_guest = models.CharField(max_length=255, default="", blank=True)
    reception_guest_qty = models.IntegerField(default=0)

    total_amount = models.CharField(max_length=255)
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=255)

    products = JSONField(blank=True, null=True)
    qbo_id = models.IntegerField(blank=True, null=True)

    source_url = models.CharField(max_length=255)

    billing_html = HTMLField(default="")
    product_html = models.TextField(default="")

    last_synced = models.DateTimeField(auto_now=True)
    access_key = models.CharField(max_length=32, blank=True)

    is_group = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.access_key:
            self.access_key = uuid.uuid4().hex

        super(ConferenceRegistration, self).save(
            force_insert=force_insert, force_update=force_update, using=using
        )

    def get_access_key_url(self):
        return reverse(
            "conferences:invoice_preview",
            kwargs={"pk": self.id, "access_key": self.access_key},
        )

    def get_absolute_url(self):
        return "/conferences/#registration-{}".format(self.id)

    def email_invoice(self):
        body = """Thank you for registering for Open Education Global Conference 2018 (24-26 April in Delft, the Netherlands).

Attached is your invoice.

Do not hesitate to contact us at conference@oeglobal.org if you have any questions.
We look forward to welcoming you in the Netherlands!

Open Education Global Conference 2018 Planning Team.
"""

        message = EmailMessage(
            subject="Open Education Global Conference 2018 - Invoice",
            body=body,
            from_email="conference@oeglobal.org",
            to=[self.email],
            # bcc = ['conference@oeglobal.org']
        )

        url = "%s%s" % (settings.INVOICES_PHANTOM_JS_HOST, self.get_access_key_url())
        pdf_file = print_pdf(url)

        message.attach(
            filename="OEGlobal-Invoice-%s.pdf" % self.entry_id,
            content=pdf_file,
            mimetype="application/pdf",
        )
        message.send()


CONFERENCE_REGISTRATION_TYPE = (
    ("normal", "Normal registration"),
    ("presenter", "Presenter registration"),
)


class ConferenceEmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    body_text = models.TextField()
    body_html = models.TextField()
    email_type = models.CharField(
        choices=CONFERENCE_REGISTRATION_TYPE, default="normal", max_length=20
    )

    def __str__(self) -> str:
        return "{}".format(self.subject)


class ConferenceEmailRegistration(models.Model):
    email = models.CharField(max_length=255)
    email_type = models.CharField(
        choices=CONFERENCE_REGISTRATION_TYPE, default="normal", max_length=20
    )

    def __str__(self) -> str:
        return "{} - {}".format(self.email, self.email_type)


class ConferenceEmailLogs(models.Model):
    action = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}".format(self.action)
