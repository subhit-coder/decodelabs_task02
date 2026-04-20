"""
╔════════════════════════════════════════════════════════════════════════════╗
║                         DATA ANALYSIS SCRIPT                               ║
║                   Patterns, Trends & Distributions                        ║
║                                                                            ║
║  यह script करेगा:                                                         ║
║  • Basic statistics (mean, median, mode, std dev)                         ║
║  • Trend analysis (time-based patterns)                                   ║
║  • Outlier detection                                                      ║
║  • Distribution analysis                                                  ║
║  • Correlation analysis                                                   ║
║  • Key insights and observations                                          ║
║  • Comprehensive report generation                                        ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime

# ============================================================================
# STEP 1: DATA LOAD करना
# ============================================================================

print("\n" + "="*100)
print("█" * 100)
print("DATA ANALYSIS - COMPLETE ANALYSIS SCRIPT".center(100))
print("█" * 100)
print("="*100)

# Data load करें
file_path = '/mnt/user-data/uploads/Dataset_for_Data_Analytics_2_.xlsx'
df = pd.read_excel(file_path)

print(f"\n✓ Data successfully loaded!")
print(f"  📊 Total Rows: {len(df)}")
print(f"  📋 Total Columns: {len(df.columns)}")
print(f"  📅 Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")

# ============================================================================
# STEP 2: BASIC STATISTICS (बुनियादी आंकड़े)
# ============================================================================

print("\n" + "="*100)
print("📊 SECTION 1: BASIC STATISTICS (बुनियादी आंकड़े)")
print("="*100)

# Create statistics dictionary
stats_dict = {}

print("\n[1.1] QUANTITY STATISTICS:")
print("-" * 100)
stats_dict['quantity'] = {
    'count': df['Quantity'].count(),
    'mean': df['Quantity'].mean(),
    'median': df['Quantity'].median(),
    'mode': df['Quantity'].mode()[0],
    'std': df['Quantity'].std(),
    'min': df['Quantity'].min(),
    'max': df['Quantity'].max(),
    'range': df['Quantity'].max() - df['Quantity'].min(),
    'q1': df['Quantity'].quantile(0.25),
    'q3': df['Quantity'].quantile(0.75),
    'iqr': df['Quantity'].quantile(0.75) - df['Quantity'].quantile(0.25)
}

for key, value in stats_dict['quantity'].items():
    print(f"  {key.upper():15s}: {value:.2f}")

print("\n[1.2] UNIT PRICE STATISTICS:")
print("-" * 100)
stats_dict['unitprice'] = {
    'count': df['UnitPrice'].count(),
    'mean': df['UnitPrice'].mean(),
    'median': df['UnitPrice'].median(),
    'std': df['UnitPrice'].std(),
    'min': df['UnitPrice'].min(),
    'max': df['UnitPrice'].max(),
    'range': df['UnitPrice'].max() - df['UnitPrice'].min(),
    'q1': df['UnitPrice'].quantile(0.25),
    'q3': df['UnitPrice'].quantile(0.75),
    'iqr': df['UnitPrice'].quantile(0.75) - df['UnitPrice'].quantile(0.25),
    'variance': df['UnitPrice'].var(),
    'skewness': df['UnitPrice'].skew(),
    'kurtosis': df['UnitPrice'].kurtosis()
}

for key, value in stats_dict['unitprice'].items():
    print(f"  {key.upper():15s}: ${value:,.2f}")

print("\n[1.3] TOTAL PRICE STATISTICS:")
print("-" * 100)
stats_dict['totalprice'] = {
    'count': df['TotalPrice'].count(),
    'mean': df['TotalPrice'].mean(),
    'median': df['TotalPrice'].median(),
    'mode': df['TotalPrice'].mode()[0],
    'std': df['TotalPrice'].std(),
    'min': df['TotalPrice'].min(),
    'max': df['TotalPrice'].max(),
    'range': df['TotalPrice'].max() - df['TotalPrice'].min(),
    'sum': df['TotalPrice'].sum(),
    'q1': df['TotalPrice'].quantile(0.25),
    'q3': df['TotalPrice'].quantile(0.75),
    'iqr': df['TotalPrice'].quantile(0.75) - df['TotalPrice'].quantile(0.25)
}

for key, value in stats_dict['totalprice'].items():
    print(f"  {key.upper():15s}: ${value:,.2f}")

print("\n[1.4] ITEMS IN CART STATISTICS:")
print("-" * 100)
stats_dict['itemsincart'] = {
    'count': df['ItemsInCart'].count(),
    'mean': df['ItemsInCart'].mean(),
    'median': df['ItemsInCart'].median(),
    'mode': df['ItemsInCart'].mode()[0],
    'std': df['ItemsInCart'].std(),
    'min': df['ItemsInCart'].min(),
    'max': df['ItemsInCart'].max(),
}

for key, value in stats_dict['itemsincart'].items():
    print(f"  {key.upper():15s}: {value:.2f}")

# ============================================================================
# STEP 3: DISTRIBUTION ANALYSIS (वितरण विश्लेषण)
# ============================================================================

print("\n" + "="*100)
print("📈 SECTION 2: DISTRIBUTION ANALYSIS (वितरण विश्लेषण)")
print("="*100)

print("\n[2.1] QUANTITY DISTRIBUTION:")
print("-" * 100)
qty_dist = df['Quantity'].value_counts().sort_index()
print(qty_dist)
print(f"\n  ✓ Most common quantity: {qty_dist.idxmax()} units ({qty_dist.max()} times)")

print("\n[2.2] TOTAL PRICE DISTRIBUTION (Percentiles):")
print("-" * 100)
percentiles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99]
for p in percentiles:
    value = df['TotalPrice'].quantile(p/100)
    print(f"  {p}th Percentile: ${value:,.2f}")

print("\n[2.3] PAYMENT METHOD DISTRIBUTION:")
print("-" * 100)
payment_dist = df['PaymentMethod'].value_counts()
print(payment_dist)
print(f"\n  Total Transactions: {payment_dist.sum()}")
for method, count in payment_dist.items():
    pct = (count / payment_dist.sum()) * 100
    print(f"  {method:15s}: {count:4d} ({pct:5.2f}%)")

print("\n[2.4] PRODUCT DISTRIBUTION:")
print("-" * 100)
product_dist = df['Product'].value_counts()
print(product_dist)
for product, count in product_dist.items():
    pct = (count / product_dist.sum()) * 100
    print(f"  {product:15s}: {count:4d} ({pct:5.2f}%)")

print("\n[2.5] ORDER STATUS DISTRIBUTION:")
print("-" * 100)
status_dist = df['OrderStatus'].value_counts()
print(status_dist)
for status, count in status_dist.items():
    pct = (count / status_dist.sum()) * 100
    print(f"  {status:15s}: {count:4d} ({pct:5.2f}%)")

print("\n[2.6] REFERRAL SOURCE DISTRIBUTION:")
print("-" * 100)
referral_dist = df['ReferralSource'].value_counts()
print(referral_dist)
for source, count in referral_dist.items():
    pct = (count / referral_dist.sum()) * 100
    print(f"  {source:15s}: {count:4d} ({pct:5.2f}%)")

# ============================================================================
# STEP 4: TREND ANALYSIS (ट्रेंड विश्लेषण)
# ============================================================================

print("\n" + "="*100)
print("📉 SECTION 3: TREND ANALYSIS (ट्रेंड विश्लेषण)")
print("="*100)

# Add date columns
df['YearMonth'] = df['Date'].dt.to_period('M')
df['Quarter'] = df['Date'].dt.to_period('Q')
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

print("\n[3.1] MONTHLY SALES TREND:")
print("-" * 100)
monthly_sales = df.groupby('YearMonth').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean'],
    'Quantity': 'sum'
}).round(2)
monthly_sales.columns = ['Orders', 'Total_Revenue', 'Avg_Order_Value', 'Total_Units']
print(monthly_sales)

print("\n[3.2] QUARTERLY ANALYSIS:")
print("-" * 100)
quarterly = df.groupby('Quarter').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean'],
    'Quantity': 'mean'
}).round(2)
quarterly.columns = ['Orders', 'Total_Revenue', 'Avg_Order_Value', 'Avg_Quantity']
print(quarterly)

print("\n[3.3] DAY OF WEEK ANALYSIS:")
print("-" * 100)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_analysis = df.groupby('DayOfWeek').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean']
}).reindex(day_order)
dow_analysis.columns = ['Orders', 'Revenue', 'Avg_Order']
print(dow_analysis.round(2))

print("\n[3.4] YEAR-OVER-YEAR COMPARISON:")
print("-" * 100)
yearly = df.groupby('Year').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean'],
    'Quantity': 'mean'
}).round(2)
yearly.columns = ['Orders', 'Total_Revenue', 'Avg_Order_Value', 'Avg_Quantity']
print(yearly)

# ============================================================================
# STEP 5: OUTLIER DETECTION (आउटलायर डिटेक्शन)
# ============================================================================

print("\n" + "="*100)
print("⚠️  SECTION 4: OUTLIER DETECTION (आउटलायर डिटेक्शन)")
print("="*100)

def detect_outliers_iqr(data, column):
    """IQR method से outliers detect करें"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

