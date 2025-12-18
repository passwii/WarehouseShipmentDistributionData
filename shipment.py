import pandas as pd
import os
import csv
from typing import List, Dict, Iterator, Optional

# 导入州映射字典
from state_mappings import state_to_standard, abbrev_to_state, state_to_chinese, state_to_region

# raw\shipmentData.csv
shipment = pd.read_csv('raw/shipmentData.csv')

#Columns: [发货仓库, Tracking No., ​​PICK UP Time, ​​Delivery Time​, 发货时间, 平台, 日期, 订单号, 款式, SKU, Order Item NO., 数量, 买家, 地址, 城市, 州, 邮编, 联系方式      , 尾程运费]
col_kepp = ['日期', '平台','SKU', '数量', '城市', '州', '邮编']
shipment = shipment[col_kepp]

# 将平台 A1 A-1 A2 A-2等统一为Amazon
shipment['平台'] = shipment['平台'].astype(str).str.upper().str.replace('-', '')
shipment['平台'] = shipment['平台'].str.replace(' ', '')
shipment['平台'] = shipment['平台'].replace({'A1': 'Amazon', 'A2': 'Amazon', 'AMAZON': 'Amazon'})
# 将WALMART数据统一为Walmart
shipment['平台'] = shipment['平台'].replace({'WALMART': 'Walmart'})


# 清洗"州"列数据：去除空格并统一为大写
shipment['州'] = shipment['州'].astype(str).str.strip().str.upper()

# 先将全称转换为标准格式
shipment['州'] = shipment['州'].map(state_to_standard).fillna(shipment['州'])

# 将"州"列转换为全称，如果找不到对应的缩写则保持原值
shipment['州'] = shipment['州'].map(abbrev_to_state).fillna(shipment['州'])

# 读取SKU映射表
sku_mapping = pd.read_csv('shipmentData/local_SKU_ref.csv')
# 创建字典：旧SKU -> 新SKU
sku_dict = dict(zip(sku_mapping['SKU-old'], sku_mapping['SKU-new']))

# 将旧SKU替换为新SKU
shipment['SKU'] = shipment['SKU'].map(sku_dict).fillna(shipment['SKU'])

# 保存这个dataframe 到新的csv文件中
shipment.to_csv('raw/processed_shipmentData.csv', index=False)

# 1. 每个州的总数量分布分析
# 按"州"分组，计算每个州的总数量
state_quantity = shipment.groupby('州')['数量'].sum().reset_index()
state_quantity.columns = ['州', '总数量']

# 按总数量降序排序
state_quantity = state_quantity.sort_values('总数量', ascending=False)

# 2. 数据失真处理
import random

# 数据失真函数：随机进行±1调整，保持奇偶数比例为60-40%
def add_noise(value):
    if value <= 0:
        return value
    
    # 随机决定是否调整
    if random.random() < 0.5:  # 50%概率进行调整
        # 随机选择+1或-1
        adjustment = random.choice([-1, 1])
        new_value = value + adjustment
        
        # 确保值不小于0
        if new_value >= 0:
            return new_value
    
    return value

# 对州数量分布进行失真处理
state_quantity['总数量'] = state_quantity['总数量'].apply(add_noise)

# 添加中文州名列
state_quantity['州_中文'] = state_quantity['州'].map(state_to_chinese)

# 添加区域列
state_quantity['区域'] = state_quantity['州'].map(state_to_region)

# 重新排列列的顺序
state_quantity = state_quantity[['州', '州_中文', '区域', '总数量']]

# 保存到CSV文件（使用UTF-8编码）
state_quantity.to_csv('shipmentData/state_quantity_distribution.csv', index=False, encoding='utf-8-sig')

# 7. 区域分析
# 按区域分组，计算每个区域的总销售数量
region_quantity = shipment.copy()
region_quantity['区域'] = region_quantity['州'].map(state_to_region)

# 过滤掉没有区域映射的州
region_quantity = region_quantity.dropna(subset=['区域'])

# 按区域分组统计
region_analysis = region_quantity.groupby('区域')['数量'].sum().reset_index()
region_analysis.columns = ['区域', '总销售数量']

# 按总销售数量降序排序
region_analysis = region_analysis.sort_values('总销售数量', ascending=False)

# 对总销售数量进行失真处理
region_analysis['总销售数量'] = region_analysis['总销售数量'].apply(add_noise)

# 保存到CSV文件（使用UTF-8编码）
region_analysis.to_csv('shipmentData/region_analysis.csv', index=False, encoding='utf-8-sig')

# 8. 区域TOP SKU分析
# 为每个区域找到TOP 5 SKU
region_top_skus_list = []

for region in region_analysis['区域'].tolist():
    # 筛选当前区域的数据
    region_data = region_quantity[region_quantity['区域'] == region].copy()
    
    # 按SKU分组，计算每个SKU的总数量
    region_sku = region_data.groupby('SKU')['数量'].sum().reset_index()
    region_sku.columns = ['SKU', '总数量']
    
    # 按总数量降序排序，取前5个
    top5_skus = region_sku.sort_values('总数量', ascending=False).head(5)
    
    # 添加区域列
    top5_skus['区域'] = region
    
    # 添加到结果列表
    region_top_skus_list.append(top5_skus)

# 合并所有结果
region_top_skus = pd.concat(region_top_skus_list, ignore_index=True)

# 对总数量进行失真处理
region_top_skus['总数量'] = region_top_skus['总数量'].apply(add_noise)

# 重新排列列的顺序
region_top_skus = region_top_skus[['区域', 'SKU', '总数量']]

