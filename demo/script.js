/**
 * Forge Brain — Public Concept Demo
 * Mock data only. No backend. No proprietary logic.
 */

const NODES = [
  {
    id: "crucible",
    label: "The Crucible Brain",
    category: "hub",
    short: "Central AKOS concept — the intelligence core of the platform vision.",
    description:
      "The conceptual heart of The Crucible AI Knowledge Operating System. Represents how local-first intelligence, composable context, and disciplined API usage come together as a unified brain — not a single app, but a platform vision.",
    connections: ["big-brain", "core", "knowledge-graph", "forge", "aether"],
  },
  {
    id: "big-brain",
    label: "Big Brain",
    category: "intelligence",
    short: "Central orchestration — routes context and coordinates specialists.",
    description:
      "High-level orchestration concept within Core. Coordinates how context flows between the Knowledge Graph, specialist units, and external model calls. Public-safe abstraction — not exposed implementation.",
    connections: ["crucible", "mini-brains", "baby-brains", "knowledge-graph", "prompt-compiler", "experience-engine"],
  },
  {
    id: "mini-brains",
    label: "Mini Brains",
    category: "intelligence",
    short: "Scoped specialists for projects, domains, or workflows.",
    description:
      "Mid-tier intelligence units scoped to a project, client, or domain. Draw from the Skills Library and Knowledge Graph to assemble focused context without reloading everything.",
    connections: ["big-brain", "baby-brains", "skills", "knowledge-graph"],
  },
  {
    id: "baby-brains",
    label: "Baby Brains",
    category: "intelligence",
    short: "Lightweight task-level units for focused execution.",
    description:
      "Small, task-scoped intelligence units for discrete jobs — a single prompt run, a file summary, a workflow step. Keeps API calls narrow and intentional.",
    connections: ["big-brain", "mini-brains", "skills", "token-optimization"],
  },
  {
    id: "skills",
    label: "Skills",
    category: "intelligence",
    short: "Reusable packaged capabilities shared across brain tiers.",
    description:
      "The Skills Library — curated capabilities, templates, and domain expertise available to Mini Brains, Baby Brains, and builders. Composable context made tangible.",
    connections: ["mini-brains", "baby-brains", "brain-gardener", "forge"],
  },
  {
    id: "experience-engine",
    label: "Experience Engine",
    category: "intelligence",
    short: "Learning loop — outcomes refine future context.",
    description:
      "Captures what worked, what didn't, and what context was in play. Feeds signals back into the brain layer so each session starts smarter — without exposing proprietary learning logic.",
    connections: ["big-brain", "memory", "knowledge-graph", "brain-gardener"],
  },
  {
    id: "brain-gardener",
    label: "Brain Gardener",
    category: "intelligence",
    short: "Curates and maintains knowledge health over time.",
    description:
      "Conceptual custodian of the knowledge layer — pruning stale context, strengthening useful connections, and keeping the graph healthy. High-level metaphor, not production tooling.",
    connections: ["knowledge-graph", "memory", "skills", "experience-engine"],
  },
  {
    id: "knowledge-graph",
    label: "Knowledge Graph",
    category: "services",
    short: "Entity-relationship store for all platform assets.",
    description:
      "The structured map of projects, prompts, agents, files, memories, skills, and their relationships. Forge Brain visualizes this graph on the canvas — this demo shows the concept at a higher level.",
    connections: ["crucible", "big-brain", "memory", "brain-gardener", "experience-engine", "forge"],
  },
  {
    id: "memory",
    label: "Memory",
    category: "services",
    short: "Persistent context that carries across sessions.",
    description:
      "Long-lived context assets that survive beyond a single chat. Part of local-first intelligence — owned by the builder, composed into future work. Implementation details are private.",
    connections: ["knowledge-graph", "brain-gardener", "experience-engine", "aether"],
  },
  {
    id: "prompt-compiler",
    label: "Prompt Compiler",
    category: "services",
    short: "Assembles scoped prompts from composable context.",
    description:
      "Abstract platform service that builds model-ready prompts from graph assets, skills, and active focus. Exists to support disciplined API usage — internal compilation logic is proprietary.",
    connections: ["big-brain", "token-optimization", "core"],
  },
  {
    id: "token-optimization",
    label: "Token Optimization",
    category: "services",
    short: "Scopes context to reduce unnecessary model input.",
    description:
      "Ensures only relevant context reaches external model calls — reducing token and API waste. Public concept only; algorithms and implementation are not disclosed.",
    connections: ["prompt-compiler", "baby-brains", "aether", "core"],
  },
  {
    id: "forge",
    label: "Forge",
    category: "visual",
    short: "Desktop workspace — where builders do daily AI work.",
    description:
      "The primary builder-facing product. Desktop workspace for projects, agents, context composition, and knowledge assets. Forge Brain lives inside Forge as its graph surface.",
    connections: ["crucible", "knowledge-graph", "skills", "core", "aether"],
  },
  {
    id: "aether",
    label: "Aether",
    category: "products",
    short: "Intelligence layer — context selection and surfacing.",
    description:
      "Cross-platform intelligence that makes large knowledge feel small in active context. Surfaces what matters without breaking flow. Internals are proprietary.",
    connections: ["crucible", "memory", "token-optimization", "forge", "core"],
  },
  {
    id: "core",
    label: "Core",
    category: "products",
    short: "Shared engine and runtime beneath all products.",
    description:
      "The foundation all Crucible products build on — entity registry, relationships, platform primitives, and runtime services. Private repository; not represented in this demo beyond concept.",
    connections: ["crucible", "big-brain", "prompt-compiler", "token-optimization", "forge", "aether", "siege", "barrage"],
  },
  {
    id: "siege",
    label: "Siege",
    category: "products",
    planned: true,
    short: "Integration platform — external tools and systems. Planned.",
    description:
      "Future integration platform connecting external APIs, tools, and services into the Crucible entity model. Planned — not shipped.",
    connections: ["core", "knowledge-graph"],
  },
  {
    id: "barrage",
    label: "Barrage",
    category: "products",
    planned: true,
    short: "Cloud and team platform. Planned.",
    description:
      "Future cloud and team platform for shared workspaces, collaborative graphs, and team-scale context. Planned — not shipped.",
    connections: ["core", "forge"],
  },
];

