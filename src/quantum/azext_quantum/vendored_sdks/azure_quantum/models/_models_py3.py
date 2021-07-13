# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._quantum_client_enums import *


class BlobDetails(msrest.serialization.Model):
    """Blob details.

    All required parameters must be populated in order to send to Azure.

    :param container_name: Required. The container name.
    :type container_name: str
    :param blob_name: The blob name.
    :type blob_name: str
    """

    _validation = {
        'container_name': {'required': True},
    }

    _attribute_map = {
        'container_name': {'key': 'containerName', 'type': 'str'},
        'blob_name': {'key': 'blobName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        container_name: str,
        blob_name: Optional[str] = None,
        **kwargs
    ):
        super(BlobDetails, self).__init__(**kwargs)
        self.container_name = container_name
        self.blob_name = blob_name


class ErrorData(msrest.serialization.Model):
    """An error response from Azure.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable for displaying in a
     user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorData, self).__init__(**kwargs)
        self.code = code
        self.message = message


class JobDetails(msrest.serialization.Model):
    """Job details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: The job id.
    :type id: str
    :param name: The job name. Is not required for the name to be unique and it's only used for
     display purposes.
    :type name: str
    :param container_uri: Required. The blob container SAS uri, the container is used to host job
     data.
    :type container_uri: str
    :param input_data_uri: The input blob SAS uri, if specified, it will override the default input
     blob in the container.
    :type input_data_uri: str
    :param input_data_format: Required. The format of the input data.
    :type input_data_format: str
    :param input_params: The input parameters for the job. JSON object used by the target solver.
     It is expected that the size of this object is small and only used to specify parameters for
     the execution target, not the input data.
    :type input_params: any
    :param provider_id: Required. The unique identifier for the provider.
    :type provider_id: str
    :param target: Required. The target identifier to run the job.
    :type target: str
    :param metadata: The job metadata. Metadata provides client the ability to store
     client-specific information.
    :type metadata: dict[str, str]
    :param output_data_uri: The output blob SAS uri. When a job finishes successfully, results will
     be uploaded to this blob.
    :type output_data_uri: str
    :param output_data_format: The format of the output data.
    :type output_data_format: str
    :ivar status: The job status. Possible values include: "Waiting", "Executing", "Succeeded",
     "Failed", "Cancelled".
    :vartype status: str or ~azure.quantum.models.JobStatus
    :ivar creation_time: The creation time of the job.
    :vartype creation_time: ~datetime.datetime
    :ivar begin_execution_time: The time when the job began execution.
    :vartype begin_execution_time: ~datetime.datetime
    :ivar end_execution_time: The time when the job finished execution.
    :vartype end_execution_time: ~datetime.datetime
    :ivar cancellation_time: The time when a job was successfully cancelled.
    :vartype cancellation_time: ~datetime.datetime
    :ivar error_data: The error data for the job. This is expected only when Status 'Failed'.
    :vartype error_data: ~azure.quantum.models.ErrorData
    """

    _validation = {
        'container_uri': {'required': True},
        'input_data_format': {'required': True},
        'provider_id': {'required': True},
        'target': {'required': True},
        'status': {'readonly': True},
        'creation_time': {'readonly': True},
        'begin_execution_time': {'readonly': True},
        'end_execution_time': {'readonly': True},
        'cancellation_time': {'readonly': True},
        'error_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'container_uri': {'key': 'containerUri', 'type': 'str'},
        'input_data_uri': {'key': 'inputDataUri', 'type': 'str'},
        'input_data_format': {'key': 'inputDataFormat', 'type': 'str'},
        'input_params': {'key': 'inputParams', 'type': 'object'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
        'output_data_uri': {'key': 'outputDataUri', 'type': 'str'},
        'output_data_format': {'key': 'outputDataFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'begin_execution_time': {'key': 'beginExecutionTime', 'type': 'iso-8601'},
        'end_execution_time': {'key': 'endExecutionTime', 'type': 'iso-8601'},
        'cancellation_time': {'key': 'cancellationTime', 'type': 'iso-8601'},
        'error_data': {'key': 'errorData', 'type': 'ErrorData'},
    }

    def __init__(
        self,
        *,
        container_uri: str,
        input_data_format: str,
        provider_id: str,
        target: str,
        id: Optional[str] = None,
        name: Optional[str] = None,
        input_data_uri: Optional[str] = None,
        input_params: Optional[Any] = None,
        metadata: Optional[Dict[str, str]] = None,
        output_data_uri: Optional[str] = None,
        output_data_format: Optional[str] = None,
        **kwargs
    ):
        super(JobDetails, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.container_uri = container_uri
        self.input_data_uri = input_data_uri
        self.input_data_format = input_data_format
        self.input_params = input_params
        self.provider_id = provider_id
        self.target = target
        self.metadata = metadata
        self.output_data_uri = output_data_uri
        self.output_data_format = output_data_format
        self.status = None
        self.creation_time = None
        self.begin_execution_time = None
        self.end_execution_time = None
        self.cancellation_time = None
        self.error_data = None


class JobDetailsList(msrest.serialization.Model):
    """List of job details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum.models.JobDetails]
    :param count: Total records count number.
    :type count: long
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[JobDetails]'},
        'count': {'key': 'count', 'type': 'long'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        **kwargs
    ):
        super(JobDetailsList, self).__init__(**kwargs)
        self.value = None
        self.count = count
        self.next_link = None


