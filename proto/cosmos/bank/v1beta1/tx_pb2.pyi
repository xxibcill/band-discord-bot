"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.bank.v1beta1.bank_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# MsgSend represents a message to send coins from one account to another.
class MsgSend(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FROM_ADDRESS_FIELD_NUMBER: builtins.int
    TO_ADDRESS_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    from_address: typing.Text = ...
    to_address: typing.Text = ...
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        from_address : typing.Text = ...,
        to_address : typing.Text = ...,
        amount : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"amount",b"amount",u"from_address",b"from_address",u"to_address",b"to_address"]) -> None: ...
global___MsgSend = MsgSend

# MsgSendResponse defines the Msg/Send response type.
class MsgSendResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgSendResponse = MsgSendResponse

# MsgMultiSend represents an arbitrary multi-in, multi-out send message.
class MsgMultiSend(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.bank.v1beta1.bank_pb2.Input]: ...
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.bank.v1beta1.bank_pb2.Output]: ...
    def __init__(self,
        *,
        inputs : typing.Optional[typing.Iterable[cosmos.bank.v1beta1.bank_pb2.Input]] = ...,
        outputs : typing.Optional[typing.Iterable[cosmos.bank.v1beta1.bank_pb2.Output]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"inputs",b"inputs",u"outputs",b"outputs"]) -> None: ...
global___MsgMultiSend = MsgMultiSend

# MsgMultiSendResponse defines the Msg/MultiSend response type.
class MsgMultiSendResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgMultiSendResponse = MsgMultiSendResponse