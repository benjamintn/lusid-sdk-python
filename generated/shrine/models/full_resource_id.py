# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FullResourceId(Model):
    """A resource identifier comprised of a domain, scope and code.

    :param scope: The scope part of the resource identifier
    :type scope: str
    :param code: The code part of the resource identifier
    :type code: str
    :param domain: The domain part of the of the resource identifier
    :type domain: str
    """

    _validation = {
        'scope': {'required': True, 'max_length': 100, 'min_length': 3},
        'code': {'required': True, 'max_length': 100, 'min_length': 3},
        'domain': {'required': True, 'max_length': 100, 'min_length': 3},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
    }

    def __init__(self, scope, code, domain):
        super(FullResourceId, self).__init__()
        self.scope = scope
        self.code = code
        self.domain = domain