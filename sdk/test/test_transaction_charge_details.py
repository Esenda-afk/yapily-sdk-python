"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import yapily
from yapily.model.amount import Amount
globals()['Amount'] = Amount
from yapily.model.transaction_charge_details import TransactionChargeDetails


class TestTransactionChargeDetails(unittest.TestCase):
    """TransactionChargeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionChargeDetails(self):
        """Test TransactionChargeDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionChargeDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
