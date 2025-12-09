import os
import json

# Folder containing label files
label_folder = r"C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames\scrambledegg"  # change this
output_json = r"C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames\scrambledegg\labels.json"

data_list = []

for file_name in os.listdir(label_folder):
    if file_name.endswith(".labels"):  # your label file extension
        file_path = os.path.join(label_folder, file_name)
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    # Split by space
                    parts = line.split(maxsplit=1)
                    frame_range = parts[0]
                    class_name = parts[1]

                    start_frame, end_frame = map(int, frame_range.split("-"))

                    entry = {
                        "ClassName": class_name,
                        "FileName": os.path.splitext(file_name)[0],
                        "start_frame": start_frame,
                        "end_frame": end_frame
                    }
                    data_list.append(entry)
                except Exception as e:
                    print(f"Skipping line in {file_name}: {line}. Error: {e}")

# Save JSON
with open(output_json, "w") as out_f:
    json.dump(data_list, out_f, indent=4)

print(f"JSON file created at {output_json}")