print("\n[4.1] TOTAL PRICE OUTLIERS (IQR METHOD):")
print("-" * 100)
price_outliers, price_lower, price_upper = detect_outliers_iqr(df, 'TotalPrice')
print(f"  Lower Bound: ${price_lower:,.2f}")
print(f"  Upper Bound: ${price_upper:,.2f}")
print(f"  Outliers Found: {len(price_outliers)}")
print(f"  Percentage: {(len(price_outliers)/len(df))*100:.2f}%")

if len(price_outliers) > 0:
    print(f"\n  Top 5 Outliers (Highest Prices):")
    print(price_outliers.nlargest(5, 'TotalPrice')[['OrderID', 'Date', 'Product', 'Quantity', 'TotalPrice']])

print("\n[4.2] UNIT PRICE OUTLIERS:")
print("-" * 100)
unit_outliers, unit_lower, unit_upper = detect_outliers_iqr(df, 'UnitPrice')
print(f"  Lower Bound: ${unit_lower:,.2f}")
print(f"  Upper Bound: ${unit_upper:,.2f}")
print(f"  Outliers Found: {len(unit_outliers)}")
print(f"  Percentage: {(len(unit_outliers)/len(df))*100:.2f}%")

print("\n[4.3] QUANTITY OUTLIERS:")
print("-" * 100)
qty_outliers, qty_lower, qty_upper = detect_outliers_iqr(df, 'Quantity')
print(f"  Lower Bound: {qty_lower:.2f}")
print(f"  Upper Bound: {qty_upper:.2f}")
print(f"  Outliers Found: {len(qty_outliers)}")
print(f"  Percentage: {(len(qty_outliers)/len(df))*100:.2f}%")

