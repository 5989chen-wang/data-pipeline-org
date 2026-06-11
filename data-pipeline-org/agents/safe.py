from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

cpa = Agent(
    role="需求经理 (CPA)",
    goal="将 Boss 分配的任务转化为详细、可落地的开发规格文档",
    backstory="你是专业的业务需求分析师，擅长把高层需求细化为具体字段、表结构、ETL 逻辑、报表需求等可执行的开发文档。",
    llm=llm,
    verbose=True,
)