import glob
import shutil

matches = glob.glob('_data/mt/vote_event_*')
for file in matches:
    shutil.move(file, '_cached_votes')
print(f'Cached {len(matches)} vote files')