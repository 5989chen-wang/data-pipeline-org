from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

boss = Agent(
    role="项目经理 (Boss)",
    goal="分析用户需求，拆解任务，协调整个团队，确保项目高质量交付",
    backstory="你是有15年经验的资深项目经理，擅长将模糊的业务需求转化为清晰的任务，并严格管理流程和质量。",
    llm=llm,
    verbose=True,
    allow_delegation=True,
)