# decodelabs_task02
═════════════════════════════════════════════════════════════════════════════

📊 EXECUTIVE SUMMARY
═════════════════════════════════════════════════════════════════════════════

Total Revenue: $1,264,761.96
Total Orders: 1,200
Average Order Value: $1,053.97
Unique Customers: 1,189
Date Range: 2023-01-01 to 2025-06-30
Products: 7
Payment Methods: 5

═════════════════════════════════════════════════════════════════════════════

📈 SECTION 1: BASIC STATISTICS
═════════════════════════════════════════════════════════════════════════════

1.1 QUANTITY STATISTICS:
    Count:      1200
    Mean:       2.95 units
    Median:     3.00 units
    Mode:       1 units
    Std Dev:    1.41
    Min:        1 units
    Max:        5 units
    Range:      4 units

1.2 UNIT PRICE STATISTICS:
    Mean:       $356.41
    Median:     $364.21
    Std Dev:    $197.18
    Min:        $11.39
    Max:        $699.93
    Range:      $688.54
    Skewness:   -0.027
    Kurtosis:   -1.191

1.3 TOTAL PRICE STATISTICS:
    Sum:        $1,264,761.96
    Mean:       $1,053.97
    Median:     $823.62
    Std Dev:    $819.86
    Min:        $11.39
    Max:        $3,456.40
    Range:      $3,445.01

1.4 ITEMS IN CART STATISTICS:
    Mean:       5.49
    Median:     5.00
    Mode:       5
    Std Dev:    2.28
    Min:        1
    Max:        10

═════════════════════════════════════════════════════════════════════════════

📊 SECTION 2: DISTRIBUTION ANALYSIS
═════════════════════════════════════════════════════════════════════════════

2.1 QUANTITY DISTRIBUTION:
Quantity
1    255
2    240
3    237
4    251
5    217

2.2 PRICE PERCENTILES:
    10th: $165.01
    20th: $331.98
    30th: $471.55
    40th: $625.06
    50th: $823.62
    60th: $1,070.10
    70th: $1,361.35
    80th: $1,768.06
    90th: $2,332.08
    95th: $2,666.45
    99th: $3,277.91

2.3 PAYMENT METHOD BREAKDOWN:
    Online              :   258 (21.50%)
    Cash                :   246 (20.50%)
    Credit Card         :   234 (19.50%)
    Debit Card          :   232 (19.33%)
    Gift Card           :   230 (19.17%)

2.4 TOP PRODUCTS BY VOLUME:
    Printer             :   181 (15.08%)
    Tablet              :   179 (14.92%)
    Chair               :   178 (14.83%)
    Laptop              :   173 (14.42%)
    Desk                :   170 (14.17%)
    Monitor             :   163 (13.58%)
    Phone               :   156 (13.00%)

2.5 ORDER STATUS DISTRIBUTION:
    Cancelled           :   250 (20.83%)
    Returned            :   247 (20.58%)
    Pending             :   237 (19.75%)
    Shipped             :   235 (19.58%)
    Delivered           :   231 (19.25%)

═════════════════════════════════════════════════════════════════════════════

📉 SECTION 3: TREND ANALYSIS
═════════════════════════════════════════════════════════════════════════════

3.1 MONTHLY PERFORMANCE SUMMARY:
    Total Orders: 1200
    Avg Monthly Orders: 40
    Peak Month: 2024-06
    Best Month Revenue: $68,068.54

3.2 SEASONAL PATTERNS:
    Average Q1 Revenue: $145,412.78
    Average Q2 Revenue: $141,088.74
    Average Q3 Revenue: $126,699.47
    Average Q4 Revenue: $139,442.25

3.3 BEST PERFORMING DAY:
    Monday: 174 orders ($184,009.38)
    Tuesday: 165 orders ($180,780.14)
    Wednesday: 163 orders ($160,519.31)
    Thursday: 166 orders ($182,066.56)
    Friday: 174 orders ($190,598.20)
    Saturday: 172 orders ($167,593.53)
    Sunday: 186 orders ($199,194.84)

═════════════════════════════════════════════════════════════════════════════

⚠️  SECTION 4: OUTLIER DETECTION
═════════════════════════════════════════════════════════════════════════════

4.1 PRICE OUTLIERS (IQR Method):
    Lower Bound: $-1,341.41
    Upper Bound: $3,330.41
    Outliers Found: 8 (0.67%)
    
    Interpretation: These are unusually high or low priced orders

