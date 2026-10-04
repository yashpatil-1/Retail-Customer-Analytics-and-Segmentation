import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "rfm.csv"
OUTPUT_FILE = BASE_DIR / "data" / "final_customer_segments.csv"


# Load RFM data
rfm = pd.read_csv(INPUT_FILE)

features = ["Recency", "Frequency", "Monetary"]
X = rfm[features].copy()

# Reduce the effect of highly skewed RFM values
X_log = np.log1p(X)

# Standardize the variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_log)


# Test different numbers of clusters
print("Testing K-Means cluster sizes...\n")

results = []

for k in range(2, 9):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    silhouette = silhouette_score(X_scaled, labels)

    results.append({
        "K": k,
        "Inertia": model.inertia_,
        "Silhouette": silhouette
    })

    print(
        f"K={k} | "
        f"Inertia={model.inertia_:.2f} | "
        f"Silhouette={silhouette:.4f}"
    )


# Select 4 clusters for business interpretability
final_k = 4

final_model = KMeans(
    n_clusters=final_k,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = final_model.fit_predict(X_scaled)


# Create business-friendly segment names
cluster_summary = (
    rfm.groupby("Cluster")
    .agg(
        Customers=("Customer ID", "count"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean"),
        Revenue=("Monetary", "sum")
    )
    .reset_index()
)

cluster_summary["Customer_Share"] = (
    cluster_summary["Customers"] / len(rfm) * 100
)

cluster_summary["Revenue_Share"] = (
    cluster_summary["Revenue"] / rfm["Monetary"].sum() * 100
)


# Identify clusters using their RFM behaviour
def assign_segment(row):
    if (
        row["Avg_Recency"] <= 50
        and row["Avg_Frequency"] >= 10
        and row["Avg_Monetary"] >= 5000
    ):
        return "Champions"

    if row["Avg_Recency"] >= 150 and row["Avg_Monetary"] >= 1000:
        return "At-Risk Valuable"

    if row["Avg_Recency"] <= 100 and row["Avg_Frequency"] >= 2:
        return "New / Promising"

    return "Low-Engagement / Lost"


cluster_summary["Segment"] = cluster_summary.apply(
    assign_segment,
    axis=1
)


# Map segment names back to customers
segment_mapping = cluster_summary.set_index("Cluster")["Segment"]

rfm["Segment"] = rfm["Cluster"].map(segment_mapping)


# Save final customer-level segmentation
rfm.to_csv(OUTPUT_FILE, index=False)


print("\nFinal customer segments:\n")

display_columns = [
    "Cluster",
    "Segment",
    "Customers",
    "Customer_Share",
    "Avg_Recency",
    "Avg_Frequency",
    "Avg_Monetary",
    "Revenue_Share"
]

print(
    cluster_summary[display_columns]
    .sort_values("Revenue_Share", ascending=False)
    .to_string(index=False)
)

print(f"\nFinal clusters: {final_k}")
print(f"Customers segmented: {len(rfm):,}")
print(f"Saved to: {OUTPUT_FILE}")
