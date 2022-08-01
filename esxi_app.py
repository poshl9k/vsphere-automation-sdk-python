import requests
import urllib3
from threading import Thread
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.cis.tagging_client import (Category, CategoryModel, Tag,
                                           TagAssociation)
from com.vmware.vcenter.vm_client import Power as HardPower
from com.vmware.vapi.std.errors_client import (NotFound, ServiceUnavailable)
from com.vmware.vcenter.vm.guest_client import Power
from com.vmware.vcenter.vm.guest_client import Identity
from vmware.vapi.vsphere.client import create_vsphere_client
from samples.vsphere.common.sample_util import parse_cli_args_vm
from samples.vsphere.common.sample_util import pp
from samples.vsphere.vcenter.setup import testbed
from samples.vsphere.vcenter.helper.vm_helper import get_vm
from samples.vsphere.common.ssl_helper import get_unverified_session
from samples.vsphere.vcenter.helper.guest_helper import \
    (wait_for_guest_info_ready, wait_for_guest_power_state,
        wait_for_power_operations_state)


class On_off(object):

    session = requests.session()
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self):
        self.vsphere_client = create_vsphere_client(
            server='vc3.local1.ru', username='administrator@vs3.local1.ru', password='123qwe123***A!!!', session=self.session)
        # List all VMs inside the vCenter Server
        self.vmlist = self.vsphere_client.vcenter.VM.list()
        self.tag_id = self.get_tag_id("onoff-test")
        self.tagged_vm = self.get_vm_id_with_tag(self.tag_id)
        self.STATE_TIMEOUT = 300
        self.power_on = False
        self.power_off = False

    def get_tag_id(self, tagname):
        taglist = self.vsphere_client.tagging.Tag.list()
        for tagid in taglist:
            t = self.vsphere_client.tagging.Tag.get(tagid).name
            if t == tagname:
                return tagid

    def get_vm_id_with_tag(self, tagid):
        return self.vsphere_client.tagging.TagAssociation.list_attached_objects(tagid)

    def power_state_vms(self, vmlist):

        for vm in vmlist:
            thr = Thread(target=self.work, args=[vm, ])
            thr.daemon = True
            thr.start()

    def work(self, vm):
        if self.power_on == True:
            self.vsphere_client.vcenter.vm.Power.start(vm)
            wait_for_power_operations_state(self.vsphere_client, vm,
                                            True, self.STATE_TIMEOUT)
            print("Shutting down VM {}.".format(vm))
        elif self.power_off == True:
            self.vsphere_client.vcenter.vm.guest.Power.shutdown(vm)
            wait_for_guest_power_state(self.vsphere_client, vm,
                                       Power.State.NOT_RUNNING, self.STATE_TIMEOUT)
            print('vm.guest.Power.shutdown({})'.format(vm))
        else:
            print("Нет команды включения/выключения")


a = On_off()
a.power_on = True
taggedvm = [x.id for x in a.tagged_vm]
a.power_state_vms(taggedvm)
pass
