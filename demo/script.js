/**
 * Forge Brain — Premium Public Concept Demo
 * Mock data only. No backend. No proprietary logic.
 */

const MODES = [
  {
    id: "ecosystem",
    label: "Ecosystem View",
    highlight: new Set([
      "crucible",
      "forge",
      "core",
      "aether",
      "siege",
      "barrage",
      "big-brain",
    ]),
    description: "Ecosystem products and platform boundary",
  },
  {
    id: "brain",
    label: "Brain View",
    highlight: new Set([
      "crucible",
      "big-brain",
      "mini-brains",
      "baby-brains",
      "skills",
      "experience-engine",
      "brain-gardener",
    ]),
    description: "Intelligence architecture layer",
  },
  {
    id: "knowledge",
    label: "Knowledge Flow",
    highlight: new Set([
      "crucible",
      "knowledge-graph",
      "memory",
      "prompt-compiler",
      "token-optimization",
      "experience-engine",
      "big-brain",
      "forge",
      "brain-gardener",
    ]),
    description: "How knowledge composes and compounds",
  },
];

const ORBIT_INNER = ["big-brain", "knowledge-graph", "experience-engine", "aether", "forge"];
const ORBIT_OUTER = [
  "mini-brains",
  "baby-brains",
  "skills",
  "memory",
  "prompt-compiler",
  "token-optimization",
  "brain-gardener",
  "core",
  "siege",
  "barrage",
];

