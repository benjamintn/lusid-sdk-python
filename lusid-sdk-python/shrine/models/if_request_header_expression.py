# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IfRequestHeaderExpression(Model):
    """IfRequestHeaderExpression.

    :param header_name:
    :type header_name: str
    :param operator: Possible values include: 'Undefined',
     'EqualsCaseSensitive', 'EqualsCaseInsensitive', 'NotEqualsCaseSensitive',
     'NotEqualsCaseInsensitive', 'ContainsCaseSensitive',
     'NotPresentOrNotContainsCaseSensitive'
    :type operator: str or ~shrine.models.enum
    :param value:
    :type value: str
    """

    _validation = {
        'header_name': {'required': True, 'min_length': 1},
        'operator': {'required': True},
    }

    _attribute_map = {
        'header_name': {'key': 'headerName', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, header_name, operator, value=None):
        super(IfRequestHeaderExpression, self).__init__()
        self.header_name = header_name
        self.operator = operator
        self.value = value