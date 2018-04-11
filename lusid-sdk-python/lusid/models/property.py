# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Property(Model):
    """This is intended to be the external facing property specification data
    type.

    :param key: The property key made up of the PropertyDomain, scope and name
     delimited with a '/'
     e.g. trade/myscope/myproperty
    :type key: str
    :param value:
    :type value: object
    :param effective_date: Date for which the property is effective from
    :type effective_date: datetime
    :param version:
    :type version: int
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'effective_date': {'key': 'effectiveDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'int'},
    }

    def __init__(self, key, value, effective_date=None, version=None):
        super(Property, self).__init__()
        self.key = key
        self.value = value
        self.effective_date = effective_date
        self.version = version