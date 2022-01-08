from itertools import product
import argparse
import math

def hex_to_bin(input):
    ret = ""
    for i in input:
        _hex = bin(int(i, base=16))[2:].zfill(4)
        ret += _hex
    return ret

def combine_vals(id, vals):
    match id:
        case 0:
            return sum(vals)
        case 1:
            return math.prod(vals)
        case 2:
            return min(vals)
        case 3:
            return max(vals)
        case 5:
            return int(vals[0] > vals[1])
        case 6:
             return int(vals[0] < vals[1])
        case 7:
            return int(vals[0] == vals[1])


def parse_pack(_str):
    pack_vers = int(_str[:3], 2)
    pack_id = int(_str[3:6], 2)
    
    if pack_id == 4:
        lit_val = ""
        ctr = 0
        while True:
            header = int(_str[6+ctr*5], 2)
            lit_val += _str[7+ctr*5: 11+ctr*5]
            if header == 0:
                break
            ctr+=1
        return int(lit_val, 2) if part == 2 else pack_vers, _str[11+ctr*5:]

    else:
        id0 = int(_str[6])==0
        vals = [] if part==2 else [pack_vers] 
        rem_str = _str[22: 22+int(_str[7:22], base=2)] if id0 else _str[18:]
        counter = int(_str[7:22], base=2) if id0 else int(_str[7:18], base=2) 
            
        while counter != 0:
            amount, rem_str = parse_pack(rem_str)
            vals.append(amount)
            counter = len(rem_str) if id0 else counter - 1
        return combine_vals(pack_id if part==2 else 0, vals) , _str[22+int(_str[7:22], 2):] if id0 else rem_str
            
if __name__=="__main__":
    with open('data.txt') as f:
         parser = argparse.ArgumentParser()
         parser.add_argument('part', type=int)
         part = parser.parse_args().part
         input = f.read().strip()
         bin_rep = hex_to_bin(input)
         print(parse_pack(bin_rep))


