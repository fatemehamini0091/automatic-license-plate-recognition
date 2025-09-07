**Steps for Fine-Tuning Yolov8:**

1) Collect dataset → images+labels
2) Annotate data → with tools like LabelImg, Roboflow, Labelme, **cvat**
3) Organize dataset structure
	- Detection / Segmentation → YOLO format (images + .txt labels)
	- Classification → one folder per class.
4) Create data.yaml file
    - Paths to train/ and val/
    - Number of classes + class names
5) Choose a pre-trained base model
	- e.g., yolov8n.pt, yolov8s.pt, yolov8m.pt (small → large).
6) Start training (Fine-tuning) with yolo ... train command
7) Monitor results and evaluate
8) Run inference with the fine-tuned weights


 **Main template:**
1. Load models
2. Load video
3. Read frames
    - Detect vehicles
    - Track vehicles
    - Detect license plates
         - Crop the license plate to the car
         - Process the license plate
         - Read the license plate number
4. Write results

**Add missing data:**
- load data from the **main** results
- Implement interpolation bounding boxes
- Interpolate missing data
- Write updated data to a new CSV file

**Visualize the result:**
- Load CSV Results
- Load Video & Output Writer
- Select Best Plate per Car
- Process Video Frames
- Save Output video
