# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListCrawledUrls
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-websecurityscanner


# [START websecurityscanner_v1alpha_generated_WebSecurityScanner_ListCrawledUrls_sync]
from google.cloud import websecurityscanner_v1alpha


def sample_list_crawled_urls():
    # Create a client
    client = websecurityscanner_v1alpha.WebSecurityScannerClient()

    # Initialize request argument(s)
    request = websecurityscanner_v1alpha.ListCrawledUrlsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_crawled_urls(request=request)

    # Handle the response
    for response in page_result:
        print(response)

# [END websecurityscanner_v1alpha_generated_WebSecurityScanner_ListCrawledUrls_sync]