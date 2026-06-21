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
- LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)
- GitHub: [github.com/yourname](https://github.com/yourname)
- Email: your@email.com

## 📄 License
MIT License — free to use and modify
