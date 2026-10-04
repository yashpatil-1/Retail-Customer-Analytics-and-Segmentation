# Retail Customer Analytics & Segmentation

> **RFM Analysis • K-Means Clustering • Power BI • Marketing Strategy**

An end-to-end retail customer analytics project that transforms
transaction-level data into actionable customer segments and marketing
strategies using **Python, RFM analysis, K-Means clustering, and Power
BI**.

The project analyzes a public retail transaction dataset and approaches
the problem from a **marketing and business strategy perspective**:
identifying valuable customers, detecting customers at risk of becoming
inactive, and translating behavioral patterns into targeted customer
strategies.

------------------------------------------------------------------------

## 📌 Project Overview

Retail businesses collect large volumes of transaction data, but raw
transactions do not directly explain **which customers matter most or
what action should be taken for each customer group**.

This project addresses the following business question:

> **How can customer transaction data be used to identify distinct
> customer segments and develop targeted marketing strategies for each
> segment?**

The workflow combines:

**Data Cleaning → RFM Analysis → K-Means Clustering → Customer
Segmentation → Power BI Visualization → Marketing Recommendations**

------------------------------------------------------------------------

## 🎯 Business Objectives

-   Identify and quantify the most valuable customer groups.
-   Understand customer purchasing behavior using **Recency, Frequency,
    and Monetary value**.
-   Segment customers based on behavioral patterns.
-   Identify customers who may require retention or win-back campaigns.
-   Translate analytical findings into actionable marketing strategies.
-   Build an interactive Power BI dashboard for business
    decision-making.

------------------------------------------------------------------------

## 🗂️ Dataset

The project uses the **Online Retail II** public retail transaction
dataset.

The dataset contains transaction-level information including:

-   Invoice
-   Stock Code
-   Product Description
-   Quantity
-   Invoice Date
-   Price
-   Customer ID
-   Country

**Important:** This is a public retail dataset and is **not proprietary
Reliance Trends data**. The project is framed through a retail/fashion
marketing business lens for portfolio and analytical purposes.

------------------------------------------------------------------------

## 🔄 Analytical Workflow

``` text
Raw Retail Dataset
        ↓
Data Cleaning
        ↓
Transaction Value Calculation
        ↓
RFM Analysis
        ↓
Log Transformation + Standardization
        ↓
K-Means Clustering
        ↓
Customer Segmentation
        ↓
Power BI Dashboard
        ↓
Marketing Strategy & Recommendations
```

------------------------------------------------------------------------

## 🧹 Data Preparation

The two source sheets were combined before analysis.

### Cleaning rules

1.  Combined the two retail transaction sheets.
2.  Removed transactions without a Customer ID.
3.  Removed cancellation invoices beginning with `C`.
4.  Removed transactions with non-positive quantities.
5.  Removed transactions with non-positive prices.
6.  Removed duplicate records.
7.  Created a `Transaction_Value` field:

``` text
Transaction Value = Quantity × Price
```

### Dataset after cleaning

  Metric                         Result
  ------------------------- -----------
  Original rows               1,067,371
  Clean rows                    779,425
  Rows removed                  287,946
  Unique customers                5,878
  Unique invoices                36,969
  Total transaction value       £17.37M

------------------------------------------------------------------------

## 📊 RFM Analysis

RFM analysis was used to measure customer behavior across three
dimensions.

### Recency

**How recently did the customer purchase?**

Lower recency indicates more recent activity.

### Frequency

**How often did the customer purchase?**

Higher frequency indicates more repeat purchasing.

### Monetary

**How much value did the customer generate?**

Higher monetary value indicates greater customer value.

### RFM results

  Metric            Average
  ----------- -------------
  Recency       201.33 days
  Frequency     6.29 orders
  Monetary        £2,955.90

The RFM snapshot date was **10 December 2011**, one day after the latest
transaction date.

------------------------------------------------------------------------

## 🤖 Customer Segmentation

K-Means clustering was applied to the RFM variables.

Because RFM values can be highly skewed, the analysis used:

1.  `log1p` transformation
2.  StandardScaler normalization
3.  K-Means clustering

### Choosing the number of clusters

Multiple values of K were evaluated using inertia and silhouette score.

    K   Inertia   Silhouette
  --- --------- ------------
    2   8588.99   **0.4386**
    3   6354.34       0.3477
    4   4921.23   **0.3650**
    5   4099.11       0.3425
    6   3554.70       0.3348
    7   3194.50       0.3066
    8   2902.43       0.3033

Although **K=2 produced the highest silhouette score**, K=4 was selected
because it provided more differentiated and actionable customer groups
for marketing strategy.

------------------------------------------------------------------------

## 👥 Final Customer Segments

  Segment                       Customers   Customer Share   Revenue Share
  --------------------------- ----------- ---------------- ---------------
  **Champions**                     1,196           20.35%      **73.87%**
  **At-Risk Valuable**              1,459           24.82%          16.36%
  **New / Promising**               1,250           21.27%           6.17%
  **Low-Engagement / Lost**         1,973           33.57%           3.60%

### Segment interpretation

#### 🏆 Champions

Recent, frequent, and high-value customers.

**Recommended actions:** - VIP rewards - Early access - Personalized
recommendations - Exclusive offers - Cross-selling

**Objective:** Retain customers and increase lifetime value.

------------------------------------------------------------------------

#### ⚠️ At-Risk Valuable

Customers with meaningful historical value but relatively high recency.

**Recommended actions:** - Win-back campaigns - Personalized product
recommendations - Targeted remarketing - Limited-time reactivation
offers

**Objective:** Reactivate valuable customers before they become
inactive.

------------------------------------------------------------------------

