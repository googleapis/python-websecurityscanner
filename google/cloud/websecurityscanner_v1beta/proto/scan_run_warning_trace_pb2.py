# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1beta/proto/scan_run_warning_trace.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1beta/proto/scan_run_warning_trace.proto",
    package="google.cloud.websecurityscanner.v1beta",
    syntax="proto3",
    serialized_options=b"\n*com.google.cloud.websecurityscanner.v1betaB\030ScanRunWarningTraceProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nIgoogle/cloud/websecurityscanner_v1beta/proto/scan_run_warning_trace.proto\x12&google.cloud.websecurityscanner.v1beta"\xed\x01\n\x13ScanRunWarningTrace\x12N\n\x04\x63ode\x18\x01 \x01(\x0e\x32@.google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace.Code"\x85\x01\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aINSUFFICIENT_CRAWL_RESULTS\x10\x01\x12\x1a\n\x16TOO_MANY_CRAWL_RESULTS\x10\x02\x12\x17\n\x13TOO_MANY_FUZZ_TASKS\x10\x03\x12\x12\n\x0e\x42LOCKED_BY_IAP\x10\x04\x42\xcb\x01\n*com.google.cloud.websecurityscanner.v1betaB\x18ScanRunWarningTraceProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1betab\x06proto3',
)


_SCANRUNWARNINGTRACE_CODE = _descriptor.EnumDescriptor(
    name="Code",
    full_name="google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace.Code",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INSUFFICIENT_CRAWL_RESULTS",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOO_MANY_CRAWL_RESULTS",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOO_MANY_FUZZ_TASKS",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BLOCKED_BY_IAP",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=222,
    serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_SCANRUNWARNINGTRACE_CODE)


_SCANRUNWARNINGTRACE = _descriptor.Descriptor(
    name="ScanRunWarningTrace",
    full_name="google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace.code",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SCANRUNWARNINGTRACE_CODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=118,
    serialized_end=355,
)

_SCANRUNWARNINGTRACE.fields_by_name["code"].enum_type = _SCANRUNWARNINGTRACE_CODE
_SCANRUNWARNINGTRACE_CODE.containing_type = _SCANRUNWARNINGTRACE
DESCRIPTOR.message_types_by_name["ScanRunWarningTrace"] = _SCANRUNWARNINGTRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRunWarningTrace = _reflection.GeneratedProtocolMessageType(
    "ScanRunWarningTrace",
    (_message.Message,),
    {
        "DESCRIPTOR": _SCANRUNWARNINGTRACE,
        "__module__": "google.cloud.websecurityscanner_v1beta.proto.scan_run_warning_trace_pb2",
        "__doc__": """Output only. Defines a warning trace message for ScanRun. Warning
  traces provide customers with useful information that helps make the
  scanning process more effective.
  Attributes:
      code:
          Indicates the warning code.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace)
    },
)
_sym_db.RegisterMessage(ScanRunWarningTrace)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
