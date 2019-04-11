# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ActionId(Model):
    """ActionId.

    :param scope:
    :type scope: str
    :param activity:
    :type activity: str
    :param entity:
    :type entity: str
    """

    _validation = {
        'scope': {'required': True, 'max_length': 100, 'min_length': 3},
        'activity': {'required': True, 'max_length': 25, 'min_length': 3},
        'entity': {'required': True, 'max_length': 25, 'min_length': 3},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'activity': {'key': 'activity', 'type': 'str'},
        'entity': {'key': 'entity', 'type': 'str'},
    }

    def __init__(self, scope, activity, entity):
        super(ActionId, self).__init__()
        self.scope = scope
        self.activity = activity
        self.entity = entity