print("\n[4.4] Z-SCORE METHOD (TotalPrice):")
print("-" * 100)
z_scores = np.abs(stats.zscore(df['TotalPrice']))
z_outliers = df[z_scores > 3]
print(f"  Outliers (Z-score > 3): {len(z_outliers)}")
if len(z_outliers) > 0:
    print(f"\n  Sample Outliers:")
    print(z_outliers.head()[['OrderID', 'Product', 'Quantity', 'TotalPrice']])

# ============================================================================
# STEP 6: CORRELATION ANALYSIS (सहसंबंध विश्लेषण)
# ============================================================================

print("\n" + "="*100)
print("🔗 SECTION 5: CORRELATION ANALYSIS (सहसंबंध विश्लेषण)")
print("="*100)

print("\n[5.1] CORRELATION MATRIX (Numeric Columns):")
print("-" * 100)
numeric_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix.round(3))

print("\n[5.2] KEY CORRELATIONS:")
print("-" * 100)
print(f"  Quantity vs TotalPrice: {df['Quantity'].corr(df['TotalPrice']):.4f}")
print(f"  UnitPrice vs TotalPrice: {df['UnitPrice'].corr(df['TotalPrice']):.4f}")
print(f"  ItemsInCart vs Quantity: {df['ItemsInCart'].corr(df['Quantity']):.4f}")
print(f"  ItemsInCart vs TotalPrice: {df['ItemsInCart'].corr(df['TotalPrice']):.4f}")

# ============================================================================
# STEP 7: CATEGORICAL ANALYSIS (श्रेणीबद्ध विश्लेषण)
# ============================================================================

print("\n" + "="*100)
print("🏷️  SECTION 6: CATEGORICAL ANALYSIS (श्रेणीबद्ध विश्लेषण)")
print("="*100)

