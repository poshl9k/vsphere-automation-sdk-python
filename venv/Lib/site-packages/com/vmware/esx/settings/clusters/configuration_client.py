# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2022 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.esx.settings.clusters.configuration.
#---------------------------------------------------------------------------

"""
The ``com.vmware.esx.settings.clusters.configuration_client`` module provides
classes to manage the configuration of an ESX cluster. The
``com.vmware.esx.settings.clusters.configuration.reports_client`` module
provides classes for accessing reports regarding the configuration state of the
cluster.

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


class DraftImportResult(VapiStruct):
    """
    The ``DraftImportResult`` class contains attributes that describe the
    result of importing the desired configuration for a cluster into a draft.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'status',
            {
                'OK' : [('draft', True)],
                'ERROR' : [('error', True)],
                'RUNNING' : [],
                'CANCELED' : [],
            }
        ),
    ]



    def __init__(self,
                 status=None,
                 draft=None,
                 error=None,
                 warnings=None,
                ):
        """
        :type  status: :class:`DraftImportResult.Status`
        :param status: Status of importing desired configuration.
        :type  draft: :class:`str`
        :param draft: This identifier refers to the commit action of importing the
            desired configuration document. This identifier can be used in the
            apply API.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.esx.settings.draft``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.esx.settings.draft``.
            This attribute is optional and it is only relevant when the value
            of ``status`` is :attr:`DraftImportResult.Status.OK`.
        :type  error: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param error: Localized message describing the error encountered while importing
            desired configuration. The import operation will fail if the
            configuration document is an invalid JSON.
            This attribute is optional and it is only relevant when the value
            of ``status`` is :attr:`DraftImportResult.Status.ERROR`.
        :type  warnings: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
        :param warnings: Any issues found during the import are reported in this list.
        """
        self.status = status
        self.draft = draft
        self.error = error
        self.warnings = warnings
        VapiStruct.__init__(self)


    class Status(Enum):
        """
        The ``DraftImportResult.Status`` class contains the possible status codes
        describing the result of importing desired configuration for a cluster.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        RUNNING = None
        """
        The task is in-progress.

        """
        OK = None
        """
        Desired configuration imported successfully.

        """
        ERROR = None
        """
        Desired configuration import failed with error.

        """
        CANCELED = None
        """


        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('RUNNING'),
        Status('OK'),
        Status('ERROR'),
        Status('CANCELED'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.esx.settings.clusters.configuration.draft_import_result.status',
        Status))

DraftImportResult._set_binding_type(type.StructType(
    'com.vmware.esx.settings.clusters.configuration.draft_import_result', {
        'status': type.ReferenceType(__name__, 'DraftImportResult.Status'),
        'draft': type.OptionalType(type.IdType()),
        'error': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'warnings': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'))),
    },
    DraftImportResult,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

