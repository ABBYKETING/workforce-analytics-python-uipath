# Workforce Analytics & Employee Satisfaction Analysis

**Python Data Analytics | Exploratory Data Analysis | UiPath Automation**

Academic Project — ST1510 Programming for Data Analytics (CA2)  
Singapore Polytechnic | February 2026

## Project Overview

This project investigates how educational background, employment characteristics, and workplace factors relate to income, graduate employment outcomes, and employee satisfaction.

Developed as a two-person academic project, it combines exploratory data analysis (EDA), data preprocessing, statistical visualisation, and robotic process automation (RPA).

## Tools & Technologies

- **Programming:** Python
- **Data Processing:** pandas, NumPy
- **Visualisation:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook
- **Automation:** UiPath Studio
- **Techniques:** Data Cleaning, EDA, Correlation Analysis, Statistical Summarisation, Browser Automation

## Datasets

### 1. Graduate Employment Survey

Explores graduate employment rates and starting salaries across universities, schools and degree fields.

Analysis includes:
- Median salary distributions by school
- Overall employment rates by degree field
- Full-time permanent employment rates

### 2. MOM Labour Force Report 2023

Investigates relationships between occupation, gender, qualification, age and median monthly income.

Analysis includes:
- Income differences by occupation and gender
- Income progression across age groups
- Income patterns by educational qualification

### 3. Glassdoor Employee Reviews

Investigates employee satisfaction and workplace perceptions using 838,566 review records.

Variables include:
- Overall employee rating
- Work-life balance
- Career opportunities
- Senior management
- Compensation and benefits
- Employee recommendations
- Current versus former employment status

## Data Preprocessing

The project uses Python and pandas to:

- Inspect data structures and missing values
- Convert categorical and numeric variables into consistent formats
- Remove invalid or incomplete analytical records where appropriate
- Group schools and degree programmes into broader categories
- Apply median imputation to missing workplace ratings
- Convert employee recommendation responses into binary values
- Aggregate data for statistical comparisons

## Exploratory Data Analysis

Six visualisations were developed across the three datasets.

| Dataset | Visualisation | Purpose |
|---|---|---|
| Graduate Employment | Boxplot | Compare salary distributions |
| Graduate Employment | Grouped Bar Chart | Compare employment rates |
| MOM Labour Force | Line Chart | Examine occupational income differences |
| MOM Labour Force | Multi-Line Chart | Compare income trends by age and qualification |
| Glassdoor Reviews | Grouped Bar Chart | Compare workplace satisfaction |
| Glassdoor Reviews | Correlation Heatmap | Analyse relationships between workplace factors |

## My Individual Contributions

### Glassdoor Employee Satisfaction Analysis

I was responsible for the Glassdoor analysis, including:

- Data cleaning and preparation using pandas
- Employee-status classification
- Missing-value handling through median imputation
- Binary encoding of recommendation responses
- Comparison of current and former employees
- Grouped bar chart visualisation
- Correlation analysis and heatmap visualisation
- Interpretation of findings

### UiPath Automation

I also contributed to the Python script execution and reporting components of the team's UiPath workflow.

The automation demonstrates how UiPath can interact with Python scripts and local output files.

## Selected Results

### Employee Satisfaction

| Metric | Current Employees | Former Employees |
|---|---:|---:|
| Overall Rating | 3.81 | 3.44 |
| Senior Management | 3.29 | 2.94 |

### Correlation with Overall Rating

| Workplace Factor | Pearson Correlation |
|---|---:|
| Senior Management | 0.6843 |
| Career Opportunities | 0.6610 |
| Compensation & Benefits | 0.5467 |
| Work-Life Balance | 0.5217 |
| Recommendation | 0.6276 |

Senior management and career opportunities showed relatively strong positive associations with overall satisfaction.

These relationships are correlational and do not establish causation.

## UiPath Automation

### Dataset Download Workflow

`Download Dataset.xaml`

Uses Chrome browser automation to interact with dataset download controls on Kaggle and the MOM statistical website.

### Python Execution & Reporting Workflow

`Reporting.xaml`

The workflow includes:

1. Execute `generate_graphs.py` using Start Process.
2. Read `report.txt` using Read Text File.
3. Display report content using Message Box.
4. Invoke Outlook Desktop Mail to send an email.

The Python script generates four visualisations covering the Graduate Employment Survey and Glassdoor Reviews datasets.

The MOM analysis is available in the Jupyter Notebook but is not included in the current graph-generation script.

## How to Run

### Python Analysis

Install the required libraries:

`pip install pandas numpy matplotlib seaborn openpyxl jupyter`

Open `PDAS_CA2.ipynb` in Jupyter Notebook and update the dataset paths before running the cells.

### Graph Generation

Run `generate_graphs.py` after configuring its input CSV paths and output locations.

### UiPath

Open the UiPath project in UiPath Studio with the required activity packages installed.

Configure the Python interpreter, dataset paths, local report location, and Outlook settings before running the automation.

## Current Limitations

- Some scripts contain machine-specific absolute file paths.
- The graph-generation script currently writes placeholder text to `report.txt`.
- The supplied report file is a manually prepared summary, not yet a dynamically generated report.
- Dataset download completion is not explicitly verified.
- Outlook reporting uses a fixed message and attachment configuration.
- The workflows have not been independently verified to run unchanged on another computer.

Future improvements include dynamic report generation, configurable paths, error handling and output verification.

## Team Collaboration

This project was completed collaboratively by two students.

**My responsibilities:** Glassdoor Employee Satisfaction Analysis and UiPath script-execution/reporting components.

**Teammate's responsibilities:** Graduate Employment Survey analysis, MOM Labour Force analysis and the data-extraction automation component.

Dataset selection and presentation preparation were collaborative.

## Data Sources

- Singapore Graduate Employment Survey
- [Ministry of Manpower — Employment Statistics](https://stats.mom.gov.sg/Pages/EmploymentTimeSeries.aspx)
- [Glassdoor Job Reviews — Kaggle](https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews)

## Key Learning Outcomes

This project strengthened my practical understanding of:

- Python-based data preprocessing
- Exploratory data analysis
- Statistical interpretation and data visualisation
- Correlation analysis
- Workflow automation using UiPath
- Integrating Python scripts with RPA activities
- Translating analytical findings into meaningful insights

**Note:** This is an academic project. Findings are based on the datasets and preprocessing methods used and should not be interpreted as causal conclusions.
