"use client";
import { useState } from "react";

export default function Home() {
  const [pdfText, setPdfText] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setPdfText(data.text);
  };

  const handleAsk = async () => {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, text: pdfText }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div className="p-10 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">PolicyLens Mini</h1>

      <input
        type="file"
        onChange={handleUpload}
        className="mb-4"
      />

      <textarea
        className="w-full h-40 p-3 border mb-4"
        value={pdfText}
        placeholder="Extracted PDF text will appear here..."
        readOnly
      />

      <input
        type="text"
        className="w-full p-3 border mb-4"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={handleAsk}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Ask
      </button>

      {answer && (
        <div className="mt-6 p-4 border bg-gray-100">
          <h2 className="font-bold mb-2">AI Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}
