let session = null;
let selectedChunkId = null;
let lastMarkdown = null;
const $ = (id) => document.getElementById(id);

$("file").addEventListener("change", async (e) => {
  const f = e.target.files[0];
  if (!f) return;
  $("status").textContent = "Uploading and parsing...";
  const fd = new FormData();
  fd.append("file", f);
  const res = await fetch("/upload", { method: "POST", body: fd });
  if (!res.ok) {
    $("status").textContent = "Error: " + (await res.text());
    return;
  }
  const data = await res.json();
  session = data.session_id;
  $("status").textContent = `Parsed ${data.chunk_count} chunks from ${data.filename}`;
  renderChunks(data.chunks);
});

function renderChunks(chunks) {
  const container = $("chunks");
  container.innerHTML = "";
  chunks.forEach((c) => {
    const div = document.createElement("div");
    div.className = "chunk";
    div.dataset.id = c.id;
    div.textContent = c.text.slice(0, 300) + (c.text.length > 300 ? "..." : "");
    div.addEventListener("click", () => selectChunk(c.id));
    container.appendChild(div);
  });
}

function selectChunk(id) {
  selectedChunkId = id;
  document.querySelectorAll(".chunk").forEach((el) => {
    el.classList.toggle("selected", el.dataset.id === id);
  });
  $("gen").disabled = false;
}

$("gen").addEventListener("click", async () => {
  if (!session || !selectedChunkId) return;
  $("preview").textContent = "Generating...";
  $("gen").disabled = true;
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id: session,
      chunk_id: selectedChunkId,
      level: $("level").value,
      detail: $("detail").value,
    }),
  });
  $("gen").disabled = false;
  if (!res.ok) {
    $("preview").textContent = "Error: " + (await res.text());
    return;
  }
  const data = await res.json();
  lastMarkdown = data.markdown;
  $("preview").textContent = data.markdown;
  $("push").disabled = false;
});

$("push").addEventListener("click", async () => {
  if (!lastMarkdown) return;
  await fetch("/push", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ markdown: lastMarkdown }),
  });
});
