# ES335 Machine Learning — Assignment Overview

This repository contains coursework for **ES335 Machine Learning** across four assignments (`A1` to `A4`).
Each assignment focuses on a different set of core machine learning concepts, experiments, and implementation tasks.

---

## Repository Structure

- [A1](A1): Decision Trees from scratch + Human Activity Recognition mini project
- [A2](A2): Optimization, multicollinearity, Random Fourier Features, matrix factorization, and HAR model comparison
- [A3](A3): Sequence modeling, XOR regularization experiments, CO2 forecasting, and MNIST/Fashion-MNIST representation analysis
- [A4](A4): CNN-based binary image classification and KNN variants (LSH, KD-tree, Naive)

---

## Assignment 1 (A1)

Primary themes: **Decision Trees (from scratch), evaluation metrics, practical classification/regression usage, and HAR deployment**.

### Part A: Decision Tree Implementation

You are expected to implement a complete decision tree pipeline, including:

- Support for four configurations:
  1. Discrete features → Discrete target
  2. Discrete features → Real target
  3. Real features → Discrete target
  4. Real features → Real target
- Split criteria:
  - Classification: **Gini Index** and **Information Gain (Entropy)**
  - Regression: **Information Gain using MSE**
- Tree visualization/printing support

Key files referenced by the assignment:

- [A1/metrics.py](A1/metrics.py): performance metrics
- [A1/tree/base.py](A1/tree/base.py): core decision tree implementation
- [A1/tree/utils.py](A1/tree/utils.py): helper functions
- [A1/usage.py](A1/usage.py): validation/demo script

### Part B: Experiments

1. Synthetic binary classification experiment using `make_classification`
   - Train/test split (70/30)
   - Report accuracy, per-class precision, and recall
2. 5-fold cross-validation + nested CV
   - Select optimal tree depth
3. Automotive efficiency task
   - Apply custom tree
   - Compare against `scikit-learn` tree
4. Runtime complexity experiments
   - Vary number of samples ($N$) and binary features ($M$)
   - Measure train and inference time
   - Compare with theoretical complexity across all four tree settings

### Part C: Human Activity Recognition (Mini Project)

Dataset: UCI-HAR (smartphone accelerometer + gyroscope)

Tasks include:

- Visual waveform comparison across six activities
- Analysis of static vs dynamic activities via total acceleration magnitude
- Decision Tree training and confusion-matrix reporting
- Depth sweep (2–8) and accuracy trend analysis
- PCA visualization from raw total acceleration and TSFEL features
- TSFEL feature extraction + Decision Tree performance comparison
- Participant/activity-wise failure analysis
- Deployment on self-collected smartphone data (10s windows, ~500 samples per segment)

---

## Assignment 2 (A2)

Primary themes: **Optimization behavior, linear algebra stability, feature mappings, image reconstruction, matrix factorization, and model interpretability**.

### 1) Gradient Descent Variants

- Implement full-batch GD and stochastic GD on two synthetic linear datasets
- Convergence to an $\epsilon$-neighborhood ($\epsilon = 0.001$)
- Visualize trajectories, contour movement, and loss vs epochs
- Implement and compare GD with momentum
- Plot vectors (gradient, parameter state, momentum) and discuss optimizer behavior

### 2) Multicollinearity and Numerical Stability

- Compare `np.linalg.inv`-based solution with `np.linalg.solve`
- Discuss numerical robustness and why direct solves are preferred

### 3) Why `scikit-learn` Linear Regression is Robust

- Analyze internals and explain robustness in presence of multicollinearity

### 4) Random Fourier Features for Image Reconstruction

- Super-resolution ($2\times$)
- Quantitative evaluation with:
  - RMSE
  - PSNR
- Random missing-data reconstruction from 10% to 90% missingness

### 5) Matrix Factorization Inpainting

