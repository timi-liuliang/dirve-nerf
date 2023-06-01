import cv2
import os

def split_video_frames(video_path, interval):
    # Create a directory to store the frames
    frame_dir = os.path.splitext(video_path)[0] + "_frames"
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate number of frames to skip between each capture
    frame_interval = round(interval * fps)

    # Loop through frames and save them as images
    for i in range(0, frame_count, frame_interval):
        # Set the current frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)

        # Read the next frame from the video
        ret, frame = cap.read()

        # If the frame was successfully read, save it as an image
        if ret:
            frame_path = os.path.join(frame_dir, f"frame_{i:04d}.jpg")
            cv2.imwrite(frame_path, frame)

    # Release the video capture object
    cap.release()

    print(f"Finished splitting video into frames with {interval} second intervals.")


split_video_frames("./data/video/test.mp4", 1)