#utility method to find mutal many to many relationships
def overlap(dol,key_name1='keys',key_name2='values'):
    dol_keys,dol_values = list(zip(*dol.items()))
    final = []
    for key in range(len(dol_keys)):
        temp = {key_name1:[dol_keys[key]],key_name2:set(dol_values[key])}
        for key2 in range(len(dol_keys)):
            if key!=key2:
                curr_val = temp[key_name2] & set(dol_values[key2])
                if len(curr_val) > 0:
                    temp[key_name1].append(dol_keys[key2])
                    temp[key_name2] = curr_val
                    final.append({key_name1:','.join(sorted(temp[key_name1])),
                                  key_name2:','.join(sorted(temp[key_name2]))})
    final = [{key_name2:final[k][key_name2].split(','),key_name1:final[k][key_name1].split(',')}
     for k in range(len(final))]

    lst = []
    for item in final:#dedupe
        if item not in lst:
            lst.append(item)

    return lst
