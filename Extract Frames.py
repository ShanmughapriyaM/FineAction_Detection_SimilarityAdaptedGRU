import os
import json
import cv2
import numpy as np

# Path to JSON file
json_file = r"C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames\scrambledegg\labels.json"  # replace with your JSON file path
# Path where extracted frames will be saved
output_dir = r"C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames\scrambledegg\Sub Actions"
# Base folder where videos are stored
video_base_path = r"C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames\scrambledegg"  # change to your video folder

os.makedirs(output_dir, exist_ok=True)

# Load JSON
with open(json_file, 'r') as f:
    data = json.load(f)

def extract_uniform_frames(video_path, start_frame, end_frame, num_frames=32):
    print(video_path, start_frame, end_frame)
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    if not cap.isOpened():
        print(f"Failed to open video {video_path}")
        return frames
    
    total_frames = end_frame - start_frame + 1
    frame_indices = np.linspace(start_frame, end_frame, min(num_frames, total_frames), dtype=int)
    
    current_frame = 0
    extracted_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if current_frame == frame_indices[extracted_idx]:
            frames.append(frame)
            extracted_idx += 1
            if extracted_idx >= len(frame_indices):
                break
        current_frame += 1
    
    cap.release()
    return frames

for entry in data:
    class_name = entry['ClassName']
    video_name = entry['FileName']  # may already have extension
    start_frame = entry['start_frame']
    end_frame = entry['end_frame']
    
    # Automatically find video file with any extension
    possible_extensions = [".avi", ".mp4", ".mov", ".mkv"]
    video_path = None
    for ext in possible_extensions:
        temp_path = os.path.join(video_base_path, video_name)
        print(temp_path)
        if os.path.exists(temp_path):
            video_path = temp_path
            break
    
    if video_path is None:
        print(f"Video file for {video_name} not found!")
        continue
    
    frames = extract_uniform_frames(video_path, start_frame, end_frame, num_frames=32)
    
    save_path = os.path.join(output_dir, class_name, video_name)
    os.makedirs(save_path, exist_ok=True)
    
    for idx, frame in enumerate(frames):
        frame_file = os.path.join(save_path, f"frame_{idx+1:03d}.jpg")
        cv2.imwrite(frame_file, frame)
    
    print(f"Saved {len(frames)} frames for {class_name}/{video_name}")
