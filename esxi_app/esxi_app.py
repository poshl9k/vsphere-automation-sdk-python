import requests
import urllib3
from threading import Thread
# from com.vmware.vcenter.vm_client import Power as HardPower
from com.vmware.vcenter.vm.guest_client import Power
from vmware.vapi.vsphere.client import create_vsphere_client
from guest_helper import (wait_for_guest_power_state,
                          wait_for_power_operations_state)
from logger.logger import Logger


class On_off(object):
    session = requests.session()
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self):
        self.vsphere_client = create_vsphere_client(
            server='vc3.local1.ru', username='administrator@vs3.local1.ru', password='123qwe123***A!!!', session=self.session)
        # List all VMs inside the vCenter Server
        self.vmlist = self.vsphere_client.vcenter.VM.list()
        self.tag_id = None
        self.default_tag = "urn:vmomi:InventoryServiceTag:71851bd3-dac7-42b6-a7a8-6b1705684e1f:GLOBAL"
        self.tagged_vm = None
        # self.tagged_vm = self.get_vm_id_with_tag(self.tag_id)
        self.STATE_TIMEOUT = 300
        self.power_on = False
        self.power_off = False
        self.categorys_of_tags
        self.get_tag_categories
        self.get_all_tags
        self.onoff_category_id = "urn:vmomi:InventoryServiceCategory:3d434e91-9864-4a6f-844a-4f1aa1307f6a:GLOBAL"
        self.getonofftags

    @property
    def get_tag_categories(self):
        tag_categories = self.vsphere_client.tagging.Category.list()
        tags_in_category = []
        for tag in tag_categories:
            cat_name = self.vsphere_client.tagging.Category.get(tag).name
            tags_in_category.append(dict(id=tag, name=cat_name))
        return tags_in_category

    @property
    def get_all_tags(self):
        return self.get_tag_id(get_all=True)

    @property
    def categorys_of_tags(self):
        result = []
        for category in self.get_tag_categories:
            vmlist = self.vsphere_client.tagging.Tag.list_tags_for_category(
                category['id'])
            result.append(
                {'id': category['id'],
                 'name': category['name'],
                 'vms': vmlist
                 })
        return result

    @property
    def getonofftags(self):
        onoff_tags_id_list = self.vsphere_client.tagging.Tag.list_tags_for_category(
            self.onoff_category_id)
        result = []
        for id in onoff_tags_id_list:
            name = self.vsphere_client.tagging.Tag.get(id).name
            vms = self.get_vm_id_with_tag(id)
            result.append(dict(id=id, name=name, vms=vms))
        return result

    def get_tag_id(self, tagname=None, get_all=False):
        if tagname == None:
            tagname = self.default_tag
        taglist = self.vsphere_client.tagging.Tag.list()
        if get_all == True:
            names_and_ids = []
            for tagid in taglist:
                name = self.vsphere_client.tagging.Tag.get(tagid).name
                names_and_ids.append(dict(id=tagid, name=name))
            return names_and_ids
        else:
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
            # self.power_off = False
            self.vsphere_client.vcenter.vm.Power.start(vm)
            wait_for_power_operations_state(self.vsphere_client, vm,
                                            True, self.STATE_TIMEOUT)
            Logger().write_log("Включена машина {}.".format(vm))

        if self.power_off == True:
            # self.power_on = False
            self.vsphere_client.vcenter.vm.guest.Power.shutdown(vm)
            wait_for_guest_power_state(self.vsphere_client, vm,
                                       Power.State.NOT_RUNNING, self.STATE_TIMEOUT)
            Logger().write_log('Выключена машина({})'.format(vm))

        else:
            Logger().write_log("Нет команды включения/выключения")
