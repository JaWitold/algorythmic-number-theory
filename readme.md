
# Algorithmic Number Theory

Witold Karaś

## Introduction

This repository contains my solutions for the Algorithmic Number Theory course. The solutions are implemented in Jupyter notebooks using SageMath and are run in a Docker container.

## Getting Started

### Prerequisites

In order to run the Jupyter notebooks, you will need to have Docker installed on your machine. You can download Docker from the official website <https://www.docker.com/>.

### Running the Notebooks

To run the notebooks, follow these steps:

Clone this repository to your local machine using the command:

``` bash
git clone https://github.com/JaWitold/algorythmic-number-theory.git
```

Open a terminal and navigate to the root of the repository.

Run the following command to start a Docker container with SageMath and Jupyter notebook:

``` bash
docker run --name sagemath -d -p 8888:8888 -v ${PWD}:/home/sage/notebook sagemath/sagemath:latest sage-jupyter
```

Open your web browser and go to <http://localhost:8888>. This will open the Jupyter notebook interface.

In the Jupyter notebook interface, navigate to the notebooks folder and open the desired notebook.

Run the cells in the notebook to execute the code.
