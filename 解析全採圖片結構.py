import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#從圖片檔案cat.png讀入資料，並劃出圖片
image=mpimg.imread("cat.png")
print(image)
print(image.shape)
plt.imshow(image)
plt.show()
##做影像處理簡單來說就是對圖片做矩陣操作

"""分離出RGB三原色的紅色頻道"""

R=image*np.array([1,0,0])
plt.imshow(R)
plt.show()
"""分離出RGB三原色的綠色頻道"""
G=image*np.array([0,1,0])
plt.imshow(G)
plt.show()
"""分離出RGB三原色的藍色頻道"""
B=image*np.array([0,0,1])
plt.imshow(B)
plt.show()
"""將圖片轉為灰階格式"""
Gray=np.dot(image,np.array([0.21,0.72,0.07]))
plt.imshow(Gray,cmap="gray")
plt.show()