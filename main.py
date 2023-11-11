import cv2
import numpy as np
import os
from os import listdir



def blur_images(folder_path, num_images, blur_strength):
    for i in range(1, num_images + 1):
        img_path = os.path.join(folder_path, f"{i}.jpg")
        img = cv2.imread(img_path)

        blurred_img = cv2.blur(img, (10, 10))

        # Save the blurred image
        cv2.imwrite(img_path, blurred_img)



def bilateralFilter(folder_path, num_images):
    for i in range(1, num_images + 1):
        img_path = os.path.join(folder_path, f"{i}.jpg")
        img = cv2.imread(img_path)

        blurred_img = cv2.bilateralFilter(img, 16, 60, 60)

        # Save the blurred image
        cv2.imwrite(img_path, blurred_img)




os.makedirs('folders after blurring')
os.chdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2')


def create_subfolders(folder_path, num_subfolders):
    for i in range(num_subfolders):
        os.makedirs(os.path.join(folder_path, f"folder{i + 1}"))


create_subfolders("C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring", 5)




x = 1

for folder in os.listdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring'):
    imgs = cv2.imread(fr'C:/Users/FreeComp/Downloads/Telegram Desktop/folders/folders/folder1/{x}.jpg')
    x = x + 1
    path = fr"C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring/folder1"
    os.chdir(path)
    for i in range(50):
        cv2.imwrite(f"{i + 1}.jpg", imgs)


blur_images(path, num_images=50, blur_strength=5)



for folder in os.listdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring'):
    imgs = cv2.imread(fr'C:/Users/FreeComp/Downloads/Telegram Desktop/folders/folders/folder2/{x}.jpg')
    x = x + 1
    path1 = fr"C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring/folder2"
    os.chdir(path1)
    for i in range(50):
        cv2.imwrite(f"{i + 1}.jpg", imgs)

bilateralFilter(path1,50)



for folder in os.listdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring'):
    imgs = cv2.imread(fr'C:/Users/FreeComp/Downloads/Telegram Desktop/folders/folders/folder3/{x}.jpg')
    x = x + 1
    path2 = fr"C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring/folder3"
    os.chdir(path2)
    for i in range(50):
        cv2.imwrite(f"{i + 1}.jpg", imgs)

bilateralFilter(path2,50)



for folder in os.listdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring'):
    imgs = cv2.imread(fr'C:/Users/FreeComp/Downloads/Telegram Desktop/folders/folders/folder4/{x}.jpg')
    x = x + 1
    path3 = fr"C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring/folder4"
    os.chdir(path3)
    for i in range(50):
        cv2.imwrite(f"{i + 1}.jpg", imgs)

bilateralFilter(path3,50)

for folder in os.listdir(r'C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring'):
    imgs = cv2.imread(fr'C:/Users/FreeComp/Downloads/Telegram Desktop/folders/folders/folder5/{x}.jpg')
    x = x + 1
    path4 = fr"C:/Users/FreeComp/PycharmProjects/pythonProject2/folders after blurring/folder5"
    os.chdir(path4)
    for i in range(50):
        cv2.imwrite(f"{i + 1}.jpg", imgs)

blur_images(path4, num_images=50, blur_strength=5)

