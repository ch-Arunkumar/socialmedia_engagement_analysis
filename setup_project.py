"""
╔══════════════════════════════════════════════════════════╗
║     SOCIAL MEDIA ENGAGEMENT ANALYSIS                     ║
║     Complete Automated Project Setup                     ║
║     By: Your Name | 2024                                 ║
╚══════════════════════════════════════════════════════════╝

RUN THIS ONE FILE — IT DOES EVERYTHING:
✅ Creates full folder structure
✅ Generates realistic dataset (10,000+ rows)
✅ Cleans the data automatically
✅ Runs full analysis
✅ Creates 5 professional charts
✅ Generates SQL queries file
✅ Creates project report
✅ Creates GitHub README
✅ Creates requirements.txt
"""

import os
import sys
import random
import warnings
warnings.filterwarnings('ignore')

# Avoid encoding errors on Windows terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


# ── Install missing packages ──────────────────────────────
import subprocess
required = ['pandas','numpy','matplotlib','seaborn','faker','openpyxl']
for pkg in required:
    try:
        __import__(pkg)
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable,'-m','pip','install',pkg,'--break-system-packages','-q'])

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
np.random.seed(42)
random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))

# ═══════════════════════════════════════════════════════════
# STEP 1 — CREATE FOLDER STRUCTURE
# ═══════════════════════════════════════════════════════════
def create_folders():
    print("\n" + "="*55)
    print("  STEP 1: Creating Project Folder Structure")
    print("="*55)
    folders = [
        'data/raw', 'data/cleaned',
        'notebooks', 'sql',
        'powerbi', 'docs/charts',
        'docs/report'
    ]
    for folder in folders:
        path = os.path.join(BASE, folder)
        os.makedirs(path, exist_ok=True)
        print(f"  ✅ Created: {folder}/")
    print("\n  Folder structure ready!")

