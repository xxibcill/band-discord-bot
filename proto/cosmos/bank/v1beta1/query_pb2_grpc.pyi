"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .query_pb2 import *
# Query defines the gRPC querier service.
class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Balance queries the balance of a single coin for a single account.
    Balance:grpc.UnaryUnaryMultiCallable[
        global___QueryBalanceRequest,
        global___QueryBalanceResponse] = ...

    # AllBalances queries the balance of all coins for a single account.
    AllBalances:grpc.UnaryUnaryMultiCallable[
        global___QueryAllBalancesRequest,
        global___QueryAllBalancesResponse] = ...

    # TotalSupply queries the total supply of all coins.
    TotalSupply:grpc.UnaryUnaryMultiCallable[
        global___QueryTotalSupplyRequest,
        global___QueryTotalSupplyResponse] = ...

    # SupplyOf queries the supply of a single coin.
    SupplyOf:grpc.UnaryUnaryMultiCallable[
        global___QuerySupplyOfRequest,
        global___QuerySupplyOfResponse] = ...

    # Params queries the parameters of x/bank module.
    Params:grpc.UnaryUnaryMultiCallable[
        global___QueryParamsRequest,
        global___QueryParamsResponse] = ...

    # DenomsMetadata queries the client metadata of a given coin denomination.
    DenomMetadata:grpc.UnaryUnaryMultiCallable[
        global___QueryDenomMetadataRequest,
        global___QueryDenomMetadataResponse] = ...

    # DenomsMetadata queries the client metadata for all registered coin denominations.
    DenomsMetadata:grpc.UnaryUnaryMultiCallable[
        global___QueryDenomsMetadataRequest,
        global___QueryDenomsMetadataResponse] = ...


# Query defines the gRPC querier service.
class QueryServicer(metaclass=abc.ABCMeta):
    # Balance queries the balance of a single coin for a single account.
    @abc.abstractmethod
    def Balance(self,
        request: global___QueryBalanceRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryBalanceResponse: ...

    # AllBalances queries the balance of all coins for a single account.
    @abc.abstractmethod
    def AllBalances(self,
        request: global___QueryAllBalancesRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryAllBalancesResponse: ...

    # TotalSupply queries the total supply of all coins.
    @abc.abstractmethod
    def TotalSupply(self,
        request: global___QueryTotalSupplyRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryTotalSupplyResponse: ...

    # SupplyOf queries the supply of a single coin.
    @abc.abstractmethod
    def SupplyOf(self,
        request: global___QuerySupplyOfRequest,
        context: grpc.ServicerContext,
    ) -> global___QuerySupplyOfResponse: ...

    # Params queries the parameters of x/bank module.
    @abc.abstractmethod
    def Params(self,
        request: global___QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryParamsResponse: ...

    # DenomsMetadata queries the client metadata of a given coin denomination.
    @abc.abstractmethod
    def DenomMetadata(self,
        request: global___QueryDenomMetadataRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryDenomMetadataResponse: ...

    # DenomsMetadata queries the client metadata for all registered coin denominations.
    @abc.abstractmethod
    def DenomsMetadata(self,
        request: global___QueryDenomsMetadataRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryDenomsMetadataResponse: ...


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...