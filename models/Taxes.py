import datetime
from mongoengine import *


class Taxes(Document):
    type = StringField(required=True, max_length=100)
    year = StringField(required=True, max_length=4)
    aliquot = DecimalField(required=True, precision=2, force_string=False)
    deduction = DecimalField(required=True, precision=2, force_string=False)
    range = ListField(DecimalField(precision=2, force_string=False))
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(Taxes, self).save(*args, **kwargs)

    def delete(self, signal_kwargs=None, **write_concern):
        self.deleted_at = datetime.datetime.now()
        return super(Taxes, self).save()
