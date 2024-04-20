# Copyright 2015 gRPC authors.

from __future__ import print_function
from google.protobuf.json_format import MessageToDict
import grpc
import images_pb2
import io, base64
import images_pb2_grpc
import cv2
import numpy as np
from datetime import datetime
from PIL import Image
# from base64 import decodestring

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

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # print("Will try to greet world ...")
    response = []
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = images_pb2_grpc.ImagesStub(channel)
        while True:
            response = stub.GetImages(images_pb2.GetImagesRequest())
            # print(response)
            img = response.images[0].img
            print(type(img))
            nparr = np.frombuffer(img, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            new_name = get_new_name()
            cv2.imwrite(f"{save_dir}{new_name}.png",img)
            


if __name__ == "__main__":
    run()