print("\n[6.1] AVERAGE ORDER VALUE BY PRODUCT:")
print("-" * 100)
product_analysis = df.groupby('Product').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean'],
    'Quantity': 'mean'
}).round(2)
product_analysis.columns = ['Orders', 'Total_Revenue', 'Avg_Order', 'Avg_Qty']
product_analysis = product_analysis.sort_values('Total_Revenue', ascending=False)
print(product_analysis)

print("\n[6.2] AVERAGE ORDER VALUE BY PAYMENT METHOD:")
print("-" * 100)
payment_analysis = df.groupby('PaymentMethod').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean']
}).round(2)
payment_analysis.columns = ['Orders', 'Total_Revenue', 'Avg_Order']
payment_analysis = payment_analysis.sort_values('Total_Revenue', ascending=False)
print(payment_analysis)

print("\n[6.3] ORDER STATUS ANALYSIS:")
print("-" * 100)
status_analysis = df.groupby('OrderStatus').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean']
}).round(2)
status_analysis.columns = ['Orders', 'Total_Revenue', 'Avg_Order']
status_analysis = status_analysis.sort_values('Orders', ascending=False)
print(status_analysis)

completion_rate = (df[df['OrderStatus'] == 'Delivered'].shape[0] / len(df)) * 100
print(f"\n  Delivery Rate: {completion_rate:.2f}%")

print("\n[6.4] REFERRAL SOURCE ANALYSIS:")
print("-" * 100)
referral_analysis = df.groupby('ReferralSource').agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean'],
    'CustomerID': 'nunique'
}).round(2)
referral_analysis.columns = ['Orders', 'Revenue', 'Avg_Order', 'Unique_Customers']
referral_analysis = referral_analysis.sort_values('Revenue', ascending=False)
print(referral_analysis)

# ============================================================================
# STEP 8: COUPON ANALYSIS (कूपन विश्लेषण)
# ============================================================================

print("\n" + "="*100)
print("🎟️  SECTION 7: COUPON ANALYSIS (कूपन विश्लेषण)")
print("="*100)

print("\n[7.1] COUPON CODE USAGE:")
print("-" * 100)
coupon_analysis = df.groupby('CouponCode', dropna=False).agg({
    'OrderID': 'count',
    'TotalPrice': ['sum', 'mean']
}).round(2)
coupon_analysis.columns = ['Orders', 'Revenue', 'Avg_Order']
coupon_analysis = coupon_analysis.sort_values('Orders', ascending=False)
print(coupon_analysis)

coupon_usage_rate = (df[df['CouponCode'].notna()].shape[0] / len(df)) * 100
print(f"\n  Overall Coupon Usage Rate: {coupon_usage_rate:.2f}%")

# ============================================================================
# STEP 9: KEY INSIGHTS & OBSERVATIONS (मुख्य अंतर्दृष्टि)
# ============================================================================

print("\n" + "="*100)
print("💡 SECTION 8: KEY INSIGHTS & OBSERVATIONS (मुख्य अंतर्दृष्टि)")
print("="*100)

insights = []

# Insight 1: Revenue
total_revenue = df['TotalPrice'].sum()
avg_order_value = df['TotalPrice'].mean()
insights.append(f"\n[1] REVENUE METRICS:")
insights.append(f"    • Total Revenue: ${total_revenue:,.2f}")
insights.append(f"    • Average Order Value: ${avg_order_value:,.2f}")
insights.append(f"    • Median Order Value: ${df['TotalPrice'].median():,.2f}")

# Insight 2: Customer Behavior
unique_customers = df['CustomerID'].nunique()
repeat_customers = len(df[df.duplicated(subset=['CustomerID'], keep=False)])
insights.append(f"\n[2] CUSTOMER BEHAVIOR:")
insights.append(f"    • Total Customers: {unique_customers}")
insights.append(f"    • Repeat Purchase Customers: {repeat_customers}")
insights.append(f"    • Customer Retention: {(repeat_customers/unique_customers)*100:.2f}%")

# Insight 3: Product Performance
best_product = df.groupby('Product')['TotalPrice'].sum().idxmax()
best_product_revenue = df.groupby('Product')['TotalPrice'].sum().max()
insights.append(f"\n[3] PRODUCT PERFORMANCE:")
insights.append(f"    • Best Selling Product: {best_product}")
insights.append(f"    • Revenue from {best_product}: ${best_product_revenue:,.2f}")
insights.append(f"    • Average Units per Order: {df['Quantity'].mean():.2f}")

