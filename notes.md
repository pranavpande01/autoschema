LlamaIndex is the framework for Context-Augmented LLM Applications

Workflows are multi-step processes that combine one or more agents, data connectors, and other tools to complete a task.


Data connectors ingest existing data.

Data indexes structure data in intermediate representations.

Query engines are interfaces for quering (e.g. a RAG flow).

Chat engines are conversational interfaces.

Observability/Evaluation enable rigorous experimentation, evaluatiion, and monitoring.

Workflows allow to combine all of the above into an event-driven system far more flexible than other, graph-based approaches.

FunctionAgent(AgentWorkflow):
agent = FunctionAgent(
    tools
    llm=OpenAI(model="gpt-4o-mini"),
    system_prompt
)

agent = AgentWorkflow.from_tools_or_functions(
    tools,
    llm=Settings.llm,
    system_prompt
)

agent.run("What is 1234 * 4567?")

Context
ctx = Context(agent)
agent.run("My name is Logan", ctx=ctx)

RAG
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
query_engine.aquery(query)

RAG Index Persistence [Saving]
index.storage_context.persist("storage")

RAG Index Persistence [Loading]
storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context)


