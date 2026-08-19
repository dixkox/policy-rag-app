from graphviz import Digraph

dot = Digraph(comment="Policy RAG Architecture (TF-IDF)", format="png")

dot.attr('node', shape='box', style='filled', color='lightblue', fontname='Arial')

dot.node('UI', 'Frontend\n(index.html + JS)')
dot.node('API', 'FastAPI Backend\n(/ask endpoint)')
dot.node('RAG', 'RAG Pipeline\n(TF-IDF Retrieval)')
dot.node('Load', 'Load Policy Files\n(.txt)')
dot.node('Chunk', 'Chunk by Headings\n(# Policy Title)')
dot.node('TFIDF', 'TF-IDF Vectorizer')
dot.node('Sim', 'Cosine Similarity\nBest-Match Retrieval')
dot.node('Docs', 'Policy Store\n(.txt files)')
dot.node('Answer', 'Best Policy Chunk\nReturned to UI')

dot.edge('UI', 'API', label='User Question')
dot.edge('API', 'RAG', label='Call RAG Pipeline')
dot.edge('RAG', 'Load')
dot.edge('Load', 'Chunk')
dot.edge('Chunk', 'TFIDF')
dot.edge('TFIDF', 'Sim')
dot.edge('Docs', 'TFIDF', label='Indexed Chunks')
dot.edge('Sim', 'API', label='Best Match')
dot.edge('API', 'UI', label='Return Answer')

dot.render('policy_rag_architecture_tfidf', view=True)
