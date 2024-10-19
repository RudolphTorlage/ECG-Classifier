Last updated: 19/10/2024
Author: Rudolph Torlage

This folder contains the code, and models for Approach B as described in the paper "Using ML to diagnose cardiac arrhythmias on 12-lead electrocardiograms"

The data used in this project is part of an open-source dataset called CODE15, and can be obtained here : https://zenodo.org/records/4916206 [1]
Alternatively the pre-processed data can be found here: https://drive.google.com/drive/folders/1-PgvdA290TXm9dzEfptKVAsiueQ9p02H?usp=sharing

The project followed the approach:

- Pre-process the data
- Train the model
- Evaluate the performance

#Pre-processing
**Note that all references to the location of files within google Drive will need to be adjusted to match your personal details**

The code for this part of the project can be found in pre-processing.ipynb.
The pre-processing had two main goals:

- Clean, Balance, and Process the data with the intent of improving model performance.
- Combine data into ready-to-use splits with the intent of reducing the resources needed (System RAM and GPU RAM) by the training file.

#Training
**Note that all references to the location of files within google Drive will need to be adjusted to match your personal details**

The code for training the model can be found in training.ipynb.
The pre-trained model is also included in this repo for ease of use.

#Evaluating the model performance
**Note that all references to the location of files within google Drive will need to be adjusted to match your personal details**

The code for evaluting the model performance can be found in testing.ipynb.

#Requirements

- The training file will require a minimum of 25Gb of system RAM, and 12Gb of GPU RAM
- Ensure all paths to google drive have been adjusted to your personal drive or local storage
- The project was carried out using Google Colab. The pre-processing and testing files can be run in a L4 or CPU runtime. I strongly suggest the A100 runtime for the training file. It is possible to host this code on a local or cloud platform other than Colab, but it will be up to you to ensure all the dependencies are installed correctly. The versions used in this project were as per the indicated runtimes on Colab at 19/10/2024.
- The GPU parallelization might need to be manually implemented depending on your set up. The strain placed on components might also reduce their lifetime. Run this on your local machine at your own risk.

References:
[1] A. H. Ribeiro et al., ‘CODE-15%: a large scale annotated dataset of 12-lead ECGs’. Zenodo, Jun. 09, 2021. doi: 10.5281/zenodo.4916206.