- Reconstruct rectangular missing patches at varying complexity locations
- Vary patch sizes $N \in \{20,40,60,80,100\}$
- Compare Gradient Descent vs Alternating Least Squares
- Compare matrix factorization with RFF-based reconstruction
- Study effect of rank $r \in \{5,10,50,100\}$

### 6) HAR Model Comparison

- Compare Decision Tree, Random Forest, and Linear Regression (as classifier surrogate)
- Use TSFEL features on flattened linear acceleration
- Evaluate whether linear regression is appropriate for classification

### 7) Feature Importance Comparison

- Normalize absolute linear-regression weights
- Compare with Random Forest feature importances
- Plot common bar chart and report top-10 features

---

## Assignment 3 (A3)

Primary themes: **Sequence models, regularization, time-series forecasting, and deep representation analysis**.

### 1) Character-Level Next Token Prediction

- Reproduce a next-character model (Karpathy-inspired setup)
- Train on one selected corpus (e.g., Shakespeare/Wikipedia/etc.)
- Generate text samples
- Visualize embeddings (scatter or t-SNE)
- Build a Streamlit app for next-$k$ character prediction

### 2) XOR Modeling Study

- Train and compare:
  - MLP
  - MLP + L1
  - MLP + L2
  - Logistic regression with engineered nonlinear features
- Use 200 train + 200 test samples
- Plot decision boundaries and compare shape capture

### 3) CO2 Forecasting

- Monthly Mauna Loa CO2 forecasting using:
  - MLP
  - Moving Average (MA)
  - ARMA
- Sliding window setup with previous $K$ points predicting next $T$ point
- Compare outputs and explain differences

### 4) MNIST vs Fashion-MNIST Transfer Behavior

- Train MLP on MNIST (full or stratified subset)
- Compare against Random Forest and Logistic Regression
- Use metrics: F1-score and confusion matrix
- Analyze commonly confused digits
- Visualize second hidden-layer embeddings (t-SNE):
  - Trained model
  - Untrained model
- Evaluate trained MNIST model on Fashion-MNIST and compare embedding structure shift

---

## Assignment 4 (A4)

Primary themes: **Computer Vision with CNNs/Transfer Learning and nearest-neighbor search scaling**.

### Question 1: Binary Image Classification

Compare the following model families on a custom 2-class dataset:

1. VGG-style CNN (1 block)
2. VGG-style CNN (3 blocks)
3. VGG-style CNN (3 blocks) + data augmentation
4. Transfer learning (VGG16/VGG19) with full fine-tuning
5. Transfer learning (VGG16/VGG19) with frozen convolution base + tuned MLP head

Expected reporting:

- Training time
- Training loss
- Training accuracy
- Testing accuracy
- Number of parameters

TensorBoard tracking requirements:

- Scalars vs **iterations**:
  - Training loss
  - Training accuracy
  - Testing accuracy
- Image panel:
  - Test images with predictions

Additional analysis:

- Whether outcomes match expectations and why
- Effect of data augmentation
- Effect of fine-tuning duration
- Typical failure/confusion cases
- Comparison with a parameter-matched MLP baseline

### Question 2: KNN Variant Comparison

Implement and compare:

- Naive KNN
- KD-tree KNN
- LSH-based approximate KNN

Experiments required:

- Vary dataset size ($N$) and dimensionality ($D$)
- Compare train/test time and memory for $K$-NN retrieval
- In 2D, visualize:
  - Approximate neighbors missed by approximate methods
  - Spatial partitions induced by the methods

---

## Suggested Deliverables Pattern

For subjective analysis tasks, the assignments generally require markdown reports named in the form:

- `assignment_q<question-number>_subjective_answers.md`

Include:

- Methodology
- Hyperparameters
- Visualizations
- Quantitative metrics
- Error/failure analysis
- Final conclusions

---

## Notes

- Many tasks involve both implementation and analysis; results are as important as code correctness.
- Keep experiments reproducible (fixed random seeds, clearly logged configs).
- For model comparison sections, ensure consistent train/test splits and evaluation protocol.
