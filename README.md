# XGBoost Streamlit Application

This repository contains a Dockerized Streamlit application for training an XGBoost model on a user-uploaded dataset. The application allows users to upload a CSV file, train an XGBoost model, and download the trained model and label encoder.

## Getting Started

### Prerequisites

- Docker must be installed on your system. You can download Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).


- The Docker image must be pulled from Docker Hub:

   ```sh
   docker pull jeffreystynen/streamlit-xgboost:latest
   ```

# Running the XGBoost Streamlit Application

## Start the Docker Container

After pulling the Docker image from Docker Hub, start the Docker container with the following command:

   ```sh
   docker run -p 8501:8501 jeffreystynen/streamlit-xgboost:latest
   ```

# Using the XGBoost Streamlit Application

## Upload a CSV File

1. Click the "Choose a CSV file" button in the Streamlit interface.
2. Select a CSV file where the last column is the target variable, and all other columns are features. Ensure the CSV file includes headers.

## Train the Model

- The application will automatically train an XGBoost model on the uploaded dataset.
- The application will display the model's accuracy after training.

## Download the Model and Label Encoder

- **Download Model**: Click the "Download model" button to download the trained XGBoost model as a `.pkl` file.
- **Download Label Encoder**: Click the "Download label encoder" button to download the label encoder used for encoding the target variable.

### Example Datasets

You can use the following datasets to test the application:

- [Red Wine Quality Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
- [White Wine Quality Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv)




# Troubleshooting for XGBoost Streamlit Application

## Docker Not Running

Ensure Docker Desktop is running on your machine. If Docker is not running, start Docker Desktop and try again.

## Port Conflicts

If port 8501 is already in use by another application, you can map the container to a different port using the following command:

```sh
docker run -p <host_port>:8501 jeffreystynen/streamlit-xgboost:latest
```

