"""
* *******************************************************
* Copyright (c) VMware, Inc. 2019. All Rights Reserved.
* SPDX-License-Identifier: MIT
* *******************************************************
*
* DISCLAIMER. THIS PROGRAM IS PROVIDED TO YOU "AS IS" WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, WHETHER ORAL OR WRITTEN,
* EXPRESS OR IMPLIED. THE AUTHOR SPECIFICALLY DISCLAIMS ANY IMPLIED
* WARRANTIES OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY,
* NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
"""

__author__ = 'VMware, Inc.'
__vcenter_version__ = '6.7+'

import time
from com.vmware.vcenter.vm.guest_client import Power
from com.vmware.vcenter.vm.guest_client import Identity
from com.vmware.vapi.std.errors_client import (NotFound, ServiceUnavailable)
from qt_core import *
from logger.logger import Logger
import logging


# def wait_for_guest_info_ready(vsphere_client, vmId, timeout):
#     """
#     Waits for the Tools info to be ready, or times out.
#     """
#     print('Waiting for guest info to be ready.')
#     start = time.time()
#     timeout = start + timeout
#     while timeout > time.time():
#         logging.info('Waiting for guest info to be ready')
#         time.sleep(1)
#         try:
#             result = vsphere_client.vcenter.vm.guest.Identity.get(vmId)
#             break
#         except ServiceUnavailable as e:
#             logging.debug('Got ServiceUnavailable waiting for guest info')
#             pass
#         except Exception as e:
#             print('Unexpected exception %s waiting for guest info' % e)
#             raise e
#     if time.time() >= timeout:
#         raise Exception('Timed out waiting for guest info to be available.\n'
#                         'Be sure the VM has VMware Tools.')
#     else:
#         logging.info('Took %d seconds for guest info to be available'
#                      % (time.time() - start))


def wait_for_guest_power_state(vsphere_client, vmId, desiredState, timeout):
    """
    Waits for the guest to reach the desired power state, or times out.
    """

    Logger().write_log("Ожидаем статуса {} от {}".format(desiredState, vmId))
    start = time.time()
    timeout = start + timeout
    while timeout > time.time():
        time.sleep(5)
        curState = vsphere_client.vcenter.vm.guest.Power.get(vmId).state
        Logger().write_log('Текущее состояние машины - %s, требуется - %s'
                           % (curState, desiredState))
        if desiredState == curState:
            break
    if desiredState != curState:
        # raise Exception(
        #     f'Таймаут ожидания ответа, проверь машну {vmId} руками')
        pass
    else:
        Logger().write_log('Заняло %s секунд насмену статуса машины на %s'
                           % (time.time() - start, desiredState))


def wait_for_power_operations_state(vsphere_client, vmId, desiredState, timeout):
    """
    Waits for the desired soft power operations state, or times out.
    """
    Logger().write_log(
        'Ожидаем смены статуса питания машины {} на {}\n'.format(vmId, desiredState))
    start = time.time()
    timeout = start + timeout
    while timeout > time.time():
        time.sleep(5)
        curState = vsphere_client.vcenter.vm.guest.Power.get(
            vmId).operations_ready
        Logger().write_log('Текущая машина в статусе - %s, требуется %s' %
                           (curState, desiredState))
        if desiredState == curState:
            break
    if desiredState != curState:
        # raise Exception('Timed out waiting for guest to reach desired '
        #                 ' operations ready state')
        pass
    else:
        Logger().write_log('Заняло %s секунд насмену статуса машины на %s' %
                           (time.time() - start, desiredState))
