import requests
import urllib3
from threading import Thread
from . import *
from vmware.vapi.vsphere.client import create_vsphere_client
from logger.logger import Logger
import time


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
        allvms = self.vsphere_client.vcenter.VM.list()
        for vm in vmlist:
            for vm_id in allvms:
                if vm in vm_id.vm:
                    vm_name = vm_id.name
                    pass
            thr = Thread(target=self.work, args=[vm, vm_name])
            thr.daemon = True
            thr.start()

    def work(self, vm, vm_name):
        if self.power_on == True:
            chk_thr = Thread(target=self.check_vm_state,
                             args=[vm, "power_up", vm_name])
        if self.power_off == True:
            chk_thr = Thread(target=self.check_vm_state,
                             args=[vm, "shutdown", vm_name])

        chk_thr.daemon = True
        chk_thr.start()

    def check_vm_state(self, vm_id, state, vm_name):
        alive = self.vsphere_client.vcenter.vm.guest.Power.get(
            vm_id).operations_ready

        if not alive and state == "shutdown":
            Logger().write_log(f'ВМ {vm_name} vm-id({vm_id}) уже ВЫКЛЮЧЕНА')
            return alive
        elif state == "shutdown" and alive:
            start = time.time()
            timeout = start + self.STATE_TIMEOUT
            self.vsphere_client.vcenter.vm.guest.Power.shutdown(vm_id)
            desiredState = self.vsphere_client.vcenter.vm.guest.Power.State.NOT_RUNNING
            while timeout > time.time():
                state = self.vsphere_client.vcenter.vm.guest.Power.get(vm_id).state
                if state != desiredState:
                    print(f"Ожидаем выключения ВМ {vm_name} vm-id({vm_id}")
                    time.sleep(5)
                else:
                    Logger().write_log(f'ВМ {vm_name} vm-id({vm_id}) успешно ВЫКЛЮЧЕНА')
                    break
            # Logger().write_log(f"[ВАЖНО]\tВремя ожидания ВЫКЛЮЧЕНИЯ истекло для ВМ {vm_name} vm-id({vm_id} ")
        if alive and state == "power_up":
            Logger().write_log(f'ВМ {vm_name} vm-id({vm_id}) уже ВКЛЮЧЕНА')
            return alive
        elif state == "power_up" and not alive:
            start = time.time()
            timeout = start + self.STATE_TIMEOUT
            self.vsphere_client.vcenter.vm.Power.start(vm_id)
            desiredState =self.vsphere_client.vcenter.vm.guest.Power.State.RUNNING
            while timeout > time.time():
                state = self.vsphere_client.vcenter.vm.guest.Power.get(vm_id).state
                if state != desiredState:
                    print(f"Ожидаем включения ВМ {vm_name} vm-id({vm_id}")
                    time.sleep(5)
                else:
                    Logger().write_log(f'ВМ {vm_name} vm-id({vm_id}) успешно ВКЛЮЧЕНА')
                    break
            # Logger().write_log(f"[ВАЖНО]\tВремя ожидания ВКЛЮЧЕНИЯ истекло для ВМ {vm_name} vm-id({vm_id} ")