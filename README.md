# WarehouseShipmentDistributionData
## Warehouse Shipment Distribution Data Analysis (2025)

## 项目概述 | Project Overview

本项目旨在通过分析2025年的销售数据，优化美国海外仓的分布策略。我们利用数据科学技术，识别销售热点、预测需求、评估仓库位置，并提出成本效益最优的仓储布局方案。

This project aims to optimize the distribution of overseas warehouses in the United States by analyzing 2025 sales data. Using data science techniques, we identify sales hotspots, forecast demand, evaluate warehouse locations, and propose cost‑effective warehouse layout strategies.

## 背景与问题 | Background & Problem

随着跨境电商的快速发展，物流效率成为影响客户满意度和运营成本的关键因素。美国作为主要市场，其海外仓的分布直接决定了配送时效和运费成本。当前仓库布局可能存在以下问题：

- 仓库位置与需求热点不匹配，导致配送距离过长。
- 库存分配不均，某些仓库积压而另一些缺货。
- 季节性波动未充分考虑，造成旺季运力不足。

通过分析2025年的销售数据，我们希望回答：
1. 销售密集区域在哪里？
2. 如何根据预测需求重新规划仓库位置？
3. 如何降低平均配送距离和运输成本？

## 目标 | Objectives

- **数据清洗与整合**：整理2025年销售订单、产品、客户地理位置等数据。
- **空间分析**：使用地理信息系统（GIS）技术可视化销售热点。
- **需求预测**：应用时间序列模型预测未来一年的销售趋势。
- **仓库选址优化**：建立数学模型（如p‑median问题）求解最优仓库位置。
- **成本效益分析**：比较不同布局方案下的运输、仓储和运营成本。
- **可视化报告**：生成交互式地图和仪表板，支持决策。

## 数据 | Data

本项目使用的数据包括（示例）：

1. **销售订单表**：订单ID、产品ID、数量、金额、下单时间、配送地址（经纬度）。
2. **产品表**：产品ID、类别、重量、体积。
3. **仓库表**：仓库ID、位置、容量、运营成本。
4. **物流成本表**：距离‑成本对照、运输方式费率。

数据已做匿名化处理，仅用于分析演示。

## 方法 | Methodology

### 1. 数据预处理
- 处理缺失值、异常值。
- 地理编码：将地址转换为经纬度坐标。
- 构建销售‑时间‑空间联合数据集。

### 2. 探索性数据分析（EDA）
- 销售时间趋势图。
- 热力图展示销售密度。
- 客户分布聚类分析。

### 3. 需求预测
- 使用ARIMA、Prophet或LSTM预测各区域未来销量。
- 考虑季节性、促销活动等因素。

### 4. 仓库选址模型
- 采用p‑median模型最小化总配送距离。
- 约束条件：仓库容量、服务半径、开设成本。
- 使用OR‑Tools或Gurobi求解。

### 5. 仿真与评估
- 模拟不同仓库布局下的配送性能。
- 计算关键指标：平均配送时间、成本、服务水平。

## 技术栈 | Tech Stack

- **编程语言**：Python 3.9+
- **数据分析**：Pandas, NumPy, SciPy
- **可视化**：Matplotlib, Seaborn, Plotly, Folium
- **地理空间分析**：GeoPandas, Shapely, OSMnx
- **机器学习**：Scikit‑learn, TensorFlow (可选)
- **优化求解**：OR‑Tools, PuLP
- **仪表板**：Streamlit / Dash
- **版本控制**：Git, GitHub

## 安装与使用 | Installation & Usage

### 环境准备
确保已安装Python 3.9或更高版本。

### 克隆仓库
```bash
git clone https://github.com/your-username/WarehouseShipmentDistributionData.git
cd WarehouseShipmentDistributionData
```

### 创建虚拟环境（推荐）
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行分析流程
1. 数据预处理：
   ```bash
   python src/data_preprocessing.py
   ```
2. 执行EDA：
   ```bash
   python src/eda.py
   ```
3. 运行优化模型：
   ```bash
   python src/optimization.py
   ```
4. 启动可视化仪表板：
   ```bash
   streamlit run src/dashboard.py
   ```

## 结果与可视化 | Results & Visualization

### 销售热点图
![Sales Hotspot Map](images/sales_hotspot.png)

### 仓库选址结果
![Warehouse Locations](images/warehouse_locations.png)

### 成本对比
| 方案 | 平均配送距离(km) | 月运输成本($) | 仓库数量 |
|------|-------------------|----------------|----------|
| 现有布局 | 420 | 125,000 | 8 |
| 优化布局 | 310 | 98,500 | 6 |

### 交互式仪表板
启动Streamlit应用后，可通过浏览器交互式探索数据、调整参数并查看实时优化结果。

## 结论 | Conclusion

通过分析2025年销售数据，我们提出了一套基于数据驱动的美国海外仓分布优化方案。该方案可减少平均配送距离约26%，降低月运输成本约21%，同时维持服务水平。优化后的仓库布局更贴近需求热点，提升了整体物流效率。

## 未来工作 | Future Work

- 纳入实时销售数据，实现动态仓库调整。
- 考虑多式联运（海运、空运、陆运）的成本模型。
- 集成供应链风险因素（如港口拥堵、天气延误）。
- 开发自动化部署管道，支持定期重优化。

## 贡献 | Contributing

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库。
2. 创建特性分支 (`git checkout -b feature/your-feature`)。
3. 提交更改 (`git commit -m 'Add some feature'`)。
4. 推送到分支 (`git push origin feature/your-feature`)。
5. 开启 Pull Request。

请确保代码符合PEP8规范，并添加适当的测试。

## 许可证 | License

本项目采用 MIT 许可证 – 详见 [LICENSE](LICENSE) 文件。

## 联系方式 | Contact

如有问题或合作意向，请联系：

- 项目维护者：Your Name
- 邮箱：your.email@example.com
- GitHub Issues: [项目 Issues 页面](https://github.com/your-username/WarehouseShipmentDistributionData/issues)

---

*最后更新：2025‑12‑18*