const NODES = [
  {
    id: "crucible",
    label: "The Crucible Brain",
    initials: "CB",
    orbit: "center",
    category: "hub",
    short: "Central AKOS intelligence — the platform brain concept.",
    description:
      "The conceptual heart of The Crucible AI Knowledge Operating System. Unifies local-first intelligence, composable context, and disciplined API usage into one navigable brain map.",
    connections: ["big-brain", "knowledge-graph", "experience-engine", "aether", "forge", "core"],
  },
  {
    id: "big-brain",
    label: "Big Brain",
    initials: "BB",
    orbit: "inner",
    category: "intelligence",
    short: "Central orchestration — routes context and coordinates specialists.",
    description:
      "High-level orchestration within Core. Coordinates context between the Knowledge Graph, specialist units, and scoped model calls. Public-safe abstraction only.",
    connections: ["crucible", "mini-brains", "baby-brains", "knowledge-graph", "prompt-compiler", "experience-engine", "aether"],
  },
  {
    id: "knowledge-graph",
    label: "Knowledge Graph",
    initials: "KG",
    orbit: "inner",
    category: "services",
    short: "Entity-relationship store for all platform assets.",
    description:
      "Structured map of projects, prompts, agents, files, memories, skills, and their relationships. Forge Brain visualizes this at the entity level in the full product vision.",
    connections: ["crucible", "big-brain", "memory", "brain-gardener", "experience-engine", "forge", "core"],
  },
  {
    id: "experience-engine",
    label: "Experience Engine",
    initials: "EE",
    orbit: "inner",
    category: "intelligence",
    short: "Learning loop — outcomes refine future context.",
    description:
      "Captures what worked and what context was in play. Feeds signals back so each session starts smarter. Learning internals are not exposed in this demo.",
    connections: ["crucible", "big-brain", "memory", "knowledge-graph", "brain-gardener"],
  },
  {
    id: "aether",
    label: "Aether",
    initials: "AE",
    orbit: "inner",
    category: "products",
    short: "Intelligence layer — context selection and surfacing.",
    description:
      "Makes large knowledge feel small in active work. Surfaces relevant context without breaking flow. Internals remain proprietary.",
    connections: ["crucible", "forge", "core", "memory", "token-optimization", "big-brain"],
  },
  {
    id: "forge",
    label: "Forge",
    initials: "FG",
    orbit: "inner",
    category: "workspace",
    short: "Desktop workspace — where builders work daily.",
    description:
      "Primary builder-facing product. Forge Brain is the graph surface inside Forge — this demo shows the higher-level brain map concept.",
    connections: ["crucible", "core", "aether", "knowledge-graph", "skills"],
  },
  {
    id: "mini-brains",
    label: "Mini Brains",
    initials: "MB",
    orbit: "outer",
    category: "intelligence",
    short: "Scoped specialists for projects and domains.",
    description:
      "Mid-tier intelligence units scoped to a project, client, or workflow. Assemble focused context from Skills and the Knowledge Graph.",
    connections: ["big-brain", "baby-brains", "skills", "knowledge-graph"],
  },
  {
    id: "baby-brains",
    label: "Baby Brains",
    initials: "BY",
    orbit: "outer",
    category: "intelligence",
    short: "Task-level units for narrow execution.",
    description:
      "Lightweight task-scoped units — a prompt run, summary, or workflow step. Keeps API calls intentional and narrow.",
    connections: ["big-brain", "mini-brains", "skills", "token-optimization"],
  },
  {
    id: "skills",
    label: "Skills",
    initials: "SK",
    orbit: "outer",
    category: "intelligence",
    short: "Reusable packaged capabilities.",
    description:
      "Skills Library — curated templates and domain expertise shared across brain tiers. Composable context made tangible.",
    connections: ["mini-brains", "baby-brains", "brain-gardener", "forge", "knowledge-graph"],
  },
  {
    id: "memory",
    label: "Memory",
    initials: "ME",
    orbit: "outer",
    category: "services",
    short: "Persistent context across sessions.",
    description:
      "Long-lived context beyond a single chat. Part of local-first intelligence — owned by the builder, composed into future work.",
    connections: ["knowledge-graph", "brain-gardener", "experience-engine", "aether"],
  },
  {
    id: "prompt-compiler",
    label: "Prompt Compiler",
    initials: "PC",
    orbit: "outer",
    category: "services",
    short: "Assembles scoped prompts from context.",
    description:
      "Abstract service building model-ready prompts from graph assets. Supports disciplined API usage — compilation internals are private.",
    connections: ["big-brain", "token-optimization", "core"],
  },
  {
    id: "token-optimization",
    label: "Token Optimization",
    initials: "TO",
    orbit: "outer",
    category: "services",
    short: "Scopes context to reduce model input waste.",
    description:
      "Ensures only relevant context reaches external model calls. Algorithms and implementation are not disclosed here.",
    connections: ["prompt-compiler", "baby-brains", "aether", "core"],
  },
  {
    id: "brain-gardener",
    label: "Brain Gardener",
    initials: "BG",
    orbit: "outer",
    category: "intelligence",
    short: "Curates knowledge health over time.",
    description:
      "Conceptual custodian — pruning stale context, strengthening useful connections, maintaining graph health.",
    connections: ["knowledge-graph", "memory", "skills", "experience-engine"],
  },
  {
    id: "core",
    label: "Core",
    initials: "CR",
    orbit: "outer",
    category: "products",
    short: "Shared engine and runtime.",
    description:
      "Foundation beneath all Crucible products — entity registry, relationships, runtime services. Private production codebase; concept only here.",
    connections: ["crucible", "big-brain", "forge", "aether", "siege", "barrage", "prompt-compiler", "token-optimization"],
  },
  {
    id: "siege",
    label: "Siege",
    initials: "SG",
    orbit: "outer",
    category: "products",
    planned: true,
    short: "Integration platform. Planned.",
    description:
      "Planned platform connecting external APIs, tools, and systems into the Crucible model. Not shipped.",
    connections: ["core", "knowledge-graph"],
  },
  {
    id: "barrage",
    label: "Barrage",
    initials: "BR",
    orbit: "outer",
    category: "products",
    planned: true,
    short: "Cloud and team platform. Planned.",
    description:
      "Planned cloud platform for shared workspaces, collaborative graphs, and team-scale context. Not shipped.",
    connections: ["core", "forge", "knowledge-graph"],
  },
];

const CATEGORY_LABELS = {
  hub: "Platform Core",
  intelligence: "Intelligence",
  services: "Platform Services",
  products: "Ecosystem",
  workspace: "Builder Workspace",
};

const nodeMap = Object.fromEntries(NODES.map((n) => [n.id, n]));

let selectedId = null;
let activeMode = "brain";
let layout = {};
let edges = [];

