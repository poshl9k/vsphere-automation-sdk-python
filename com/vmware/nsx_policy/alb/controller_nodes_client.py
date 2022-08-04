# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2022 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.alb.controller_nodes.
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


class Cluster(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.alb.controller_nodes.cluster'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Returns information about Advanced Load Balancer controller cluster
        status


        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerClusterInfo`
        :return: com.vmware.nsx_policy.model.ALBControllerClusterInfo
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
        return self._invoke('get', None)

    def update(self):
        """
        Re-trigger clustering for Advanced Load Balancer Nodes.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerClusterTrigger`
        :return: com.vmware.nsx_policy.model.ALBControllerClusterTrigger
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
        return self._invoke('update', None)
class Clusterconfig(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.alb.controller_nodes.clusterconfig'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterconfigStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               a_lb_controller_node_vm_cluster_config,
               ):
        """
        Set the cluster configuration for Advanced Load Balancer controller
        cluster.

        :type  a_lb_controller_node_vm_cluster_config: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMClusterConfig`
        :param a_lb_controller_node_vm_cluster_config: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMClusterConfig`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMClusterConfig
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
        return self._invoke('create',
                            {
                            'a_lb_controller_node_vm_cluster_config': a_lb_controller_node_vm_cluster_config,
                            })

    def get(self):
        """
        Returns cluster configuration for the Advanced Load Balancer controller
        cluster.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMClusterConfig`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMClusterConfig
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
        return self._invoke('get', None)
class Deployments(VapiInterface):
    """
    
    """
    LIST_STATE_DEPLOYED = "DEPLOYED"
    """
    Possible value for ``state`` of method :func:`Deployments.list`.

    """
    LIST_STATE_PENDING = "PENDING"
    """
    Possible value for ``state`` of method :func:`Deployments.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.alb.controller_nodes.deployments'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DeploymentsStub)
        self._VAPI_OPERATION_IDS = {}


    def create(self,
               add_alb_controller_node_vm_info,
               ):
        """
        Deploys a Advanced Load Balancer controller node VM as specified by the
        deployment config.

        :type  add_alb_controller_node_vm_info: :class:`com.vmware.nsx_policy.model_client.AddALBControllerNodeVMInfo`
        :param add_alb_controller_node_vm_info: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMDeploymentRequestList`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMDeploymentRequestList
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
        return self._invoke('create',
                            {
                            'add_alb_controller_node_vm_info': add_alb_controller_node_vm_info,
                            })

    def delete(self,
               node_id,
               force_delete=None,
               inaccessible=None,
               ):
        """
        Attempts to unregister and undeploy a specified auto-deployed cluster
        node VM. If it is a member of a cluster, then the VM will be
        automatically detached from the cluster before being unregistered and
        undeployed. Alternatively, if the original deployment attempt failed or
        the VM is not found, cleans up the deployment information associated
        with the deployment attempt. Note: If a VM has been successfully
        auto-deployed, then the associated deployment information will not be
        deleted unless and until the VM is successfully deleted.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  force_delete: :class:`bool` or ``None``
        :param force_delete: Delete by force (optional)
        :type  inaccessible: :class:`str` or ``None``
        :param inaccessible: Delete when controller is inaccessible (optional)
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
                            'node_id': node_id,
                            'force_delete': force_delete,
                            'inaccessible': inaccessible,
                            })

    def get(self,
            node_id,
            ):
        """
        Returns deployment request information for a specific attempted
        deployment of a cluster node VM.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMDeploymentRequest`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMDeploymentRequest
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
                            'node_id': node_id,
                            })

    def list(self,
             state=None,
             ):
        """
        Returns request information for every attempted deployment of a cluster
        node VM.

        :type  state: :class:`str` or ``None``
        :param state: the current state of the Advanced Load Balancer controller VM
            (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMDeploymentRequestList`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMDeploymentRequestList
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
                            'state': state,
                            })

    def update(self,
               node_id,
               a_lb_controller_node_vm_deployment_request,
               running_config=None,
               ):
        """
        Update Advanced Load Balancer Controller node VM details

        :type  node_id: :class:`str`
        :param node_id: (required)
        :type  a_lb_controller_node_vm_deployment_request: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMDeploymentRequest`
        :param a_lb_controller_node_vm_deployment_request: (required)
        :type  running_config: :class:`bool` or ``None``
        :param running_config: Update Advanced Load Balancer Controller runtime config as well
            (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeVMDeploymentRequest`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeVMDeploymentRequest
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
                            'node_id': node_id,
                            'a_lb_controller_node_vm_deployment_request': a_lb_controller_node_vm_deployment_request,
                            'running_config': running_config,
                            })
class FormFactors(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.alb.controller_nodes.form_factors'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FormFactorsStub)
        self._VAPI_OPERATION_IDS = {}


    def get(self):
        """
        Returns information about all form factors available for Advanced Load
        Balancer controller nodes.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ALBControllerNodeFormFactors`
        :return: com.vmware.nsx_policy.model.ALBControllerNodeFormFactors
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
        return self._invoke('get', None)
class _ClusterStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/alb/controller-nodes/cluster',
            path_variables={
            },
             header_parameters={
             },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {})
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/alb/controller-nodes/cluster',
            path_variables={
            },
             header_parameters={
             },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerClusterInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerClusterTrigger'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.alb.controller_nodes.cluster',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ClusterconfigStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'a_LB_controller_node_VM_cluster_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMClusterConfig'),
        })
        create_error_dict = {
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
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/alb/controller-nodes/clusterconfig',
            request_body_parameter='a_LB_controller_node_VM_cluster_config',
            path_variables={
            },
             header_parameters={
               },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/alb/controller-nodes/clusterconfig',
            path_variables={
            },
             header_parameters={
             },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMClusterConfig'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMClusterConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.alb.controller_nodes.clusterconfig',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _DeploymentsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'add_ALB_controller_node_VM_info': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AddALBControllerNodeVMInfo'),
        })
        create_error_dict = {
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
        create_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/alb/controller-nodes/deployments',
            request_body_parameter='add_ALB_controller_node_VM_info',
            path_variables={
            },
             header_parameters={
               },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'force_delete': type.OptionalType(type.BooleanType()),
            'inaccessible': type.OptionalType(type.StringType()),
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
            http_method='POST',
            url_template='/policy/api/v1/alb/controller-nodes/deployments/{node-id}?action=delete',
            path_variables={
                'node_id': 'node-id',
            },
             header_parameters={
                   },
            query_parameters={
                'force_delete': 'force_delete',
                'inaccessible': 'inaccessible',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/policy/api/v1/alb/controller-nodes/deployments/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
             header_parameters={
               },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'state': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/alb/controller-nodes/deployments',
            path_variables={
            },
             header_parameters={
               },
            query_parameters={
                'state': 'state',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'a_LB_controller_node_VM_deployment_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMDeploymentRequest'),
            'running_config': type.OptionalType(type.BooleanType()),
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
            url_template='/policy/api/v1/alb/controller-nodes/deployments/{node-id}',
            request_body_parameter='a_LB_controller_node_VM_deployment_request',
            path_variables={
                'node_id': 'node-id',
            },
             header_parameters={
                   },
            query_parameters={
                'running_config': 'running_config',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMDeploymentRequestList'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMDeploymentRequest'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMDeploymentRequestList'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeVMDeploymentRequest'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.alb.controller_nodes.deployments',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _FormFactorsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/alb/controller-nodes/form-factors',
            path_variables={
            },
             header_parameters={
             },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ALBControllerNodeFormFactors'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.alb.controller_nodes.form_factors',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Cluster': Cluster,
        'Clusterconfig': Clusterconfig,
        'Deployments': Deployments,
        'FormFactors': FormFactors,
        'deployments': 'com.vmware.nsx_policy.alb.controller_nodes.deployments_client.StubFactory',
    }

