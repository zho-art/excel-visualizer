import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from matplotlib.ticker import MaxNLocator
import seaborn as sns
import re
import subprocess
import sys

# 设置中文字体
def setup_chinese_font():
    """配置matplotlib以支持中文显示"""
    plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False
    sns.set(font="SimHei", font_scale=1.0)

class ExcelVisualizer:
    def __init__(self):
        self.df = None
        self.data_range = None
        self.valid_series = {}
        self.categories = []
        self.numeric_columns = []
        self.categorical_columns = []
        self.file_path = ""
        self.sheet_name = 0
        self.auto_fix = True
        
    def validate_file_path(self, file_path):
        """验证文件路径是否有效"""
        path = Path(file_path)
        
        if not path.exists():
            return False, f"文件路径不存在: {file_path}"
        
        if not path.is_file():
            return False, f"不是有效的文件: {file_path}"
        
        valid_extensions = ['.xlsx', '.xls']
        if path.suffix.lower() not in valid_extensions:
            return False, f"不支持的文件格式，支持: {', '.join(valid_extensions)}"
        
        return True, "文件路径验证通过"
    
    def load_data(self, excel_file, sheet_name=0):
        """加载并初步处理Excel数据"""
        self.file_path = excel_file
        self.sheet_name = sheet_name
        
        # 验证文件路径
        print("正在验证文件路径...")
        valid, msg = self.validate_file_path(excel_file)
        if not valid:
            raise ValueError(f"文件验证失败: {msg}")
        print("文件路径验证通过")
        
        # 读取Excel文件
        print("正在读取Excel文件...")
        try:
            self.df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
        except Exception as e:
            try:
                self.df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, engine='xlrd')
            except:
                raise ValueError(f"读取Excel文件失败: {str(e)}")
        
        print(f"成功读取数据，维度: {self.df.shape[0]}行, {self.df.shape[1]}列")
        return self.df
    
    def analyze_data_quality(self):
        """分析数据质量并返回问题列表"""
        if self.df is None:
            raise ValueError("请先加载数据")
            
        issues = []
        total_cells = self.df.size
        empty_cells = self.df.isna().sum().sum()
        empty_ratio = empty_cells / total_cells if total_cells > 0 else 0
        
        if empty_ratio > 0.7:
            issues.append(f"空值比例过高 ({empty_ratio:.1%})，可能导致无有效数据")
        
        numeric_df = self.df.apply(pd.to_numeric, errors='coerce')
        numeric_cells = numeric_df.notna().sum().sum()
        numeric_ratio = numeric_cells / total_cells if total_cells > 0 else 0
        
        # 识别数值列和分类列
        self.numeric_columns = []
        self.categorical_columns = []
        
        for col in range(self.df.shape[1]):
            col_data = self.df.iloc[:, col]
            numeric_col = pd.to_numeric(col_data, errors='coerce')
            if numeric_col.notna().mean() > 0.7:  # 70%以上是数值则视为数值列
                self.numeric_columns.append(col)
            else:
                self.categorical_columns.append(col)
        
        print(f"识别到 {len(self.numeric_columns)} 个数值列，{len(self.categorical_columns)} 个分类列")
        
        if numeric_ratio < 0.3:
            issues.append(f"数值型数据比例过低 ({numeric_ratio:.1%})，可视化可能受限")
        
        return issues, empty_ratio, numeric_ratio
    
    def find_potential_data_ranges(self):
        """自动寻找潜在的数据范围"""
        if self.df is None:
            raise ValueError("请先加载数据")
            
        ranges = []
        
        for start_row in range(min(5, self.df.shape[0])):  # 从开头几行开始寻找
            for start_col in range(min(5, self.df.shape[1])):  # 从开头几列开始寻找
                end_row = start_row
                end_col = start_col
                
                # 扩展行
                while end_row + 1 < self.df.shape[0]:
                    if pd.to_numeric(self.df.iloc[end_row + 1, start_col], errors='coerce') is not np.nan:
                        end_row += 1
                    else:
                        break
                
                # 扩展列
                while end_col + 1 < self.df.shape[1]:
                    if pd.to_numeric(self.df.iloc[start_row, end_col + 1], errors='coerce') is not np.nan:
                        end_col += 1
                    else:
                        break
                
                # 只保留有一定大小的区域
                if (end_row - start_row + 1) >= 3 and (end_col - start_col + 1) >= 1:
                    ranges.append({
                        'x_start_row': start_row,
                        'x_end_row': end_row,
                        'x_start_col': start_col,
                        'x_end_col': start_col,
                        'y_start_row': start_row,
                        'y_end_row': end_row,
                        'y_start_col': start_col + 1 if start_col + 1 <= end_col else start_col,
                        'y_end_col': end_col
                    })
        
        # 按区域大小排序
        ranges.sort(key=lambda x: (x['x_end_row'] - x['x_start_row']) * 
                   (x['y_end_col'] - x['y_start_col']), reverse=True)
        
        return ranges[:3]
    
    def prepare_data(self, data_range=None):
        """准备可视化所需的数据"""
        if self.df is None:
            raise ValueError("请先加载数据")
            
        self.data_range = data_range
        series_data = {}
        self.categories = []
        
        # 手动指定范围
        if data_range is not None:
            print("使用手动指定的数据范围...")
            try:
                x_sr, x_er, x_sc, x_ec, y_sr, y_er, y_sc, y_ec = data_range
                
                if x_sr < 0 or x_er >= self.df.shape[0] or x_sc < 0 or x_ec >= self.df.shape[1]:
                    raise ValueError("X轴范围超出数据边界")
                if y_sr < 0 or y_er >= self.df.shape[0] or y_sc < 0 or y_ec >= self.df.shape[1]:
                    raise ValueError("Y轴范围超出数据边界")
                
                # 类别数据（X轴）
                self.categories = [str(self.df.iloc[i, x_sc]) if pd.notna(self.df.iloc[i, x_sc]) else f"类别{i - x_sr + 1}" 
                             for i in range(x_sr, x_er + 1)]
                
                # 提取系列数据
                for col in range(y_sc, y_ec + 1):
                    series_name = self.df.iloc[y_sr, col] if pd.notna(self.df.iloc[y_sr, col]) else f"系列{col - y_sc + 1}"
                    y_data = [pd.to_numeric(self.df.iloc[i, col], errors='coerce') for i in range(y_sr, y_er + 1)]
                    series_data[str(series_name)] = y_data
            except Exception as e:
                raise ValueError(f"处理手动指定范围失败: {str(e)}")
        
        # 自动识别范围
        else:
            print("正在自动识别数据范围...")
            potential_ranges = self.find_potential_data_ranges()
            
            if not potential_ranges:
                raise ValueError("未找到有效的数据区域，请尝试手动指定范围")
            
            # 使用最佳潜在范围
            best_range = potential_ranges[0]
            print(f"使用自动识别的最佳数据范围: 行 {best_range['x_start_row']}-{best_range['x_end_row']}, "
                  f"列 {best_range['x_start_col']}-{best_range['y_end_col']}")
            
            # 类别数据（X轴）
            self.categories = [str(self.df.iloc[i, best_range['x_start_col']]) if pd.notna(self.df.iloc[i, best_range['x_start_col']]) 
                         else f"类别{i - best_range['x_start_row'] + 1}" 
                         for i in range(best_range['x_start_row'], best_range['x_end_row'] + 1)]
            
            # 提取系列数据
            for col in range(best_range['y_start_col'], best_range['y_end_col'] + 1):
                series_name = self.df.iloc[best_range['y_start_row'], col] if pd.notna(self.df.iloc[best_range['y_start_row'], col]) else f"系列{col - best_range['y_start_col'] + 1}"
                y_data = [pd.to_numeric(self.df.iloc[i, col], errors='coerce') for i in range(best_range['y_start_row'], best_range['y_end_row'] + 1)]
                series_data[str(series_name)] = y_data
        
        # 数据清洗和验证
        n_series = len(series_data)
        n_categories = len(self.categories)
        
        # 确保所有系列长度一致
        for name, data in series_data.items():
            if len(data) != n_categories:
                if len(data) > n_categories:
                    series_data[name] = data[:n_categories]
                else:
                    series_data[name] = data + [np.nan] * (n_categories - len(data))
        
        # 过滤无效值
        self.valid_series = {}
        for name, data in series_data.items():
            cleaned = []
            for val in data:
                if pd.notna(val) and isinstance(val, (int, float, np.number)) and not np.isnan(val):
                    cleaned.append(val)
                else:
                    cleaned.append(0 if self.auto_fix else np.nan)
            self.valid_series[name] = cleaned
        
        # 检查是否有有效数据
        if not self.valid_series or (all(all(v == 0 or np.isnan(v) for v in data) for data in self.valid_series.values()) and not self.auto_fix):
            if self.auto_fix and data_range is None:
                # 尝试其他潜在范围
                potential_ranges = self.find_potential_data_ranges()
                for i, range_data in enumerate(potential_ranges[1:], 1):
                    print(f"尝试第{i+1}个潜在数据范围...")
                    self.categories = [str(self.df.iloc[j, range_data['x_start_col']]) if pd.notna(self.df.iloc[j, range_data['x_start_col']]) 
                                 else f"类别{j - range_data['x_start_row'] + 1}" 
                                 for j in range(range_data['x_start_row'], range_data['x_end_row'] + 1)]
                    
                    for col in range(range_data['y_start_col'], range_data['y_end_col'] + 1):
                        series_name = self.df.iloc[range_data['y_start_row'], col] if pd.notna(self.df.iloc[range_data['y_start_row'], col]) else f"系列{col - range_data['y_start_col'] + 1}"
                        y_data = [pd.to_numeric(self.df.iloc[j, col], errors='coerce') for j in range(range_data['y_start_row'], range_data['y_end_row'] + 1)]
                        self.valid_series[str(series_name)] = [v if pd.notna(v) and not np.isnan(v) else 0 for v in y_data]
                
                if all(all(v == 0 for v in data) for data in self.valid_series.values()):
                    raise ValueError("没有有效数据可用于可视化，请检查数据或手动指定正确范围")
            else:
                raise ValueError("没有有效数据可用于可视化，请检查数据或手动指定正确范围")
        
        print(f"成功提取 {len(self.valid_series)} 个有效数据系列，{len(self.categories)} 个类别")
        return self.categories, self.valid_series
    
    def analyze_data_and_recommend(self):
        """分析数据特征并推荐合适的图表类型"""
        if not self.valid_series or not self.categories:
            raise ValueError("请先准备数据")
            
        recommendations = []
        n_series = len(self.valid_series)
        n_categories = len(self.categories)
        
        # 分析数据特征
        is_time_series = False
        if n_categories > 0:
            # 检查类别是否为日期时间格式
            date_patterns = [
                r'\d{4}-\d{2}-\d{2}',  # yyyy-mm-dd
                r'\d{2}/\d{2}/\d{4}',  # mm/dd/yyyy
                r'\d{2}-\d{2}-\d{4}',  # dd-mm-yyyy
                r'\d{4}年\d{2}月\d{2}日'  # 中文日期
            ]
            
            date_count = 0
            for cat in self.categories[:10]:  # 检查前10个类别
                for pattern in date_patterns:
                    if re.match(pattern, str(cat)):
                        date_count += 1
                        break
            
            if date_count / min(10, n_categories) > 0.7:
                is_time_series = True
                print("检测到时间序列数据")
        
        is_categorical_data = len(self.categorical_columns) > 0
        is_numeric_data = len(self.numeric_columns) > 0
        has_single_series = n_series == 1
        has_multiple_series = n_series > 1
        has_few_categories = n_categories <= 12
        has_many_categories = n_categories > 12
        
        # 基于数据特征推荐图表
        if is_time_series:
            recommendations.extend(["折线图", "面积图"])
            if has_multiple_series:
                recommendations.append("组合图")
        
        if is_categorical_data and has_few_categories:
            recommendations.extend(["柱状图", "条形图"])
            if has_single_series:
                recommendations.append("饼图")
        
        if is_numeric_data and has_many_categories:
            recommendations.append("直方图")
        
        if has_multiple_series and is_numeric_data:
            recommendations.extend(["散点图", "气泡图"])
        
        if has_multiple_series and n_series <= 5 and has_few_categories:
            recommendations.append("箱线图")
        
        # 去重并保持一定顺序
        unique_recommendations = []
        for rec in recommendations:
            if rec not in unique_recommendations:
                unique_recommendations.append(rec)
        
        # 总是添加一些通用选项
        for chart in ["柱状图", "折线图", "组合图"]:
            if chart not in unique_recommendations:
                unique_recommendations.append(chart)
        
        return unique_recommendations[:5]  # 返回前5个推荐
    
    def plot_bar_chart(self, title="数据柱状图", x_label="类别", y_label="数值", 
                      output_file="bar_chart.png", figsize=(12, 7), show_values=True):
        """绘制柱状图"""
        fig, ax = plt.subplots(figsize=figsize)
        
        n_series = len(self.valid_series)
        indices = np.arange(len(self.categories))
        bar_width = 0.8 / n_series
        
        color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        
        for i, (series_name, data) in enumerate(self.valid_series.items()):
            color_idx = i % len(color_cycle)
            bars = ax.bar(indices + i * bar_width, data, bar_width, 
                         label=series_name, color=color_cycle[color_idx], alpha=0.85)
            
            if show_values:
                for bar in bars:
                    height = bar.get_height()
                    if height > 0:
                        ax.annotate(f'{height:.1f}',
                                   xy=(bar.get_x() + bar.get_width() / 2, height),
                                   xytext=(0, 3),
                                   textcoords="offset points",
                                   ha='center', va='bottom', fontsize=8)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.set_xticks(indices + bar_width * (n_series - 1) / 2)
        ax.set_xticklabels(self.categories, rotation=45, ha='right', fontsize=10)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(True, axis='y', linestyle='--', alpha=0.6)
        ax.legend(loc='best', fontsize=10)
        
        total_values = sum(sum(data) for data in self.valid_series.values())
        info_text = f"数据点总数: {len(self.categories) * n_series}, 数值总和: {total_values:.1f}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"柱状图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_pie_chart(self, title="数据饼图", output_file="pie_chart.png", 
                      figsize=(10, 10), explode_small=0.05, small_threshold=0.05):
        """绘制饼图（使用第一个数据系列）"""
        if len(self.valid_series) == 0:
            raise ValueError("没有有效数据可绘制饼图")
            
        # 取第一个数据系列
        first_series_name = next(iter(self.valid_series.keys()))
        data = self.valid_series[first_series_name]
        
        # 过滤零值
        filtered_data = []
        filtered_categories = []
        for d, c in zip(data, self.categories):
            if d > 0:
                filtered_data.append(d)
                filtered_categories.append(c)
        
        if len(filtered_data) == 0:
            raise ValueError("没有有效数据可绘制饼图（所有值均为零）")
        
        total = sum(filtered_data)
        percentages = [d / total for d in filtered_data]
        explode = [explode_small if p < small_threshold else 0 for p in percentages]
        
        fig, ax = plt.subplots(figsize=figsize)
        wedges, texts, autotexts = ax.pie(filtered_data, explode=explode, labels=filtered_categories,
                                         autopct='%1.1f%%', startangle=90, shadow=True)
        
        plt.setp(texts, size=10, weight="bold")
        plt.setp(autotexts, size=8, color="white", weight="bold")
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.axis('equal')
        ax.legend(filtered_categories, title="类别", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"饼图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_line_chart(self, title="数据折线图", x_label="X轴", y_label="Y值", 
                       output_file="line_chart.png", figsize=(12, 7)):
        """绘制折线图"""
        fig, ax = plt.subplots(figsize=figsize)
        
        styles = ['-', '--', '-.', ':']
        markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*']
        color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        
        for i, (series_name, data) in enumerate(self.valid_series.items()):
            style_idx = i % len(styles)
            marker_idx = i % len(markers)
            color_idx = i % len(color_cycle)
            
            ax.plot(range(len(self.categories)), data, label=series_name,
                    linestyle=styles[style_idx], marker=markers[marker_idx],
                    color=color_cycle[color_idx], markersize=6, linewidth=2, alpha=0.85)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.set_xticks(range(len(self.categories)))
        ax.set_xticklabels(self.categories, rotation=45, ha='right', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(loc='best', fontsize=10)
        
        total_points = sum(len(data) for data in self.valid_series.values())
        info_text = f"数据点总数: {total_points}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"折线图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_area_chart(self, title="数据面积图", x_label="X轴", y_label="Y值", 
                       output_file="area_chart.png", figsize=(12, 7), stacked=True):
        """绘制面积图"""
        fig, ax = plt.subplots(figsize=figsize)
        
        color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        x = range(len(self.categories))
        
        for i, (series_name, data) in enumerate(self.valid_series.items()):
            color_idx = i % len(color_cycle)
            ax.fill_between(x, data, label=series_name, color=color_cycle[color_idx], 
                          alpha=0.6, stacked=stacked)
            ax.plot(x, data, color=color_cycle[color_idx], linewidth=2)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories, rotation=45, ha='right', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(loc='best', fontsize=10)
        
        total_points = sum(len(data) for data in self.valid_series.values())
        info_text = f"数据点总数: {total_points}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"面积图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_scatter_chart(self, title="数据散点图", x_label="X值", y_label="Y值", 
                         output_file="scatter_chart.png", figsize=(12, 7)):
        """绘制散点图（使用前两个数据系列）"""
        if len(self.valid_series) < 2:
            raise ValueError("散点图需要至少两个数据系列")
            
        series_list = list(self.valid_series.items())
        x_series_name, x_data = series_list[0]
        y_series_name, y_data = series_list[1]
        
        # 确保数据长度一致
        min_len = min(len(x_data), len(y_data))
        x_data = x_data[:min_len]
        y_data = y_data[:min_len]
        categories = self.categories[:min_len]
        
        fig, ax = plt.subplots(figsize=figsize)
        
        scatter = ax.scatter(x_data, y_data, c=range(min_len), cmap='viridis', 
                            s=100, alpha=0.7, edgecolors='w', linewidth=0.5)
        
        # 添加颜色条
        cbar = plt.colorbar(scatter)
        cbar.set_label('数据点顺序', fontsize=10)
        
        # 为前10个点添加标签，避免过于拥挤
        for i, txt in enumerate(categories[:10]):
            ax.annotate(txt, (x_data[i], y_data[i]), fontsize=8)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(f"{x_series_name} ({x_label})", fontsize=12, labelpad=10)
        ax.set_ylabel(f"{y_series_name} ({y_label})", fontsize=12, labelpad=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        
        info_text = f"数据点总数: {min_len}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.1)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"散点图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_bubble_chart(self, title="数据气泡图", x_label="X值", y_label="Y值", 
                         size_label="大小", output_file="bubble_chart.png", figsize=(12, 7)):
        """绘制气泡图（使用前三个数据系列）"""
        if len(self.valid_series) < 3:
            raise ValueError("气泡图需要至少三个数据系列")
            
        series_list = list(self.valid_series.items())
        x_series_name, x_data = series_list[0]
        y_series_name, y_data = series_list[1]
        size_series_name, size_data = series_list[2]
        
        # 确保数据长度一致
        min_len = min(len(x_data), len(y_data), len(size_data))
        x_data = x_data[:min_len]
        y_data = y_data[:min_len]
        size_data = size_data[:min_len]
        categories = self.categories[:min_len]
        
        # 标准化大小数据
        sizes = np.array(size_data)
        if sizes.max() > 0:
            sizes = (sizes - sizes.min()) / (sizes.max() - sizes.min()) * 500 + 50
        else:
            sizes = np.ones_like(sizes) * 200
        
        fig, ax = plt.subplots(figsize=figsize)
        
        scatter = ax.scatter(x_data, y_data, s=sizes, c=range(min_len), cmap='viridis',
                            alpha=0.7, edgecolors='w', linewidth=0.5)
        
        # 添加颜色条
        cbar = plt.colorbar(scatter)
        cbar.set_label('数据点顺序', fontsize=10)
        
        # 为前10个点添加标签
        for i, txt in enumerate(categories[:10]):
            ax.annotate(txt, (x_data[i], y_data[i]), fontsize=8)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(f"{x_series_name} ({x_label})", fontsize=12, labelpad=10)
        ax.set_ylabel(f"{y_series_name} ({y_label})", fontsize=12, labelpad=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        
        info_text = f"数据点总数: {min_len}, 大小基于: {size_series_name}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.1)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"气泡图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_heatmap(self, title="数据热力图", output_file="heatmap.png", figsize=(12, 10)):
        """绘制热力图"""
        # 转换数据为矩阵形式
        data_matrix = np.array(list(self.valid_series.values()))
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # 绘制热力图
        sns.heatmap(data_matrix, annot=True, fmt=".1f", cmap="YlGnBu", 
                   xticklabels=self.categories, yticklabels=list(self.valid_series.keys()),
                   ax=ax, cbar_kws={'label': '数值'})
        
        ax.set_title(title, fontsize=16, pad=20)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        
        info_text = f"数据维度: {data_matrix.shape[0]}×{data_matrix.shape[1]}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"热力图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_histogram(self, title="数据直方图", x_label="数值", y_label="频数", 
                      output_file="histogram.png", figsize=(12, 7), bins=10):
        """绘制直方图（使用第一个数据系列）"""
        if len(self.valid_series) == 0:
            raise ValueError("没有有效数据可绘制直方图")
            
        # 取第一个数据系列
        first_series_name = next(iter(self.valid_series.keys()))
        data = self.valid_series[first_series_name]
        
        # 过滤零值
        data = [d for d in data if d > 0]
        
        if len(data) < 5:
            raise ValueError("直方图需要至少5个非零数据点")
        
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.hist(data, bins=bins, alpha=0.7, color='skyblue', edgecolor='black')
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(f"{first_series_name} ({x_label})", fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.grid(True, axis='y', linestyle='--', alpha=0.6)
        
        info_text = f"数据点总数: {len(data)},  bins数量: {bins}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.1)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"直方图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_boxplot(self, title="数据箱线图", x_label="类别", y_label="数值", 
                    output_file="boxplot.png", figsize=(12, 7)):
        """绘制箱线图"""
        data = list(self.valid_series.values())
        
        fig, ax = plt.subplots(figsize=figsize)
        
        bp = ax.boxplot(data, patch_artist=True)
        
        # 设置箱体颜色
        colors = plt.cm.Set3(np.linspace(0, 1, len(data)))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.set_xticklabels(self.valid_series.keys(), rotation=45, ha='right', fontsize=10)
        ax.grid(True, axis='y', linestyle='--', alpha=0.6)
        
        info_text = f"数据系列数量: {len(data)}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"箱线图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_combo_chart(self, title="组合图", x_label="类别", y_label="数值", 
                       output_file="combo_chart.png", figsize=(14, 8)):
        """绘制组合图（柱状图+折线图）"""
        if len(self.valid_series) < 2:
            raise ValueError("组合图需要至少两个数据系列")
            
        series_list = list(self.valid_series.items())
        bar_series_name, bar_data = series_list[0]
        line_series_name, line_data = series_list[1]
        
        fig, ax1 = plt.subplots(figsize=figsize)
        
        # 柱状图
        ax1.bar(range(len(self.categories)), bar_data, width=0.6, alpha=0.7, 
               color='skyblue', label=bar_series_name)
        ax1.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax1.set_ylabel(f"{bar_series_name} ({y_label})", fontsize=12, labelpad=10, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        ax1.set_xticks(range(len(self.categories)))
        ax1.set_xticklabels(self.categories, rotation=45, ha='right', fontsize=10)
        
        # 折线图（共享X轴）
        ax2 = ax1.twinx()
        ax2.plot(range(len(self.categories)), line_data, color='red', marker='o', 
                linewidth=2, markersize=6, label=line_series_name)
        ax2.set_ylabel(f"{line_series_name} ({y_label})", fontsize=12, labelpad=10, color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        
        # 合并图例
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=10)
        
        ax1.set_title(title, fontsize=16, pad=20)
        ax1.grid(True, linestyle='--', alpha=0.6)
        
        total_points = len(bar_data) + len(line_data)
        info_text = f"数据点总数: {total_points}, 柱状图: {bar_series_name}, 折线图: {line_series_name}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"组合图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def plot_sankey_diagram(self, title="桑基图", output_file="sankey_diagram.png", figsize=(12, 10)):
        """绘制桑基图（简化版，使用前两列数据）"""
        try:
            import plotly.graph_objects as go
        except ImportError:
            raise ImportError("绘制桑基图需要plotly库，请先安装：pip install plotly")
            
        if len(self.valid_series) < 2 or len(self.categories) < 2:
            raise ValueError("桑基图需要至少两个数据系列和两个类别")
        
        # 准备数据
        series_list = list(self.valid_series.items())
        source_data = series_list[0][1]
        target_data = series_list[1][1]
        
        # 简化处理，使用前10个数据点
        max_nodes = 10
        source_data = source_data[:max_nodes]
        target_data = target_data[:max_nodes]
        labels = self.categories[:max_nodes] + [f"目标{i+1}" for i in range(max_nodes)]
        
        # 创建节点和链接
        links = []
        
        for i in range(min(max_nodes, len(source_data))):
            source = i
            target = max_nodes + i
            value = abs(source_data[i]) if source_data[i] != 0 else 1
            links.append({"source": source, "target": target, "value": value})
        
        # 创建桑基图
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels
            ),
            link=dict(
                source=[link["source"] for link in links],
                target=[link["target"] for link in links],
                value=[link["value"] for link in links]
            )
        )])
        
        fig.update_layout(title_text=title, font_size=10, width=figsize[0]*100, height=figsize[1]*100)
        fig.write_image(output_file, format='png', scale=3)
        print(f"桑基图已保存至: {os.path.abspath(output_file)}")
    
    def plot_tree_map(self, title="树状图", output_file="tree_map.png", figsize=(12, 10)):
        """绘制树状图"""
        try:
            import plotly.express as px
        except ImportError:
            raise ImportError("绘制树状图需要plotly库，请先安装：pip install plotly")
            
        if len(self.valid_series) == 0 or len(self.categories) < 2:
            raise ValueError("树状图需要至少一个数据系列和两个类别")
        
        # 取第一个数据系列
        first_series_name = next(iter(self.valid_series.keys()))
        values = self.valid_series[first_series_name]
        
        # 准备数据框
        labels = self.categories[:len(values)]
        parents = [first_series_name] * len(labels)
        
        # 创建数据框
        df = pd.DataFrame({
            '标签': labels,
            '父类别': parents,
            '数值': values
        })
        
        # 过滤零值
        df = df[df['数值'] > 0]
        
        if len(df) < 2:
            raise ValueError("树状图需要至少两个非零数据点")
        
        # 创建树状图
        fig = px.treemap(df, ids='标签', parents='父类别', values='数值',
                         title=title)
        
        fig.update_layout(width=figsize[0]*100, height=figsize[1]*100)
        fig.write_image(output_file, format='png', scale=3)
        print(f"树状图已保存至: {os.path.abspath(output_file)}")
    
    def plot_barh_chart(self, title="水平条形图", x_label="数值", y_label="类别", 
                       output_file="barh_chart.png", figsize=(12, 7), show_values=True):
        """绘制水平条形图"""
        fig, ax = plt.subplots(figsize=figsize)
        
        n_series = len(self.valid_series)
        indices = np.arange(len(self.categories))
        bar_height = 0.8 / n_series
        
        color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        
        for i, (series_name, data) in enumerate(self.valid_series.items()):
            color_idx = i % len(color_cycle)
            bars = ax.barh(indices + i * bar_height, data, bar_height, 
                          label=series_name, color=color_cycle[color_idx], alpha=0.85)
            
            if show_values:
                for bar in bars:
                    width = bar.get_width()
                    if width > 0:
                        ax.annotate(f'{width:.1f}',
                                   xy=(width, bar.get_y() + bar.get_height() / 2),
                                   xytext=(3, 0),
                                   textcoords="offset points",
                                   ha='left', va='center', fontsize=8)
        
        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel(x_label, fontsize=12, labelpad=10)
        ax.set_ylabel(y_label, fontsize=12, labelpad=10)
        ax.set_yticks(indices + bar_height * (n_series - 1) / 2)
        ax.set_yticklabels(self.categories, fontsize=10)
        ax.grid(True, axis='x', linestyle='--', alpha=0.6)
        ax.legend(loc='best', fontsize=10)
        
        total_values = sum(sum(data) for data in self.valid_series.values())
        info_text = f"数据点总数: {len(self.categories) * n_series}, 数值总和: {total_values:.1f}"
        plt.figtext(0.5, 0.01, info_text, ha="center", fontsize=9, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.1)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"水平条形图已保存至: {os.path.abspath(output_file)}")
        plt.close()
    
    def generate_chart(self, chart_type, title=None, output_file=None, **kwargs):
        """根据选择的图表类型生成相应的图表"""
        chart_mapping = {
            "柱状图": self.plot_bar_chart,
            "饼图": self.plot_pie_chart,
            "折线图": self.plot_line_chart,
            "面积图": self.plot_area_chart,
            "散点图": self.plot_scatter_chart,
            "气泡图": self.plot_bubble_chart,
            "热力图": self.plot_heatmap,
            "直方图": self.plot_histogram,
            "箱线图": self.plot_boxplot,
            "组合图": self.plot_combo_chart,
            "桑基图": self.plot_sankey_diagram,
            "树状图": self.plot_tree_map,
            "条形图": self.plot_barh_chart
        }
        
        if chart_type not in chart_mapping:
            raise ValueError(f"不支持的图表类型: {chart_type}，支持的类型有: {', '.join(chart_mapping.keys())}")
        
        # 自动生成标题和输出文件名
        if title is None:
            title = f"{chart_type}"
        
        if output_file is None:
            output_file = f"{chart_type.lower().replace('图', '')}_chart.png"
        
        # 调用相应的绘图函数
        try:
            chart_mapping[chart_type](title=title, output_file=output_file,** kwargs)
            return True
        except Exception as e:
            print(f"生成{chart_type}时出错: {str(e)}")
            return False
    #:\Vscode\excel_visualizer.py