(() => {
  const root = document.documentElement, btn = document.getElementById("theme");
  const isDark = () => root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  const label = () => { const d = isDark(); root.classList.toggle("is-dark", d); btn.setAttribute("aria-label", d ? "Switch to light mode" : "Switch to dark mode"); };
  try { const t = localStorage.getItem("theme"); if (t) root.dataset.theme = t; } catch (e) {}
  label();
  try { matchMedia("(prefers-color-scheme: dark)").addEventListener("change", label); } catch (e) {}
  btn.addEventListener("click", () => {
    root.dataset.theme = isDark() ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
    label();
  });
  document.querySelectorAll(".copy").forEach(b => b.addEventListener("click", () => {
    const icon = b.innerHTML;
    const done = () => { b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'; b.style.color = "var(--accent)"; setTimeout(() => { b.innerHTML = icon; b.style.color = ""; }, 1500); };
    try { navigator.clipboard.writeText(b.dataset.copy).then(done, () => {}); } catch (e) {}
  }));
  const menu = document.getElementById("menu"), jump = document.getElementById("jump");
  const close = () => { jump.hidden = true; menu.setAttribute("aria-expanded", "false"); };
  menu.addEventListener("click", e => { e.stopPropagation(); jump.hidden = !jump.hidden; menu.setAttribute("aria-expanded", String(!jump.hidden)); });
  jump.addEventListener("click", e => { if (e.target.closest("a")) close(); });
  document.addEventListener("click", e => { if (!jump.hidden && !e.target.closest("#jump")) close(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") close(); });
  // phones: fold each project to its title and problem; one tap opens it
  const phone = matchMedia("(max-width: 820px)");
  document.querySelectorAll(".proj").forEach(pr => {
    const story = pr.querySelector(".story"), prob = story.querySelector(".problem");
    const first = story.querySelector(".pts li:first-child"), does = first && first.querySelector("b").textContent === "Does" ? first.querySelector("span") : null;
    const one = document.createElement("p"); one.className = "oneliner";
    one.textContent = does ? does.textContent : prob.textContent; prob.before(one);
    let actions = story.querySelector(".actions");
    if (!actions) { actions = document.createElement("div"); actions.className = "actions"; story.append(actions); }
    const t = document.createElement("button");
    t.type = "button"; t.className = "toggle";
    const set = open => { pr.classList.toggle("folded", !open); t.textContent = open ? "Hide details ▴" : "Details ▾"; t.setAttribute("aria-expanded", open); };
    t.addEventListener("click", () => set(pr.classList.contains("folded")));
    actions.append(t);
    set(!phone.matches);
    phone.addEventListener?.("change", e => set(!e.matches));
  });
  // only one video plays at a time
  document.querySelectorAll("video").forEach(v => v.addEventListener("play", () =>
    document.querySelectorAll("video").forEach(o => { if (o !== v) o.pause(); })));
})();