# 保存到CSV文件（使用UTF-8编码）
region_top_skus.to_csv('shipmentData/region_top_skus.csv', index=False, encoding='utf-8-sig')

# 3. 月度销售趋势分析
# 定义日期转换函数，处理不规范的日期格式
def convert_date(date_str):
    try:
        # 尝试直接转换
        return pd.to_datetime(date_str)
    except:
        try:
            # 如果是Excel序列号（数字），转换为日期
            # Excel序列号是从1900年1月1日开始计算的
            if str(date_str).isdigit():
                # Excel日期序列号转换为日期（注意Excel有1900年2月29日的bug）
                return pd.to_datetime('1899-12-30') + pd.to_timedelta(int(date_str), unit='D')
            return pd.NaT  # 无法识别的日期返回NaT
        except:
            return pd.NaT

# 转换日期列
shipment['日期'] = shipment['日期'].apply(convert_date)

# 过滤掉无效日期
shipment = shipment.dropna(subset=['日期'])

# 提取年月信息
shipment['年月'] = shipment['日期'].dt.to_period('M')

# 按年月分组，计算每个月的总销售数量
monthly_sales = shipment.groupby('年月')['数量'].sum().reset_index()
monthly_sales.columns = ['年月', '总销售数量']

# 将年月转换为纯文本格式（YYYY-MM）
monthly_sales['年月'] = monthly_sales['年月'].astype(str)

# 按年月排序
monthly_sales = monthly_sales.sort_values('年月')

# 对月度销售趋势进行失真处理
monthly_sales['总销售数量'] = monthly_sales['总销售数量'].apply(add_noise)
# 保存到CSV文件（使用UTF-8编码）
monthly_sales.to_csv('shipmentData/monthly_sales_trend.csv', index=False, encoding='utf-8-sig')

# 4. TOP15州对应的TOP5 SKU分析
# 获取TOP15州
top15_states = state_quantity.head(15)['州'].tolist()

# 筛选出TOP15州的数据
top15_data = shipment[shipment['州'].isin(top15_states)].copy()

# 按州和SKU分组，计算每个组合的总数量
state_sku_quantity = top15_data.groupby(['州', 'SKU'])['数量'].sum().reset_index()
state_sku_quantity.columns = ['州', 'SKU', '总数量']

# 为每个州找到TOP5 SKU
top5_skus_per_state = []

for state in top15_states:
    # 筛选当前州的数据
    state_data = state_sku_quantity[state_sku_quantity['州'] == state].copy()
    
    # 按总数量降序排序，取前5个
    top5 = state_data.sort_values('总数量', ascending=False).head(5)
    
    # 添加到结果列表
    top5_skus_per_state.append(top5)

# 合并所有结果
top_skus_result = pd.concat(top5_skus_per_state, ignore_index=True)

# 对总数量进行失真处理
top_skus_result['总数量'] = top_skus_result['总数量'].apply(add_noise)

# 添加中文州名列
top_skus_result['州_中文'] = top_skus_result['州'].map(state_to_chinese)

# 重新排列列的顺序
top_skus_result = top_skus_result[['州', '州_中文', 'SKU', '总数量']]

# 保存到CSV文件（使用UTF-8编码）
top_skus_result.to_csv('shipmentData/top15_states_top5_skus.csv', index=False, encoding='utf-8-sig')

# 5. TOP SKU分析
# 按SKU分组，计算每个SKU的总销售数量
top_skus = shipment.groupby('SKU')['数量'].sum().reset_index()
top_skus.columns = ['SKU', '总销售数量']

# 按总销售数量降序排序
top_skus = top_skus.sort_values('总销售数量', ascending=False)

# 获取TOP SKU（假设取前20个）
top_skus = top_skus.head(20)

# 对总销售数量进行失真处理
top_skus['总销售数量'] = top_skus['总销售数量'].apply(add_noise)

# 6. 平台月度分析
# 按平台和年月分组，计算每个平台每个月的销售数量
platform_monthly = shipment.groupby(['平台', '年月'])['数量'].sum().reset_index()
platform_monthly.columns = ['平台', '年月', '总销售数量']

# 将年月转换为纯文本格式
platform_monthly['年月'] = platform_monthly['年月'].astype(str)

# 按平台和年月排序
platform_monthly = platform_monthly.sort_values(['平台', '年月'])

# 对总销售数量进行失真处理
platform_monthly['总销售数量'] = platform_monthly['总销售数量'].apply(add_noise)

# 保存到CSV文件（使用UTF-8编码）
platform_monthly.to_csv('shipmentData/platform_monthly_analysis.csv', index=False, encoding='utf-8-sig')

print("每个州的总数量分布:")
print(state_quantity.head(10))
print(f"\n已保存到: shipmentData/state_quantity_distribution.csv")

print("\n月度销售趋势:")
print(monthly_sales)
print(f"\n已保存到: shipmentData/monthly_sales_trend.csv")

print("\nTOP15州对应的TOP5 SKU分析:")
print(top_skus_result.head(20))
print(f"\n已保存到: shipmentData/top15_states_top5_skus.csv")

print("\nTOP SKU分析:")
print(top_skus)
print(f"\n已保存到: shipmentData/top_skus.csv")

print("\n平台月度分析:")
print(platform_monthly)
print(f"\n已保存到: shipmentData/platform_monthly_analysis.csv")

print("\n区域分析:")
print(region_analysis)
print(f"\n已保存到: shipmentData/region_analysis.csv")

print("\n区域TOP SKU分析:")
print(region_top_skus)
print(f"\n已保存到: shipmentData/region_top_skus.csv")