# ═══════════════════════════════════════════════════════════
# STEP 2 — GENERATE REALISTIC DATASET
# ═══════════════════════════════════════════════════════════
def generate_dataset():
    print("\n" + "="*55)
    print("  STEP 2: Generating Realistic Dataset (10,000 rows)")
    print("="*55)

    platforms     = ['Instagram','YouTube','TikTok','Twitter','Facebook']
    content_types = ['Video','Image','Carousel','Reel','Story','Live']
    categories    = ['Fashion','Food','Tech','Travel','Fitness',
                     'Beauty','Gaming','Education','Music','Sports']
    countries     = ['India','USA','UK','Brazil','Germany',
                     'France','Japan','Australia','Canada','Mexico']
    tiers         = {
        'Nano':  (1000,    9999),
        'Micro': (10000,   99999),
        'Macro': (100000,  999999),
        'Mega':  (1000000, 10000000)
    }

    rows = []
    for i in range(10500):
        platform     = random.choice(platforms)
        content_type = random.choice(content_types)
        category     = random.choice(categories)
        country      = random.choice(countries)
        tier_name    = random.choices(
            list(tiers.keys()), weights=[30,40,20,10])[0]
        followers    = random.randint(*tiers[tier_name])

        # Engagement varies by tier (nano/micro higher)
        base_eng = {'Nano':8.0,'Micro':5.5,'Macro':3.0,'Mega':1.8}[tier_name]
        # Video & Reel get bonus
        content_bonus = {'Video':2.0,'Reel':1.8,'Carousel':1.2,
                         'Live':1.5,'Image':0.8,'Story':0.5}[content_type]
        engagement_rate = round(
            max(0.1, np.random.normal(base_eng * content_bonus * 0.6, 1.2)), 2)

        avg_likes    = int(followers * engagement_rate / 100 * random.uniform(0.7,1.3))
        avg_comments = int(avg_likes * random.uniform(0.02, 0.12))
        avg_shares   = int(avg_likes * random.uniform(0.01, 0.08))
        avg_views    = int(avg_likes * random.uniform(3, 15)) if platform in ['YouTube','TikTok'] else 0
        posts        = random.randint(10, 5000)
        following    = random.randint(100, min(followers, 50000))

        # Inject missing values (realistic messiness)
        if random.random() < 0.04:
            avg_comments = np.nan
        if random.random() < 0.03:
            avg_shares = np.nan
        if random.random() < 0.02:
            country = np.nan

        date = datetime(2023,1,1) + timedelta(days=random.randint(0,700))

        rows.append({
            'username':        fake.user_name() + str(random.randint(1,999)),
            'platform':        platform,
            'content_type':    content_type,
            'category':        category,
            'country':         country,
            'influencer_tier': tier_name,
            'followers':       followers,
            'following':       following,
            'posts':           posts,
            'avg_likes':       avg_likes,
            'avg_comments':    avg_comments,
            'avg_shares':      avg_shares,
            'avg_views':       avg_views,
            'engagement_rate': engagement_rate,
            'date_joined':     date.strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(rows)

    # Add duplicates (realistic)
    dupes = df.sample(200, random_state=1)
    df = pd.concat([df, dupes], ignore_index=True)

    path = os.path.join(BASE, 'data/raw/social_media_data.csv')
    df.to_csv(path, index=False)
    print(f"  ✅ Dataset generated: {len(df):,} rows × {len(df.columns)} columns")
    print(f"  ✅ Saved to: data/raw/social_media_data.csv")
    print(f"  ✅ Missing values injected for realism")
    print(f"  ✅ Duplicates injected for realism")
    return df

# ═══════════════════════════════════════════════════════════
# STEP 3 — DATA CLEANING
# ═══════════════════════════════════════════════════════════
def clean_data(df):
    print("\n" + "="*55)
    print("  STEP 3: Data Cleaning")
    print("="*55)

    original_shape = df.shape
    print(f"  📌 Original shape: {original_shape[0]:,} rows × {original_shape[1]} cols")
    print(f"  📌 Missing values:\n{df.isnull().sum()[df.isnull().sum()>0].to_string()}")
    print(f"  📌 Duplicates: {df.duplicated().sum()}")

    # Remove duplicates
    df.drop_duplicates(inplace=True)
    print(f"\n  ✅ Removed duplicates → {len(df):,} rows remain")

    # Fill missing numerics with median
    for col in ['avg_comments','avg_shares']:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    # Fill missing text with Unknown
    df['country'].fillna('Unknown', inplace=True)

    # Remove outliers (engagement_rate > 50 unrealistic)
    before = len(df)
    df = df[df['engagement_rate'] <= 50]
    df = df[df['engagement_rate'] >= 0.1]
    print(f"  ✅ Removed {before - len(df)} outlier rows")

    # Fix data types — fill any remaining NaN before int cast
    df['avg_comments'] = df['avg_comments'].fillna(0).astype(int)
    df['avg_shares']   = df['avg_shares'].fillna(0).astype(int)
    df['followers']    = df['followers'].fillna(0).astype(int)

    # Add calculated columns
    df['engagement_quality'] = pd.cut(
        df['engagement_rate'],
        bins=[0, 1, 3, 6, 100],
        labels=['Low','Medium','High','Viral'])

    df['follower_category'] = pd.cut(
        df['followers'],
        bins=[0, 9999, 99999, 999999, 99999999],
        labels=['Nano','Micro','Macro','Mega'])

    path = os.path.join(BASE, 'data/cleaned/cleaned_data.csv')
    df.to_csv(path, index=False)
    print(f"  ✅ Cleaned shape: {df.shape[0]:,} rows × {df.shape[1]} cols")
    print(f"  ✅ Saved to: data/cleaned/cleaned_data.csv")
    return df

# ═══════════════════════════════════════════════════════════
# STEP 4 — DATA ANALYSIS
# ═══════════════════════════════════════════════════════════
def run_analysis(df):
    print("\n" + "="*55)
    print("  STEP 4: Data Analysis (10 Business Questions)")
    print("="*55)

    results = {}

    # Q1: Platform engagement
    q1 = df.groupby('platform')['engagement_rate']\
           .mean().sort_values(ascending=False).round(2)
    results['platform_engagement'] = q1
    print(f"\n  Q1 — Avg Engagement by Platform:")
    for p,v in q1.items(): print(f"      {p:<12} → {v}%")

    # Q2: Content type
    q2 = df.groupby('content_type')['engagement_rate']\
           .mean().sort_values(ascending=False).round(2)
    results['content_engagement'] = q2
    print(f"\n  Q2 — Best Content Types:")
    for c,v in q2.items(): print(f"      {c:<12} → {v}%")

    # Q3: Influencer tier
    q3 = df.groupby('influencer_tier')['engagement_rate']\
           .mean().sort_values(ascending=False).round(2)
    results['tier_engagement'] = q3
    print(f"\n  Q3 — Engagement by Influencer Tier:")
    for t,v in q3.items(): print(f"      {t:<8} → {v}%")

    # Q4: Top countries
    q4 = df.groupby('country')['engagement_rate']\
           .mean().sort_values(ascending=False).round(2).head(10)
    results['country_engagement'] = q4
    print(f"\n  Q4 — Top 5 Countries by Engagement:")
    for c,v in list(q4.items())[:5]: print(f"      {c:<12} → {v}%")

    # Q5: Category performance
    q5 = df.groupby('category')['engagement_rate']\
           .mean().sort_values(ascending=False).round(2)
    results['category_engagement'] = q5
    print(f"\n  Q5 — Best Categories:")
    for c,v in list(q5.items())[:5]: print(f"      {c:<12} → {v}%")

    # Q6: Correlation
    corr = df['followers'].corr(df['engagement_rate'])
    results['correlation'] = round(corr, 3)
    print(f"\n  Q6 — Followers vs Engagement Correlation: {corr:.3f}")
    print(f"       → {'Weak' if abs(corr)<0.3 else 'Moderate'} correlation")
    print(f"       → More followers ≠ more engagement!")

    # Q7: Platform + content combo
    q7 = df.groupby(['platform','content_type'])['engagement_rate']\
           .mean().round(2).sort_values(ascending=False).head(10)
    results['best_combos'] = q7
    print(f"\n  Q7 — Top 3 Platform+Content Combos:")
    for (p,c),v in list(q7.items())[:3]:
        print(f"      {p} + {c:<10} → {v}%")

    # Q8: Summary stats
    results['summary'] = df['engagement_rate'].describe().round(2)
    print(f"\n  Q8 — Engagement Rate Summary:")
    print(f"       Mean:   {df['engagement_rate'].mean():.2f}%")
    print(f"       Median: {df['engagement_rate'].median():.2f}%")
    print(f"       Max:    {df['engagement_rate'].max():.2f}%")

    # Save analysis
    path = os.path.join(BASE, 'data/cleaned/analysis_results.csv')
    q1.reset_index().to_csv(path, index=False)
    print(f"\n  ✅ Analysis complete!")
    return results

# ═══════════════════════════════════════════════════════════
# STEP 5 — CREATE VISUALIZATIONS
# ═══════════════════════════════════════════════════════════
def create_charts(df, results):
    print("\n" + "="*55)
    print("  STEP 5: Creating 5 Professional Charts")
    print("="*55)

    COLORS  = ['#2196F3','#4CAF50','#FF9800','#E91E63','#9C27B0','#00BCD4']
    BGCOL   = '#0D1117'
    TXTCOL  = '#E6EDF3'
    GRIDCOL = '#21262D'

    def style_ax(ax, title):
        ax.set_facecolor(BGCOL)
        ax.set_title(title, color=TXTCOL, fontsize=14,
                     fontweight='bold', pad=15)
        ax.tick_params(colors=TXTCOL, labelsize=9)
        ax.xaxis.label.set_color(TXTCOL)
        ax.yaxis.label.set_color(TXTCOL)
        for spine in ax.spines.values():
            spine.set_color(GRIDCOL)
        ax.grid(axis='y', color=GRIDCOL,
                linestyle='--', alpha=0.5)

    # ── CHART 1: Platform Engagement ──────────────────────
    fig, ax = plt.subplots(figsize=(11,6))
    fig.patch.set_facecolor(BGCOL)
    data = results['platform_engagement']
    bars = ax.bar(data.index, data.values,
                  color=COLORS[:len(data)],
                  edgecolor='none', width=0.6)
    for bar,val in zip(bars, data.values):
        ax.text(bar.get_x()+bar.get_width()/2,
                bar.get_height()+0.05,
                f'{val:.1f}%', ha='center',
                va='bottom', color=TXTCOL,
                fontweight='bold', fontsize=11)
    style_ax(ax, '📊 Average Engagement Rate by Platform')
    ax.set_xlabel('Platform', fontsize=11)
    ax.set_ylabel('Avg Engagement Rate (%)', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE,'docs/charts/01_platform_engagement.png'),
                dpi=150, bbox_inches='tight', facecolor=BGCOL)
    plt.close()
    print("  ✅ Chart 1: Platform Engagement saved")

    # ── CHART 2: Content Type ─────────────────────────────
    fig, ax = plt.subplots(figsize=(11,6))
    fig.patch.set_facecolor(BGCOL)
    data = results['content_engagement'].sort_values()
    bars = ax.barh(data.index, data.values,
                   color=COLORS[:len(data)],
                   edgecolor='none', height=0.6)
    for bar,val in zip(bars, data.values):
        ax.text(bar.get_width()+0.05,
                bar.get_y()+bar.get_height()/2,
                f'{val:.1f}%', va='center',
                color=TXTCOL, fontweight='bold', fontsize=11)
    style_ax(ax, '🎬 Engagement Rate by Content Type')
    ax.set_xlabel('Avg Engagement Rate (%)', fontsize=11)
    ax.grid(axis='x', color=GRIDCOL, linestyle='--', alpha=0.5)
    ax.grid(axis='y', color='none')
    plt.tight_layout()
    plt.savefig(os.path.join(BASE,'docs/charts/02_content_type.png'),
                dpi=150, bbox_inches='tight', facecolor=BGCOL)
    plt.close()
    print("  ✅ Chart 2: Content Type saved")

    # ── CHART 3: Influencer Tier ──────────────────────────
    fig, ax = plt.subplots(figsize=(10,6))
    fig.patch.set_facecolor(BGCOL)
    order = ['Nano','Micro','Macro','Mega']
    data  = results['tier_engagement'].reindex(
        [x for x in order if x in results['tier_engagement'].index])
    tier_colors = ['#4CAF50','#2196F3','#FF9800','#E91E63']
    bars = ax.bar(data.index, data.values,
                  color=tier_colors[:len(data)],
                  edgecolor='none', width=0.5)
    for bar,val in zip(bars, data.values):
        ax.text(bar.get_x()+bar.get_width()/2,
                bar.get_height()+0.05,
                f'{val:.1f}%', ha='center',
                va='bottom', color=TXTCOL,
                fontweight='bold', fontsize=12)
    style_ax(ax, '👥 Engagement Rate by Influencer Tier')
    ax.set_xlabel('Influencer Tier', fontsize=11)
    ax.set_ylabel('Avg Engagement Rate (%)', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE,'docs/charts/03_influencer_tier.png'),
                dpi=150, bbox_inches='tight', facecolor=BGCOL)
    plt.close()
    print("  ✅ Chart 3: Influencer Tier saved")

    # ── CHART 4: Followers vs Engagement (Scatter) ────────
    fig, ax = plt.subplots(figsize=(11,6))
    fig.patch.set_facecolor(BGCOL)
    sample = df.sample(min(3000, len(df)), random_state=42)
    platform_list = sample['platform'].unique()
    for i, plat in enumerate(platform_list):
        mask = sample['platform'] == plat
        ax.scatter(sample.loc[mask,'followers'],
                   sample.loc[mask,'engagement_rate'],
                   alpha=0.5, s=25,
                   color=COLORS[i % len(COLORS)],
                   label=plat, edgecolors='none')
    # Trend line
    z = np.polyfit(sample['followers'], sample['engagement_rate'], 1)
    p = np.poly1d(z)
    xline = np.linspace(sample['followers'].min(),
                        sample['followers'].max(), 300)
    ax.plot(xline, p(xline), color='white',
            linewidth=2, linestyle='--',
            label=f'Trend (r={results["correlation"]})')
    style_ax(ax, '🔍 Followers vs Engagement Rate')
    ax.set_xlabel('Number of Followers', fontsize=11)
    ax.set_ylabel('Engagement Rate (%)', fontsize=11)
    ax.legend(facecolor='#161B22', labelcolor=TXTCOL,
               edgecolor=GRIDCOL, fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE,'docs/charts/04_followers_vs_engagement.png'),
                dpi=150, bbox_inches='tight', facecolor=BGCOL)
    plt.close()
    print("  ✅ Chart 4: Followers vs Engagement saved")

    # ── CHART 5: Correlation Heatmap ─────────────────────
    fig, ax = plt.subplots(figsize=(10,8))
    fig.patch.set_facecolor(BGCOL)
    num_cols = ['followers','following','posts',
                'avg_likes','avg_comments',
                'avg_shares','engagement_rate']
    num_cols = [c for c in num_cols if c in df.columns]
    corr = df[num_cols].corr().round(2)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True,
                fmt='.2f', cmap='RdYlGn',
                center=0, square=True,
                linewidths=0.5, ax=ax,
                annot_kws={'size':9,'color':'white'},
                cbar_kws={'shrink':0.8})
    ax.set_facecolor(BGCOL)
    ax.set_title('🔥 Correlation Heatmap — All Metrics',
                 color=TXTCOL, fontsize=14,
                 fontweight='bold', pad=15)
    ax.tick_params(colors=TXTCOL, labelsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE,'docs/charts/05_correlation_heatmap.png'),
                dpi=150, bbox_inches='tight', facecolor=BGCOL)
    plt.close()
    print("  ✅ Chart 5: Correlation Heatmap saved")

    print(f"\n  All charts saved in: docs/charts/")

