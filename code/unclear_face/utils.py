import matplotlib.pyplot as plt
from PIL import Image
def visualize_group(list_imgs,step):
    list_imgs = sorted(list_imgs)
    fig=plt.figure(figsize=(20, 7))
    columns = len(list_imgs)
    rows = 1
    plt.xlabel('step {}'.format(step))
    for i in range(0, columns*rows):
        img = list_imgs[i]
        fig.add_subplot(rows, columns, i+1)
        plt.imshow(Image.open(img))
        plt.title(str(list_imgs[i].split('/')[-1]+'-'+str(5*step+i+2)))
