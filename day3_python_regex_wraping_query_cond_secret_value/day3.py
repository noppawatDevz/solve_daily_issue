import re

def Main():
    SECRET_SYSTEM = {
        "_uuid": "2b13e671-c04f-4d83-9c1a-cb37757ef99f",
        "_username": "noppawat.devz",
        "_dcdp": "503211d8-660c-4908-95b3-5fc28310d5b4"
    }

    def wrapping_cond(cond):
        temp_cond = cond
        re_system = r'{(.*?)}'
        # check str cond wrapping secret key
        system_list = re.findall(re_system, cond)
        # uniq system_list
        system_list = set(system_list)
        for ssy in system_list:
            # find key
            target_key = ssy.split(".")[1]
            # value default None
            value = None
            if target_key in SECRET_SYSTEM:
                value = SECRET_SYSTEM.get(target_key)
            if value:
                value = '"{}"'.format(value) if isinstance(value, str) else value
            temp_cond = temp_cond.replace('{' + ssy + '}', value if value else "null")
        return temp_cond

    condition = "_create_by = {$System._username} and _dcdp = {$System._dcdp} and _order_type = 2 and _unit_type = {$System._unit}"

    final_cond = wrapping_cond(condition)