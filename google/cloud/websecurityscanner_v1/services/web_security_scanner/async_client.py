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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.websecurityscanner_v1.services.web_security_scanner import pagers
from google.cloud.websecurityscanner_v1.types import crawled_url
from google.cloud.websecurityscanner_v1.types import finding
from google.cloud.websecurityscanner_v1.types import finding_addon
from google.cloud.websecurityscanner_v1.types import finding_type_stats
from google.cloud.websecurityscanner_v1.types import scan_config
from google.cloud.websecurityscanner_v1.types import scan_run
from google.cloud.websecurityscanner_v1.types import scan_run_error_trace
from google.cloud.websecurityscanner_v1.types import scan_run_warning_trace
from google.cloud.websecurityscanner_v1.types import web_security_scanner
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import WebSecurityScannerTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import WebSecurityScannerGrpcAsyncIOTransport
from .client import WebSecurityScannerClient


class WebSecurityScannerAsyncClient:
    """Web Security Scanner Service identifies security
    vulnerabilities in web applications hosted on Google Cloud. It
    crawls your application, and attempts to exercise as many user
    inputs and event handlers as possible.
    """

    _client: WebSecurityScannerClient

    DEFAULT_ENDPOINT = WebSecurityScannerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WebSecurityScannerClient.DEFAULT_MTLS_ENDPOINT

    finding_path = staticmethod(WebSecurityScannerClient.finding_path)
    parse_finding_path = staticmethod(WebSecurityScannerClient.parse_finding_path)
    common_billing_account_path = staticmethod(
        WebSecurityScannerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        WebSecurityScannerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(WebSecurityScannerClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        WebSecurityScannerClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        WebSecurityScannerClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        WebSecurityScannerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(WebSecurityScannerClient.common_project_path)
    parse_common_project_path = staticmethod(
        WebSecurityScannerClient.parse_common_project_path
    )
    common_location_path = staticmethod(WebSecurityScannerClient.common_location_path)
    parse_common_location_path = staticmethod(
        WebSecurityScannerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebSecurityScannerAsyncClient: The constructed client.
        """
        return WebSecurityScannerClient.from_service_account_info.__func__(WebSecurityScannerAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebSecurityScannerAsyncClient: The constructed client.
        """
        return WebSecurityScannerClient.from_service_account_file.__func__(WebSecurityScannerAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return WebSecurityScannerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> WebSecurityScannerTransport:
        """Returns the transport used by the client instance.

        Returns:
            WebSecurityScannerTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(WebSecurityScannerClient).get_transport_class,
        type(WebSecurityScannerClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, WebSecurityScannerTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the web security scanner client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.WebSecurityScannerTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = WebSecurityScannerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_scan_config(
        self,
        request: Union[web_security_scanner.CreateScanConfigRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_config.ScanConfig:
        r"""Creates a new ScanConfig.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_create_scan_config():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.CreateScanConfigRequest(
                )

                # Make the request
                response = client.create_scan_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.CreateScanConfigRequest, dict]):
                The request object. Request for the `CreateScanConfig`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanConfig:
                A ScanConfig resource contains the
                configurations to launch a scan.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.CreateScanConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_scan_config,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_scan_config(
        self,
        request: Union[web_security_scanner.DeleteScanConfigRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an existing ScanConfig and its child
        resources.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_delete_scan_config():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.DeleteScanConfigRequest(
                )

                # Make the request
                client.delete_scan_config(request=request)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.DeleteScanConfigRequest, dict]):
                The request object. Request for the `DeleteScanConfig`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.DeleteScanConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_scan_config,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_scan_config(
        self,
        request: Union[web_security_scanner.GetScanConfigRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_config.ScanConfig:
        r"""Gets a ScanConfig.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_get_scan_config():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.GetScanConfigRequest(
                )

                # Make the request
                response = client.get_scan_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.GetScanConfigRequest, dict]):
                The request object. Request for the `GetScanConfig`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanConfig:
                A ScanConfig resource contains the
                configurations to launch a scan.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.GetScanConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_scan_config,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_scan_configs(
        self,
        request: Union[web_security_scanner.ListScanConfigsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListScanConfigsAsyncPager:
        r"""Lists ScanConfigs under a given project.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_list_scan_configs():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.ListScanConfigsRequest(
                )

                # Make the request
                page_result = client.list_scan_configs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.ListScanConfigsRequest, dict]):
                The request object. Request for the `ListScanConfigs`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.services.web_security_scanner.pagers.ListScanConfigsAsyncPager:
                Response for the ListScanConfigs method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.ListScanConfigsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_scan_configs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListScanConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_scan_config(
        self,
        request: Union[web_security_scanner.UpdateScanConfigRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_config.ScanConfig:
        r"""Updates a ScanConfig. This method support partial
        update of a ScanConfig.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_update_scan_config():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.UpdateScanConfigRequest(
                )

                # Make the request
                response = client.update_scan_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.UpdateScanConfigRequest, dict]):
                The request object. Request for the
                `UpdateScanConfigRequest` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanConfig:
                A ScanConfig resource contains the
                configurations to launch a scan.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.UpdateScanConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_scan_config,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("scan_config.name", request.scan_config.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def start_scan_run(
        self,
        request: Union[web_security_scanner.StartScanRunRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_run.ScanRun:
        r"""Start a ScanRun according to the given ScanConfig.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_start_scan_run():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.StartScanRunRequest(
                )

                # Make the request
                response = client.start_scan_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.StartScanRunRequest, dict]):
                The request object. Request for the `StartScanRun`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanRun:
                A ScanRun is a output-only resource
                representing an actual run of the scan.
                Next id: 12

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.StartScanRunRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_scan_run,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_scan_run(
        self,
        request: Union[web_security_scanner.GetScanRunRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_run.ScanRun:
        r"""Gets a ScanRun.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_get_scan_run():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.GetScanRunRequest(
                )

                # Make the request
                response = client.get_scan_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.GetScanRunRequest, dict]):
                The request object. Request for the `GetScanRun` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanRun:
                A ScanRun is a output-only resource
                representing an actual run of the scan.
                Next id: 12

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.GetScanRunRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_scan_run,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_scan_runs(
        self,
        request: Union[web_security_scanner.ListScanRunsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListScanRunsAsyncPager:
        r"""Lists ScanRuns under a given ScanConfig, in
        descending order of ScanRun stop time.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_list_scan_runs():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.ListScanRunsRequest(
                )

                # Make the request
                page_result = client.list_scan_runs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.ListScanRunsRequest, dict]):
                The request object. Request for the `ListScanRuns`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.services.web_security_scanner.pagers.ListScanRunsAsyncPager:
                Response for the ListScanRuns method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.ListScanRunsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_scan_runs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListScanRunsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def stop_scan_run(
        self,
        request: Union[web_security_scanner.StopScanRunRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> scan_run.ScanRun:
        r"""Stops a ScanRun. The stopped ScanRun is returned.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_stop_scan_run():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.StopScanRunRequest(
                )

                # Make the request
                response = client.stop_scan_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.StopScanRunRequest, dict]):
                The request object. Request for the `StopScanRun`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ScanRun:
                A ScanRun is a output-only resource
                representing an actual run of the scan.
                Next id: 12

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.StopScanRunRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.stop_scan_run,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_crawled_urls(
        self,
        request: Union[web_security_scanner.ListCrawledUrlsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCrawledUrlsAsyncPager:
        r"""List CrawledUrls under a given ScanRun.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_list_crawled_urls():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.ListCrawledUrlsRequest(
                )

                # Make the request
                page_result = client.list_crawled_urls(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.ListCrawledUrlsRequest, dict]):
                The request object. Request for the `ListCrawledUrls`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.services.web_security_scanner.pagers.ListCrawledUrlsAsyncPager:
                Response for the ListCrawledUrls method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.ListCrawledUrlsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_crawled_urls,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCrawledUrlsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_finding(
        self,
        request: Union[web_security_scanner.GetFindingRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> finding.Finding:
        r"""Gets a Finding.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_get_finding():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.GetFindingRequest(
                )

                # Make the request
                response = client.get_finding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.GetFindingRequest, dict]):
                The request object. Request for the `GetFinding` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.Finding:
                A Finding resource represents a
                vulnerability instance identified during
                a ScanRun.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.GetFindingRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_finding,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_findings(
        self,
        request: Union[web_security_scanner.ListFindingsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListFindingsAsyncPager:
        r"""List Findings under a given ScanRun.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_list_findings():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.ListFindingsRequest(
                )

                # Make the request
                page_result = client.list_findings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.ListFindingsRequest, dict]):
                The request object. Request for the `ListFindings`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.services.web_security_scanner.pagers.ListFindingsAsyncPager:
                Response for the ListFindings method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.ListFindingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_findings,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListFindingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_finding_type_stats(
        self,
        request: Union[web_security_scanner.ListFindingTypeStatsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> web_security_scanner.ListFindingTypeStatsResponse:
        r"""List all FindingTypeStats under a given ScanRun.

        .. code-block:: python

            from google.cloud import websecurityscanner_v1

            def sample_list_finding_type_stats():
                # Create a client
                client = websecurityscanner_v1.WebSecurityScannerClient()

                # Initialize request argument(s)
                request = websecurityscanner_v1.ListFindingTypeStatsRequest(
                )

                # Make the request
                response = client.list_finding_type_stats(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.websecurityscanner_v1.types.ListFindingTypeStatsRequest, dict]):
                The request object. Request for the
                `ListFindingTypeStats` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.websecurityscanner_v1.types.ListFindingTypeStatsResponse:
                Response for the ListFindingTypeStats method.
        """
        # Create or coerce a protobuf request object.
        request = web_security_scanner.ListFindingTypeStatsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_finding_type_stats,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-websecurityscanner",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("WebSecurityScannerAsyncClient",)
