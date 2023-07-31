# Django Support Vector Machine Learning Project

![image](form_image.png)

## Overview
This is a Django web application that demonstrates the use of Support Vector Machine (SVM) for machine learning, to classify diabetes using Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin levels,BMI,DiabetesPedigreeFunction and Age as Features. The project aims to classify data into different classes using SVM, a powerful supervised learning algorithm.

## Features

- User-friendly web interface for uploading and managing datasets
- SVM model training and classification
- Visualization of classification results
- Model evaluation metrics display (accuracy, precision, recall, F1-score)

## Installation
 1. Clone the repository:  https://github.com/mauriceoboya/django_analysis.git 
 2. Navigate to the project directory: cd diabetes_analysis 
 3. Create a virtual environment : python -m venv venv
                                   source venv/bin/activate # On Windows, use 'venv\Scripts\activate'    
4. Install the required dependencies: python manage.py migrate
5. Start the development server: python manage.py runserver
  
6. Access the web application at [http://localhost:8000/](http://localhost:8000/) in your browser.

## How to Use

1. Upload Dataset: In the web interface, go to the "Upload Dataset" section and upload your dataset in CSV format.

2. Train SVM Model: After uploading the dataset, select the target variable and features for training the SVM model. Click on the "Train Model" button to start the training process.

3. Classify Data: Once the model is trained, navigate to the "Classify Data" section. Upload a new dataset or use the same uploaded dataset for classification. The model will predict the target variable for the data.

4. View Results: After classification, the results will be displayed in the "Classification Results" section. The model evaluation metrics, such as accuracy, precision, recall, and F1-score, will also be shown.

## Technologies Used

- Django: Python web framework for building the application's backend
- Scikit-learn: Python library for machine learning and SVM implementation
- Pandas: Data manipulation library for handling datasets
- Matplotlib: Data visualization library for generating charts and plots


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to express our gratitude to the developers of Scikit-learn and Django for their excellent libraries that made this project possible.