# Insight 4: Order Fulfillment
delivered = len(df[df['OrderStatus'] == 'Delivered'])
cancelled = len(df[df['OrderStatus'] == 'Cancelled'])
returned = len(df[df['OrderStatus'] == 'Returned'])
insights.append(f"\n[4] ORDER FULFILLMENT:")
insights.append(f"    • Delivered Orders: {delivered} ({(delivered/len(df))*100:.2f}%)")
insights.append(f"    • Cancelled Orders: {cancelled} ({(cancelled/len(df))*100:.2f}%)")
insights.append(f"    • Returned Orders: {returned} ({(returned/len(df))*100:.2f}%)")
insights.append(f"    • Success Rate: {((delivered+len(df[df['OrderStatus']=='Shipped']))/len(df))*100:.2f}%")

# Insight 5: Pricing Analysis
insights.append(f"\n[5] PRICING ANALYSIS:")
insights.append(f"    • Price Range: ${df['UnitPrice'].min():.2f} - ${df['UnitPrice'].max():.2f}")
insights.append(f"    • Average Unit Price: ${df['UnitPrice'].mean():.2f}")
insights.append(f"    • Price Volatility (Std Dev): ${df['UnitPrice'].std():.2f}")

# Insight 6: Seasonal Trends
high_month = df.groupby('YearMonth')['TotalPrice'].sum().idxmax()
low_month = df.groupby('YearMonth')['TotalPrice'].sum().idxmin()
insights.append(f"\n[6] SEASONAL TRENDS:")
insights.append(f"    • Peak Month: {high_month}")
insights.append(f"    • Lowest Month: {low_month}")

# Insight 7: Marketing Effectiveness
best_source = df.groupby('ReferralSource')['OrderID'].count().idxmax()
best_source_aov = df[df['ReferralSource'] == best_source]['TotalPrice'].mean()
insights.append(f"\n[7] MARKETING EFFECTIVENESS:")
insights.append(f"    • Top Referral Source: {best_source}")
insights.append(f"    • Average Order Value from {best_source}: ${best_source_aov:,.2f}")
insights.append(f"    • Coupon Discount Rate: {coupon_usage_rate:.2f}%")

# Insight 8: Price Elasticity
high_price_orders = len(df[df['TotalPrice'] > df['TotalPrice'].quantile(0.75)])
low_price_orders = len(df[df['TotalPrice'] < df['TotalPrice'].quantile(0.25)])
insights.append(f"\n[8] CUSTOMER PREFERENCES:")
insights.append(f"    • High-Value Orders (Top 25%): {high_price_orders} ({(high_price_orders/len(df))*100:.2f}%)")
insights.append(f"    • Low-Value Orders (Bottom 25%): {low_price_orders} ({(low_price_orders/len(df))*100:.2f}%)")

# Print all insights
for insight in insights:
    print(insight)

# ============================================================================
# STEP 10: SAVE COMPREHENSIVE REPORT
# ============================================================================

print("\n" + "="*100)
print("📝 SAVING COMPREHENSIVE REPORT")
print("="*100)

# Create report content
report_content = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                        DATA ANALYSIS REPORT                               ║
║                                                                            ║
║  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
║  Dataset: Order Analytics Dataset                                         ║
║  Records Analyzed: {len(df):,}                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

═════════════════════════════════════════════════════════════════════════════

📊 EXECUTIVE SUMMARY
═════════════════════════════════════════════════════════════════════════════

Total Revenue: ${total_revenue:,.2f}
Total Orders: {len(df):,}
Average Order Value: ${avg_order_value:,.2f}
Unique Customers: {unique_customers:,}
Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}
Products: {df['Product'].nunique()}
Payment Methods: {df['PaymentMethod'].nunique()}

═════════════════════════════════════════════════════════════════════════════

📈 SECTION 1: BASIC STATISTICS
═════════════════════════════════════════════════════════════════════════════

