import time
from logger.logger import Logger
import logging

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
