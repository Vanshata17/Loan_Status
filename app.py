import streamlit as st
# import pandas as pd
# import joblib
# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix,
#     classification_report
# )
# import seaborn as sns
# import matplotlib.pyplot as plt

# # --------------------------------------------------
# # Page configuration
# # --------------------------------------------------
# st.set_page_config(
#     page_title="Loan Approval Prediction System",
#     page_icon="💰",
#     layout="centered"
# )

# st.title("💰 Loan Approval Prediction System")

# # --------------------------------------------------
# # Model selection (Requirement b)
# # --------------------------------------------------
# st.subheader("Select Model")

# MODEL_PATHS = {
#     "Logistic Regression": "model/logistic_regression.pkl",
#     "Random Forest" : "model/random_forest.pkl",
#     "Descision Tree" : "model/decision_tree.pkl",
#     "KNN" : "model/knn.pkl",
#     "Naive Bayes" : "model/naive_bayes.pkl",
#     "XGBoost" : "model/xgboost.pkl"
# }

# model_name = st.selectbox("Choose a model", list(MODEL_PATHS.keys()))
# model = joblib.load(MODEL_PATHS[model_name])

# st.success(f"Loaded model: {model_name}")

# # --------------------------------------------------
# # Dataset upload (Requirement a)
# # --------------------------------------------------
# st.subheader("Upload Test Dataset (CSV)")

# uploaded_file = st.file_uploader(
#     "Upload test CSV file (with Loan_Status column)",
#     type=["csv"]
# )

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.write("📄 Preview of uploaded data:")
#     st.dataframe(df.head())

#     # --------------------------------------------------
#     # Check target column
#     # --------------------------------------------------
#     if "Loan_Status" not in df.columns:
#         st.error("❌ Uploaded dataset must contain 'Loan_Status' column")
#         st.stop()

#     X_test = df.drop(columns=["Loan_Status"])
#     y_test = df["Loan_Status"]

#     # --------------------------------------------------
#     # Prediction
#     # --------------------------------------------------
#     y_pred = model.predict(X_test)

#     # --------------------------------------------------
#     # Evaluation metrics (Requirement c)
#     # --------------------------------------------------
#     st.subheader("📊 Evaluation Metrics")

#     accuracy = accuracy_score(y_test, y_pred)
#     precision = precision_score(y_test, y_pred)
#     recall = recall_score(y_test, y_pred)
#     f1 = f1_score(y_test, y_pred)

#     col1, col2 = st.columns(2)
#     col1.metric("Accuracy", f"{accuracy:.2f}")
#     col2.metric("Precision", f"{precision:.2f}")

#     col3, col4 = st.columns(2)
#     col3.metric("Recall", f"{recall:.2f}")
#     col4.metric("F1 Score", f"{f1:.2f}")

#     # --------------------------------------------------
#     # Confusion Matrix (Requirement d)
#     # --------------------------------------------------
#     st.subheader("📉 Confusion Matrix")

#     cm = confusion_matrix(y_test, y_pred)

#     fig, ax = plt.subplots()
#     sns.heatmap(
#         cm,
#         annot=True,
#         fmt="d",
#         cmap="Blues",
#         xticklabels=["Rejected", "Approved"],
#         yticklabels=["Rejected", "Approved"],
#         ax=ax
#     )
#     ax.set_xlabel("Predicted")
#     ax.set_ylabel("Actual")
#     st.pyplot(fig)

#     # --------------------------------------------------
#     # Classification Report (Requirement d)
#     # --------------------------------------------------
#     st.subheader("📄 Classification Report")

#     report = classification_report(y_test, y_pred, output_dict=True)
#     report_df = pd.DataFrame(report).transpose()
#     st.dataframe(report_df)

# else:
#     st.info("👆 Please upload a test CSV file to continue.")



st.write("welcome")
