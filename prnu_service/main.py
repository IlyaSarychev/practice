import os
import numpy as np
import requests as r

import prnu_service.Functions as Fu
import prnu_service.getFingerprint as gF

from time import time


def _download_image(url):
    res = r.get(url)
    os.makedirs('prnu_service' + os.sep + 'cache', exist_ok=True)
    name = 'image-%s.jpg' % time()
    path = 'prnu_service' + os.sep + 'cache' + os.sep + name

    with open(path, 'wb') as file:
        file.write(res.content)
        return file, path 


def get_fingerprint_from_images(urls=None, images=[]):
    # extracting Fingerprint from same size images in a path
    for url in urls:
        _, path = _download_image(url)
        images.append(path)

    RP,_,_ = gF.getFingerprint(images)
    RP = Fu.rgb2gray1(RP)
    sigmaRP = np.std(RP)
    Fingerprint = Fu.WienerInDFT(RP, sigmaRP)

    return Fingerprint