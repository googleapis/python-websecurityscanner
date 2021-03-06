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

from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore


import grpc  # type: ignore

from google.cloud.websecurityscanner_v1alpha.types import finding
from google.cloud.websecurityscanner_v1alpha.types import scan_config
from google.cloud.websecurityscanner_v1alpha.types import scan_config as gcw_scan_config
from google.cloud.websecurityscanner_v1alpha.types import scan_run
from google.cloud.websecurityscanner_v1alpha.types import web_security_scanner
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import WebSecurityScannerTransport


class WebSecurityScannerGrpcTransport(WebSecurityScannerTransport):
    """gRPC backend transport for WebSecurityScanner.

    Cloud Web Security Scanner Service identifies security
    vulnerabilities in web applications hosted on Google Cloud
    Platform. It crawls your application, and attempts to exercise
    as many user inputs and event handlers as possible.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "websecurityscanner.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
        )

        self._stubs = {}  # type: Dict[str, Callable]

    @classmethod
    def create_channel(
        cls,
        host: str = "websecurityscanner.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = self.create_channel(
                self._host, credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_scan_config(
        self,
    ) -> Callable[
        [web_security_scanner.CreateScanConfigRequest], gcw_scan_config.ScanConfig
    ]:
        r"""Return a callable for the create scan config method over gRPC.

        Creates a new ScanConfig.

        Returns:
            Callable[[~.CreateScanConfigRequest],
                    ~.ScanConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_scan_config" not in self._stubs:
            self._stubs["create_scan_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/CreateScanConfig",
                request_serializer=web_security_scanner.CreateScanConfigRequest.serialize,
                response_deserializer=gcw_scan_config.ScanConfig.deserialize,
            )
        return self._stubs["create_scan_config"]

    @property
    def delete_scan_config(
        self,
    ) -> Callable[[web_security_scanner.DeleteScanConfigRequest], empty.Empty]:
        r"""Return a callable for the delete scan config method over gRPC.

        Deletes an existing ScanConfig and its child
        resources.

        Returns:
            Callable[[~.DeleteScanConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_scan_config" not in self._stubs:
            self._stubs["delete_scan_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/DeleteScanConfig",
                request_serializer=web_security_scanner.DeleteScanConfigRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_scan_config"]

    @property
    def get_scan_config(
        self,
    ) -> Callable[[web_security_scanner.GetScanConfigRequest], scan_config.ScanConfig]:
        r"""Return a callable for the get scan config method over gRPC.

        Gets a ScanConfig.

        Returns:
            Callable[[~.GetScanConfigRequest],
                    ~.ScanConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scan_config" not in self._stubs:
            self._stubs["get_scan_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/GetScanConfig",
                request_serializer=web_security_scanner.GetScanConfigRequest.serialize,
                response_deserializer=scan_config.ScanConfig.deserialize,
            )
        return self._stubs["get_scan_config"]

    @property
    def list_scan_configs(
        self,
    ) -> Callable[
        [web_security_scanner.ListScanConfigsRequest],
        web_security_scanner.ListScanConfigsResponse,
    ]:
        r"""Return a callable for the list scan configs method over gRPC.

        Lists ScanConfigs under a given project.

        Returns:
            Callable[[~.ListScanConfigsRequest],
                    ~.ListScanConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scan_configs" not in self._stubs:
            self._stubs["list_scan_configs"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/ListScanConfigs",
                request_serializer=web_security_scanner.ListScanConfigsRequest.serialize,
                response_deserializer=web_security_scanner.ListScanConfigsResponse.deserialize,
            )
        return self._stubs["list_scan_configs"]

    @property
    def update_scan_config(
        self,
    ) -> Callable[
        [web_security_scanner.UpdateScanConfigRequest], gcw_scan_config.ScanConfig
    ]:
        r"""Return a callable for the update scan config method over gRPC.

        Updates a ScanConfig. This method support partial
        update of a ScanConfig.

        Returns:
            Callable[[~.UpdateScanConfigRequest],
                    ~.ScanConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scan_config" not in self._stubs:
            self._stubs["update_scan_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/UpdateScanConfig",
                request_serializer=web_security_scanner.UpdateScanConfigRequest.serialize,
                response_deserializer=gcw_scan_config.ScanConfig.deserialize,
            )
        return self._stubs["update_scan_config"]

    @property
    def start_scan_run(
        self,
    ) -> Callable[[web_security_scanner.StartScanRunRequest], scan_run.ScanRun]:
        r"""Return a callable for the start scan run method over gRPC.

        Start a ScanRun according to the given ScanConfig.

        Returns:
            Callable[[~.StartScanRunRequest],
                    ~.ScanRun]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_scan_run" not in self._stubs:
            self._stubs["start_scan_run"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/StartScanRun",
                request_serializer=web_security_scanner.StartScanRunRequest.serialize,
                response_deserializer=scan_run.ScanRun.deserialize,
            )
        return self._stubs["start_scan_run"]

    @property
    def get_scan_run(
        self,
    ) -> Callable[[web_security_scanner.GetScanRunRequest], scan_run.ScanRun]:
        r"""Return a callable for the get scan run method over gRPC.

        Gets a ScanRun.

        Returns:
            Callable[[~.GetScanRunRequest],
                    ~.ScanRun]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scan_run" not in self._stubs:
            self._stubs["get_scan_run"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/GetScanRun",
                request_serializer=web_security_scanner.GetScanRunRequest.serialize,
                response_deserializer=scan_run.ScanRun.deserialize,
            )
        return self._stubs["get_scan_run"]

    @property
    def list_scan_runs(
        self,
    ) -> Callable[
        [web_security_scanner.ListScanRunsRequest],
        web_security_scanner.ListScanRunsResponse,
    ]:
        r"""Return a callable for the list scan runs method over gRPC.

        Lists ScanRuns under a given ScanConfig, in
        descending order of ScanRun stop time.

        Returns:
            Callable[[~.ListScanRunsRequest],
                    ~.ListScanRunsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scan_runs" not in self._stubs:
            self._stubs["list_scan_runs"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/ListScanRuns",
                request_serializer=web_security_scanner.ListScanRunsRequest.serialize,
                response_deserializer=web_security_scanner.ListScanRunsResponse.deserialize,
            )
        return self._stubs["list_scan_runs"]

    @property
    def stop_scan_run(
        self,
    ) -> Callable[[web_security_scanner.StopScanRunRequest], scan_run.ScanRun]:
        r"""Return a callable for the stop scan run method over gRPC.

        Stops a ScanRun. The stopped ScanRun is returned.

        Returns:
            Callable[[~.StopScanRunRequest],
                    ~.ScanRun]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_scan_run" not in self._stubs:
            self._stubs["stop_scan_run"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/StopScanRun",
                request_serializer=web_security_scanner.StopScanRunRequest.serialize,
                response_deserializer=scan_run.ScanRun.deserialize,
            )
        return self._stubs["stop_scan_run"]

    @property
    def list_crawled_urls(
        self,
    ) -> Callable[
        [web_security_scanner.ListCrawledUrlsRequest],
        web_security_scanner.ListCrawledUrlsResponse,
    ]:
        r"""Return a callable for the list crawled urls method over gRPC.

        List CrawledUrls under a given ScanRun.

        Returns:
            Callable[[~.ListCrawledUrlsRequest],
                    ~.ListCrawledUrlsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_crawled_urls" not in self._stubs:
            self._stubs["list_crawled_urls"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/ListCrawledUrls",
                request_serializer=web_security_scanner.ListCrawledUrlsRequest.serialize,
                response_deserializer=web_security_scanner.ListCrawledUrlsResponse.deserialize,
            )
        return self._stubs["list_crawled_urls"]

    @property
    def get_finding(
        self,
    ) -> Callable[[web_security_scanner.GetFindingRequest], finding.Finding]:
        r"""Return a callable for the get finding method over gRPC.

        Gets a Finding.

        Returns:
            Callable[[~.GetFindingRequest],
                    ~.Finding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_finding" not in self._stubs:
            self._stubs["get_finding"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/GetFinding",
                request_serializer=web_security_scanner.GetFindingRequest.serialize,
                response_deserializer=finding.Finding.deserialize,
            )
        return self._stubs["get_finding"]

    @property
    def list_findings(
        self,
    ) -> Callable[
        [web_security_scanner.ListFindingsRequest],
        web_security_scanner.ListFindingsResponse,
    ]:
        r"""Return a callable for the list findings method over gRPC.

        List Findings under a given ScanRun.

        Returns:
            Callable[[~.ListFindingsRequest],
                    ~.ListFindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_findings" not in self._stubs:
            self._stubs["list_findings"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/ListFindings",
                request_serializer=web_security_scanner.ListFindingsRequest.serialize,
                response_deserializer=web_security_scanner.ListFindingsResponse.deserialize,
            )
        return self._stubs["list_findings"]

    @property
    def list_finding_type_stats(
        self,
    ) -> Callable[
        [web_security_scanner.ListFindingTypeStatsRequest],
        web_security_scanner.ListFindingTypeStatsResponse,
    ]:
        r"""Return a callable for the list finding type stats method over gRPC.

        List all FindingTypeStats under a given ScanRun.

        Returns:
            Callable[[~.ListFindingTypeStatsRequest],
                    ~.ListFindingTypeStatsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_finding_type_stats" not in self._stubs:
            self._stubs["list_finding_type_stats"] = self.grpc_channel.unary_unary(
                "/google.cloud.websecurityscanner.v1alpha.WebSecurityScanner/ListFindingTypeStats",
                request_serializer=web_security_scanner.ListFindingTypeStatsRequest.serialize,
                response_deserializer=web_security_scanner.ListFindingTypeStatsResponse.deserialize,
            )
        return self._stubs["list_finding_type_stats"]


__all__ = ("WebSecurityScannerGrpcTransport",)
