import pyrealsense2 as rs
import numpy as np

# Configure depth and color streams
class Camera:

    def __init__(self):
        """
        Camera initializing part, usually insert here your camera code except loop part(l.e. get next frame)
        """
        self.pipeline = rs.pipeline()
        config = rs.config()

        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        found_rgb = False
        for s in device.sensors:
            if s.get_info(rs.camera_info.name) == 'RGB Camera':
                found_rgb = True
                break
        if not found_rgb:
            print("The demo requires Depth camera with Color sensor")
            exit(0)

        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 0)

        # Start streaming
        self.pipeline.start(config)

    def get_next_img(self) -> np.ndarray:

        """
        Send Img to main code return type "must" np.ndarray
        Returns: img (np.ndarray)

        """

        # Wait for a coherent pair of frames: depth and color
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        return color_image
