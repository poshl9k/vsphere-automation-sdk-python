# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2022 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.global_infra.settings.firewall.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class CpuMemThresholdsProfileBindingMaps(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.global_infra.settings.firewall.cpu_mem_thresholds_profile_binding_maps'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CpuMemThresholdsProfileBindingMapsStub)
        self._VAPI_OPERATION_IDS = {}


    def list(self,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        API will list all Firewall CPU Memory Thresholds Profile Binding Maps.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCPUMemThresholdsProfileBindingMapListResult`
        :return: com.vmware.nsx_policy.model.PolicyFirewallCPUMemThresholdsProfileBindingMapListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class CpuMemThresholdsProfiles(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.global_infra.settings.firewall.cpu_mem_thresholds_profiles'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CpuMemThresholdsProfilesStub)
        self._VAPI_OPERATION_IDS = {}


    def delete(self,
               profile_id,
               override=None,
               ):
        """
        Delete CPU and memory thresholds profile.

        :type  profile_id: :class:`str`
        :param profile_id: (required)
        :type  override: :class:`bool` or ``None``
        :param override: Locally override the global object (optional, default to false)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('delete',
                            {
                            'profile_id': profile_id,
                            'override': override,
                            })

    def get(self,
            profile_id,
            ):
        """
        Read the CPU and memory thresholds profile.

        :type  profile_id: :class:`str`
        :param profile_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCpuMemThresholdsProfile`
        :return: com.vmware.nsx_policy.model.PolicyFirewallCpuMemThresholdsProfile
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'profile_id': profile_id,
                            })

    def list(self,
             cursor=None,
             include_mark_for_delete_objects=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all CPU and memory thresholds profiles.

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  include_mark_for_delete_objects: :class:`bool` or ``None``
        :param include_mark_for_delete_objects: Include objects that are marked for deletion in results (optional,
            default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCpuMemThresholdsProfileListResult`
        :return: com.vmware.nsx_policy.model.PolicyFirewallCpuMemThresholdsProfileListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'cursor': cursor,
                            'include_mark_for_delete_objects': include_mark_for_delete_objects,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              profile_id,
              policy_firewall_cpu_mem_thresholds_profile,
              override=None,
              ):
        """
        Create or update CPU and memory thresholds profile.

        :type  profile_id: :class:`str`
        :param profile_id: (required)
        :type  policy_firewall_cpu_mem_thresholds_profile: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCpuMemThresholdsProfile`
        :param policy_firewall_cpu_mem_thresholds_profile: (required)
        :type  override: :class:`bool` or ``None``
        :param override: Locally override the global object (optional, default to false)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('patch',
                            {
                            'profile_id': profile_id,
                            'policy_firewall_cpu_mem_thresholds_profile': policy_firewall_cpu_mem_thresholds_profile,
                            'override': override,
                            })

    def update(self,
               profile_id,
               policy_firewall_cpu_mem_thresholds_profile,
               override=None,
               ):
        """
        Create or update CPU and memory thresholds profile.

        :type  profile_id: :class:`str`
        :param profile_id: (required)
        :type  policy_firewall_cpu_mem_thresholds_profile: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCpuMemThresholdsProfile`
        :param policy_firewall_cpu_mem_thresholds_profile: (required)
        :type  override: :class:`bool` or ``None``
        :param override: Locally override the global object (optional, default to false)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyFirewallCpuMemThresholdsProfile`
        :return: com.vmware.nsx_policy.model.PolicyFirewallCpuMemThresholdsProfile
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'profile_id': profile_id,
                            'policy_firewall_cpu_mem_thresholds_profile': policy_firewall_cpu_mem_thresholds_profile,
                            'override': override,
                            })
class Stats(VapiInterface):
    """
    
    """
    RESET_CATEGORY_DFW = "DFW"
    """
    Possible value for ``category`` of method :func:`Stats.reset`.

    """
    RESET_CATEGORY_EDGE = "EDGE"
    """
    Possible value for ``category`` of method :func:`Stats.reset`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.global_infra.settings.firewall.stats'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatsStub)
        self._VAPI_OPERATION_IDS = {}


    def reset(self,
              category,
              container_cluster_path=None,
              enforcement_point_path=None,
              ):
        """
        Sets firewall rule statistics counter to zero. This operation is
        supported for given category, for example: DFW i.e. for all layer3
        firewall (transport nodes only) rules or EDGE i.e. for all layer3 edge
        firewall (edge nodes only) rules. - no enforcement point path
        specified: On global manager, it is mandatory to give an enforcement
        point path. On local manager, reset of stats will be executed for each
        enforcement point. - {enforcement_point_path}: Reset of stats will be
        executed only for the given enforcement point.

        :type  category: :class:`str`
        :param category: Aggregation statistic category (required)
        :type  container_cluster_path: :class:`str` or ``None``
        :param container_cluster_path: String Path of the Container Cluster entity (optional)
        :type  enforcement_point_path: :class:`str` or ``None``
        :param enforcement_point_path: String Path of the enforcement point (optional)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('reset',
                            {
                            'category': category,
                            'container_cluster_path': container_cluster_path,
                            'enforcement_point_path': enforcement_point_path,
                            })
class _CpuMemThresholdsProfileBindingMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profile-binding-maps',
            path_variables={
            },
             header_parameters={
                         },
            query_parameters={
                'cursor': 'cursor',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCPUMemThresholdsProfileBindingMapListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.global_infra.settings.firewall.cpu_mem_thresholds_profile_binding_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _CpuMemThresholdsProfilesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'profile_id': type.StringType(),
            'override': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/{profile-id}',
            path_variables={
                'profile_id': 'profile-id',
            },
             header_parameters={
                 },
            query_parameters={
                'override': 'override',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'profile_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/{profile-id}',
            path_variables={
                'profile_id': 'profile-id',
            },
             header_parameters={
               },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'include_mark_for_delete_objects': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles',
            path_variables={
            },
             header_parameters={
                         },
            query_parameters={
                'cursor': 'cursor',
                'include_mark_for_delete_objects': 'include_mark_for_delete_objects',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'profile_id': type.StringType(),
            'policy_firewall_cpu_mem_thresholds_profile': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCpuMemThresholdsProfile'),
            'override': type.OptionalType(type.BooleanType()),
        })
        patch_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/{profile-id}',
            request_body_parameter='policy_firewall_cpu_mem_thresholds_profile',
            path_variables={
                'profile_id': 'profile-id',
            },
             header_parameters={
                   },
            query_parameters={
                'override': 'override',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'profile_id': type.StringType(),
            'policy_firewall_cpu_mem_thresholds_profile': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCpuMemThresholdsProfile'),
            'override': type.OptionalType(type.BooleanType()),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/{profile-id}',
            request_body_parameter='policy_firewall_cpu_mem_thresholds_profile',
            path_variables={
                'profile_id': 'profile-id',
            },
             header_parameters={
                   },
            query_parameters={
                'override': 'override',
            },
            content_type='application/json'
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCpuMemThresholdsProfile'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCpuMemThresholdsProfileListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyFirewallCpuMemThresholdsProfile'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.global_infra.settings.firewall.cpu_mem_thresholds_profiles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for reset operation
        reset_input_type = type.StructType('operation-input', {
            'category': type.StringType(),
            'container_cluster_path': type.OptionalType(type.StringType()),
            'enforcement_point_path': type.OptionalType(type.StringType()),
        })
        reset_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reset_input_value_validator_list = [
        ]
        reset_output_validator_list = [
        ]
        reset_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/global-infra/settings/firewall/stats?action=reset',
            path_variables={
            },
             header_parameters={
                   },
            query_parameters={
                'category': 'category',
                'container_cluster_path': 'container_cluster_path',
                'enforcement_point_path': 'enforcement_point_path',
            },
            content_type='application/json'
        )

        operations = {
            'reset': {
                'input_type': reset_input_type,
                'output_type': type.VoidType(),
                'errors': reset_error_dict,
                'input_value_validator_list': reset_input_value_validator_list,
                'output_validator_list': reset_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'reset': reset_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.global_infra.settings.firewall.stats',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'CpuMemThresholdsProfileBindingMaps': CpuMemThresholdsProfileBindingMaps,
        'CpuMemThresholdsProfiles': CpuMemThresholdsProfiles,
        'Stats': Stats,
    }

