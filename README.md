# 📊 Social Media Engagement Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)

## 🎯 Overview
Complete end-to-end data analysis of **10,500+ social media records**
across Instagram, YouTube, TikTok, Twitter and Facebook using
Python, SQL and Power BI.

## 📌 Business Problem
Which platforms, content types and influencer tiers drive the
highest engagement for brands and marketing agencies?

## 🔑 Key Findings
- 📈 **Nano influencers** have the highest engagement rate
- 🎬 **Video content** drives the most engagement
- 📱 **Facebook** is the top platform for engagement
- ⚠️ More followers does NOT equal more engagement (r=-0.341)

## 🛠️ Tools Used
| Tool | Purpose |
|------|---------|
| Python | Data cleaning & analysis |
| Pandas | Data manipulation |
| Matplotlib & Seaborn | Visualizations |
| MySQL | Business SQL queries |
| Power BI | Executive dashboard |

## 📁 Project Structure
```
social-media-analysis/
├── data/
│   ├── raw/                  ← Original dataset
│   └── cleaned/              ← Cleaned data + results
├── notebooks/                ← Jupyter notebooks
├── sql/                      ← 8 SQL business queries
├── powerbi/                  ← Dashboard (.pbix)
├── docs/
│   ├── charts/               ← 5 professional charts
│   └── report/               ← Project report
├── requirements.txt
├── setup_project.py          ← Run this to set up everything
└── README.md
```

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/YOURUSERNAME/social-media-analysis.git
cd social-media-analysis
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run Complete Setup
```bash
python setup_project.py
```
This single file does EVERYTHING automatically!

### 4. Open SQL Queries
Import `data/cleaned/cleaned_data.csv` into MySQL
Then run queries from `sql/analysis_queries.sql`

### 5. Open Power BI Dashboard
Open `powerbi/dashboard.pbix` in Power BI Desktop
Connect to `data/cleaned/cleaned_data.csv`

## 📊 Charts Generated
| Chart | Description |
|-------|-------------|
| 01_platform_engagement | Avg engagement by platform |
| 02_content_type | Best content types |
| 03_influencer_tier | Tier performance comparison |
| 04_followers_vs_engagement | Scatter plot + trend |
| 05_correlation_heatmap | All metrics correlation |

## 💼 Business Recommendations
1. **Invest in Micro influencers** — higher ROI
2. **Prioritize Video content** — highest engagement
3. **Focus on Facebook** — best platform performance
4. **Avoid fake influencers** — check engagement rate first

## 👤 Author
**Your Name**
- LinkedIn: [linkedin.com/in/challagali-arun-kumar-5a4668290](www.linkedin.com/in/challagali-arun-kumar-5a4668290)
- GitHub: [github.com/ch-Arunkumar](https://github.com/ch-Arunkumar)
- Email: challagaliarun4@email.com

## 📄 License
MIT License — free to use and modify

## INFORMATION ABOUT PROJECT 
This project is an end-to-end Social Media Engagement Analysis portfolio project. It demonstrates how a data analyst cleans, processes, visualizes, and extracts business insights from social media data.

Here is exactly what the project does, step-by-step:

1. Data Generation (Mimicking Real-World Data)
The project automatically generates a realistic dataset of 10,500 social media accounts across 5 platforms (Instagram, YouTube, TikTok, Twitter, and Facebook) and 10 categories (Tech, Fashion, Travel, Fitness, etc.).

To make it realistic, the script injects typical "dirty data" problems like duplicate rows, missing values (NaNs), and unrealistic outliers.
2. Automated Data Cleaning
It cleans the generated dataset using Python (Pandas):

Removes duplicate records.
Fills missing values with logical estimates (e.g., replaces missing comment/share values with the median).
Handles missing country names by labeling them as "Unknown".
Filters out unrealistic engagement rate outliers (like engagement rates over 50%).
3. Business Questions & Analysis
The script runs calculations to answer 10 key marketing business questions:

Avg Engagement by Platform: Which platforms hold the audience's attention best (e.g., Facebook and TikTok lead at over 4.2%).
Best Content Types: Compares Videos, Reels, Lives, Images, and Stories (Videos/Reels have significantly higher engagement rates).
Influencer Tier Performance: Compares Nano, Micro, Macro, and Mega accounts.
Followers vs. Engagement: It calculates the mathematical correlation between follower count and engagement rate. (It finds a negative correlation, proving that more followers do NOT equal higher engagement—smaller Nano/Micro influencers actually get better interaction rates).
4. Data Visualization
It creates 5 professional dark-themed charts inside docs/charts/:

Platform Engagement (Bar Chart): Compares average engagement rates by platform.
Content Type Performance (Horizontal Bar Chart): Visualizes which format (Video vs. Story) gets the most clicks.
Influencer Tier (Bar Chart): Visualizes why Nano and Micro influencers outperform Megas.
Followers vs. Engagement (Scatter Plot): Displays a scatter plot of accounts with a trendline showing the decline in engagement as follower counts grow.
Metrics Correlation Heatmap (Seaborn Heatmap): Shows relationships between followers, views, likes, shares, comments, and engagement rates.
5. SQL & Business Reporting
SQL Queries: It generates sql/analysis_queries.sql containing 8 SQL business queries (such as identifying potential fake influencers by flag-raising accounts with high followers but low engagement).
Markdown Report: It generates a written report (docs/report/project_report.md) detailing the methodology, tools used, key findings, and concrete marketing recommendations (e.g., investing in micro-influencers and prioritizing video content).
What it proves on your GitHub:
For potential employers or clients, this project showcases your ability to:

Write clean Python code.
Clean messy data.
Use analytical libraries (pandas, numpy).
Build professional data visualizations (matplotlib, seaborn).
Write structured database queries (SQL).
Communicate complex analysis as clear business suggestions.