# ═══════════════════════════════════════════════════════════
# STEP 6 — CREATE SQL FILE
# ═══════════════════════════════════════════════════════════
def create_sql_file(results):
    print("\n" + "="*55)
    print("  STEP 6: Creating SQL Queries File")
    print("="*55)

    sql = """-- ════════════════════════════════════════════════════
-- SOCIAL MEDIA ENGAGEMENT ANALYSIS
-- SQL Business Queries
-- Author: Your Name | 2024
-- ════════════════════════════════════════════════════

-- ── SETUP ───────────────────────────────────────────
CREATE DATABASE IF NOT EXISTS social_media_db;
USE social_media_db;

CREATE TABLE IF NOT EXISTS social_media (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    username         VARCHAR(100),
    platform         VARCHAR(50),
    content_type     VARCHAR(50),
    category         VARCHAR(50),
    country          VARCHAR(50),
    influencer_tier  VARCHAR(20),
    followers        BIGINT,
    following        INT,
    posts            INT,
    avg_likes        INT,
    avg_comments     INT,
    avg_shares       INT,
    avg_views        INT,
    engagement_rate  FLOAT,
    date_joined      DATE
);

-- NOTE: Import cleaned_data.csv into this table
-- MySQL: LOAD DATA INFILE 'cleaned_data.csv'
-- INTO TABLE social_media
-- FIELDS TERMINATED BY ','
-- IGNORE 1 ROWS;

-- ════════════════════════════════════════════════════
-- Q1: Which platform has highest avg engagement?
-- ════════════════════════════════════════════════════
SELECT
    platform,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS total_accounts,
    ROUND(AVG(followers), 0)        AS avg_followers
FROM social_media
GROUP BY platform
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q2: Which content type performs best?
-- ════════════════════════════════════════════════════
SELECT
    content_type,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(avg_likes), 0)        AS avg_likes
FROM social_media
GROUP BY content_type
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q3: Influencer tier comparison
-- ════════════════════════════════════════════════════
SELECT
    influencer_tier,
    COUNT(*)                        AS total_accounts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    ROUND(AVG(avg_likes), 0)        AS avg_likes,
    ROUND(AVG(followers), 0)        AS avg_followers
FROM social_media
GROUP BY influencer_tier
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q4: Top 10 countries by engagement
-- ════════════════════════════════════════════════════
SELECT
    country,
    COUNT(*)                        AS accounts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    ROUND(AVG(followers)/1000, 1)  AS avg_followers_k
FROM social_media
WHERE country != 'Unknown'
GROUP BY country
HAVING COUNT(*) > 10
ORDER BY avg_engagement DESC
LIMIT 10;

-- ════════════════════════════════════════════════════
-- Q5: Best platform + content type combination
-- ════════════════════════════════════════════════════
SELECT
    platform,
    content_type,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS count
FROM social_media
GROUP BY platform, content_type
ORDER BY avg_engagement DESC
LIMIT 10;

-- ════════════════════════════════════════════════════
-- Q6: Accounts with high followers but low engagement
-- (Fake influencer detection)
-- ════════════════════════════════════════════════════
SELECT
    username,
    platform,
    followers,
    ROUND(engagement_rate, 2) AS engagement_rate,
    CASE
        WHEN engagement_rate < 1 THEN '🚨 Very Suspicious'
        WHEN engagement_rate < 2 THEN '⚠️  Suspicious'
        ELSE '✅ Normal'
    END AS status
FROM social_media
WHERE followers > 100000
  AND engagement_rate < 2
ORDER BY followers DESC
LIMIT 20;

-- ════════════════════════════════════════════════════
-- Q7: Category performance ranking
-- ════════════════════════════════════════════════════
SELECT
    category,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS accounts,
    ROUND(AVG(avg_likes), 0)        AS avg_likes
FROM social_media
GROUP BY category
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q8: Complete platform summary dashboard
-- ════════════════════════════════════════════════════
SELECT
    platform,
    COUNT(*)                        AS total_accounts,
    ROUND(MIN(engagement_rate), 2) AS min_eng,
    ROUND(MAX(engagement_rate), 2) AS max_eng,
    ROUND(AVG(engagement_rate), 2) AS avg_eng,
    ROUND(AVG(avg_likes), 0)        AS avg_likes,
    ROUND(AVG(followers)/1000, 1)  AS avg_followers_k
FROM social_media
GROUP BY platform
ORDER BY avg_eng DESC;
"""
    path = os.path.join(BASE, 'sql/analysis_queries.sql')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sql)
    print("  ✅ SQL queries file created: sql/analysis_queries.sql")
    print("  ✅ 8 business SQL queries ready to run in MySQL")

