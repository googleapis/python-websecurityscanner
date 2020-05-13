# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1beta/proto/finding_type_stats.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1beta/proto/finding_type_stats.proto",
    package="google.cloud.websecurityscanner.v1beta",
    syntax="proto3",
    serialized_options=b"\n*com.google.cloud.websecurityscanner.v1betaB\025FindingTypeStatsProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta",
    serialized_pb=b'\nEgoogle/cloud/websecurityscanner_v1beta/proto/finding_type_stats.proto\x12&google.cloud.websecurityscanner.v1beta"?\n\x10\x46indingTypeStats\x12\x14\n\x0c\x66inding_type\x18\x01 \x01(\t\x12\x15\n\rfinding_count\x18\x02 \x01(\x05\x42\xc8\x01\n*com.google.cloud.websecurityscanner.v1betaB\x15\x46indingTypeStatsProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1betab\x06proto3',
)


_FINDINGTYPESTATS = _descriptor.Descriptor(
    name="FindingTypeStats",
    full_name="google.cloud.websecurityscanner.v1beta.FindingTypeStats",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="finding_type",
            full_name="google.cloud.websecurityscanner.v1beta.FindingTypeStats.finding_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="finding_count",
            full_name="google.cloud.websecurityscanner.v1beta.FindingTypeStats.finding_count",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=113,
    serialized_end=176,
)

DESCRIPTOR.message_types_by_name["FindingTypeStats"] = _FINDINGTYPESTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindingTypeStats = _reflection.GeneratedProtocolMessageType(
    "FindingTypeStats",
    (_message.Message,),
    {
        "DESCRIPTOR": _FINDINGTYPESTATS,
        "__module__": "google.cloud.websecurityscanner_v1beta.proto.finding_type_stats_pb2",
        "__doc__": """A FindingTypeStats resource represents stats regarding a
  specific FindingType of Findings under a given ScanRun.
  
  
  Attributes:
      finding_type:
          The finding type associated with the stats.
      finding_count:
          The count of findings belonging to this finding type.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.FindingTypeStats)
    },
)
_sym_db.RegisterMessage(FindingTypeStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
