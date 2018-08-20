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


class AdjustHoldingRequest(Model):
    """This 'dto' contains target holdings. i.e. holding data that the
    system should match. When processed by the movement
    engine, it will create 'true-up' adjustments on the fly.

    :param security_uid: Unique security identifier
    :type security_uid: str
    :param sub_holding_keys: Key fields to uniquely index the sub holdings of
     a security
    :type sub_holding_keys: list[~lusid.models.CreatePerpetualPropertyRequest]
    :param tax_lots: 1 or more quantity amounts
    :type tax_lots: list[~lusid.models.TargetTaxLotDto]
    """

    _validation = {
        'security_uid': {'required': True},
        'tax_lots': {'required': True},
    }

    _attribute_map = {
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'sub_holding_keys': {'key': 'subHoldingKeys', 'type': '[CreatePerpetualPropertyRequest]'},
        'tax_lots': {'key': 'taxLots', 'type': '[TargetTaxLotDto]'},
    }

    def __init__(self, security_uid, tax_lots, sub_holding_keys=None):
        super(AdjustHoldingRequest, self).__init__()
        self.security_uid = security_uid
        self.sub_holding_keys = sub_holding_keys
        self.tax_lots = tax_lots