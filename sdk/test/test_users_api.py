"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import yapily
from yapily.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user(self):
        """Test case for add_user

        Create User  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete User  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get User  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Get Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
