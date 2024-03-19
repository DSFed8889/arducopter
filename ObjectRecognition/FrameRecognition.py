from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8m.pt")
results = model.predict("cat_dog.jpg")
result = results[0]
print(len(result.boxes))
box = result.boxes[0]
print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)
print("Object type:",box.cls[0])
print("Coordinates:",box.xyxy[0])
print("Probability:",box.conf[0])
print(Image.fromarray(result.plot()[:, :, ::-1]))
