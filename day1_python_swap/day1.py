def Main():
    def swap_postions(resp_list, pos1, pos2):
        resp_list[pos1], resp_list[pos2] = resp_list[pos2], resp_list[pos1]
        return resp_list

    order_resp = [
        {
            "type": "1",
            "order_number": "001" 
        },
        {
            "type": "1",
            "order_number": "002" 
        },
        {
            "type": "4",
            "order_number": "003" 
        },
        {
            "type": "2",
            "order_number": "003" 
        },
        {
            "type": "1",
            "order_number": "005" 
        },
        {
            "type": "5",
            "order_number": "006" 
        },
        {
            "type": "3",
            "order_number": "006" 
        },
        {
            "type": "1",
            "order_number": "007" 
        }
    ]
    
    temp_swap = dict()
    for idx, rec in order_resp:
        order_type = rec.get("type")
        if order_type in ["2", "4", "3", "5"]:
            key_target = 'order_' + rec.get("order_number")
            target_order = temp_swap.get(key_target) if temp_swap.get(key_target) else { "pos1": None, "pos2": None}
            if order_type in ["2", "3"]:
                target_order["pos1"] = idx
            else:
                target_order["pos2"] = idx
            temp_swap[key_target] = target_order
    
    for key, value in temp_swap.items():
        val_pos1 = value.get("pos1")
        val_pos2 = value.get("pos2")
        
        if val_pos1 != None and val_pos2 != None:
            order_resp = swap_postions(order_resp, val_pos1, val_pos2)

        