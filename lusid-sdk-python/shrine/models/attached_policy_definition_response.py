# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AttachedPolicyDefinitionResponse(Model):
    """AttachedPolicyDefinitionResponse.

    :param source_role:
    :type source_role: ~shrine.models.RoleId
    :param role_hierarchy_index:
    :type role_hierarchy_index: int
    :param description:
    :type description: str
    :param applications:
    :type applications: list[str]
    :param meta:
    :type meta: ~shrine.models.AttachedPolicyDefinitionResponseMeta
    :param policy_type: Possible values include: 'Undefined', 'Entitlement',
     'Licence'
    :type policy_type: str or ~shrine.models.enum
    :param id:
    :type id: ~shrine.models.PolicyId
    :param grant: Possible values include: 'Undefined', 'Allow', 'Deny'
    :type grant: str or ~shrine.models.enum
    :param paths:
    :type paths: list[~shrine.models.PathDefinition]
    :param for_property:
    :type for_property: list[~shrine.models.ForSpec]
    :param if_property:
    :type if_property: list[~shrine.models.IfExpression]
    :param when:
    :type when: ~shrine.models.WhenSpec
    :param how:
    :type how: ~shrine.models.HowSpec
    """

    _attribute_map = {
        'source_role': {'key': 'sourceRole', 'type': 'RoleId'},
        'role_hierarchy_index': {'key': 'roleHierarchyIndex', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'applications': {'key': 'applications', 'type': '[str]'},
        'meta': {'key': 'meta', 'type': 'AttachedPolicyDefinitionResponseMeta'},
        'policy_type': {'key': 'policyType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'PolicyId'},
        'grant': {'key': 'grant', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[PathDefinition]'},
        'for_property': {'key': 'for', 'type': '[ForSpec]'},
        'if_property': {'key': 'if', 'type': '[IfExpression]'},
        'when': {'key': 'when', 'type': 'WhenSpec'},
        'how': {'key': 'how', 'type': 'HowSpec'},
    }

    def __init__(self, source_role=None, role_hierarchy_index=None, description=None, applications=None, meta=None, policy_type=None, id=None, grant=None, paths=None, for_property=None, if_property=None, when=None, how=None):
        super(AttachedPolicyDefinitionResponse, self).__init__()
        self.source_role = source_role
        self.role_hierarchy_index = role_hierarchy_index
        self.description = description
        self.applications = applications
        self.meta = meta
        self.policy_type = policy_type
        self.id = id
        self.grant = grant
        self.paths = paths
        self.for_property = for_property
        self.if_property = if_property
        self.when = when
        self.how = how
