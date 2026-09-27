import pandas as pd
import numpy as np
import os

# ---------------------------------------------------------
# PRACTICAL 5: ANONYMIZATION TECHNIQUES
# Techniques:
# 1. Data Masking
# 2. K-Anonymity
# 3. Differential Privacy
# ---------------------------------------------------------

# Create output folder
os.makedirs("output", exist_ok=True)

# ---------------------------------------------------------
# STEP 1: Load Dataset
# ---------------------------------------------------------

data = pd.read_csv("dataset/patient_data.csv")

print("ORIGINAL DATASET")
print(data)

# ---------------------------------------------------------
# STEP 2: DATA MASKING
# ---------------------------------------------------------

masked_data = data.copy()

# Mask names
masked_data["Name"] = masked_data["Name"].apply(
    lambda x: x[0] + "*" * (len(x) - 1)
)

# Mask phone numbers
masked_data["Phone"] = masked_data["Phone"].apply(
    lambda x: "XXXXXX" + str(x)[-4:]
)

# Mask email addresses
masked_data["Email"] = masked_data["Email"].apply(
    lambda x: x[0] + "****" + x[x.index("@"):]
)

# Save masked dataset
masked_data.to_csv("output/masked_data.csv", index=False)

print("\n\nMASKED DATA")
print(masked_data)

# ---------------------------------------------------------
# STEP 3: K-ANONYMITY
# ---------------------------------------------------------

k_data = data.copy()

# Remove direct identifiers
k_data = k_data.drop(
    columns=["Patient_ID", "Name", "Phone", "Email"]
)

# Generalize Age into age groups
def age_group(age):
    if age < 30:
        return "20-29"
    elif age < 40:
        return "30-39"
    else:
        return "40-49"

k_data["Age"] = k_data["Age"].apply(age_group)

# Generalize city into region
def city_region(city):
    if city in ["Delhi", "Noida"]:
        return "Delhi-NCR"
    else:
        return "Gurugram-NCR"

k_data["City"] = k_data["City"].apply(city_region)

# Define k
k = 3

# Quasi-identifiers
quasi_identifiers = ["Age", "Gender", "City"]

# Count records in each group
group_counts = (
    k_data.groupby(quasi_identifiers)["Disease"]
    .transform("count")
)

# Keep only groups having at least k records
k_anonymous_data = k_data[group_counts >= k].copy()

# Save k-anonymous dataset
k_anonymous_data.to_csv(
    "output/k_anonymous_data.csv",
    index=False
)

print("\n\nK-ANONYMOUS DATA (k = 3)")
print(k_anonymous_data)

# ---------------------------------------------------------
# STEP 4: DIFFERENTIAL PRIVACY
# ---------------------------------------------------------

# Count patients suffering from Diabetes
actual_count = (data["Disease"] == "Diabetes").sum()

# Privacy parameter
epsilon = 1.0

# Sensitivity for a count query
sensitivity = 1

# Generate Laplace noise
noise = np.random.laplace(
    0,
    sensitivity / epsilon
)

# Differentially private count
private_count = actual_count + noise

# Save result
with open(
    "output/differential_privacy_output.txt",
    "w"
) as file:

    file.write("DIFFERENTIAL PRIVACY RESULT\n")
    file.write("---------------------------\n")
    file.write(f"Actual number of Diabetes patients: {actual_count}\n")
    file.write(f"Epsilon: {epsilon}\n")
    file.write(f"Laplace noise: {noise:.4f}\n")
    file.write(
        f"Differentially private count: {private_count:.4f}\n"
    )

print("\n\nDIFFERENTIAL PRIVACY")
print("Actual Diabetes count:", actual_count)
print("Epsilon:", epsilon)
print("Laplace noise:", round(noise, 4))
print(
    "Differentially private count:",
    round(private_count, 4)
)

# ---------------------------------------------------------
# COMPLETION MESSAGE
# ---------------------------------------------------------

print("\n\nAll anonymization techniques completed successfully!")

print("\nOutput files created:")
print("1. output/masked_data.csv")
print("2. output/k_anonymous_data.csv")
print("3. output/differential_privacy_output.txt")
