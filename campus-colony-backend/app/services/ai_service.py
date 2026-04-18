import pickle
import numpy as np
import pandas as pd
import os

# =========================================================
# LOAD MODELS
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ML_PATH = os.path.join(BASE_DIR, "ml_models")

model = pickle.load(open(os.path.join(ML_PATH, "rent_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(ML_PATH, "scaler.pkl"), "rb"))
label_encoders = pickle.load(open(os.path.join(ML_PATH, "label_encoders.pkl"), "rb"))
feature_columns = pickle.load(open(os.path.join(ML_PATH, "feature_columns.pkl"), "rb"))


# =========================================================
# SAFE ENCODER (IMPORTANT FIX)
# =========================================================

def safe_transform(le, value):
    """
    Prevents crash on unseen labels
    """
    value = str(value)

    # try exact match
    if value in le.classes_:
        return le.transform([value])[0]

    # fallback: try lowercase match
    lower_map = {str(v).lower(): v for v in le.classes_}
    if value.lower() in lower_map:
        return le.transform([lower_map[value.lower()]])[0]

    # final fallback (safe default)
    return 0


# =========================================================
# MAIN PREDICTION FUNCTION
# =========================================================

def predict_rent(data):

    # Convert input to dataframe
    input_df = pd.DataFrame([data])

    # -----------------------------------------------------
    # STEP 1: Normalize strings (VERY IMPORTANT)
    # -----------------------------------------------------
    for col in input_df.columns:
        if input_df[col].dtype == "object":
            input_df[col] = input_df[col].astype(str).str.strip()

    # =====================================================
    # CATEGORICAL COLUMNS
    # =====================================================
    categorical_columns = [
        "area_name", "area_category", "property_type",
        "furnished", "electricity_backup", "gas_available",
        "near_school", "near_market"
    ]

    # -----------------------------------------------------
    # STEP 2: SAFE ENCODING
    # -----------------------------------------------------
    for col in categorical_columns:
        if col in input_df.columns:
            le = label_encoders[col]
            input_df[col] = input_df[col].apply(lambda x: safe_transform(le, x))

    # =====================================================
    # STEP 3: FEATURE ENGINEERING (same as training)
    # =====================================================

    input_df["total_rooms"] = input_df["bedrooms"] + input_df["bathrooms"]

    input_df["amenities_score"] = (
        input_df["parking"] +
        input_df["electricity_backup"] +
        input_df["gas_available"]
    )

    input_df["location_score"] = (
        input_df["near_school"] +
        input_df["near_market"]
    )

    # =====================================================
    # STEP 4: ALIGN FEATURE ORDER
    # =====================================================

    input_df = input_df.reindex(columns=feature_columns)

    # fill missing (safety)
    input_df = input_df.fillna(0)

    # =====================================================
    # STEP 5: SCALE
    # =====================================================

    input_scaled = scaler.transform(input_df)

    # =====================================================
    # STEP 6: PREDICT
    # =====================================================

    prediction = model.predict(input_scaled)[0]

    return float(prediction)