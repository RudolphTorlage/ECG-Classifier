import h5py
import numpy as np

# List of the parts to combine
combined_parts = [
    'Combined_Part_14.h5',
    'Combined_Part_15.h5',
    'Combined_Part_16.h5',
    'Combined_Part_17.h5'
]

# Output path for the combined file
output_file = 'Combined_Undersampled_normal_14_to_17.h5'

# List of all arrhythmia labels, including 'normal_ecg'
arrhythmias = ['1dAVb', 'RBBB', 'LBBB', 'SB', 'ST', 'AF', 'normal_ecg']

# Initialize lists to store combined data
combined_tracings = []
combined_labels = []

# Loop over the parts and load the data
for part_file in combined_parts:
    with h5py.File(part_file, 'r') as f:
        for exam_id in f.keys():
            group = f[exam_id]
            tracing = group['tracing'][:]
            
            # Load all arrhythmia labels as a list
            label = [group.attrs[arrhythmia] for arrhythmia in arrhythmias]
            combined_tracings.append(tracing)
            combined_labels.append(label)

# Convert to numpy arrays for easy manipulation
tracings = np.array(combined_tracings)
labels = np.array(combined_labels)

# Separate normal ECGs from the rest
normal_indices = np.where(labels[:, -1] == 1)[0]  # Assuming 'normal_ecg' is the last column
non_normal_indices = np.where(labels[:, -1] == 0)[0]

# Undersample normal ECGs by keeping only 25%
np.random.shuffle(normal_indices)
undersampled_normal_indices = normal_indices[:len(normal_indices) // 4]

# Combine undersampled normal ECGs with non-normal ECGs
balanced_indices = np.concatenate([undersampled_normal_indices, non_normal_indices])

# Shuffle the final combined dataset
np.random.shuffle(balanced_indices)

# Create final combined arrays
final_tracings = tracings[balanced_indices]
final_labels = labels[balanced_indices]

# Save the combined data into a new HDF5 file
with h5py.File(output_file, 'w') as f_out:
    for i, (tracing, label) in enumerate(zip(final_tracings, final_labels)):
        group = f_out.create_group(f'exam_{i}')
        group.create_dataset('tracing', data=tracing)
        
        # Add all arrhythmia labels as attributes
        for arrhythmia, value in zip(arrhythmias, label):
            group.attrs[arrhythmia] = value

print(f"Combined file saved at: {output_file}")
