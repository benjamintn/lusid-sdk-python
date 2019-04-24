# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MatchAllPathDefinition(Model):
    """MatchAllPathDefinition.

    :param category: Possible values include: 'None', 'Identifier', 'Quality',
     'Licence'
    :type category: str or ~shrine.models.enum
    :param actions:
    :type actions: list[~shrine.models.ActionId]
    :param name:
    :type name: str
    :param description:
    :type description: str
    """

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'actions': {'key': 'actions', 'type': '[ActionId]'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, category=None, actions=None, name=None, description=None):
        super(MatchAllPathDefinition, self).__init__()
        self.category = category
        self.actions = actions
        self.name = name
        self.description = description