class ProviderStatus(msrest.serialization.Model):
    """Providers status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Provider id.
    :vartype id: str
    :ivar current_availability: Provider availability. Possible values include: "Available",
     "Degraded", "Unavailable".
    :vartype current_availability: str or ~azure.quantum.models.ProviderAvailability
    :ivar targets:
    :vartype targets: list[~azure.quantum.models.TargetStatus]
    """

    _validation = {
        'id': {'readonly': True},
        'current_availability': {'readonly': True},
        'targets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_availability': {'key': 'currentAvailability', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[TargetStatus]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderStatus, self).__init__(**kwargs)
        self.id = None
        self.current_availability = None
        self.targets = None


class ProviderStatusList(msrest.serialization.Model):
    """Providers status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum.models.ProviderStatus]
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ProviderStatus]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderStatusList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class Quota(msrest.serialization.Model):
    """Quota information.

    :param dimension: The name of the dimension associated with the quota.
    :type dimension: str
    :param scope: The scope at which the quota is applied. Possible values include: "Workspace",
     "Subscription".
    :type scope: str or ~azure.quantum.models.DimensionScope
    :param provider_id: The unique identifier for the provider.
    :type provider_id: str
    :param utilization: The amount of the usage that has been applied for the current period.
    :type utilization: float
    :param holds: The amount of the usage that has been reserved but not applied for the current
     period.
    :type holds: float
    :param limit: The maximum amount of usage allowed for the current period.
    :type limit: float
    :param period: The time period in which the quota's underlying meter is accumulated. Based on
     calendar year. 'None' is used for concurrent quotas. Possible values include: "None",
     "Monthly".
    :type period: str or ~azure.quantum.models.MeterPeriod
    """

    _attribute_map = {
        'dimension': {'key': 'dimension', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'utilization': {'key': 'utilization', 'type': 'float'},
        'holds': {'key': 'holds', 'type': 'float'},
        'limit': {'key': 'limit', 'type': 'float'},
        'period': {'key': 'period', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        dimension: Optional[str] = None,
        scope: Optional[Union[str, "DimensionScope"]] = None,
        provider_id: Optional[str] = None,
        utilization: Optional[float] = None,
        holds: Optional[float] = None,
        limit: Optional[float] = None,
        period: Optional[Union[str, "MeterPeriod"]] = None,
        **kwargs
    ):
        super(Quota, self).__init__(**kwargs)
        self.dimension = dimension
        self.scope = scope
        self.provider_id = provider_id
        self.utilization = utilization
        self.holds = holds
        self.limit = limit
        self.period = period


class QuotaList(msrest.serialization.Model):
    """List of quotas.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum.models.Quota]
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Quota]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuotaList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class RestError(msrest.serialization.Model):
    """Error information returned by the API.

    :param error: An error response from Azure.
    :type error: ~azure.quantum.models.ErrorData
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorData'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorData"] = None,
        **kwargs
    ):
        super(RestError, self).__init__(**kwargs)
        self.error = error


class SasUriResponse(msrest.serialization.Model):
    """Get SAS URL operation response.

    :param sas_uri: A URL with a SAS token to upload a blob for execution in the given workspace.
    :type sas_uri: str
    """

    _attribute_map = {
        'sas_uri': {'key': 'sasUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        sas_uri: Optional[str] = None,
        **kwargs
    ):
        super(SasUriResponse, self).__init__(**kwargs)
        self.sas_uri = sas_uri


class TargetStatus(msrest.serialization.Model):
    """Target status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Target id.
    :vartype id: str
    :ivar current_availability: Target availability. Possible values include: "Available",
     "Degraded", "Unavailable".
    :vartype current_availability: str or ~azure.quantum.models.TargetAvailability
    :ivar average_queue_time: Average queue time in seconds.
    :vartype average_queue_time: long
    :ivar status_page: A page with detailed status of the provider.
    :vartype status_page: str
    """

    _validation = {
        'id': {'readonly': True},
        'current_availability': {'readonly': True},
        'average_queue_time': {'readonly': True},
        'status_page': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_availability': {'key': 'currentAvailability', 'type': 'str'},
        'average_queue_time': {'key': 'averageQueueTime', 'type': 'long'},
        'status_page': {'key': 'statusPage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TargetStatus, self).__init__(**kwargs)
        self.id = None
        self.current_availability = None
        self.average_queue_time = None
        self.status_page = None