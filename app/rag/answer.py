from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "google/flan-t5-base"

# Load ONCE at startup
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_answer(question: str, context: str) -> str:
    if not context or context.strip() == "":
        context = "No relevant policy information was found in the knowledge base."

    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        f"Answer:"
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_length=256,
        temperature=0.2,
        top_p=0.9
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
