from pathlib import Path
import os

# Local directory (Local AppData)
local_dir = Path(os.getenv('LOCALAPPDATA'))
local_file_path = local_dir / 'MyApp' / 'data.txt'

# Roaming directory (Roaming AppData)
roaming_dir = Path(os.getenv('APPDATA'))
roaming_file_path = roaming_dir / 'MyApp' / 'settings.txt'

# ProgramData directory
programdata_dir = Path(os.getenv('PROGRAMDATA'))
programdata_file_path = programdata_dir / 'MyApp' / 'shared_data.txt'

# Write to files
with open(local_file_path, 'w') as f:
    f.write('Local directory data\n')

with open(roaming_file_path, 'w') as f:
    f.write('Roaming directory data\n')

with open(programdata_file_path, 'w') as f:
    f.write('ProgramData directory data\n')

# Read from files
with open(local_file_path, 'r') as f:
    print(f.read())

with open(roaming_file_path, 'r') as f:
    print(f.read())

with open(programdata_file_path, 'r') as f:
    print(f.read())
