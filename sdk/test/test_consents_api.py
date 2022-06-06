"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import yapily
from yapily.api.consents_api import ConsentsApi  # noqa: E501


class TestConsentsApi(unittest.TestCase):
    """ConsentsApi unit test stubs"""

    def setUp(self):
        self.api = ConsentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_consent_with_code(self):
        """Test case for create_consent_with_code

        Exchange OAuth2 Code  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete Consent  # noqa: E501
        """
        pass

    def test_get_consent_by_id(self):
        """Test case for get_consent_by_id

        Get Consent  # noqa: E501
        """
        pass

    def test_get_consent_by_single_access_consent(self):
        """Test case for get_consent_by_single_access_consent

        Exchange One Time Token  # noqa: E501
        """
        pass

    def test_get_consents(self):
        """Test case for get_consents

        Get Consents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