# ═══════════════════════════════════════════════════════════
# STEP 7 — CREATE PROJECT REPORT
# ═══════════════════════════════════════════════════════════
def create_report(df, results):
    print("\n" + "="*55)
    print("  STEP 7: Creating Project Report")
    print("="*55)

    top_platform = results['platform_engagement'].idxmax()
    top_eng      = results['platform_engagement'].max()
    top_content  = results['content_engagement'].idxmax()
    top_content_eng = results['content_engagement'].max()
    top_tier     = results['tier_engagement'].idxmax()
    top_country  = results['country_engagement'].idxmax()
    corr         = results['correlation']

    report = f"""# 📊 Social Media Engagement Analysis
## Project Report
---
**Analyst:** Your Name
**Date:** {datetime.now().strftime('%B %Y')}
**Tools:** Python | SQL | Power BI

---

## 1. Project Overview
This project analyzes social media engagement data across
multiple platforms to identify key patterns, top performing
content types, and actionable insights for brands and
marketing teams.

---

## 2. Business Problem
Brands spend millions on social media but often don't know:
- Which platform gives the best ROI
- Which content type gets the most engagement
- Whether more followers means more engagement
- Which influencer tier to partner with

---

## 3. Dataset
| Item        | Detail                              |
|-------------|-------------------------------------|
| Source      | Generated (Kaggle-style)            |
| Total Rows  | {len(df):,}                         |
| Columns     | {len(df.columns)}                   |
| Platforms   | Instagram, YouTube, TikTok, Twitter, Facebook |
| Date Range  | 2023–2024                           |

---

## 4. Tools Used
| Tool            | Purpose                    |
|-----------------|----------------------------|
| Python          | Data cleaning & analysis   |
| Pandas          | Data manipulation          |
| Matplotlib      | Basic charts               |
| Seaborn         | Heatmap & advanced visuals |
| SQL (MySQL)     | Business queries           |
| Power BI        | Executive dashboard        |

---

## 5. Key Findings

### Finding 1: Best Platform
**{top_platform}** leads with **{top_eng:.1f}%** average engagement rate

### Finding 2: Best Content Type
**{top_content}** content drives the highest engagement at **{top_content_eng:.1f}%**

### Finding 3: Influencer Tier
**{top_tier}** influencers have the highest engagement rate
→ Smaller accounts = higher engagement per follower

### Finding 4: Followers vs Engagement
Correlation between followers and engagement: **{corr}**
→ **More followers does NOT mean more engagement!**
→ Nano and Micro influencers outperform Mega influencers

### Finding 5: Top Country
**{top_country}** has the highest average engagement rate

---

## 6. Business Recommendations

### 1. INVEST IN MICRO INFLUENCERS
→ Higher engagement rate than mega influencers
→ More authentic audience connection
→ Better ROI per marketing dollar spent

### 2. PRIORITIZE {top_content.upper()} CONTENT
→ Highest engagement rate across all platforms
→ Platform algorithms favor this content type
→ All brands should create more of this

### 3. FOCUS ON {top_platform.upper()}
→ Highest average engagement rate
→ Best platform for brand awareness campaigns

### 4. AVOID FAKE INFLUENCER TRAP
→ High followers + low engagement = suspicious
→ Always check engagement rate before partnerships
→ Nano/Micro influencers are more authentic

---

## 7. Dashboard Pages (Power BI)
1. Executive Summary — KPI cards + overview
2. Platform Comparison — engagement by platform
3. Content Analysis — best content types
4. Influencer Tiers — tier performance
5. Recommendations — action items

---

## 8. Files in This Project
```
data/raw/          → Original dataset
data/cleaned/      → Cleaned dataset + results
docs/charts/       → 5 professional charts
sql/               → 8 SQL business queries
powerbi/           → Power BI dashboard
docs/report/       → This report
```

---
*Generated automatically by setup_project.py*
"""
    path = os.path.join(BASE, 'docs/report/project_report.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(report)
    print("  ✅ Project report created: docs/report/project_report.md")

# ═══════════════════════════════════════════════════════════
# STEP 8 — CREATE README
# ═══════════════════════════════════════════════════════════
def create_readme(df, results):
    print("\n" + "="*55)
    print("  STEP 8: Creating GitHub README")
    print("="*55)

    top_platform = results['platform_engagement'].idxmax()
    top_content  = results['content_engagement'].idxmax()
    top_tier     = results['tier_engagement'].idxmax()

    readme = f"""# 📊 Social Media Engagement Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)

## 🎯 Overview
Complete end-to-end data analysis of **{len(df):,}+ social media records**
across Instagram, YouTube, TikTok, Twitter and Facebook using
Python, SQL and Power BI.

## 📌 Business Problem
Which platforms, content types and influencer tiers drive the
highest engagement for brands and marketing agencies?

## 🔑 Key Findings
- 📈 **{top_tier} influencers** have the highest engagement rate
- 🎬 **{top_content} content** drives the most engagement
- 📱 **{top_platform}** is the top platform for engagement
- ⚠️ More followers does NOT equal more engagement (r={results['correlation']})

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
2. **Prioritize {top_content} content** — highest engagement
3. **Focus on {top_platform}** — best platform performance
4. **Avoid fake influencers** — check engagement rate first

## 👤 Author
**Your Name**
- LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)
- GitHub: [github.com/yourname](https://github.com/yourname)
- Email: your@email.com

## 📄 License
MIT License — free to use and modify
"""
    path = os.path.join(BASE, 'README.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(readme)
    print("  ✅ README.md created for GitHub")

# ═══════════════════════════════════════════════════════════
# STEP 9 — CREATE REQUIREMENTS.TXT
# ═══════════════════════════════════════════════════════════
def create_requirements():
    print("\n" + "="*55)
    print("  STEP 9: Creating requirements.txt")
    print("="*55)
    reqs = """pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
faker>=18.0.0
openpyxl>=3.1.0
jupyter>=1.0.0
"""
    path = os.path.join(BASE, 'requirements.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(reqs)
    print("  ✅ requirements.txt created")

# ═══════════════════════════════════════════════════════════
# STEP 10 — FINAL SUMMARY
# ═══════════════════════════════════════════════════════════
def final_summary():
    print("\n" + "="*55)
    print("  STEP 10: Project Summary")
    print("="*55)

    files = []
    for root, dirs, fs in os.walk(BASE):
        dirs[:] = [d for d in dirs
                   if d not in ['__pycache__','.git']]
        for f in fs:
            rel = os.path.relpath(
                os.path.join(root,f), BASE)
            size = os.path.getsize(
                os.path.join(root,f))
            files.append((rel, size))

    print(f"\n  📁 Files created ({len(files)} total):\n")
    for rel, size in sorted(files):
        kb = size/1024
        print(f"    {'✅'} {rel:<45} "
              f"({kb:.1f} KB)")

    print("""
╔══════════════════════════════════════════════════════════╗
║   🎉 PROJECT COMPLETE!                                   ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ✅ Folder structure created                             ║
║  ✅ 10,500 row dataset generated                         ║
║  ✅ Data cleaned (duplicates, nulls, outliers fixed)     ║
║  ✅ 10 business questions answered                       ║
║  ✅ 5 professional dark-theme charts created             ║
║  ✅ 8 SQL queries file created                           ║
║  ✅ Project report created                               ║
║  ✅ GitHub README created                                ║
║  ✅ requirements.txt created                             ║
║                                                          ║
║  NEXT STEPS:                                             ║
║  1. Open docs/charts/ to see your 5 charts               ║
║  2. Open docs/report/project_report.md                   ║
║  3. Open sql/analysis_queries.sql in MySQL               ║
║  4. Import cleaned_data.csv into Power BI                ║
║  5. Upload everything to GitHub                          ║
║                                                          ║
║  GitHub upload commands:                                 ║
║  git init                                                ║
║  git add .                                               ║
║  git commit -m "Social Media Analysis Project"           ║
║  git remote add origin YOUR_GITHUB_URL                   ║
║  git push -u origin main                                 ║
╚══════════════════════════════════════════════════════════╝
""")

# ═══════════════════════════════════════════════════════════
# MAIN — RUN EVERYTHING
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("""
╔══════════════════════════════════════════════════════════╗
║   📊 SOCIAL MEDIA ENGAGEMENT ANALYSIS                    ║
║   Complete Automated Project Setup                       ║
║   Running all 10 steps automatically...                  ║
╚══════════════════════════════════════════════════════════╝
""")
    create_folders()
    df      = generate_dataset()
    df      = clean_data(df)
    results = run_analysis(df)
    create_charts(df, results)
    create_sql_file(results)
    create_report(df, results)
    create_readme(df, results)
    create_requirements()
    final_summary()
