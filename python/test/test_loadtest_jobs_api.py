# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_client
from seldon_deploy_client.api.loadtest_jobs_api import LoadtestJobsApi  # noqa: E501
from seldon_deploy_client.rest import ApiException


class TestLoadtestJobsApi(unittest.TestCase):
    """LoadtestJobsApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_client.api.loadtest_jobs_api.LoadtestJobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_loadtest_inference_service(self):
        """Test case for create_loadtest_inference_service

        """
        pass

    def test_create_loadtest_seldon_deployment(self):
        """Test case for create_loadtest_seldon_deployment

        """
        pass

    def test_delete_loadtest_inference_service(self):
        """Test case for delete_loadtest_inference_service

        """
        pass

    def test_delete_loadtest_seldon_deployment(self):
        """Test case for delete_loadtest_seldon_deployment

        """
        pass

    def test_list_loadtest_inference_service(self):
        """Test case for list_loadtest_inference_service

        """
        pass

    def test_list_loadtest_seldon_deployment(self):
        """Test case for list_loadtest_seldon_deployment

        """
        pass


if __name__ == '__main__':
    unittest.main()