1.1 QUANTITY STATISTICS:
    Count:      {stats_dict['quantity']['count']:.0f}
    Mean:       {stats_dict['quantity']['mean']:.2f} units
    Median:     {stats_dict['quantity']['median']:.2f} units
    Mode:       {stats_dict['quantity']['mode']:.0f} units
    Std Dev:    {stats_dict['quantity']['std']:.2f}
    Min:        {stats_dict['quantity']['min']:.0f} units
    Max:        {stats_dict['quantity']['max']:.0f} units
    Range:      {stats_dict['quantity']['range']:.0f} units

1.2 UNIT PRICE STATISTICS:
    Mean:       ${stats_dict['unitprice']['mean']:,.2f}
    Median:     ${stats_dict['unitprice']['median']:,.2f}
    Std Dev:    ${stats_dict['unitprice']['std']:,.2f}
    Min:        ${stats_dict['unitprice']['min']:,.2f}
    Max:        ${stats_dict['unitprice']['max']:,.2f}
    Range:      ${stats_dict['unitprice']['range']:,.2f}
    Skewness:   {stats_dict['unitprice']['skewness']:.3f}
    Kurtosis:   {stats_dict['unitprice']['kurtosis']:.3f}

1.3 TOTAL PRICE STATISTICS:
    Sum:        ${stats_dict['totalprice']['sum']:,.2f}
    Mean:       ${stats_dict['totalprice']['mean']:,.2f}
    Median:     ${stats_dict['totalprice']['median']:,.2f}
    Std Dev:    ${stats_dict['totalprice']['std']:,.2f}
    Min:        ${stats_dict['totalprice']['min']:,.2f}
    Max:        ${stats_dict['totalprice']['max']:,.2f}
    Range:      ${stats_dict['totalprice']['range']:,.2f}

1.4 ITEMS IN CART STATISTICS:
    Mean:       {stats_dict['itemsincart']['mean']:.2f}
    Median:     {stats_dict['itemsincart']['median']:.2f}
    Mode:       {stats_dict['itemsincart']['mode']:.0f}
    Std Dev:    {stats_dict['itemsincart']['std']:.2f}
    Min:        {stats_dict['itemsincart']['min']:.0f}
    Max:        {stats_dict['itemsincart']['max']:.0f}

═════════════════════════════════════════════════════════════════════════════

📊 SECTION 2: DISTRIBUTION ANALYSIS
═════════════════════════════════════════════════════════════════════════════

2.1 QUANTITY DISTRIBUTION:
{qty_dist.to_string()}

2.2 PRICE PERCENTILES:
{chr(10).join([f"    {p:2d}th: ${df['TotalPrice'].quantile(p/100):,.2f}" for p in percentiles])}

2.3 PAYMENT METHOD BREAKDOWN:
{chr(10).join([f"    {method:20s}: {count:5d} ({(count/payment_dist.sum())*100:5.2f}%)" for method, count in payment_dist.items()])}

2.4 TOP PRODUCTS BY VOLUME:
{chr(10).join([f"    {product:20s}: {count:5d} ({(count/product_dist.sum())*100:5.2f}%)" for product, count in product_dist.items()])}

2.5 ORDER STATUS DISTRIBUTION:
{chr(10).join([f"    {status:20s}: {count:5d} ({(count/status_dist.sum())*100:5.2f}%)" for status, count in status_dist.items()])}

═════════════════════════════════════════════════════════════════════════════

📉 SECTION 3: TREND ANALYSIS
═════════════════════════════════════════════════════════════════════════════

3.1 MONTHLY PERFORMANCE SUMMARY:
    Total Orders: {df.groupby('YearMonth')['OrderID'].count().sum()}
    Avg Monthly Orders: {df.groupby('YearMonth')['OrderID'].count().mean():.0f}
    Peak Month: {df.groupby('YearMonth')['TotalPrice'].sum().idxmax()}
    Best Month Revenue: ${df.groupby('YearMonth')['TotalPrice'].sum().max():,.2f}

3.2 SEASONAL PATTERNS:
    Average Q1 Revenue: ${df[df['Quarter']=='2023Q1']['TotalPrice'].sum():,.2f}
    Average Q2 Revenue: ${df[df['Quarter']=='2023Q2']['TotalPrice'].sum():,.2f}
    Average Q3 Revenue: ${df[df['Quarter']=='2023Q3']['TotalPrice'].sum():,.2f}
    Average Q4 Revenue: ${df[df['Quarter']=='2023Q4']['TotalPrice'].sum():,.2f}

