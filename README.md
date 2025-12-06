================================================================================
NASA TURBOFAN JET ENGINE RUL PREDICTION - SETUP AND EXECUTION INSTRUCTIONS
================================================================================

PROJECT OVERVIEW
----------------
This project uses Simple Neural Nets and Recurrent Neural Networks (RNN/LSTM) to predict the Remaining 
Useful Life (RUL) of NASA turbofan jet engines across four different datasets 
with varying operating conditions and fault modes.

PREREQUISITES
-------------
- Python 3.8 or higher
- Visual Studio Code (recommended) with Jupyter extension
- CUDA-capable GPU (recommended for faster training, but CPU will work)
- Internet connection for downloading required packages

SETUP INSTRUCTIONS
------------------

1. INSTALL REQUIRED PACKAGES
   
   Open a terminal (PowerShell or Command Prompt) in the project directory and run:
   
   pip install -r requirements.txt
   
   This will install all necessary packages:
   - PyTorch (deep learning framework)
   - pandas (data manipulation)
   - matplotlib (visualization)
   - scikit-learn (preprocessing)
   - numpy (numerical operations)
   - jupyter and ipykernel (notebook support)
   
   Note: If you have a CUDA-capable GPU, PyTorch will automatically use it.
         Otherwise, it will run on CPU (slower but functional).

2. VERIFY DATA FILES
   
   Ensure the following CSV files are present in the project directory:
   - Train1.csv, Train2.csv, Train3.csv, Train4.csv (training data)
   - Test1.csv, Test2.csv, Test3.csv, Test4.csv (test data)
   
   Original raw data files are also included in the CMaps/ subdirectory.

RUNNING THE CODE
----------------

OPTION A: Using Visual Studio Code (Recommended)

1. Open VS Code in the project directory
2. Open any of the notebook files:
   - Simple_NeuralNetwork_Set1.ipynb ((Dataset 1: Single operating condition, single fault mode)
   - Simple_NeuralNetwork_Set2.ipynb (Dataset 2: Multiple operating conditions, single fault mode)
   - Simple_NeuralNetwork_Set3.ipynb (Dataset 3: Single operating condition, multiple fault modes)
   - Simple_NeuralNetwork_Set4.ipynb (Dataset 4: Multiple operating conditions, multiple fault modes))
   - RNN_Set 1.ipynb (Dataset 1: Single operating condition, single fault mode)
   - RNN_Set 2.ipynb (Dataset 2: Multiple operating conditions, single fault mode)
   - RNN_Set 3.ipynb (Dataset 3: Single operating condition, multiple fault modes)
   - RNN_Set 4.ipynb (Dataset 4: Multiple operating conditions, multiple fault modes)
   
3. Select the Python kernel (VS Code will prompt you to select one)
4. Run cells sequentially by clicking the "Run" button or pressing Shift+Enter
5. The notebook will:
   - Load and preprocess the data
   - Train the LSTM model
   - Evaluate performance on test data
   - Generate visualizations

OPTION B: Using Jupyter Notebook/Lab

1. Open a terminal in the project directory
2. Launch Jupyter:
   
   jupyter notebook
   
   OR
   
   jupyter lab
   
3. Navigate to and open the desired RNN_Set notebook
4. Run cells sequentially

DATASET DESCRIPTIONS
--------------------

Dataset 1 (FD001): 100 train engines, 100 test engines
- Single operating condition
- Single fault mode (HPC Degradation)
- Simplest scenario

Dataset 2 (FD002): 260 train engines, 259 test engines
- Six operating conditions
- Single fault mode (HPC Degradation)
- More complex due to varying operating conditions

Dataset 3 (FD003): 100 train engines, 100 test engines
- Single operating condition
- Two fault modes (HPC + Fan Degradation)
- Complex due to multiple failure modes

Dataset 4 (FD004): 249 train engines, 248 test engines
- Six operating conditions
- Two fault modes (HPC + Fan Degradation)
- Most complex scenario

NOTEBOOK STRUCTURE
------------------

Each notebook contains the following sections:

1. Import Libraries and Check GPU Availability
2. Define LSTM Model Architecture
3. Load and Preprocess Data (scaling, sequence creation)
4. Train the Model
5. Visualize Training Loss
6. Evaluate on Test Set (calculate MSE and MAE)
7. Visualize Predictions for Random Engines
8. Visualize Predictions for Engines with Lowest Final RUL

EXECUTION TIME
--------------

With GPU:
- Dataset 1 & 3: ~2-5 minutes
- Dataset 2 & 4: ~5-10 minutes

With CPU:
- Dataset 1 & 3: ~10-20 minutes
- Dataset 2 & 4: ~20-40 minutes

EXPECTED OUTPUT
---------------

The notebooks will produce:
- Training loss curve showing model convergence
- Test set performance metrics (MSE and MAE)
- Scatter plots comparing actual vs. predicted RUL for selected engines
- Summary statistics for each visualized engine

TROUBLESHOOTING
---------------

Issue: "CUDA out of memory" error
Solution: The code already includes batch processing to handle this. If the error
          persists, reduce the batch_size parameter (currently 16 or 32).

Issue: "Module not found" error
Solution: Ensure all packages from requirements.txt are installed. Run:
          pip install -r requirements.txt

Issue: Slow execution
Solution: Training on CPU is slower. Consider using Google Colab with GPU or
          reducing the number of epochs.

Issue: Poor predictions
Solution: This is expected for some datasets (especially Dataset 4). The model
          can be improved by adjusting hyperparameters:
          - sequence_length (currently 70)
          - hidden_size (currently 128)
          - num_layers (currently 1)
          - learning rate (currently 0.001)
          - epochs (currently 50)

ADDITIONAL FILES
----------------

- Edit_Format_Features.py: Preprocessing script for training data
- Edit_Format_TestData.py: Preprocessing script for test data
- Simple_NeuralNetwork_Set*.ipynb: Alternative approach using feedforward networks
- CMaps/: Directory containing original raw data files

CONTACT
-------

For questions about this code, please contact Adam Hosburgh adho6298@colorado.edu

================================================================================
