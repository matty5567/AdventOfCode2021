import numpy as np


def enhance_image(img, decoder, ctr):
    pad_img = np.pad(img, pad_width=6, constant_values=1 if ((ctr%2) and decoder[0]==1) else 0)
    ret_img = np.zeros((pad_img.shape[0]-2, pad_img.shape[1]-2), dtype=int)
    

    for y in range(pad_img.shape[0] - 2):
        for x in range(pad_img.shape[1] - 2):
            window = pad_img[y:y+3, x:x+3]
            bin_num = int("".join(map(str, window.flatten())), base=2)
            ret_img[y, x] = decoder[bin_num]

    return ret_img


with open(r'data.txt') as f:
    decode_input, _, *raw_im = f.readlines()
    hash_to_int = {'#':1, '.':0}

    decoder = [hash_to_int[i] for i in decode_input.strip()]    
    image = np.array([[hash_to_int[x] for x in i.strip()] for i in raw_im])

    for i in range(50):
        image = enhance_image(image, decoder, i)

    print(np.sum(image))

