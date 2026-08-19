async function ask() {
  const q = document.getElementById("question").value;
  const answerBox = document.getElementById("answer");
  const loadingBox = document.getElementById("loading");
  const errorBox = document.getElementById("error");

  answerBox.innerText = "";
  errorBox.innerText = "";
  loadingBox.innerText = "Thinking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q })
    });

    if (!res.ok) {
      throw new Error("Backend returned status " + res.status);
    }

    const data = await res.json();
    loadingBox.innerText = "";
    answerBox.innerText = data.answer || "(No answer returned)";
  } catch (err) {
    loadingBox.innerText = "";
    errorBox.innerText = "Error: " + err.message;
  }
}
