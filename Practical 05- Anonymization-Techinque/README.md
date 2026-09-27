
# Practical 5 – Anonymization Techniques

## Aim

To study and implement different data anonymization techniques to protect sensitive and personally identifiable information (PII) while retaining useful information for analysis.

## Objective

The objectives of this practical are:

* To understand the need for data anonymization.
* To implement data masking.
* To implement k-anonymity.
* To demonstrate differential privacy using the Laplace mechanism.
* To compare original and anonymized data.
* To understand how anonymization helps protect individual privacy.

## Dataset

A synthetic patient dataset was created for this practical.

The dataset contains the following attributes:

| Attribute  | Description                    |
| ---------- | ------------------------------ |
| Patient_ID | Unique identifier of a patient |
| Name       | Name of the patient            |
| Age        | Age of the patient             |
| Gender     | Gender of the patient          |
| City       | City of the patient            |
| Disease    | Medical condition              |
| Salary     | Salary information             |
| Phone      | Phone number                   |
| Email      | Email address                  |

**Note:** The dataset contains completely synthetic data and does not represent real individuals.

## Types of Information

### Direct Identifiers

Direct identifiers can directly identify an individual.

Examples:

* Patient_ID
* Name
* Phone
* Email

### Quasi-Identifiers

Quasi-identifiers may identify an individual when combined with other information.

Examples:

* Age
* Gender
* City

### Sensitive Information

Sensitive information contains private information about an individual.

Examples:

* Disease
* Salary

---

# Anonymization Techniques

## 1. Data Masking

Data masking replaces sensitive information with modified or partially hidden values while maintaining the general format of the data.

In this practical:

* Names were partially masked.
* Phone numbers were partially masked.
* Email addresses were partially masked.

### Example

Original:

```text
Aarav Sharma
9000000001
patient01@example.com
```

Masked:

```text
A***********
XXXXXX0001
p****@example.com
```

The masked dataset is saved as:

```text
output/masked_data.csv
```

---

## 2. K-Anonymity

K-anonymity protects individuals by ensuring that each combination of selected quasi-identifiers occurs at least `k` times in the dataset.

For this practical:

```text
k = 3
```

The following quasi-identifiers were used:

* Age
* Gender
* City

To achieve greater privacy:

* Direct identifiers were removed.
* Age was generalized into age groups.
* Cities were generalized into regions.
* Records were retained only when their quasi-identifier combination had at least 3 occurrences.

### Age Generalization

```text
20–29
30–39
40–49
```

### City Generalization

```text
Delhi + Noida → Delhi-NCR
Gurugram → Gurugram-NCR
```

The resulting k-anonymous dataset is saved as:

```text
output/k_anonymous_data.csv
```

---

## 3. Differential Privacy

Differential privacy protects individual information by adding controlled statistical noise to query results.

In this practical, the number of patients having diabetes was calculated.

The Laplace mechanism was used to add noise.

### Formula

The Laplace mechanism can be represented as:

```text
M(D) = f(D) + Laplace(0, Δf/ε)
```

Where:

* `M(D)` = private result
* `f(D)` = original query result
* `Δf` = sensitivity of the query
* `ε` = privacy parameter
* `Laplace` = Laplace-distributed random noise

For the practical:

```text
ε = 1.0
Sensitivity = 1
```

The actual count and differentially private count are stored in:

```text
output/differential_privacy_output.txt
```

Because random noise is added, the differentially private result may be slightly different each time the program is executed.

---

# Technologies Used

* Python 3.13
* Pandas
* NumPy
* CSV Dataset

## Python Libraries

```python
import pandas as pd
import numpy as np
import os
```

---

# Procedure

1. Create a synthetic patient dataset.
2. Load the dataset using Pandas.
3. Apply data masking to direct identifiers.
4. Remove direct identifiers for k-anonymity.
5. Generalize age and city values.
6. Apply k-anonymity with `k = 3`.
7. Count the number of diabetes patients.
8. Apply Laplace noise to the count.
9. Save all anonymized results.
10. Compare the original and anonymized datasets.

---

# Files and Folders

```text
Practical-5-Anonymization-Techniques/
│
├── README.md
├── anonymization.py
│
├── dataset/
│   └── patient_data.csv
│
└── output/
    ├── masked_data.csv
    ├── k_anonymous_data.csv
    └── differential_privacy_output.txt
```

### File Description

| File                              | Purpose                                               |
| --------------------------------- | ----------------------------------------------------- |
| `anonymization.py`                | Python implementation of all anonymization techniques |
| `patient_data.csv`                | Synthetic original dataset                            |
| `masked_data.csv`                 | Dataset after data masking                            |
| `k_anonymous_data.csv`            | Dataset after applying k-anonymity                    |
| `differential_privacy_output.txt` | Differential privacy calculation and result           |

---

# Results

The following anonymization techniques were successfully implemented:

### Data Masking

Directly identifiable information such as names, phone numbers and email addresses was partially hidden.

### K-Anonymity

The dataset was generalized and filtered using:

```text
k = 3
```

so that retained quasi-identifier combinations occur at least three times.

### Differential Privacy

Laplace noise was added to the diabetes patient count to demonstrate privacy-preserving statistical analysis.

---

# Advantages of Anonymization

* Protects personally identifiable information.
* Reduces the risk of privacy breaches.
* Allows data to be used for analysis while protecting individuals.
* Helps organizations follow privacy and data protection principles.
* Reduces the possibility of identifying individuals from released datasets.

---

# Limitations

* Anonymization may reduce the usefulness of some data.
* Poorly designed anonymization can still allow re-identification.
* Stronger privacy protection may reduce data accuracy.
* Differential privacy introduces statistical noise into results.
* K-anonymity alone may not protect against all privacy attacks.

---

# Conclusion

This practical demonstrated three important anonymization techniques: **data masking, k-anonymity, and differential privacy**.

Data masking was used to hide direct identifiers, k-anonymity was used to generalize quasi-identifiers and reduce the possibility of identifying individuals, and differential privacy was demonstrated by adding Laplace noise to an aggregate query.

These techniques demonstrate how sensitive datasets can be processed and analyzed while reducing the exposure of individual information.
