# The following file shows how the class should function

from steganog import Steg

steg = Steg('settings')
steg.load_normal_img('file_path')
steg.load_data('data_path')
hidden_img = steg.encrypt()

steg = Steg()
steg.load_hidden_img()
data = steg.decrypt_img()