const graphStage = document.getElementById("graph-stage");
const nodesLayer = document.getElementById("nodes-layer");
const pulseRings = document.getElementById("pulse-rings");
const spokeLayer = document.getElementById("spoke-layer");
const edgeLayer = document.getElementById("edge-layer");
const tooltip = document.getElementById("tooltip");
const panelEmpty = document.getElementById("panel-empty");
const panelContent = document.getElementById("panel-content");
const modeToggles = document.getElementById("mode-toggles");
const particlesCanvas = document.getElementById("particles");

function buildEdges() {
  const seen = new Set();
  edges = [];
  NODES.forEach((node) => {
    node.connections.forEach((tid) => {
      const key = [node.id, tid].sort().join("--");
      if (!seen.has(key) && nodeMap[tid]) {
        seen.add(key);
        edges.push({ from: node.id, to: tid });
      }
    });
  });
}

function computeLayout() {
  const rect = graphStage.getBoundingClientRect();
  const cx = rect.width / 2;
  const cy = rect.height / 2;
  const minDim = Math.min(rect.width, rect.height);
  const innerR = minDim * 0.21;
  const outerR = minDim * 0.38;

  layout = { crucible: { x: cx, y: cy } };

  ORBIT_INNER.forEach((id, i) => {
    const angle = (i / ORBIT_INNER.length) * Math.PI * 2 - Math.PI / 2;
    layout[id] = { x: cx + Math.cos(angle) * innerR, y: cy + Math.sin(angle) * innerR };
  });

  ORBIT_OUTER.forEach((id, i) => {
    const angle = (i / ORBIT_OUTER.length) * Math.PI * 2 - Math.PI / 2 + 0.15;
    layout[id] = { x: cx + Math.cos(angle) * outerR, y: cy + Math.sin(angle) * outerR };
  });
}

function curvePath(x1, y1, x2, y2, bend = 0.22) {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.hypot(dx, dy) || 1;
  const cx = mx + (-dy / len) * len * bend;
  const cy = my + (dx / len) * len * bend;
  return `M ${x1} ${y1} Q ${cx} ${cy} ${x2} ${y2}`;
}

function renderPulseRings() {
  const ns = "http://www.w3.org/2000/svg";
  const { x, y } = layout.crucible;
  pulseRings.innerHTML = "";
  [72, 108, 148].forEach((r, i) => {
    const c = document.createElementNS(ns, "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", r);
    c.setAttribute("class", `pulse-ring pulse-${i + 1}`);
    pulseRings.appendChild(c);
  });
  const glow = document.createElementNS(ns, "circle");
  glow.setAttribute("cx", x);
  glow.setAttribute("cy", y);
  glow.setAttribute("r", 64);
  glow.setAttribute("fill", "url(#hub-glow)");
  glow.setAttribute("class", "hub-glow-disc");
  pulseRings.appendChild(glow);
}

function renderSpokes() {
  const ns = "http://www.w3.org/2000/svg";
  spokeLayer.innerHTML = "";
  const hub = layout.crucible;
  NODES.forEach((node) => {
    if (node.id === "crucible") return;
    const p = layout[node.id];
    if (!p) return;
    const path = document.createElementNS(ns, "path");
    path.setAttribute("d", curvePath(hub.x, hub.y, p.x, p.y, 0.08));
    path.setAttribute("class", "spoke");
    path.dataset.to = node.id;
    spokeLayer.appendChild(path);
  });
}

function renderEdges() {
  const ns = "http://www.w3.org/2000/svg";
  edgeLayer.innerHTML = "";
  edges.forEach(({ from, to }) => {
    const a = layout[from];
    const b = layout[to];
    if (!a || !b) return;
    if (from === "crucible" || to === "crucible") return;
    const path = document.createElementNS(ns, "path");
    path.setAttribute("d", curvePath(a.x, a.y, b.x, b.y, 0.18));
    path.setAttribute("class", "edge");
    path.dataset.from = from;
    path.dataset.to = to;
    edgeLayer.appendChild(path);
  });
}

