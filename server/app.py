from concurrent import futures

import grpc
import images_pb2
import images_pb2_grpc
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

class Images(images_pb2_grpc.ImagesServicer):
    def GetImages(self, request, context):
        while True:
            # Read input from the camera
            success, img = cap.read()
            if success:
                _, img_bytes = cv2.imencode('.jpg', img)
                return images_pb2.GetImagesResponse(images=[
                    images_pb2.Image(
                        width = 100,
                        height = 200,
                        img = img_bytes.tobytes(),
                    )
                ])

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    images_pb2_grpc.add_ImagesServicer_to_server(Images(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