#### 🌱 New / Promising

Recent customers with lower purchase frequency but potential for repeat
behavior.

**Recommended actions:** - Second-purchase offers - Product discovery
campaigns - Loyalty enrollment - Post-purchase engagement

**Objective:** Convert new customers into repeat customers.

------------------------------------------------------------------------

#### 💤 Low-Engagement / Lost

Customers with high recency, low frequency, and relatively low monetary
value.

**Recommended actions:** - Automated low-cost reactivation campaigns -
Test incentives selectively - Avoid excessive acquisition/retention
spending

**Objective:** Identify customers worth reactivating while controlling
marketing cost.

------------------------------------------------------------------------

## 💡 Key Business Insight

> **Approximately 20.35% of customers contribute 73.87% of total
> revenue.**

This highlights a strong concentration of revenue among a relatively
small high-value customer segment.

The implication is that customer strategy should not treat every
customer equally. **Retention of high-value customers, reactivation of
valuable inactive customers, and development of promising customers
require different approaches.**

------------------------------------------------------------------------

## 📈 Power BI Dashboard

The project includes a **5-page Power BI dashboard**.

### 1. Executive Overview

Provides a high-level view of:

-   Customers
-   Revenue
-   Orders
-   Customer segment distribution
-   Revenue contribution by segment
-   Overall business performance

### 2. Customer Behaviour & RFM Analysis

Explores:

-   Recency by segment
-   Frequency by segment
-   Customer value
-   Frequency vs. monetary behavior
-   RFM-based customer patterns

### 3. Customer Segmentation

Visualizes:

-   Customer distribution
-   Revenue contribution
-   Segment profiles
-   Average customer value
-   Segment-level comparisons

### 4. Marketing Strategy & Recommendations

Connects analytical findings to business action:

-   Champions → Retention & value expansion
-   At-Risk Valuable → Win-back
-   New / Promising → Repeat purchase development
-   Low-Engagement / Lost → Selective reactivation

### 5. Transaction & Product Analysis

Examines:

-   Revenue trends
-   Country-level revenue
-   Top products by revenue
-   Transaction-level relationships

------------------------------------------------------------------------

## 🛠️ Technology Stack

  Tool               Purpose
  ------------------ -----------------------------------------------
  **Python**         Data preparation and analytics
  **Pandas**         Data manipulation
  **NumPy**          Numerical transformation
  **Scikit-learn**   Standardization, K-Means, silhouette analysis
  **Power BI**       Interactive business dashboard
  **Git & GitHub**   Version control and project documentation

------------------------------------------------------------------------

## 📁 Project Structure

``` text
retail-customer-analytics/
│
├── data/
│   ├── clean_retail_transactions.csv
│   ├── rfm.csv
│   └── final_customer_segments.csv
│
├── powerbi/
│   └── Retail_Customer_Analytics.pbix
│
├── reports/
│
├── screenshots/
│   ├── page1_executive_overview.png
│   ├── page2_rfm_analysis.png
│   ├── page3_customer_segmentation.png
│   ├── page4_marketing_strategy.png
│   └── page5_transaction_analysis.png
│
├── scripts/
│   ├── data_cleaning.py
│   ├── rfm_analysis.py
│   └── clustering.py
│
└── README.md
```

------------------------------------------------------------------------

## ▶️ How to Run the Python Analysis

### 1. Clone the repository

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd retail-customer-analytics
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

``` bash
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install pandas numpy scikit-learn openpyxl
```

### 4. Place the source dataset

Place the `online_retail_II.xlsx` dataset in the project directory
according to the path expected by `data_cleaning.py`.

### 5. Run the analysis

``` bash
python scripts/data_cleaning.py
python scripts/rfm_analysis.py
python scripts/clustering.py
```

The scripts generate:

``` text
data/clean_retail_transactions.csv
data/rfm.csv
data/final_customer_segments.csv
```

------------------------------------------------------------------------

## 📌 Limitations

-   The dataset is historical and therefore does not represent current
    retail behavior.
-   Customer segmentation is based primarily on transaction behavior.
-   K-Means results depend on preprocessing and the selected number of
    clusters.
-   The four segments are designed for business actionability and should
    not be interpreted as fixed customer identities.
-   Marketing recommendations are strategic hypotheses and would require
    A/B testing and campaign-level performance data for validation.
-   The dataset is public and does not represent proprietary data from
    any specific retailer.

------------------------------------------------------------------------

## 🚀 Potential Future Improvements

-   Build customer lifetime value (CLV) models.
-   Add cohort and retention analysis.
-   Introduce predictive churn modeling.
-   Develop propensity-to-purchase models.
-   Test marketing strategies using A/B experiments.
-   Add customer-level recommendation models.
-   Automate dashboard data refresh.
-   Deploy the analytics workflow as a business intelligence
    application.

------------------------------------------------------------------------

## 📌 Portfolio Context

This project demonstrates the ability to combine:

**Technical Analytics**

Python • Data Cleaning • RFM • Machine Learning • K-Means • Data
Visualization

**Business & Management**

Customer Segmentation • Marketing Strategy • Customer Retention •
Revenue Analysis • Business Recommendations

The goal is to bridge **data-driven analysis with practical marketing
decision-making**, rather than treating customer segmentation as a
purely technical exercise.

------------------------------------------------------------------------

## 👤 Author

**Yash Patil**

MBA Tech --- Computer Engineering \
NMIMS

Areas of interest:

**Marketing Strategy • Business Analytics • Strategic Consulting •
Operations • Business Development**

------------------------------------------------------------------------

## ⭐ Project Takeaway

> **The value of customer analytics is not simply identifying different
> customer groups --- it is translating those groups into different
> business actions.**
