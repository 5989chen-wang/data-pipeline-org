import os
from dotenv import load_dotenv
from crew.crew_definition import create_crew

load_dotenv()

def main():
    user_input = input("请输入你的需求（例如：做一个销售数据分析仪表盘）：\n") or "做一个公司销售数据的月度分析仪表盘"
    
    print("🚀 多 Agent 数据流水线系统启动中...\n")
    crew = create_crew(user_input)
    
    print("👷 开始执行任务流程...\n")
    result = crew.kickoff()
    
    print("\n✅ 项目流程执行完成！")
    print(result)

if __name__ == "__main__":
    main()
