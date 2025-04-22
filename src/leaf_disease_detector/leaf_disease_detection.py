from ultralytics import YOLO
from PIL import Image
from torchvision import transforms
from config.config import MODEL_PATH

class LeafDiseaseDetection:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)
        self.model.conf = 0.90  # Set confidence threshold

    def preprocess_image(self, image_path: str):
        """
        Preprocess the input image before passing it to the model.
        """
        transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Resize to the model's expected input size
            transforms.ToTensor(),  # Convert image to tensor
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize
        ])
        image = Image.open(image_path).convert("RGB")  # Ensure it's in RGB
        return transform(image).unsqueeze(0)  # Add batch dimension

    def predict(self, image_path):
        results = self.model(image_path)  # Run inference

        if isinstance(results, list) and len(results) > 0:
            # Retrieve the first result object
            result = results[0]

            # Ensure that 'boxes' attribute is present and not empty
            if hasattr(result, 'boxes') and result.boxes is not None and len(result.boxes) > 0:
                # Initialize list to store detected class names
                predicted_class_names = []

                # Iterate through each detection
                for box in result.boxes:
                    # Get the class ID of each detection
                    predicted_class_id = int(box.cls)

                    # Map class ID to class name using result.names
                    predicted_class_name = result.names[predicted_class_id]
                    predicted_class_names.append(predicted_class_name)  # Add to the list of predictions

                return predicted_class_names  # Return list of all detected class names
            else:
                print("No bounding boxes detected.")
                return None
        else:
            print("No valid results returned from the model.")
            return None  # Return None if no results or empty list
