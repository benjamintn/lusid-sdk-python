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


class ConfigurationRecipe(Model):
    """The Configuration or Calculation Recipe controls how LUSID processes a
    given request.
    This can be used to change where market data used in pricing is loaded from
    and in what order, or which model is used to
    price a given instrument as well as how aggregation will process the
    produced results.

    :param code: User given string name (code) to identify the recipe.
    :type code: str
    :param market: The market configuration node that defines where market
     data used in processing a request is loaded from and how it is resolved.
    :type market: ~lusid.models.MarketContext
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'market': {'key': 'market', 'type': 'MarketContext'},
    }

    def __init__(self, code, market=None):
        super(ConfigurationRecipe, self).__init__()
        self.code = code
        self.market = market