function renderNodes() {
  nodesLayer.innerHTML = "";
  NODES.forEach((node, i) => {
    const pos = layout[node.id];
    if (!pos) return;

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = `node ${node.category} orbit-${node.orbit}${node.planned ? " planned" : ""}`;
    btn.dataset.id = node.id;
    btn.style.left = `${pos.x}px`;
    btn.style.top = `${pos.y}px`;
    btn.setAttribute("aria-label", `${node.label}. ${node.short}`);
    btn.setAttribute("aria-pressed", "false");

    btn.innerHTML = `
      <span class="node-card">
        <span class="node-glow" aria-hidden="true"></span>
        <span class="node-icon">${node.initials}</span>
        <span class="node-label">${node.label}</span>
      </span>
    `;

    btn.addEventListener("mouseenter", (e) => showTooltip(e, node));
    btn.addEventListener("mousemove", moveTooltip);
    btn.addEventListener("mouseleave", hideTooltip);
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      selectNode(node.id);
    });

    nodesLayer.appendChild(btn);
  });
  applyModeHighlight();
}

function getModeSet() {
  return MODES.find((m) => m.id === activeMode)?.highlight ?? new Set();
}

function applyModeHighlight() {
  const modeSet = getModeSet();
  document.querySelectorAll(".node").forEach((el) => {
    const inMode = modeSet.has(el.dataset.id);
    el.classList.toggle("mode-active", inMode);
    el.classList.toggle("mode-dim", !inMode && !selectedId);
  });
}

function getRelatedIds(id) {
  const node = nodeMap[id];
  if (!node) return new Set();
  return new Set([id, ...node.connections]);
}

function updateHighlights() {
  const related = selectedId ? getRelatedIds(selectedId) : null;
  const modeSet = getModeSet();

  document.querySelectorAll(".node").forEach((el) => {
    const id = el.dataset.id;
    const selected = id === selectedId;
    const inRelated = related ? related.has(id) : false;
    const inMode = modeSet.has(id);

    el.classList.toggle("selected", selected);
    if (selectedId) {
      el.classList.toggle("dimmed", !inRelated);
      el.classList.toggle("mode-dim", false);
    } else {
      el.classList.toggle("dimmed", false);
      el.classList.toggle("mode-dim", !inMode);
    }
    el.classList.toggle("mode-active", inMode && !selectedId);
    el.setAttribute("aria-pressed", selected ? "true" : "false");
  });

  const highlightEdge = (el, from, to) => {
    const direct =
      selectedId &&
      ((from === selectedId && related.has(to)) || (to === selectedId && related.has(from)));
    const neighbor = related && related.has(from) && related.has(to);
    el.classList.toggle("edge-hot", !!direct);
    el.classList.toggle("edge-warm", !direct && !!neighbor);
    el.classList.toggle("edge-dim", selectedId ? !neighbor : !modeSet.has(from) || !modeSet.has(to));
  };

  spokeLayer.querySelectorAll(".spoke").forEach((el) => {
    const to = el.dataset.to;
    if (selectedId) {
      el.classList.toggle("edge-hot", related.has(to) && (to === selectedId || selectedId === "crucible"));
      el.classList.toggle("edge-warm", related.has(to) && to !== selectedId);
      el.classList.toggle("edge-dim", !related.has(to));
    } else {
      el.classList.toggle("edge-hot", false);
      el.classList.toggle("edge-warm", modeSet.has(to));
      el.classList.toggle("edge-dim", !modeSet.has(to));
    }
  });

  edgeLayer.querySelectorAll(".edge").forEach((el) => {
    highlightEdge(el, el.dataset.from, el.dataset.to);
  });
}

function selectNode(id) {
  if (selectedId === id) {
    selectedId = null;
    document.getElementById("sidebar-heading").textContent = "Select a node";
    showPanelEmpty();
  } else {
    selectedId = id;
    document.getElementById("sidebar-heading").textContent = nodeMap[id].label;
    showPanel(nodeMap[id]);
  }
  updateHighlights();
}

function clearSelection() {
  selectedId = null;
  document.getElementById("sidebar-heading").textContent = "Select a node";
  showPanelEmpty();
  updateHighlights();
}

function showPanelEmpty() {
  panelEmpty.style.display = "flex";
  panelContent.classList.remove("active");
}

