import h5py
import pandas as pd
import numpy as np

# Define paths for the HDF5 and CSV files
hdf5_file_template = 'Part_{}_filtered_data.hdf5'
csv_file_template = 'Part_{}_cleaned_data.csv'
output_file_template = 'Combined_Part_{}.h5'

# Function to load, combine, and save data for each part with undersampling of normal ECGs
def combine_and_save_data(part_num, undersample_ratio=0.2): #only save 20% of normal ecgs.
    # Paths to the HDF5 and CSV files for this part
    hdf5_file_path = hdf5_file_template.format(part_num)
    csv_file_path = csv_file_template.format(part_num)
    output_file_path = output_file_template.format(part_num)

    # Load the CSV file containing exam info and arrhythmia labels
    csv_data = pd.read_csv(csv_file_path)

    # Separate normal ECGs and arrhythmias
    normal_ecg_rows = csv_data[csv_data['normal_ecg'] == True]
    arrhythmia_rows = csv_data[csv_data['normal_ecg'] == False]

    # Undersample the normal ECGs by the given ratio
    normal_ecg_sampled = normal_ecg_rows.sample(frac=undersample_ratio, random_state=42)

    # Combine normal ECGs and arrhythmias back into one dataset
    combined_data = pd.concat([normal_ecg_sampled, arrhythmia_rows])

    # Open the HDF5 file and load the datasets
    with h5py.File(hdf5_file_path, 'r') as f:
        exam_ids = f['exam_id'][:]
        tracings = f['tracings'][:]

        # Create a new HDF5 file to save the combined data
        with h5py.File(output_file_path, 'w') as out_f:
            # Loop through all rows in the combined CSV data
            for _, row in combined_data.iterrows():
                exam_id = row['exam_id']
                
                # Find the corresponding ECG tracing from the HDF5 file
                tracing_index = np.where(exam_ids == exam_id)[0]
                
                if tracing_index.size > 0:
                    tracing_index = tracing_index[0]
                    tracing = tracings[tracing_index]
                    
                    # Create a dataset in the output file for this exam
                    group = out_f.create_group(str(exam_id))
                    
                    # Store the tracing
                    group.create_dataset('tracing', data=tracing)
                    
                    # Store the labels (as attributes or datasets)
                    for label in ['1dAVb', 'RBBB', 'LBBB', 'SB', 'ST', 'AF', 'normal_ecg']:
                        group.attrs[label] = row[label]

    print(f"Part {part_num} combined data (with undersampling) saved to {output_file_path}")

# Loop through all parts (0 to 14) and process them with undersampling

combine_and_save_data(14, undersample_ratio=0.2)

print("All parts processed and saved with undersampling.")
