# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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

from google.cloud.websecurityscanner_v1beta.services.web_security_scanner.client import WebSecurityScannerClient
from google.cloud.websecurityscanner_v1beta.services.web_security_scanner.async_client import WebSecurityScannerAsyncClient

from google.cloud.websecurityscanner_v1beta.types.crawled_url import CrawledUrl
from google.cloud.websecurityscanner_v1beta.types.finding import Finding
from google.cloud.websecurityscanner_v1beta.types.finding_addon import Form
from google.cloud.websecurityscanner_v1beta.types.finding_addon import OutdatedLibrary
from google.cloud.websecurityscanner_v1beta.types.finding_addon import ViolatingResource
from google.cloud.websecurityscanner_v1beta.types.finding_addon import VulnerableHeaders
from google.cloud.websecurityscanner_v1beta.types.finding_addon import VulnerableParameters
from google.cloud.websecurityscanner_v1beta.types.finding_addon import Xss
from google.cloud.websecurityscanner_v1beta.types.finding_type_stats import FindingTypeStats
from google.cloud.websecurityscanner_v1beta.types.scan_config import ScanConfig
from google.cloud.websecurityscanner_v1beta.types.scan_config_error import ScanConfigError
from google.cloud.websecurityscanner_v1beta.types.scan_run import ScanRun
from google.cloud.websecurityscanner_v1beta.types.scan_run_error_trace import ScanRunErrorTrace
from google.cloud.websecurityscanner_v1beta.types.scan_run_warning_trace import ScanRunWarningTrace
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import CreateScanConfigRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import DeleteScanConfigRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import GetFindingRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import GetScanConfigRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import GetScanRunRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListCrawledUrlsRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListCrawledUrlsResponse
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListFindingsRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListFindingsResponse
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListFindingTypeStatsRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListFindingTypeStatsResponse
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListScanConfigsRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListScanConfigsResponse
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListScanRunsRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import ListScanRunsResponse
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import StartScanRunRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import StopScanRunRequest
from google.cloud.websecurityscanner_v1beta.types.web_security_scanner import UpdateScanConfigRequest

__all__ = ('WebSecurityScannerClient',
    'WebSecurityScannerAsyncClient',
    'CrawledUrl',
    'Finding',
    'Form',
    'OutdatedLibrary',
    'ViolatingResource',
    'VulnerableHeaders',
    'VulnerableParameters',
    'Xss',
    'FindingTypeStats',
    'ScanConfig',
    'ScanConfigError',
    'ScanRun',
    'ScanRunErrorTrace',
    'ScanRunWarningTrace',
    'CreateScanConfigRequest',
    'DeleteScanConfigRequest',
    'GetFindingRequest',
    'GetScanConfigRequest',
    'GetScanRunRequest',
    'ListCrawledUrlsRequest',
    'ListCrawledUrlsResponse',
    'ListFindingsRequest',
    'ListFindingsResponse',
    'ListFindingTypeStatsRequest',
    'ListFindingTypeStatsResponse',
    'ListScanConfigsRequest',
    'ListScanConfigsResponse',
    'ListScanRunsRequest',
    'ListScanRunsResponse',
    'StartScanRunRequest',
    'StopScanRunRequest',
    'UpdateScanConfigRequest',
)
