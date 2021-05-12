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

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.websecurityscanner_v1.types import finding
from google.cloud.websecurityscanner_v1.types import scan_config
from google.cloud.websecurityscanner_v1.types import scan_run
from google.cloud.websecurityscanner_v1.types import web_security_scanner
from google.protobuf import empty_pb2 as empty  # type: ignore


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-websecurityscanner",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class WebSecurityScannerTransport(abc.ABC):
    """Abstract transport class for WebSecurityScanner."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "websecurityscanner.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=self._scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=self._scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_scan_config: gapic_v1.method.wrap_method(
                self.create_scan_config, default_timeout=600.0, client_info=client_info,
            ),
            self.delete_scan_config: gapic_v1.method.wrap_method(
                self.delete_scan_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_scan_config: gapic_v1.method.wrap_method(
                self.get_scan_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_scan_configs: gapic_v1.method.wrap_method(
                self.list_scan_configs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_scan_config: gapic_v1.method.wrap_method(
                self.update_scan_config, default_timeout=600.0, client_info=client_info,
            ),
            self.start_scan_run: gapic_v1.method.wrap_method(
                self.start_scan_run, default_timeout=600.0, client_info=client_info,
            ),
            self.get_scan_run: gapic_v1.method.wrap_method(
                self.get_scan_run,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_scan_runs: gapic_v1.method.wrap_method(
                self.list_scan_runs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.stop_scan_run: gapic_v1.method.wrap_method(
                self.stop_scan_run, default_timeout=600.0, client_info=client_info,
            ),
            self.list_crawled_urls: gapic_v1.method.wrap_method(
                self.list_crawled_urls,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_finding: gapic_v1.method.wrap_method(
                self.get_finding,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_findings: gapic_v1.method.wrap_method(
                self.list_findings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_finding_type_stats: gapic_v1.method.wrap_method(
                self.list_finding_type_stats,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
        }

    @property
    def create_scan_config(
        self,
    ) -> typing.Callable[
        [web_security_scanner.CreateScanConfigRequest],
        typing.Union[scan_config.ScanConfig, typing.Awaitable[scan_config.ScanConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_scan_config(
        self,
    ) -> typing.Callable[
        [web_security_scanner.DeleteScanConfigRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_scan_config(
        self,
    ) -> typing.Callable[
        [web_security_scanner.GetScanConfigRequest],
        typing.Union[scan_config.ScanConfig, typing.Awaitable[scan_config.ScanConfig]],
    ]:
        raise NotImplementedError()

    @property
    def list_scan_configs(
        self,
    ) -> typing.Callable[
        [web_security_scanner.ListScanConfigsRequest],
        typing.Union[
            web_security_scanner.ListScanConfigsResponse,
            typing.Awaitable[web_security_scanner.ListScanConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_scan_config(
        self,
    ) -> typing.Callable[
        [web_security_scanner.UpdateScanConfigRequest],
        typing.Union[scan_config.ScanConfig, typing.Awaitable[scan_config.ScanConfig]],
    ]:
        raise NotImplementedError()

    @property
    def start_scan_run(
        self,
    ) -> typing.Callable[
        [web_security_scanner.StartScanRunRequest],
        typing.Union[scan_run.ScanRun, typing.Awaitable[scan_run.ScanRun]],
    ]:
        raise NotImplementedError()

    @property
    def get_scan_run(
        self,
    ) -> typing.Callable[
        [web_security_scanner.GetScanRunRequest],
        typing.Union[scan_run.ScanRun, typing.Awaitable[scan_run.ScanRun]],
    ]:
        raise NotImplementedError()

    @property
    def list_scan_runs(
        self,
    ) -> typing.Callable[
        [web_security_scanner.ListScanRunsRequest],
        typing.Union[
            web_security_scanner.ListScanRunsResponse,
            typing.Awaitable[web_security_scanner.ListScanRunsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def stop_scan_run(
        self,
    ) -> typing.Callable[
        [web_security_scanner.StopScanRunRequest],
        typing.Union[scan_run.ScanRun, typing.Awaitable[scan_run.ScanRun]],
    ]:
        raise NotImplementedError()

    @property
    def list_crawled_urls(
        self,
    ) -> typing.Callable[
        [web_security_scanner.ListCrawledUrlsRequest],
        typing.Union[
            web_security_scanner.ListCrawledUrlsResponse,
            typing.Awaitable[web_security_scanner.ListCrawledUrlsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_finding(
        self,
    ) -> typing.Callable[
        [web_security_scanner.GetFindingRequest],
        typing.Union[finding.Finding, typing.Awaitable[finding.Finding]],
    ]:
        raise NotImplementedError()

    @property
    def list_findings(
        self,
    ) -> typing.Callable[
        [web_security_scanner.ListFindingsRequest],
        typing.Union[
            web_security_scanner.ListFindingsResponse,
            typing.Awaitable[web_security_scanner.ListFindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_finding_type_stats(
        self,
    ) -> typing.Callable[
        [web_security_scanner.ListFindingTypeStatsRequest],
        typing.Union[
            web_security_scanner.ListFindingTypeStatsResponse,
            typing.Awaitable[web_security_scanner.ListFindingTypeStatsResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("WebSecurityScannerTransport",)