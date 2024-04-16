import os
from tqdm import tqdm
from time import sleep
def save_states(path):
    states = []
    for root, dirs, files in tqdm(os.walk(path), desc="Saving states", unit="files"):
        for file in files:  # Use tqdm to show progress bar for files:
            s = os.path.getmtime(os.path.join(root, file))
            states.append(s)
    with open('states.txt', 'w') as f:
        for state in states:
            f.write(str(state) + '\n')

def detect_changed_state(path):
    states = []
    modified = []
    with open('states.txt', 'r') as f:
        for line in tqdm(f, desc="Reading states from file"):
            states.append(float(line.strip()))
    for root, dirs, files in tqdm(os.walk(path), desc="Detecting changes"):
        for file in files:
            abs_path = os.path.join(root, file)
            s = os.path.getmtime(abs_path)
            if s not in states:
                modified.append(abs_path)
    return modified


if __name__ == '__main__':

    # Example usage
    path = r'D:\Documentations'
    save_states(path)
    print("Saved states")
    print("Sleeping for 5 seconds...")
    sleep(5)
    print("Detecting changes...")
    changed_files = detect_changed_state(path)
    print("Modified files:", changed_files)
