import os

def count_folders_and_images(root_dir, exts=(".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
    folder_count = 0
    image_count = 0

    for current_path, subfolders, files in os.walk(root_dir):
        # 計算子資料夾數量
        folder_count += len(subfolders)

        # 計算圖片數量
        for f in files:
            if f.lower().endswith(exts):
                image_count += 1

    return folder_count, image_count


if __name__ == "__main__":
    path = "RepSet_X_15_vec2face_pose_dcface"  # 改成你的資料夾路徑
    folders, images = count_folders_and_images(path)
    print(f"資料夾數量: {folders}")
    print(f"圖片數量: {images}")
