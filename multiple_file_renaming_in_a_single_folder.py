import os
base_path = "C:/Users/suman/OneDrive/Documents/Pics"
files = os.listdir(base_path)
files.sort()
for idx, filename in enumerate(files, start=1):
    old_file = os.path.join(base_path, filename)
    new_name = f"image{idx}.jpeg"
    new_file = os.path.join(base_path, new_name)
    if not os.path.exists(new_file):
        os.rename(old_file, new_file)
    else:
        print(f"Skipping {filename}, target name {new_name} already exists.")
print("\nRenamed Files:")
for f in os.listdir(base_path):
    print(f)