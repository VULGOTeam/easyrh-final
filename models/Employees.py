import datetime
from mongoengine import *
import mongoengine_goodjson as gj


class Employees(gj.Document):
    company_id = ObjectIdField(required=True)
    name = StringField(required=True, max_length=100)
    data = DictField()
    gross = DecimalField(required=True, precision=2, force_string=False)
    vacations = IntField()
    department = StringField(max_length=60)
    hired_at = DateTimeField(required=True)
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(Employees, self).save(*args, **kwargs)

    def delete(self, signal_kwargs=None, **write_concern):
        self.deleted_at = datetime.datetime.now()
        return super(Employees, self).save()
