import sys, os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.rag.vectorstore import collection

print("Document count:", collection.count())

docs = collection.get()
print("Sample IDs:", docs["ids"][:5] if docs["ids"] else [])
