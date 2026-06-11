from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

develop = Agent(
    role="应用开发工程师",
    goal="负责报表开发、可视化界面和最终项目交付",
    backstory="你是全栈开发工程师，擅长使用 Superset / Streamlit 等工具快速实现数据可视化仪表盘。",
    llm=llm,
    verbose=True,
)