function showPanel(node) {
  panelEmpty.style.display = "none";
  panelContent.classList.add("active");

  const cat = document.getElementById("panel-category");
  cat.className = `cat-badge ${node.category}`;
  cat.textContent =
    CATEGORY_LABELS[node.category] + (node.planned ? " · Planned" : "");

  document.getElementById("panel-orbit").textContent =
    node.orbit === "center"
      ? "Center"
      : node.orbit === "inner"
        ? "First orbit"
        : "Second orbit";

  document.getElementById("panel-title").textContent = node.label;
  document.getElementById("panel-desc").textContent = node.description;

  const relList = document.getElementById("rel-list");
  relList.innerHTML = "";
  node.connections.forEach((cid) => {
    const related = nodeMap[cid];
    if (!related) return;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "pill";
    btn.textContent = related.label + (related.planned ? " · planned" : "");
    btn.addEventListener("click", () => selectNode(cid));
    relList.appendChild(btn);
  });
}

function showTooltip(e, node) {
  tooltip.textContent = node.short;
  tooltip.classList.add("visible");
  moveTooltip(e);
}

function moveTooltip(e) {
  const pad = 16;
  let x = e.clientX + pad;
  let y = e.clientY + pad;
  const r = tooltip.getBoundingClientRect();
  if (x + r.width > window.innerWidth - 10) x = e.clientX - r.width - pad;
  if (y + r.height > window.innerHeight - 10) y = e.clientY - r.height - pad;
  tooltip.style.left = `${x}px`;
  tooltip.style.top = `${y}px`;
}

function hideTooltip() {
  tooltip.classList.remove("visible");
}

function setMode(modeId) {
  activeMode = modeId;
  modeToggles.querySelectorAll("button").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.mode === modeId);
    btn.setAttribute("aria-pressed", btn.dataset.mode === modeId ? "true" : "false");
  });
  if (!selectedId) updateHighlights();
}

function initModes() {
  MODES.forEach((mode) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = mode.label;
    btn.dataset.mode = mode.id;
    btn.setAttribute("aria-pressed", mode.id === activeMode ? "true" : "false");
    if (mode.id === activeMode) btn.classList.add("active");
    btn.addEventListener("click", () => setMode(mode.id));
    modeToggles.appendChild(btn);
  });
}

function render() {
  computeLayout();
  renderPulseRings();
  renderSpokes();
  renderEdges();
  renderNodes();
  updateHighlights();
}

/* Subtle particle field */
function initParticles() {
  const ctx = particlesCanvas.getContext("2d");
  const particles = Array.from({ length: 48 }, () => ({
    x: Math.random(),
    y: Math.random(),
    r: Math.random() * 1.4 + 0.4,
    vx: (Math.random() - 0.5) * 0.00025,
    vy: (Math.random() - 0.5) * 0.00025,
    a: Math.random() * 0.35 + 0.08,
  }));

  function frame() {
    const w = (particlesCanvas.width = window.innerWidth * devicePixelRatio);
    const h = (particlesCanvas.height = window.innerHeight * devicePixelRatio);
    particlesCanvas.style.width = `${window.innerWidth}px`;
    particlesCanvas.style.height = `${window.innerHeight}px`;
    ctx.clearRect(0, 0, w, h);
    particles.forEach((p) => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > 1) p.vx *= -1;
      if (p.y < 0 || p.y > 1) p.vy *= -1;
      ctx.beginPath();
      ctx.fillStyle = `rgba(34, 211, 238, ${p.a})`;
      ctx.arc(p.x * w, p.y * h, p.r * devicePixelRatio, 0, Math.PI * 2);
      ctx.fill();
    });
    requestAnimationFrame(frame);
  }
  frame();
}

function init() {
  buildEdges();
  initModes();
  initParticles();
  render();
  showPanelEmpty();

  graphStage.addEventListener("click", (e) => {
    if (e.target.closest(".node")) return;
    clearSelection();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") clearSelection();
  });

  let t;
  window.addEventListener("resize", () => {
    clearTimeout(t);
    t = setTimeout(render, 100);
  });
}

document.addEventListener("DOMContentLoaded", init);
