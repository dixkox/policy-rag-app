document.getElementById("send").addEventListener("click", async () => {
  const questionEl = document.getElementById("question");
  const messagesEl = document.getElementById("messages");

  const question = questionEl.value.trim();
  if (!question) return;

  messagesEl.textContent = "Thinking...";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  const data = await res.json();

  let text = `Answer:\n${data.answer}\n\nCitations:\n`;
  for (const c of data.citations) {
    text += `- ${c}\n`;
  }

  messagesEl.textContent = text;
});
