import imageio

name_list = ['images/tip20denoise_after.png', 'images/tip20denoise_before.png']
for name in name_list:
    img = imageio.imread(name)
    img = img[0:img.shape[0], 0:img.shape[0]]
    imageio.imwrite(name[:-4]+'_cut.png', img)
