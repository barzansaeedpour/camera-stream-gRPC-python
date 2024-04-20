import grpc
import cv2
import camera_pb2
import camera_pb2_grpc
import numpy as np
from datetime import datetime

save_dir = './saved_images/'
def get_new_name():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the datetime as desired (e.g., YYYYMMDD-HHMMSS)
    formatted_datetime = current_datetime.strftime("%Y%m%d-%H%M%S")
    # Create a unique filename
    filename = f"my_file_{formatted_datetime}"
    # print(f"Unique filename: {filename}")
    return filename

def stream_camera():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = camera_pb2_grpc.CameraStub(channel)
        # response = stub.StreamCamera(camera_pb2.CameraFrame())
        # print(response)
        try:
            for response in stub.StreamCamera(camera_pb2.CameraFrame()):
                # Process the received frame (e.g., display it)
                frame = response.frame
                nparr = np.frombuffer(frame, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                new_name = get_new_name()
                cv2.imwrite(f"{save_dir}{new_name}.png", frame)
                
            # frame = cv2.imdecode(response.frame, cv2.IMREAD_COLOR)
            # cv2.imshow('Camera Stream', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows()

    # channel = grpc.insecure_channel('localhost:50051')  # Replace with your server address
    # stub = camera_pb2_grpc.CameraStub(channel)

    # try:
    #     for response in stub.StreamCamera(camera_pb2.CameraFrame()):
    #         # Process the received frame (e.g., display it)
    #         frame = cv2.imdecode(response.frame, cv2.IMREAD_COLOR)
    #         cv2.imshow('Camera Stream', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     cv2.destroyAllWindows()


if __name__ == '__main__':
    stream_camera()


# # Copyright 2015 gRPC authors.

# from __future__ import print_function
# from google.protobuf.json_format import MessageToDict
# import grpc
# import images_pb2
# import io, base64
# import images_pb2_grpc
# import cv2
# import numpy as np
# from datetime import datetime
# from PIL import Image
# # from base64 import decodestring

# save_dir = './saved_images/'
# def get_new_name():
#     # Get the current date and time
#     current_datetime = datetime.now()
#     # Format the datetime as desired (e.g., YYYYMMDD-HHMMSS)
#     formatted_datetime = current_datetime.strftime("%Y%m%d-%H%M%S")
#     # Create a unique filename
#     filename = f"my_file_{formatted_datetime}"
#     # print(f"Unique filename: {filename}")
#     return filename

# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     # print("Will try to greet world ...")
#     response = []
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = images_pb2_grpc.ImagesStub(channel)
#         while True:
#             response = stub.GetImages(images_pb2.GetImagesRequest())
#             # print(response)
#             img = response.images[0].img
#             print(type(img))
#             nparr = np.frombuffer(img, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#             new_name = get_new_name()
#             cv2.imwrite(f"{save_dir}{new_name}.png",img)


# if __name__ == "__main__":
#     run()
