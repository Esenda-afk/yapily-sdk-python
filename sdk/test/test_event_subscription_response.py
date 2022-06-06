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
from yapily.model.notification import Notification
globals()['Notification'] = Notification
from yapily.model.event_subscription_response import EventSubscriptionResponse


class TestEventSubscriptionResponse(unittest.TestCase):
    """EventSubscriptionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventSubscriptionResponse(self):
        """Test EventSubscriptionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventSubscriptionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