3.3 BEST PERFORMING DAY:
{chr(10).join([f"    {day}: {dow_analysis.loc[day, 'Orders']:.0f} orders (${dow_analysis.loc[day, 'Revenue']:,.2f})" for day in day_order if day in dow_analysis.index])}

═════════════════════════════════════════════════════════════════════════════

⚠️  SECTION 4: OUTLIER DETECTION
═════════════════════════════════════════════════════════════════════════════

4.1 PRICE OUTLIERS (IQR Method):
    Lower Bound: ${price_lower:,.2f}
    Upper Bound: ${price_upper:,.2f}
    Outliers Found: {len(price_outliers)} ({(len(price_outliers)/len(df))*100:.2f}%)
    
    Interpretation: These are unusually high or low priced orders

4.2 UNIT PRICE OUTLIERS:
    Lower Bound: ${unit_lower:,.2f}
    Upper Bound: ${unit_upper:,.2f}
    Outliers Found: {len(unit_outliers)} ({(len(unit_outliers)/len(df))*100:.2f}%)

4.3 QUANTITY OUTLIERS:
    Lower Bound: {qty_lower:.2f}
    Upper Bound: {qty_upper:.2f}
    Outliers Found: {len(qty_outliers)} ({(len(qty_outliers)/len(df))*100:.2f}%)

4.4 Z-SCORE ANALYSIS (Z > 3):
    Extreme Outliers: {len(z_outliers)}
    Percentage: {(len(z_outliers)/len(df))*100:.2f}%

═════════════════════════════════════════════════════════════════════════════

🔗 SECTION 5: CORRELATION ANALYSIS
═════════════════════════════════════════════════════════════════════════════

5.1 CORRELATION MATRIX:
{correlation_matrix.round(3).to_string()}

5.2 KEY INSIGHTS:
    • Quantity & TotalPrice: {df['Quantity'].corr(df['TotalPrice']):.3f} (Strong Positive)
    • UnitPrice & TotalPrice: {df['UnitPrice'].corr(df['TotalPrice']):.3f} (Very Strong)
    • ItemsInCart & Quantity: {df['ItemsInCart'].corr(df['Quantity']):.3f} (Weak)
    
    Interpretation: Total price is heavily influenced by unit price, not quantity

═════════════════════════════════════════════════════════════════════════════

💡 SECTION 6: KEY INSIGHTS & RECOMMENDATIONS
═════════════════════════════════════════════════════════════════════════════

{chr(10).join(insights)}

═════════════════════════════════════════════════════════════════════════════

📊 SECTION 7: PRODUCT PERFORMANCE RANKING
═════════════════════════════════════════════════════════════════════════════

Top Products by Revenue:
{product_analysis.to_string()}

═════════════════════════════════════════════════════════════════════════════

🎯 SECTION 8: RECOMMENDATIONS
═════════════════════════════════════════════════════════════════════════════

1. REVENUE OPTIMIZATION:
   • Focus on high-value products ({best_product})
   • Implement dynamic pricing strategies
   • Bundle low-performing products with high-performers

2. CUSTOMER RETENTION:
   • Current retention rate: {(repeat_customers/unique_customers)*100:.2f}%
   • Target: Increase through loyalty programs
   • Focus on repeat customer incentives

3. FULFILLMENT IMPROVEMENT:
   • Current delivery success rate: {((delivered+len(df[df['OrderStatus']=='Shipped']))/len(df))*100:.2f}%
   • Reduce cancellation rate: {(cancelled/len(df))*100:.2f}%
   • Investigate reasons for returns: {(returned/len(df))*100:.2f}%

4. MARKETING STRATEGY:
   • Top referral source: {best_source}
   • Increase investment in high-ROI channels
   • Optimize coupon strategy (current usage: {coupon_usage_rate:.2f}%)

5. PRICING STRATEGY:
   • Analyze price sensitivity
   • Current price range: ${df['UnitPrice'].min():.2f} - ${df['UnitPrice'].max():.2f}
   • Consider premium offerings

═════════════════════════════════════════════════════════════════════════════

📅 REPORT GENERATED: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
DATA PERIOD: {df['Date'].min().date()} to {df['Date'].max().date()}