const CATEGORY_LABELS = {
  hub: "Platform Core",
  intelligence: "Intelligence Architecture",
  services: "Platform Services",
  products: "Ecosystem Product",
  visual: "Builder Workspace",
};

const nodeMap = Object.fromEntries(NODES.map((n) => [n.id, n]));

let selectedId = null;
let layoutPositions = {};
let edges = [];

const graphWrap = document.getElementById("graph-wrap");
const nodesLayer = document.getElementById("nodes-layer");
const svgEl = document.getElementById("graph-svg");
const tooltip = document.getElementById("tooltip");
const panelEmpty = document.getElementById("panel-empty");
const panelContent = document.getElementById("panel-content");

function buildEdges() {
  const seen = new Set();
  edges = [];
  NODES.forEach((node) => {
    node.connections.forEach((targetId) => {
      const key = [node.id, targetId].sort().join("--");
      if (!seen.has(key) && nodeMap[targetId]) {
        seen.add(key);
        edges.push({ from: node.id, to: targetId });
      }
    });
  });
}

function computeLayout() {
  const rect = graphWrap.getBoundingClientRect();
  const cx = rect.width / 2;
  const cy = rect.height / 2;
  const hub = nodeMap.crucible;
  layoutPositions[hub.id] = { x: cx, y: cy };

  const rings = [
    { ids: ["big-brain", "knowledge-graph", "core", "forge", "aether"], radius: 0.26 },
    { ids: ["mini-brains", "baby-brains", "skills", "memory", "prompt-compiler"], radius: 0.38 },
    { ids: ["experience-engine", "brain-gardener", "token-optimization", "siege", "barrage"], radius: 0.48 },
  ];

  const minDim = Math.min(rect.width, rect.height);

  rings.forEach((ring) => {
    const count = ring.ids.length;
    ring.ids.forEach((id, i) => {
      const angle = (i / count) * Math.PI * 2 - Math.PI / 2;
      const r = minDim * ring.radius;
      layoutPositions[id] = {
        x: cx + Math.cos(angle) * r,
        y: cy + Math.sin(angle) * r,
      };
    });
  });
}

function renderSVG() {
  svgEl.innerHTML = "";
  const ns = "http://www.w3.org/2000/svg";

  edges.forEach(({ from, to }) => {
    const a = layoutPositions[from];
    const b = layoutPositions[to];
    if (!a || !b) return;

    const line = document.createElementNS(ns, "line");
    line.setAttribute("x1", a.x);
    line.setAttribute("y1", a.y);
    line.setAttribute("x2", b.x);
    line.setAttribute("y2", b.y);
    line.dataset.from = from;
    line.dataset.to = to;
    svgEl.appendChild(line);
  });
}

