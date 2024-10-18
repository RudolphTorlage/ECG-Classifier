Date: 18/10/2024
Author: Max Brenner 

This folder contains the code, and models for Approach A as described in the paper "Automatic diagnosis of Cardiac arrhythmias from 12-lead ECG data using machine learning algorithms. "

Due to storage constraints, the data used to test and train the models is excluded from this repository, but can be downloaded from : https://zenodo.org/records/4916206 [1]


A) Approach_A_Data_preprocessing_1.ipynb is used to obtain a smaller, cleaned dataset per part of the dataset downloaded. It removes cases where all arrythmias are false and normal ecg is also false, and creates a reduced .hdf5 file with the 
remaining ECGs, as well as a corresponding csv file with the arrhythmia labels and patient details.

B) Approach_A_Data_preprocessing_2.py is a script which merges the arrythmia labels found in the csv, with the corresponding ECG tracings from the .hdf5 file, and creates a new combined .h5 file. 

C) Approach_A_Data_preprocessing_3.py is an optional script which combines all the testing data into a single .h5 file for convenience and for use on RAM limited machines. 

D) Approach_A_Data_Loading_and_Model_Training.ipynb is the entire model training pipeline. it begins with loading in the test data and filtering it. It then defines the model, the learning rate, and training parameters.
finally it calls the model to train, and saves the normalisation constants, the trained model, and the training weights after training completes. It also saves periodic checkpoints.

E) Approach_A_Testing_and_validation.ipynb is a notebook that contains the testing and validation protocols of the models trained using Approach A. 

F) The trained model is provided both in a .keras file "trained_model.keras" as well as in a .h5 file "trained_model.h5", please use the right format based on your working version of Keras. 

G) Mean, standard deviation and Normalisation data is also provided in "train_mean.npy", "train_std.npy" and "normalization_data.txt"

For the code to run as planned, several requirements need to be met.
1) Parts 0 to 17 of the database must be downloaded.
2) ensure that all file paths and file names are correct.
3) Ensure you have sufficient RAM, otherwise consider batching training.
4) Ensure you save your normalisation constants (standard deviation and mean) numpy arrays from the training data and use them for testing the data to ensure consistency. 


References:
[1] A. H. Ribeiro et al., ‘CODE-15%: a large scale annotated dataset of 12-lead ECGs’. Zenodo, Jun. 09, 2021. doi: 10.5281/zenodo.4916206.
