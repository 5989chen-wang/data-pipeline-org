\# 数据流水线多 Agent 组织系统 (data-pipeline-org)



\## 项目介绍

这是一个模拟企业项目管理流程的多 Agent 系统：

\- 你（用户）发布自然语言指令

\- agent-boss（项目经理）分析并拆解任务

\- agent\_cpa（需求经理） + agent\_safe（安全经理）并行工作

\- approver（审批经理）审查并可能打回

\- agent\_etl（数据开发） + agent\_develop（报表开发）执行落地



支持自动入库、ETL、Superset 可视化。



\## 快速启动（Windows）

1\. 安装 Python 3.10+

2\. `pip install -r requirements.txt`

3\. 配置 `.env` 文件

4\. `python main.py "做一个销售分析仪表盘"`



\## Agent 层级

详见 agents/ 文件夹

