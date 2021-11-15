# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import StoragePoolManagementConfiguration
from .operations import Operations
from .operations import DiskPoolsOperations
from .operations import DiskPoolZonesOperations
from .operations import ResourceSkusOperations
from .operations import IscsiTargetsOperations
from . import models


class StoragePoolManagement(object):
    """StoragePoolManagement.

    :ivar operations: Operations operations
    :vartype operations: storage_pool_management.operations.Operations
    :ivar disk_pools: DiskPoolsOperations operations
    :vartype disk_pools: storage_pool_management.operations.DiskPoolsOperations
    :ivar disk_pool_zones: DiskPoolZonesOperations operations
    :vartype disk_pool_zones: storage_pool_management.operations.DiskPoolZonesOperations
    :ivar resource_skus: ResourceSkusOperations operations
    :vartype resource_skus: storage_pool_management.operations.ResourceSkusOperations
    :ivar iscsi_targets: IscsiTargetsOperations operations
    :vartype iscsi_targets: storage_pool_management.operations.IscsiTargetsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StoragePoolManagementConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disk_pools = DiskPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disk_pool_zones = DiskPoolZonesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_skus = ResourceSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iscsi_targets = IscsiTargetsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> StoragePoolManagement
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
