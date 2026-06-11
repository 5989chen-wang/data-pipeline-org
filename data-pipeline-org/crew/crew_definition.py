from crewai import Crew, Process
from agents.boss import boss
from agents.cpa import cpa
from agents.safe import safe
from agents.approver import approver
from agents.etl import etl
from agents.develop import develop

# 定义任务
def create_crew(user_query: str):
    from crewai import Task

    task1 = Task(
        description=f"分析以下需求并拆解任务：{user_query}",
        agent=boss,
        expected_output="详细的任务拆解清单，包括分配给需求经理、安全经理的任务"
    )

    task2 = Task(
        description="根据 Boss 分配的任务，输出详细可落地的开发需求规格（字段、表结构、ETL逻辑、报表要求）",
        agent=cpa,
        expected_output="完整的PRD和技术规格文档"
    )

    task3 = Task(
        description="针对上述需求，提供全面的安全设计和风险评估",
        agent=safe,
        expected_output="安全方案文档"
    )

    task4 = Task(
        description="审查需求规格和安全方案，发现问题打回修改，否则批准进入开发阶段",
        agent=approver,
        expected_output="审批意见：通过/打回 + 具体修改意见"
    )

    task5 = Task(
        description="根据批准的需求，完成数据ETL处理流程",
        agent=etl,
        expected_output="ETL 代码和处理结果说明"
    )

    task6 = Task(
        description="完成报表开发和可视化展示",
        agent=develop,
        expected_output="最终报表方案和可视化链接说明"
    )

    crew = Crew(
        agents=[boss, cpa, safe, approver, etl, develop],
        tasks=[task1, task2, task3, task4, task5, task6],
        process=Process.hierarchical,
        manager_agent=boss,
        verbose=2,
        memory=True,
    )
    return crew