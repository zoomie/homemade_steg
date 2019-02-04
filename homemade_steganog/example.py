# Example usage
import matplotlib.pyplot as plt
# from homemade_steganog import Steg
from main import Steg

img_path = '../data/img.jpeg'
data_path = '../data/text.txt'
s = Steg()
s.load_img(img_path)
s.load_data(data_path)
data_in_img = s.encrypt()

# Send image here
plt.imshow(data_in_img)
plt.show()

s_new = Steg()
message = s_new.decrypt_img(data_in_img)
print(message)
