a. Problem statement - Loan Status is a binary classification problem.
b. Dataset description - The dataset contains customer information collected by a housing finance company. The goal is to predict whether a loan application will be approved or not based on applicant details.
Typically includes:

Numerical Features
ApplicantIncome – Applicant’s income
CoapplicantIncome – Co-applicant’s income
LoanAmount – Loan amount requested
Loan_Amount_Term – Loan repayment period (in months)

Categorical Features
Gender
Married
Dependents
Education
Self_Employed
Property_Area
Credit_History – 1 = good credit, 0 = bad credit

Target Variable:
Loan_Status

c. Models used: 
| Model                | Accuracy  | AUC      | Precision | Recall   | F1 Score  | MCC      |
|----------------------|-----------|----------|-----------|----------|-----------|----------|
| Logistic Regression  | 0.790323  | 0.733170 | 0.800000  | 0.930233 | 0.860215  | 0.471332 |
| Decision Tree        | 0.758065  | 0.729498 | 0.769231  | 0.930233 | 0.842105  | 0.374349 |
| KNN                  | 0.806452  | 0.733170 | 0.803922  | 0.953488 | 0.872340  | 0.515505 |
| Naive Bayes          | 0.774194  | 0.742962 | 0.795918  | 0.906977 | 0.847826  | 0.431102 |
| Random Forest        | 0.758065  | 0.746634 | 0.791667  | 0.883721 | 0.835165  | 0.394083 |
| XGBoost              | 0.806452  | 0.780906 | 0.803922  | 0.953488 | 0.872340  | 0.515505 |


| ML Model Name              | Observation about Model Performance |
|----------------------------|--------------------------------------|
| Logistic Regression        | Achieved strong recall (0.93) and balanced precision (0.80),resulting in a high F1-score (0.86). Performs well overall but AUC is moderate, indicating limited separation ability compared to XGBoost. |
--------------------------------------------------------------------------------------------------
| Decision Tree              | High recall (0.93) but lower precision and MCC. Likely overfitting and less stable compared to ensemble models. |
--------------------------------------------------------------------------------------------------
| kNN                        | High accuracy (0.80) and recall (0.95). Strong F1-score (0.87) and MCC (0.52) indicate good balanced performance. Performs among the best models overall. |
--------------------------------------------------------------------------------------------------
| Naive Bayes                | Good recall (0.91) with moderate precision and AUC. Performs reasonably well but slightly weaker than kNN and XGBoost. |
--------------------------------------------------------------------------------------------------
| Random Forest (Ensemble)   | Strong AUC (0.75) but slightly lower accuracy and F1 compared to kNN and XGBoost. Stable but not the top performer in this case. |
--------------------------------------------------------------------------------------------------
| XGBoost (Ensemble)         | Best overall performance with highest AUC (0.78), high recall (0.95), strong F1-score (0.87), and highest MCC (0.52). Demonstrates superior classification and generalization ability. |
--------------------------------------------------------------------------------------------------

XGBoost and kNN performed the best among all models, achieving the highest accuracy, recall, F1-score, and MCC. XGBoost slightly outperformed others in AUC, indicating better class separation capability. Decision Tree showed comparatively weaker stability, while Logistic Regression and Naive Bayes provided solid baseline performance. Ensemble methods demonstrated improved generalization compared to single models.