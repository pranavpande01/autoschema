import dspy
from dotenv import load_dotenv
load_dotenv()
lm = dspy.LM("gemini/gemini-2.5-flash")
dspy.configure(lm=lm)
lm("Say this is a test!", temperature=0.7) 
a=lm(messages=[{"role": "user", "content": "Say this is a test!"}])  # => ['This is a test!']
print(a)