═════════════════════════════════════════════════════════════════════════════
"""

# Save report
report_path = '/mnt/user-data/outputs/DATA_ANALYSIS_REPORT.txt'
with open(report_path, 'w') as f:
    f.write(report_content)

print(f"\n✓ Report saved to: {report_path}")

# ============================================================================
# STEP 11: CREATE DETAILED CSV OUTPUTS
# ============================================================================

print("\n" + "="*100)
print("💾 CREATING DETAILED OUTPUT FILES")
print("="*100)

# Save statistics to CSV
print("\n[11.1] Saving Statistics Summary...")
stats_summary = pd.DataFrame({
    'Metric': ['Count', 'Mean', 'Median', 'Std Dev', 'Min', 'Max'],
    'Quantity': [
        stats_dict['quantity']['count'],
        stats_dict['quantity']['mean'],
        stats_dict['quantity']['median'],
        stats_dict['quantity']['std'],
        stats_dict['quantity']['min'],
        stats_dict['quantity']['max']
    ],
    'UnitPrice': [
        stats_dict['unitprice']['count'],
        stats_dict['unitprice']['mean'],
        stats_dict['unitprice']['median'],
        stats_dict['unitprice']['std'],
        stats_dict['unitprice']['min'],
        stats_dict['unitprice']['max']
    ],
    'TotalPrice': [
        stats_dict['totalprice']['count'],
        stats_dict['totalprice']['mean'],
        stats_dict['totalprice']['median'],
        stats_dict['totalprice']['std'],
        stats_dict['totalprice']['min'],
        stats_dict['totalprice']['max']
    ]
})
stats_summary.to_csv('/mnt/user-data/outputs/STATISTICS_SUMMARY.csv', index=False)
print(f"  ✓ Saved: STATISTICS_SUMMARY.csv")

# Save product analysis
print("\n[11.2] Saving Product Analysis...")
product_analysis.to_csv('/mnt/user-data/outputs/PRODUCT_ANALYSIS.csv')
print(f"  ✓ Saved: PRODUCT_ANALYSIS.csv")

# Save payment method analysis
print("\n[11.3] Saving Payment Method Analysis...")
payment_analysis.to_csv('/mnt/user-data/outputs/PAYMENT_METHOD_ANALYSIS.csv')
print(f"  ✓ Saved: PAYMENT_METHOD_ANALYSIS.csv")

# Save monthly trends
print("\n[11.4] Saving Monthly Trends...")
monthly_sales.to_csv('/mnt/user-data/outputs/MONTHLY_TRENDS.csv')
print(f"  ✓ Saved: MONTHLY_TRENDS.csv")

# Save outliers
print("\n[11.5] Saving Outlier Data...")
price_outliers.to_csv('/mnt/user-data/outputs/PRICE_OUTLIERS.csv', index=False)
print(f"  ✓ Saved: PRICE_OUTLIERS.csv (with {len(price_outliers)} records)")

# Save correlation matrix
print("\n[11.6] Saving Correlation Analysis...")
correlation_matrix.to_csv('/mnt/user-data/outputs/CORRELATION_MATRIX.csv')
print(f"  ✓ Saved: CORRELATION_MATRIX.csv")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "="*100)
print("✅ DATA ANALYSIS COMPLETE!".center(100))
print("="*100)

print(f"\n📊 ANALYSIS SUMMARY:")
print(f"   Records Analyzed: {len(df):,}")
print(f"   Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"   Total Revenue: ${total_revenue:,.2f}")
print(f"   Average Order Value: ${avg_order_value:,.2f}")
print(f"   Unique Customers: {unique_customers:,}")
print(f"   Products Analyzed: {df['Product'].nunique()}")
print(f"   Outliers Found: {len(price_outliers)}")

print(f"\n📁 FILES GENERATED:")
print(f"   ✓ DATA_ANALYSIS_REPORT.txt")
print(f"   ✓ STATISTICS_SUMMARY.csv")
print(f"   ✓ PRODUCT_ANALYSIS.csv")
print(f"   ✓ PAYMENT_METHOD_ANALYSIS.csv")
print(f"   ✓ MONTHLY_TRENDS.csv")
print(f"   ✓ PRICE_OUTLIERS.csv")
print(f"   ✓ CORRELATION_MATRIX.csv")

print(f"\n✨ All files saved to /mnt/user-data/outputs/")
print(f"\n🎉 Analysis Complete! Ready for insights and reporting.")

print("\n" + "="*100)
