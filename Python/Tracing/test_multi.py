# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:29:45 2021

@author: Roboadmin
"""


import concurrent.futures
import os
from PIL import Image
import numpy as np
from tqdm import tqdm


def thread_function(sdir):
    data = []
    # print("start")
    imageList = os.listdir(sdir)
    imageList = np.char.add(sdir + "/", imageList)
    for image in imageList:
        with open(image, 'rb') as i:
            img = Image.open(i)
            img = img.resize((128, 128), Image.LANCZOS)
            img = img.convert("RGB")
            img = np.asarray(img)
            data.append(np.asarray(img))
    return data


if __name__ == '__main__':

    # start 4 worker processes
    data = []
    PATH = "F:/Matura/Pictures_128/thumbnails128x128"
    dirList = os.listdir(PATH)
    dirList = np.char.add(PATH + "/", dirList)
    for sdir, it in zip(dirList, range(dirList.shape[0])):
        if not(os.path.isdir(sdir)):
            dirList = np.delete(dirList, it, axis=0)

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        # Start the load operations and mark each future with its URL
        future_to_img = {executor.submit(
            thread_function, sdir): sdir for sdir in dirList}
        for future in tqdm(concurrent.futures.as_completed(future_to_img)):
            img = future_to_img[future]
            try:
                data_img = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (img, exc))
            else:
                data.append(data_img)
    print(np.asarray(data).reshape(-1, 128, 128, 3).shape)
    # q = JoinableQueue()

    # # turn-on the worker thread
    # threading.Thread(target=worker, daemon=True).start()

    # # send thirty task requests to the worker
    # for item in range(30):
    #     q.put(item)
    # print('All task requests sent\n', end='')

    # # block until all tasks are done
    # q.join()
    # print('All work completed')

    # # print(dirList)
    # with Pool(processes=4) as pool:

    #     # print "[0, 1, 4,..., 81]"
    #     # "F:/Matura/Pictures_128/thumbnails128x128/00000"))
    #     print(pool.map(open_image, range(100)))

    #     # # launching multiple evaluations asynchronously *may* use more processes
    #     # multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    #     # print([res.get(timeout=1) for res in multiple_results])

    # # exiting the 'with'-block has stopped the pool
    # print("Now the pool is closed and no longer available")
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
