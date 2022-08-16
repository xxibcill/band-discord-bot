"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# Params defines the parameters for the bank module.
class Params(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SEND_ENABLED_FIELD_NUMBER: builtins.int
    DEFAULT_SEND_ENABLED_FIELD_NUMBER: builtins.int
    @property
    def send_enabled(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SendEnabled]: ...
    default_send_enabled: builtins.bool = ...
    def __init__(self,
        *,
        send_enabled : typing.Optional[typing.Iterable[global___SendEnabled]] = ...,
        default_send_enabled : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"default_send_enabled",b"default_send_enabled",u"send_enabled",b"send_enabled"]) -> None: ...
global___Params = Params

# SendEnabled maps coin denom to a send_enabled status (whether a denom is
# sendable).
class SendEnabled(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    denom: typing.Text = ...
    enabled: builtins.bool = ...
    def __init__(self,
        *,
        denom : typing.Text = ...,
        enabled : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denom",b"denom",u"enabled",b"enabled"]) -> None: ...
global___SendEnabled = SendEnabled

# Input models transaction input.
class Input(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text = ...
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        address : typing.Text = ...,
        coins : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"coins",b"coins"]) -> None: ...
global___Input = Input

# Output models transaction outputs.
class Output(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text = ...
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        address : typing.Text = ...,
        coins : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"coins",b"coins"]) -> None: ...
global___Output = Output

# Supply represents a struct that passively keeps track of the total supply
# amounts in the network.
# This message is deprecated now that supply is indexed by denom.
class Supply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_FIELD_NUMBER: builtins.int
    @property
    def total(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        total : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"total",b"total"]) -> None: ...
global___Supply = Supply

# DenomUnit represents a struct that describes a given
# denomination unit of the basic token.
class DenomUnit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    EXPONENT_FIELD_NUMBER: builtins.int
    ALIASES_FIELD_NUMBER: builtins.int
    # denom represents the string name of the given denom unit (e.g uatom).
    denom: typing.Text = ...
    # exponent represents power of 10 exponent that one must
    # raise the base_denom to in order to equal the given DenomUnit's denom
    # 1 denom = 1^exponent base_denom
    # (e.g. with a base_denom of uatom, one can create a DenomUnit of 'atom' with
    # exponent = 6, thus: 1 atom = 10^6 uatom).
    exponent: builtins.int = ...
    # aliases is a list of string aliases for the given denom
    @property
    def aliases(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        denom : typing.Text = ...,
        exponent : builtins.int = ...,
        aliases : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"aliases",b"aliases",u"denom",b"denom",u"exponent",b"exponent"]) -> None: ...
global___DenomUnit = DenomUnit

# Metadata represents a struct that describes
# a basic token.
class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DENOM_UNITS_FIELD_NUMBER: builtins.int
    BASE_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SYMBOL_FIELD_NUMBER: builtins.int
    description: typing.Text = ...
    # denom_units represents the list of DenomUnit's for a given coin
    @property
    def denom_units(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DenomUnit]: ...
    # base represents the base denom (should be the DenomUnit with exponent = 0).
    base: typing.Text = ...
    # display indicates the suggested denom that should be
    # displayed in clients.
    display: typing.Text = ...
    # name defines the name of the token (eg: Cosmos Atom)
    name: typing.Text = ...
    # symbol is the token symbol usually shown on exchanges (eg: ATOM). This can
    # be the same as the display.
    symbol: typing.Text = ...
    def __init__(self,
        *,
        description : typing.Text = ...,
        denom_units : typing.Optional[typing.Iterable[global___DenomUnit]] = ...,
        base : typing.Text = ...,
        display : typing.Text = ...,
        name : typing.Text = ...,
        symbol : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"base",b"base",u"denom_units",b"denom_units",u"description",b"description",u"display",b"display",u"name",b"name",u"symbol",b"symbol"]) -> None: ...
global___Metadata = Metadata
