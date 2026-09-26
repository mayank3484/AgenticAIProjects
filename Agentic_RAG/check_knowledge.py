from vectorstore import vector_store

vs=vector_store()
docs=vs.similarity_search(
    "I am getting access denied error",k=2
)
print(docs)