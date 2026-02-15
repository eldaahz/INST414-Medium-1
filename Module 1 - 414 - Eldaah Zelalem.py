import pandas as pd
import matplotlib.pyplot as plt 


#load data 
df = pd.read_csv('/Users/eldaahzelalem/Downloads/healthcare-dataset-stroke-data.csv')
print(f"Loaded {len(df)} records")

#cleaning 
df = df[df['gender'] != 'Other']
df['bmi'].fillna(df['bmi'].median(), inplace=True)

# analysis 1 - stroke rate by age group 
df['age_group'] = pd.cut(df['age'], bins=[0,40,55,60,100],
                         labels={'<40', '40-55', '55-70', "70+]"})
age_stroke = df.groupby('age_group')['stroke'].mean() * 100
print(age_stroke)

#analysis 2 - stroke rate by hypertension 
hypertension_stroke = df.groupby('hypertension')['stroke'].mean() * 100
print(hypertension_stroke)

#analysis 3 - stroke rate by glucose 
df['glucose_cat'] = pd.cut(df['avg_glucose_level'],
                           bins=[0,100, 126, 300],
                           labels=['Normal', 'Prediabetic', 'Diabetic'])
glucose_stroke = df.groupby('glucose_cat')['stroke'].mean() * 100
print(glucose_stroke)

#figure 1 - age group
plt.figure(figsize=(8,4))
age_stroke.plot(kind='bar', color='steelblue')
plt.title('Stroke rate bye age group')
plt.ylabel('Stroke rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('stroke_by_age.png')

#figure 2 - hypertension
plt.figure(figsize=(8, 4))
hypertension_stroke.plot(kind='bar', color='crimson')
plt.title('Stroke Rate by Hypertension Status')
plt.xlabel('Hypertension (0 = No, 1 = Yes)')
plt.ylabel('Stroke Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('stroke_by_hypertension.png')


#figure 3 - glucose
plt.figure(figsize=(8,4))
glucose_stroke.plot(kind='bar', color='coral')
plt.title('Stroke rate by glucose level')
plt.ylabel('stroke rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('stroke_by_glucose.png')

#validation 
print(f"missing values: {df.isnull().sum()}")
print(f"stroke rate: {df['stroke'].mean():.1%}")