4.2 UNIT PRICE OUTLIERS:
    Lower Bound: $-317.20
    Upper Bound: $1,024.83
    Outliers Found: 0 (0.00%)

4.3 QUANTITY OUTLIERS:
    Lower Bound: -1.00
    Upper Bound: 7.00
    Outliers Found: 0 (0.00%)

4.4 Z-SCORE ANALYSIS (Z > 3):
    Extreme Outliers: 0
    Percentage: 0.00%

═════════════════════════════════════════════════════════════════════════════

🔗 SECTION 5: CORRELATION ANALYSIS
═════════════════════════════════════════════════════════════════════════════

5.1 CORRELATION MATRIX:
             Quantity  UnitPrice  ItemsInCart  TotalPrice
Quantity        1.000      0.015        0.650       0.615
UnitPrice       0.015      1.000        0.001       0.717
ItemsInCart     0.650      0.001        1.000       0.393
TotalPrice      0.615      0.717        0.393       1.000

5.2 KEY INSIGHTS:
    • Quantity & TotalPrice: 0.615 (Strong Positive)
    • UnitPrice & TotalPrice: 0.717 (Very Strong)
    • ItemsInCart & Quantity: 0.650 (Weak)
    
    Interpretation: Total price is heavily influenced by unit price, not quantity

═════════════════════════════════════════════════════════════════════════════

💡 SECTION 6: KEY INSIGHTS & RECOMMENDATIONS
═════════════════════════════════════════════════════════════════════════════


[1] REVENUE METRICS:
    • Total Revenue: $1,264,761.96
    • Average Order Value: $1,053.97
    • Median Order Value: $823.62

[2] CUSTOMER BEHAVIOR:
    • Total Customers: 1189
    • Repeat Purchase Customers: 22
    • Customer Retention: 1.85%

[3] PRODUCT PERFORMANCE:
    • Best Selling Product: Chair
    • Revenue from Chair: $195,620.11
    • Average Units per Order: 2.95

[4] ORDER FULFILLMENT:
    • Delivered Orders: 231 (19.25%)
    • Cancelled Orders: 250 (20.83%)
    • Returned Orders: 247 (20.58%)
    • Success Rate: 38.83%

[5] PRICING ANALYSIS:
    • Price Range: $11.39 - $699.93
    • Average Unit Price: $356.41
    • Price Volatility (Std Dev): $197.18

[6] SEASONAL TRENDS:
    • Peak Month: 2024-06
    • Lowest Month: 2023-04

[7] MARKETING EFFECTIVENESS:
    • Top Referral Source: Instagram
    • Average Order Value from Instagram: $1,062.88
    • Coupon Discount Rate: 74.25%

[8] CUSTOMER PREFERENCES:
    • High-Value Orders (Top 25%): 300 (25.00%)
    • Low-Value Orders (Bottom 25%): 299 (24.92%)

═════════════════════════════════════════════════════════════════════════════

📊 SECTION 7: PRODUCT PERFORMANCE RANKING
═════════════════════════════════════════════════════════════════════════════

Top Products by Revenue:
         Orders  Total_Revenue  Avg_Order  Avg_Qty
Product                                           
Chair       178      195620.11    1098.99     3.16
Printer     181      195612.61    1080.73     2.99
Laptop      173      192126.56    1110.56     3.09
Tablet      179      186568.95    1042.28     2.78
Monitor     163      175651.41    1077.62     2.94
Desk        170      167459.93     985.06     2.99
Phone       156      151722.39     972.58     2.63

═════════════════════════════════════════════════════════════════════════════

🎯 SECTION 8: RECOMMENDATIONS
═════════════════════════════════════════════════════════════════════════════

1. REVENUE OPTIMIZATION:
   • Focus on high-value products (Chair)
   • Implement dynamic pricing strategies
   • Bundle low-performing products with high-performers

2. CUSTOMER RETENTION:
   • Current retention rate: 1.85%
   • Target: Increase through loyalty programs
   • Focus on repeat customer incentives

3. FULFILLMENT IMPROVEMENT:
   • Current delivery success rate: 38.83%
   • Reduce cancellation rate: 20.83%
   • Investigate reasons for returns: 20.58%

4. MARKETING STRATEGY:
   • Top referral source: Instagram
   • Increase investment in high-ROI channels
   • Optimize coupon strategy (current usage: 74.25%)

5. PRICING STRATEGY:
   • Analyze price sensitivity
   • Current price range: $11.39 - $699.93
   • Consider premium offerings
