import os
import sys
import subprocess
from excel_visualizer import ExcelVisualizer, setup_chinese_font

def check_and_install_libraries():
    """检查并安装必要的依赖库"""
    required_libs = {
        "pandas": "pandas",
        "matplotlib": "matplotlib",
        "numpy": "numpy",
        "seaborn": "seaborn",
        "openpyxl": "openpyxl",  # 用于读取xlsx文件
        "xlrd": "xlrd==1.2.0",   # 用于读取xls文件
        "plotly": "plotly",
        "kaleido": "kaleido"
    }
    
    for lib_name, pip_name in required_libs.items():
        try:
            __import__(lib_name)
            print(f"{lib_name} 已安装")
        except ImportError:
            print(f"检测到缺少{lib_name}库，正在安装...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

def main():
    """主函数，处理用户交互流程"""
    print("=" * 50)
    print("        Excel全能数据可视化工具        ")
    print("=" * 50)
    print("GitHub: https://github.com/yourusername/excel-visualizer")  # 替换为你的GitHub仓库地址
    print("版本: 1.0.0")
    print("=" * 50)
    
    # 初始化环境
    check_and_install_libraries()
    setup_chinese_font()
    
    # 创建输出目录
    if not os.path.exists("output"):
        os.makedirs("output")
        print("已创建输出目录: output")
    
    # 初始化可视化器
    visualizer = ExcelVisualizer()
    
    # 获取Excel文件路径
    while True:
        excel_file = input("\n请输入Excel文件路径 (或直接拖放文件到窗口): ").strip()
        if not excel_file:
            print("文件路径不能为空，请重新输入")
            continue
            
        # 处理拖放文件可能带有的引号
        if excel_file.startswith(('"', "'")) and excel_file.endswith(('"', "'")):
            excel_file = excel_file[1:-1]
            
        try:
            visualizer.load_data(excel_file)
            break
        except Exception as e:
            print(f"加载文件失败: {str(e)}，请重新输入")
    
    # 分析数据质量
    print("\n正在分析数据质量...")
    issues, empty_ratio, numeric_ratio = visualizer.analyze_data_quality()
    
    if issues:
        print("数据质量问题:")
        for issue in issues:
            print(f"- {issue}")
        
        auto_fix = input("是否启用自动修复功能? (y/n，默认y): ").strip().lower()
        visualizer.auto_fix = auto_fix != 'n'
    
    print(f"\n数据质量摘要:")
    print(f"- 空值比例: {empty_ratio:.1%}")
    print(f"- 数值数据比例: {numeric_ratio:.1%}")
    
    # 准备数据
    print("\n正在准备数据...")
    while True:
        use_manual_range = input("是否需要手动指定数据范围? (y/n，默认n): ").strip().lower()
        if use_manual_range == 'y':
            try:
                print("\n请输入数据范围参数（用逗号分隔）:")
                print("格式: x_start_row, x_end_row, x_start_col, x_end_col, y_start_row, y_end_row, y_start_col, y_end_col")
                print("说明: 行和列的索引从0开始，例如: 1,10,0,0,1,10,1,3")
                range_str = input("请输入: ").strip()
                data_range = tuple(map(int, range_str.split(',')))
                
                if len(data_range) != 8:
                    print("数据范围参数必须是8个整数，请重新输入")
                    continue
                
                visualizer.prepare_data(data_range)
                break
            except Exception as e:
                print(f"处理手动范围失败: {str(e)}，请重试")
        else:
            try:
                visualizer.prepare_data()
                break
            except Exception as e:
                print(f"自动准备数据失败: {str(e)}")
                retry = input("是否尝试手动指定范围? (y/n): ").strip().lower()
                if retry != 'y':
                    print("程序退出")
                    return
    
    # 分析数据并推荐图表类型
    print("\n正在分析数据特征并推荐图表类型...")
    recommendations = visualizer.analyze_data_and_recommend()
    
    print("\n根据您的数据特征，推荐以下图表类型:")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    
    # 显示所有可用图表类型
    all_charts = ["柱状图", "饼图", "折线图", "面积图", "散点图", "气泡图", 
                 "热力图", "直方图", "箱线图", "组合图", "桑基图", "树状图", "条形图"]
    
    print("\n所有可用的图表类型:")
    for i, chart in enumerate(all_charts, 1):
        print(f"{i}. {chart}", end='  ' if i % 4 != 0 else '\n')
    print()
    
    # 让用户选择图表类型
    while True:
        try:
            choice = input(f"请选择要生成的图表类型 (输入序号，1-{len(all_charts)}): ").strip()
            if not choice:
                continue
                
            chart_idx = int(choice) - 1
            if 0 <= chart_idx < len(all_charts):
                selected_chart = all_charts[chart_idx]
                break
            else:
                print(f"请输入1到{len(all_charts)}之间的数字")
        except ValueError:
            print("请输入有效的数字")
    
    # 设置图表标题
    default_title = f"{selected_chart}"
    title = input(f"请输入图表标题 (默认: {default_title}): ").strip() or default_title
    
    # 设置输出文件名，默认保存到output目录
    default_output = os.path.join("output", f"{selected_chart.lower().replace('图', '')}_chart.png")
    output_file = input(f"请输入输出文件名 (默认: {default_output}): ").strip() or default_output
    
    # 生成图表
    print(f"\n正在生成{selected_chart}...")
    success = visualizer.generate_chart(selected_chart, title=title, output_file=output_file)
    
    if success:
        print(f"\n成功生成{selected_chart}，文件保存至: {os.path.abspath(output_file)}")
        
        # 询问是否生成其他图表
        another = input("是否要生成其他类型的图表? (y/n): ").strip().lower()
        if another == 'y':
            main()  # 递归调用，重新选择图表类型
        else:
            print("\n感谢使用，再见！")
    else:
        print(f"\n生成{selected_chart}失败")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序已被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {str(e)}")
        print("请尝试重新运行程序或提交issue到GitHub仓库")
    