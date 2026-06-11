from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

etl = Agent(
    role="数据开发工程师 (ETL)",
    goal="根据批准的需求完成数据清洗、转换、入库和 ETL 流程开发",
    backstory="你是资深数据工程师，擅长使用 Pandas / SQL 实现高效、稳定的 ETL 管道。",
    llm=llm,
    verbose=True,
)