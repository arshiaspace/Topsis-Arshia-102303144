# topsis_logic.py
import pandas as pd
import numpy as np
import os

def run_topsis(input_file, weights, impacts, output_file):
    # Check file extension
    ext = os.path.splitext(input_file)[1].lower()
    
    if ext == ".csv":
        # Use latin1 encoding to avoid UnicodeDecodeError
        data = pd.read_csv(input_file, encoding='latin1')
    elif ext in [".xls", ".xlsx"]:
        data = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file format. Upload CSV or Excel.")

    matrix = data.iloc[:, 1:].values.astype(float)
    weights = np.array(weights, dtype=float)

    # Step 1: Normalize
    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Weighted normalized matrix
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distances
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score and Rank
    score = dist_worst / (dist_best + dist_worst)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    # Save result as CSV (for email attachment)
    data.to_csv(output_file, index=False)
