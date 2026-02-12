# Copilot / AI Agent Instructions

Short, actionable guidance to make an AI coding agent productive in this repo.

## Big picture
- This is a small ML assignment repo: data + a training notebook + a Streamlit UI.
- Key artifacts:
  - [loan_status.ipynb](loan_status.ipynb): EDA, preprocessing, training and model export cells (source of truth for data transforms and training).
  - [model/](model/): directory of serialized model artifacts (e.g. `final_model.pkl`, `logistic_regression.pkl`, `xgboost.pkl`). The Streamlit app loads `model/final_model.pkl` at runtime.
  - [app.py](app.py): Streamlit app that loads the pickled model via `joblib.load("model/final_model.pkl")` and builds a small input form.
  - [loan_dataset.csv](loan_dataset.csv): primary dataset used by the notebook.

## Primary workflows (concrete commands)
- Install dependencies (quick):

  ```bash
  python -m pip install -r requirements.txt
  ```

- Run the UI locally:

  ```bash
  streamlit run app.py
  ```

- Reproduce / retrain the model:
  - Open [loan_status.ipynb](loan_status.ipynb) in Jupyter or VS Code and run the notebook cells that train models and call `joblib.dump(...)`.
  - The notebook contains the explicit save pattern: `joblib.dump(model, f"model/{file_name}")` — ensure the exported filename is `model/final_model.pkl` (or update `app.py` to match).

## Project-specific conventions & patterns
- Models are stored as pickled artifacts under `model/`. The app expects scikit-learn-compatible objects (loaded with `joblib`).
- The notebook is the canonical place for preprocessing logic. When updating the model, mirror any transform code from the notebook to the app or bundle transforms with the saved model.
- `app.py` exposes specific categorical options — use these exact categories when constructing test inputs or replacing the UI:
  - `Gender`: `Male` / `Female`
  - `Married`: `Yes` / `No`
  - `Education`: `Graduate` / `Not Graduate`
  - `Self Employed`: `Yes` / `No`
  - `Credit History`: `1.0` / `0.0`
  - `Dependents`: `0`, `1`, `2`, `3+`
  - `Property Area`: `Urban`, `Semiurban`, `Rural`

## Integration points & checks for edits
- If you modify preprocessing or feature encodings in the notebook, update the code that prepares `input_df` in `app.py` (or replace `app.py` to load a transformer alongside the model).
- To inspect or test a model artifact interactively, use a short REPL snippet:

  ```python
  import joblib
  m = joblib.load('model/final_model.pkl')
  print(type(m), hasattr(m, 'predict'))
  ```

## What to watch for / gotchas
- Pickle security: loading arbitrary `*.pkl` is unsafe. Only load artifacts you or this repository produced.
- The repository contains a local `ml/` folder with conda metadata; treat it as an environment snapshot (do not modify it here).
- The notebook may save multiple models (see `model/` contents). Confirm which model is intended for production usage and keep the filename consistent with `app.py`.

## Quick checklist for agent changes
- If changing model training or preprocessing:
  1. Update `loan_status.ipynb` (reproducible cell) and re-run relevant cells.
  2. Ensure `joblib.dump(..., 'model/final_model.pkl')` (or update `app.py`).
  3. Run `streamlit run app.py` locally to validate the UI input path and predictions.

If any part is unclear or you'd like me to add tests/CI steps to validate model artifacts and the Streamlit app, tell me which area to expand.
