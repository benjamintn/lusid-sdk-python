# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AttachedPolicyDefinitionResponseMeta(Model):
    """AttachedPolicyDefinitionResponseMeta.

    :param undefined:
    :type undefined: str
    :param usage_token:
    :type usage_token: str
    :param document_type:
    :type document_type: str
    """

    _attribute_map = {
        'undefined': {'key': 'Undefined', 'type': 'str'},
        'usage_token': {'key': 'UsageToken', 'type': 'str'},
        'document_type': {'key': 'DocumentType', 'type': 'str'},
    }

    def __init__(self, undefined=None, usage_token=None, document_type=None):
        super(AttachedPolicyDefinitionResponseMeta, self).__init__()
        self.undefined = undefined
        self.usage_token = usage_token
        self.document_type = document_type
