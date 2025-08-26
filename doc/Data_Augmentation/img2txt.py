import os

root = '' # <dataset_path>

with open('id_path.txt', 'w') as f:  # 只開一次檔案，所有路徑寫進去
    for current, sub, files in os.walk(root):
        for img in files:
            image_path = os.path.join(current, img)
            # print(image_path)
            f.write(image_path + '\n')
    print('Write finish!!')
