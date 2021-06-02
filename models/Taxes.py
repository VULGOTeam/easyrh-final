import datetime
from mongoengine import *


class Taxes(Document):
    type = StringField(required=True, max_length=100)
    ranges = ListField()
    year = StringField(required=True, max_length=4)
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
