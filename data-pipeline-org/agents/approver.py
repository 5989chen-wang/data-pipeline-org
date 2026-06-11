from crewai import Agent
from config.llm_config import LLM_CONFIG
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(**LLM_CONFIG)

approver = Agent(
    role="审批经理",
    goal="严格审查需求规格和安全设计，发现问题及时打回修改",
    backstory="你是严谨的审批专家，负责把关可落地性、一致性和风险点。只有全部通过才允许进入开发阶段。",
    llm=llm,
    verbose=True,
)