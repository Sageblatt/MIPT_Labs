import numpy as np
from PIL import Image

for i in range(1, 4):
    img = Image.open(f"lunar0{i}_raw.jpg")
    data = np.array(img, dtype=np.uint8)

    k = 255 / (data.max() - data.min())
    b = -k*data.min()

    updated_data = np.array(k * data + b, dtype=np.uint8)

    res_img = Image.fromarray(updated_data)

    res_img.save(f"lunar0{i}.png")
    res_img.close()
    img.close()
