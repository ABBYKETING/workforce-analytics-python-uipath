result_to_send = "This is a summary of all datasets."
with open(r"C:/Users/yyuel/Downloads/report.txt", "w") as f:
    f.write(result_to_send)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#----------------------------------------------------------------------------------------
#Dataset 1
# Load CSVs
df_info = pd.read_csv(r"C:/Users/yyuel/Downloads/CA2 Datasets/CA2 Datasets/(1) graduate employment survey modified.csv")
df_employ = pd.read_csv(r"C:/Users/yyuel/Downloads/CA2 Datasets/CA2 Datasets/(2) graduate employment survey modified .csv")

df_employ['Key'] = df_info['Key'] 
df_info_small = df_info[['Key', 'year', 'university', 'school', 'degree']]
df_employ_small = df_employ[['Key','employment_rate_overall','employment_rate_ft_perm','gross_monthly_median']]
df1 = pd.merge(df_info_small, df_employ_small, on='Key', how='inner')

df1['employment_rate_overall'] = pd.to_numeric(df1['employment_rate_overall'].str.strip(), errors='coerce')
df1['employment_rate_ft_perm'] = pd.to_numeric(df1['employment_rate_ft_perm'].str.strip(), errors='coerce')
df1['gross_monthly_median'] = pd.to_numeric(df1['gross_monthly_median'], errors='coerce')
df1['employment_rate_overall'] = df1['employment_rate_overall'] / 100
df1['employment_rate_ft_perm'] = df1['employment_rate_ft_perm'] / 100

df1_clean = df1.dropna(subset=['employment_rate_overall','employment_rate_ft_perm','gross_monthly_median'])

# Simplify degrees into major fields using keyword matching
def simplify_degree(degree):
    degree = str(degree).lower()
    if any(x in degree for x in ['engineering', 'aerospace', 'mechanical', 'civil', 'electrical', 'computer', 'bio', 'chemical', 'materials', 'industrial', 'naval', 'offshore']):
        return 'Engineering'
    elif any(x in degree for x in ['accountancy', 'business', 'economics', 'management', 'finance', 'marketing']):
        return 'Business & Economics'
    elif any(x in degree for x in ['psychology', 'sociology', 'arts', 'communication', 'linguistics', 'public policy']):
        return 'Arts & Social Sciences'
    elif any(x in degree for x in ['medicine', 'nursing', 'dental', 'pharmacy', 'health', 'therap']):
        return 'Medicine & Health'
    elif any(x in degree for x in ['science', 'math', 'biology', 'physics', 'chemistry']):
        return 'Science'
    elif any(x in degree for x in ['law']):
        return 'Law'
    else:
        return 'Other'

df1_clean['degree_field'] = df1_clean['degree'].apply(simplify_degree)

# Simplify schools using keyword matching
def simplify_school(school):
    school = str(school).lower()
    if 'engineering' in school:
        return 'Engineering'
    elif 'business' in school:
        return 'Business'
    elif 'arts' in school or 'humanities' in school or 'social sciences' in school:
        return 'Arts & Social Sciences'
    elif 'science' in school:
        return 'Science'
    elif 'medicine' in school or 'dental' in school or 'law' in school:
        return 'Professional / Law / Medicine'
    elif 'computing' in school or 'information systems' in school:
        return 'Computing / IT'
    elif 'sit' in school or 'trinity' in school or 'overseas' in school:
        return 'SIT / Overseas'
    else:
        return 'Other'

df1_clean['school_simplified'] = df1_clean['school'].apply(simplify_school)
df1_clean[['degree', 'degree_field', 'school', 'school_simplified']].head(10)
#-------------------------------------------------------------------------------

#graph 1
plt.figure(figsize=(10,7))
sns.boxplot(x='school_simplified', y='gross_monthly_median', data=df1_clean, palette='Set1')
plt.ylabel('Median Gross Monthly Salary (SGD)')
plt.title('Distribution of Median Gross Monthly Salary by School')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(r"C:/Users/yyuel/Downloads/graph1.png", dpi=300, bbox_inches='tight')
plt.close()

#-------------------------------------------------------------------------------

#graph2
degree_emp = df1_clean.groupby('degree_field')[['employment_rate_overall', 'employment_rate_ft_perm']].mean().reset_index()

degree_emp = degree_emp.sort_values(by='employment_rate_overall', ascending=True)

degree_emp.plot(x='degree_field', kind='bar', stacked=False, color=['skyblue','salmon'], figsize=(10,6))
plt.ylabel('Employment Rate')
plt.title('Average Employment Rates by Degree Field')
plt.xticks(rotation=0)
plt.ylim(0,1)

