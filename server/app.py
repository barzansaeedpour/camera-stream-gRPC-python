import grpc
import cv2
import time
from concurrent import futures
import camera_pb2
import camera_pb2_grpc

class CameraServicer(camera_pb2_grpc.CameraServicer):
    def StreamCamera(self, request_iterator, context):
        # Initialize camera (replace with your actual camera setup)
        cap = cv2.VideoCapture(0)

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Convert frame to bytes
                print(frame)
                frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()

                # Yield the frame to the client
                yield camera_pb2.CameraFrame(frame=frame_bytes)

                # Simulate camera frame rate (adjust as needed)
                time.sleep(0.1)
        finally:
            cap.release()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    camera_pb2_grpc.add_CameraServicer_to_server(CameraServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()


# from concurrent import futures

# import grpc
# import images_pb2
# import images_pb2_grpc
# import cv2
# from datetime import datetime

# cap = cv2.VideoCapture(0)

# class Images(images_pb2_grpc.ImagesServicer):
#     def GetImages(self, request, context):
#         while True:
#             # Read input from the camera
#             success, img = cap.read()
#             if success:
#                 _, img_bytes = cv2.imencode('.jpg', img)
#                 return images_pb2.GetImagesResponse(images=[
#                     images_pb2.Image(
#                         width = 100,
#                         height = 200,
#                         img = img_bytes.tobytes(),
#                     )
#                 ])

# def serve():
#     port = "50051"
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     images_pb2_grpc.add_ImagesServicer_to_server(Images(), server)
#     server.add_insecure_port("[::]:" + port)
#     server.start()
#     print("Server started, listening on " + port)
#     server.wait_for_termination()


# if __name__ == "__main__":
#     serve()
