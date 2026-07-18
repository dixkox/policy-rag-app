from graphviz import Digraph

# Create directed graph
dot = Digraph(comment="Enhanced RAG Architecture", format="png")

# Node styles
dot.attr('node', shape='box', style='filled', color='lightblue', fontname='Arial')

# Define nodes
dot.node('UI', 'User Interface\n(chat.html)')
dot.node('API', 'FastAPI Backend\n(/ask Endpoint)')
dot.node('Rewriter', 'Query Rewriter\n(Query Enhancement)')
dot.node('Embed', 'Embeddings Model\n(sentence-transformers)')
dot.node('Vector', 'Vector Store\n(FAISS Database)')
dot.node('Reranker', 'Reranker\n(Results Re-ranking)')
dot.node('LLM', 'LLM\n(Answer Generation)')
dot.node('Response', 'Response to User\n(Policy-Aligned Answer)')

# Define edges
dot.edge('UI', 'API', label='User Query')
dot.edge('API', 'Rewriter')
dot.edge('Rewriter', 'Embed')
dot.edge('Embed', 'Vector')
dot.edge('Vector', 'Reranker')
dot.edge('Reranker', 'LLM')
dot.edge('LLM', 'Response', label='Answer')
dot.edge('Response', 'UI', label='Display Answer')

# Save and render
dot.render('enhanced_rag_architecture', view=True)
