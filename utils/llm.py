from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from groq import RateLimitError
# load_dotenv()

# PRIMARY = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")
# FALLBACK = os.getenv("LLM_FALLBACK_MODEL", "openai/gpt-oss-safeguard-20b")
# MODEL = PRIMARY

# _primary = ChatGroq(model=PRIMARY, temperature=0, max_retries=2, timeout=120)
# _fallback = ChatGroq(model=FALLBACK, temperature=0, max_retries=4, timeout=120)

# llm = _primary.with_fallbacks([_fallback], exceptions_to_handle=(RateLimitError,))

