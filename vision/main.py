from transformers import pipeline
from PIL import Image
import requests
from datetime import datetime

print(r'''
   _______    _______  _______  
  /       \//       \/       \
 /        ///        /        //
/         /        _/         / 
\___/____/\____/___/\__/__/__/  
''')

print("Starting depth estimation...")


# load pipe
print("Loading depth estimation model...")
pipe = pipeline(task="depth-estimation", model="xingyang1/Distill-Any-Depth-Large-hf")

# load image
print("Loading image from URL...")
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

# save original image
image.save("original_image.jpg")


# inference
depth = pipe(image)["depth"]

#shows heat map for depth
depth.show()

# write the image in logs
file_name = "logs.txt"

with open(file_name, 'a') as file:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"\nLog entry at {current_time} : ")
    file.write(str(depth))

#save depth image
depth.save("depth_image.png")



