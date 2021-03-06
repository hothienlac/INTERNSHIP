# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: picture.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='picture.proto',
  package='picture',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rpicture.proto\x12\x07picture\"\x1a\n\x07Picture\x12\x0f\n\x07picture\x18\x01 \x01(\t\"\x14\n\x04Pose\x12\x0c\n\x04pose\x18\x01 \x01(\t27\n\x07GetPose\x12,\n\x07getPose\x12\x10.picture.Picture\x1a\r.picture.Pose\"\x00\x62\x06proto3'
)




_PICTURE = _descriptor.Descriptor(
  name='Picture',
  full_name='picture.Picture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='picture', full_name='picture.Picture.picture', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=52,
)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='picture.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='picture.Pose.pose', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['Picture'] = _PICTURE
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Picture = _reflection.GeneratedProtocolMessageType('Picture', (_message.Message,), {
  'DESCRIPTOR' : _PICTURE,
  '__module__' : 'picture_pb2'
  # @@protoc_insertion_point(class_scope:picture.Picture)
  })
_sym_db.RegisterMessage(Picture)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'picture_pb2'
  # @@protoc_insertion_point(class_scope:picture.Pose)
  })
_sym_db.RegisterMessage(Pose)



_GETPOSE = _descriptor.ServiceDescriptor(
  name='GetPose',
  full_name='picture.GetPose',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=131,
  methods=[
  _descriptor.MethodDescriptor(
    name='getPose',
    full_name='picture.GetPose.getPose',
    index=0,
    containing_service=None,
    input_type=_PICTURE,
    output_type=_POSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETPOSE)

DESCRIPTOR.services_by_name['GetPose'] = _GETPOSE

# @@protoc_insertion_point(module_scope)
