# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EffectiveDateRelative(Model):
    """EffectiveDateRelative.

    :param date_property: Possible values include: 'Undefined', 'Now',
     'FirstOfMonth', 'FirstBusinessDayOfTheMonth', 'LastDayOfTheMonth',
     'LastBusinessDayOfMonth', 'FirstDayOfYear', 'LastDayOfYear'
    :type date_property: str or ~shrine.models.enum
    :param adjustment:
    :type adjustment: int
    :param unit: Possible values include: 'Undefined', 'Minute', 'Hour',
     'Day', 'BusinessDay', 'Weeks', 'Months', 'Years'
    :type unit: str or ~shrine.models.enum
    :param relative_to_date_time: Possible values include: 'Undefined',
     'BeforeOrOn', 'Before', 'OnDayOf', 'AfterOrOn', 'After', 'Exactly'
    :type relative_to_date_time: str or ~shrine.models.enum
    """

    _attribute_map = {
        'date_property': {'key': 'date', 'type': 'str'},
        'adjustment': {'key': 'adjustment', 'type': 'int'},
        'unit': {'key': 'unit', 'type': 'str'},
        'relative_to_date_time': {'key': 'relativeToDateTime', 'type': 'str'},
    }

    def __init__(self, date_property=None, adjustment=None, unit=None, relative_to_date_time=None):
        super(EffectiveDateRelative, self).__init__()
        self.date_property = date_property
        self.adjustment = adjustment
        self.unit = unit
        self.relative_to_date_time = relative_to_date_time