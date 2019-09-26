import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image


def mfilter(image_path,w):
    image = np.array(Image.open(image_path))
    img2 = np.zeros_like(image)
    for r in range(w,image.shape[0]-w):
        for c in range(w,image.shape[1]-w):
            img2[r, c,0] = image[r-w:r+w,c-w:c+w,0].mean()
            img2[r, c,1] = image[r - w:r + w, c - w:c + w,1].mean()
            img2[r, c,2] = image[r - w:r + w, c - w:c + w,2].mean()
    return img2

def gfilter(image_path,w,std):
    original_image = Image.open(image_path)
    image = np.array(original_image)
    img2 = np.zeros_like(image)
    width, height = original_image.size
    resized_image = np.array(original_image.resize((width + w, height + w)))
    resized_image[w//2:resized_image.shape[0] - (w+1)//2, w//2:resized_image.shape[1] - (w+1)//2] = image
    gmat = np.array([[[math.exp(-((w//2-k)**2 + (w//2-l)**2)/(2*std**2))/(math.sqrt(2*math.pi)*std) for l in range(w)] for k in range(w)] for i in range(3)])
    gmat /= sum(sum(gmat[0]))
    for r in range(img2.shape[0]):
        for c in range(img2.shape[1]):
            img2[r, c] = np.sum(np.sum(resized_image[r:r+w,c:c+w]*gmat, axis=0), axis=0)
    return img2

def main():
    image_path = 'C:\\Users\\User\\PycharmProjects\\task2\\picture_2.png'
    std = 3
    w = 3
    fig, axes = plt.subplots(1, 2)
    image = np.array(Image.open(image_path))
    res_image = gfilter(image_path, w, std)
    axes[0].imshow(image)
    axes[1].imshow(res_image)
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
    fig.set_figwidth(12)
    fig.set_figheight(4)
    plt.show()


if __name__ == "__main__":
    main()