plt.tight_layout()
plt.savefig(r"C:/Users/yyuel/Downloads/graph2.png", dpi=300, bbox_inches='tight')
plt.close()

#-----------------------------------------------------------------------------

#Dataset 2
glassdoor_df = pd.read_csv("C:/Users/yyuel/Downloads/glassdoor_reviews.csv/glassdoor_reviews.csv")
glassdoor_df = glassdoor_df[['current', 'overall_rating', 'work_life_balance', 'career_opp', 'senior_mgmt', 'comp_benefits', 'recommend']]

glassdoor_final = glassdoor_df[
    ['current', 'overall_rating', 'work_life_balance',
     'career_opp', 'senior_mgmt', 'comp_benefits', 'recommend']
].copy()

glassdoor_final['current'] = glassdoor_final['current'].str.lower()

glassdoor_final['employee_status'] = glassdoor_final['current'].apply(
    lambda x: 'current' if 'current' in x
    else 'former' if 'former' in x
    else 'other'
)

glassdoor_final['recommend'] = glassdoor_final['recommend'].str.lower()

glassdoor_final['recommend_binary'] = glassdoor_final['recommend'].replace({
    'v': 1,
    'o': 1,
    'x': 0
})

rating_cols = [
    'overall_rating',
    'work_life_balance',
    'career_opp',
    'senior_mgmt',
    'comp_benefits'
]

for col in rating_cols:
    glassdoor_final[col] = glassdoor_final[col].astype('Int64')

for col in ['work_life_balance', 'career_opp', 'senior_mgmt', 'comp_benefits']:
    glassdoor_final[col] = glassdoor_final[col].fillna(
        glassdoor_final[col].median()
    )

glassdoor_final = glassdoor_final[
    ['employee_status', 'overall_rating', 'work_life_balance',
     'career_opp', 'senior_mgmt', 'comp_benefits', 'recommend_binary']
]

#graph 3

rating_cols = [
    'overall_rating',
    'work_life_balance',
    'career_opp',
    'senior_mgmt',
    'comp_benefits'
]
status_grouped = glassdoor_final.groupby('employee_status')[rating_cols].mean()

current_means = status_grouped.loc['current'].values
former_means = status_grouped.loc['former'].values

rec_grouped = (
    glassdoor_final
    .groupby(['employee_status', 'recommend_binary'])['overall_rating']
    .mean()
)

current_rec = rec_grouped.loc[('current', 1)]
current_not = rec_grouped.loc[('current', 0)]
former_rec = rec_grouped.loc[('former', 1)]
former_not = rec_grouped.loc[('former', 0)]

labels = rating_cols + ['recommend', 'not_recommend']

current_ext = np.append(current_means, [current_rec, current_not])
former_ext = np.append(former_means, [former_rec, former_not])
overall_ext = (current_ext + former_ext) / 2

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots(figsize=(13,6))

bars1 = ax.bar(
    x - width, current_ext, width,
    label='Current Employees',
    color='#5DADE2', edgecolor='black'
)

bars2 = ax.bar(
    x, former_ext, width,
    label='Former Employees',
    color='#F1948A', edgecolor='black'
)

bars3 = ax.bar(
    x + width, overall_ext, width,
    label='Average',
    color='#58D68D', edgecolor='black'
)

ax.set_ylabel('Average Rating (1–5)', fontsize=11)
ax.set_title('Employee Satisfaction by Status and Recommendation', fontsize=13)

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend(frameon=False)

ax.set_ylim(0, 5)
ax.grid(axis='y', linestyle='--', alpha=0.4)

def add_labels(bars):
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.05,
            f'{h:.2f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()
plt.savefig(r"C:/Users/yyuel/Downloads/graph3.png", dpi=300, bbox_inches='tight')
plt.close()


#---------------------------------------------

#graph 4
# =======================
# Columns to include in heatmap
# =======================
heatmap_cols = [
    'overall_rating',
    'work_life_balance',
    'career_opp',
    'senior_mgmt',
    'comp_benefits',
    'recommend_binary'  # 1 = recommend, 0 = not recommend
]

# Compute correlation matrix
corr_matrix = glassdoor_final[heatmap_cols].corr()

# =======================
# Plot heatmap
# =======================
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix, 
    annot=True, 
    fmt=".2f", 
    cmap="YlGnBu", 
    cbar=True,
    linewidths=0.5,
    linecolor='gray'
)

plt.title("Correlation Between Workplace Factors and Recommendation", fontsize=13)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(r"C:/Users/yyuel/Downloads/graph4.png", dpi=300, bbox_inches='tight')
plt.close()