function renderNodes() {
  nodesLayer.innerHTML = "";
  const floatClasses = ["float-a", "float-b", "float-c"];

  NODES.forEach((node, i) => {
    const pos = layoutPositions[node.id];
    if (!pos) return;

    const el = document.createElement("div");
    el.className = `node ${node.category}${node.planned ? " planned" : ""} ${node.category === "hub" ? "hub" : ""} ${floatClasses[i % 3]}`;
    el.dataset.id = node.id;
    el.style.left = `${pos.x}px`;
    el.style.top = `${pos.y}px`;

    el.innerHTML = `
      <div class="node-inner">
        <div class="node-orb" aria-hidden="true"></div>
        <span class="node-label">${node.label}</span>
      </div>
    `;

    el.addEventListener("mouseenter", (e) => showTooltip(e, node));
    el.addEventListener("mousemove", moveTooltip);
    el.addEventListener("mouseleave", hideTooltip);
    el.addEventListener("click", () => selectNode(node.id));

    nodesLayer.appendChild(el);
  });
}

function showTooltip(e, node) {
  tooltip.textContent = node.short;
  tooltip.classList.add("visible");
  moveTooltip(e);
}

function moveTooltip(e) {
  const pad = 14;
  let x = e.clientX + pad;
  let y = e.clientY + pad;
  const rect = tooltip.getBoundingClientRect();
  if (x + rect.width > window.innerWidth - 8) x = e.clientX - rect.width - pad;
  if (y + rect.height > window.innerHeight - 8) y = e.clientY - rect.height - pad;
  tooltip.style.left = `${x}px`;
  tooltip.style.top = `${y}px`;
}

function hideTooltip() {
  tooltip.classList.remove("visible");
}

function getRelatedIds(id) {
  const node = nodeMap[id];
  if (!node) return new Set();
  const related = new Set([id, ...node.connections]);
  node.connections.forEach((cid) => {
    const other = nodeMap[cid];
    if (other) other.connections.forEach((r) => related.add(r));
  });
  return related;
}

function selectNode(id) {
  if (selectedId === id) {
    selectedId = null;
    clearHighlights();
    showPanelEmpty();
    return;
  }

  selectedId = id;
  const related = getRelatedIds(id);

  document.querySelectorAll(".node").forEach((el) => {
    const nid = el.dataset.id;
    el.classList.toggle("selected", nid === id);
    el.classList.toggle("dimmed", !related.has(nid));
  });

  svgEl.querySelectorAll("line").forEach((line) => {
    const from = line.dataset.from;
    const to = line.dataset.to;
    const active = related.has(from) && related.has(to);
    line.classList.toggle("highlighted", active);
    line.classList.toggle("dimmed", !active);
  });

  showPanel(nodeMap[id]);
}

function clearHighlights() {
  document.querySelectorAll(".node").forEach((el) => {
    el.classList.remove("selected", "dimmed");
  });
  svgEl.querySelectorAll("line").forEach((line) => {
    line.classList.remove("highlighted", "dimmed");
  });
}

function showPanelEmpty() {
  panelEmpty.style.display = "block";
  panelContent.classList.remove("active");
}

function showPanel(node) {
  panelEmpty.style.display = "none";
  panelContent.classList.add("active");

  const catLabel = CATEGORY_LABELS[node.category] || node.category;

  document.getElementById("panel-category").className = `panel-category ${node.category}`;
  document.getElementById("panel-category").textContent = catLabel + (node.planned ? " · Planned" : "");
  document.getElementById("panel-title").textContent = node.label;
  document.getElementById("panel-desc").textContent = node.description;

  const relList = document.getElementById("rel-list");
  relList.innerHTML = "";
  node.connections.forEach((cid) => {
    const related = nodeMap[cid];
    if (!related) return;
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.textContent = related.label + (related.planned ? " (planned)" : "");
    btn.addEventListener("click", () => selectNode(cid));
    li.appendChild(btn);
    relList.appendChild(li);
  });
}

function init() {
  buildEdges();
  computeLayout();
  renderSVG();
  renderNodes();

  graphWrap.addEventListener("click", (e) => {
    if (e.target === graphWrap || e.target === svgEl || e.target === nodesLayer) {
      selectedId = null;
      clearHighlights();
      showPanelEmpty();
    }
  });

  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      computeLayout();
      renderSVG();
      renderNodes();
      if (selectedId) selectNode(selectedId);
    }, 120);
  });
}

document.addEventListener("DOMContentLoaded", init);
