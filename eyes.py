import cv2
from ultralytics import YOLO
import io
import os

class ImageAnalysis:
    def __init__(self, yolo_model_path='yolov8m.pt', google_api_key=None):
        self.yolo_model = YOLO(yolo_model_path)
        self.client = vision.ImageAnnotatorClient()
        if google_api_key:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_api_key
        self.image_counter = 0
        self.cap = cv2.VideoCapture(0)

    def start_tracking(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            results = self.yolo_model(frame)
            annotated_frame = results.render()[0]

            cv2.imshow("Object Tracking", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('c'):
                self.capture_image(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def capture_image(self, frame):
        image_name = f"captured_image_{self.image_counter}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Image {image_name} captured.")
        self.image_counter += 1

    def analyze_image(self, image_path):
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
            image = vision.Image(content=content)

        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        if texts:
            detected_text = texts[0].description
            print(f"Detected text: {detected_text}")
            return detected_text
        else:
            print("No text detected.")
            return None

if __name__ == "__main__":
    analyzer = ImageAnalysis(google_api_key='path_to_google_api_key.json')
    analyzer.start_tracking()
