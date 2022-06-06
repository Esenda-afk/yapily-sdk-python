"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import yapily
from yapily.api.notifications_api import NotificationsApi  # noqa: E501


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_event_subscription(self):
        """Test case for create_event_subscription

        post event subscription  # noqa: E501
        """
        pass

    def test_delete_event_subscription_by_id(self):
        """Test case for delete_event_subscription_by_id

        delete event subscription by event type id  # noqa: E501
        """
        pass

    def test_get_event_subscription_by_id(self):
        """Test case for get_event_subscription_by_id

        get event subscription by event type id  # noqa: E501
        """
        pass

    def test_get_event_subscriptions(self):
        """Test case for get_event_subscriptions

        get event subscriptions  # noqa: E501
        """
        pass

    def test_get_event_types(self):
        """Test case for get_event_types

        get event types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()