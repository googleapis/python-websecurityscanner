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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1",
    manifest={
        "Form",
        "OutdatedLibrary",
        "ViolatingResource",
        "VulnerableParameters",
        "VulnerableHeaders",
        "Xss",
        "Xxe",
    },
)


class Form(proto.Message):
    r"""! Information about a vulnerability with an HTML.

    Attributes:
        action_uri (str):
            ! The URI where to send the form when it's
            submitted.
        fields (MutableSequence[str]):
            ! The names of form fields related to the
            vulnerability.
    """

    action_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class OutdatedLibrary(proto.Message):
    r"""Information reported for an outdated library.

    Attributes:
        library_name (str):
            The name of the outdated library.
        version (str):
            The version number.
        learn_more_urls (MutableSequence[str]):
            URLs to learn more information about the
            vulnerabilities in the library.
    """

    library_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    learn_more_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ViolatingResource(proto.Message):
    r"""Information regarding any resource causing the vulnerability
    such as JavaScript sources, image, audio files, etc.

    Attributes:
        content_type (str):
            The MIME type of this resource.
        resource_url (str):
            URL of this violating resource.
    """

    content_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_url: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VulnerableParameters(proto.Message):
    r"""Information about vulnerable request parameters.

    Attributes:
        parameter_names (MutableSequence[str]):
            The vulnerable parameter names.
    """

    parameter_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class VulnerableHeaders(proto.Message):
    r"""Information about vulnerable or missing HTTP Headers.

    Attributes:
        headers (MutableSequence[google.cloud.websecurityscanner_v1.types.VulnerableHeaders.Header]):
            List of vulnerable headers.
        missing_headers (MutableSequence[google.cloud.websecurityscanner_v1.types.VulnerableHeaders.Header]):
            List of missing headers.
    """

    class Header(proto.Message):
        r"""Describes a HTTP Header.

        Attributes:
            name (str):
                Header name.
            value (str):
                Header value.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    headers: MutableSequence[Header] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Header,
    )
    missing_headers: MutableSequence[Header] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Header,
    )


class Xss(proto.Message):
    r"""Information reported for an XSS.

    Attributes:
        stack_traces (MutableSequence[str]):
            Stack traces leading to the point where the
            XSS occurred.
        error_message (str):
            An error message generated by a javascript
            breakage.
        attack_vector (google.cloud.websecurityscanner_v1.types.Xss.AttackVector):
            The attack vector of the payload triggering
            this XSS.
        stored_xss_seeding_url (str):
            The reproduction url for the seeding POST
            request of a Stored XSS.
    """

    class AttackVector(proto.Enum):
        r"""Types of XSS attack vector."""
        ATTACK_VECTOR_UNSPECIFIED = 0
        LOCAL_STORAGE = 1
        SESSION_STORAGE = 2
        WINDOW_NAME = 3
        REFERRER = 4
        FORM_INPUT = 5
        COOKIE = 6
        POST_MESSAGE = 7
        GET_PARAMETERS = 8
        URL_FRAGMENT = 9
        HTML_COMMENT = 10
        POST_PARAMETERS = 11
        PROTOCOL = 12
        STORED_XSS = 13
        SAME_ORIGIN = 14
        USER_CONTROLLABLE_URL = 15

    stack_traces: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attack_vector: AttackVector = proto.Field(
        proto.ENUM,
        number=3,
        enum=AttackVector,
    )
    stored_xss_seeding_url: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Xxe(proto.Message):
    r"""Information reported for an XXE.

    Attributes:
        payload_value (str):
            The XML string that triggered the XXE
            vulnerability. Non-payload values might be
            redacted.
        payload_location (google.cloud.websecurityscanner_v1.types.Xxe.Location):
            Location within the request where the payload
            was placed.
    """

    class Location(proto.Enum):
        r"""Locations within a request where XML was substituted."""
        LOCATION_UNSPECIFIED = 0
        COMPLETE_REQUEST_BODY = 1

    payload_value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload_location: Location = proto.Field(
        proto.ENUM,
        number=2,
        enum=Location,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
