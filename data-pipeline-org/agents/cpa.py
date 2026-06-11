from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

safe = Agent(
    role="安全经理",
    goal="为项目提供全面的安全设计、风险评估和防护方案",
    backstory="你是资深安全专家，专注于数据安全、权限控制、隐私合规和系统风险防控。",
    llm=llm,
    verbose=True,
)