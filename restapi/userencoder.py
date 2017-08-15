import json

from restapi.models import User


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'id':obj.id,
                'username':obj.username,
                'password':obj.password,
                'sex':obj.sex,
                'age':obj.age,
                'email':obj.email
            }
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)