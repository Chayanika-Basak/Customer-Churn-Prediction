import numpy as np
import numpy.linalg as la
import pandas as pd
import cv2 as cv
from skimage import io
from PIL import Image
import matplotlib.pyplot as plt

url ="ML_Maths/Captain_Jack_Sparrow.jpg"
myImg = io.imread(url)
gray_image = cv.cvtColor(myImg, cv.COLOR_BGR2GRAY)
img_mat = np.array(list(gray_image), float)
print(img_mat)
print(img_mat.shape)
# plt.imshow(img_mat)
# plt.show()

img_mat_scaled = (img_mat-img_mat.mean())/img_mat.std()
u,s,v = la.svd(img_mat_scaled, full_matrices=True)

# variance = np.round(s**2/np.sum(s**2), decimals=3)

# import seaborn as sns
# sns.barplot(x=list(range(1,26)), y=variance[0:25], color="red")
# plt.xlabel('Singular Vector', fontsize=14, color="blue")
# plt.ylabel('Variance', fontsize=14, color="green")
# plt.tight_layout()
# plt.savefig('ML_Maths/Variance_plot_of_img.png')
# plt.show()

# [1334, 750]

num_of_components = 5
p = u[:,:num_of_components]
sd = np.diag(s)
r,c = img_mat.shape
sigma = np.zeros((r,c))
if(r>c):
    sigma[:c,:] = sd
else:
    sigma[:,:r] = sd
sigma = sigma[:num_of_components,:num_of_components]
q = v[:num_of_components,:]

reconst_img_5 = np.dot(np.dot(p,sigma),q)

num_of_components = 25
p = u[:,:num_of_components]
sd = np.diag(s)
r,c = img_mat.shape
sigma = np.zeros((r,c))
if(r>c):
    sigma[:c,:] = sd
else:
    sigma[:,:r] = sd
sigma = sigma[:num_of_components,:num_of_components]
q = v[:num_of_components,:]

reconst_img_25 = np.dot(np.dot(p,sigma),q)

num_of_components = 100
p = u[:,:num_of_components]
sd = np.diag(s)
r,c = img_mat.shape
sigma = np.zeros((r,c))
if(r>c):
    sigma[:c,:] = sd
else:
    sigma[:,:r] = sd
sigma = sigma[:num_of_components,:num_of_components]
q = v[:num_of_components,:]

reconst_img_100 = np.dot(np.dot(p,sigma),q)

num_of_components = 500
p = u[:,:num_of_components]
sd = np.diag(s)
r,c = img_mat.shape
sigma = np.zeros((r,c))
if(r>c):
    sigma[:c,:] = sd
else:
    sigma[:,:r] = sd
sigma = sigma[:num_of_components,:num_of_components]
q = v[:num_of_components,:]

reconst_img_500 = np.dot(np.dot(p,sigma),q)

fig,axs = plt.subplots(2, 2, figsize=(10,10))
axs[0,0].imshow(reconst_img_5)
axs[0,0].set_title('Reconstructed Image: 5 SVs')
axs[0,1].imshow(reconst_img_25)
axs[0,1].set_title('Reconstructed Image: 25 SVs')
axs[1,0].imshow(reconst_img_100)
axs[1,0].set_title('Reconstructed Image: 100 SVs')
axs[1,1].imshow(reconst_img_500)
axs[1,1].set_title('Reconstructed Image: 500 SVs')

plt.savefig('ML_Maths/Image_Reconstructions.png')
plt.show()