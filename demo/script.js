/**
 * Forge Brain — Living Knowledge Graph (Public Concept Demo)
 * Canvas-rendered mock graph. No backend. No proprietary logic.
 */

const DENSITY = { low: 300, medium: 700, high: 1400 };
const DEFAULT_DENSITY = "medium";
const DEFAULT_ZOOM = 1.12;
const WORLD_RADIUS_FACTOR = 0.47;
const EXPORT_SCALE = 2;

const MODES = [
  { id: "brain", label: "Brain Map" },
  { id: "flow", label: "Knowledge Flow" },
  { id: "cluster", label: "Cluster View" },
  { id: "signal", label: "Signal View" },
];

const FLOW_HIGHLIGHT = new Set([
  "hub",
  "user",
  "forge",
  "big-brain",
  "knowledge",
  "claude",
  "experience-engine",
]);

const CLUSTER_DEFS = [
  {
    id: "projects",
    label: "Projects",
    color: "#22d3ee",
    desc: "Scoped workspaces and goals across a builder's practice.",
  },
  {
    id: "prompts",
    label: "Prompts",
    color: "#38bdf8",
    desc: "Reusable instruction templates and variants.",
  },
  {
    id: "memories",
    label: "Memories",
    color: "#a78bfa",
    desc: "Persistent context that carries across sessions.",
  },
  {
    id: "skills",
    label: "Skills",
    color: "#c084fc",
    desc: "Packaged capabilities and domain expertise.",
  },
  {
    id: "agents",
    label: "Agents",
    color: "#34d399",
    desc: "Configured AI workers with roles and capabilities.",
  },
  {
    id: "files",
    label: "Files",
    color: "#2dd4bf",
    desc: "Documents, code, and reference material.",
  },
  {
    id: "models",
    label: "Models",
    color: "#fb7185",
    desc: "LLM and tool endpoints available to the system.",
  },
  {
    id: "workflows",
    label: "Workflows",
    color: "#fbbf24",
    desc: "Multi-step processes linking agents, prompts, and outputs.",
  },
  {
    id: "clients",
    label: "Clients",
    color: "#f59e0b",
    desc: "External parties, accounts, or engagement contexts.",
  },
  {
    id: "knowledge",
    label: "Knowledge",
    color: "#4ade80",
    desc: "Structured and unstructured information assets.",
  },
  {
    id: "big-brain",
    label: "Big Brain",
    color: "#e879f9",
    desc: "Central orchestration — routes context and coordinates specialists.",
  },
  {
    id: "mini-brains",
    label: "Mini Brains",
    color: "#d946ef",
    desc: "Scoped specialists for projects, domains, or workflows.",
  },
  {
    id: "baby-brains",
    label: "Baby Brains",
    color: "#f0abfc",
    desc: "Lightweight task-level execution units.",
  },
  {
    id: "experience-engine",
    label: "Experience Engine",
    color: "#818cf8",
    desc: "Learning loop — outcomes refine future context.",
  },
  {
    id: "brain-gardener",
    label: "Brain Gardener",
    color: "#6ee7b7",
    desc: "Curates and maintains knowledge health over time.",
  },
];

const SPECIAL_ANCHORS = [
  {
    id: "user",
    label: "User",
    cluster: "flow",
    color: "#94a3b8",
    desc: "Builder — source of intent, goals, and context.",
    angle: -0.85,
    dist: 0.38,
  },
  {
    id: "forge",
    label: "Forge",
    cluster: "ecosystem",
    color: "#fbbf24",
    desc: "Desktop workspace — where builders do daily AI work.",
    angle: -0.4,
    dist: 0.32,
  },
  {
    id: "core",
    label: "Core",
    cluster: "ecosystem",
    color: "#34d399",
    desc: "Shared engine and runtime beneath all products.",
    angle: 0.9,
    dist: 0.34,
  },
  {
    id: "aether",
    label: "Aether",
    cluster: "ecosystem",
    color: "#a78bfa",
    desc: "Intelligence layer — context selection and surfacing.",
    angle: 2.1,
    dist: 0.33,
  },
  {
    id: "claude",
    label: "Claude",
    cluster: "flow",
    color: "#fb923c",
    desc: "Primary model target — scoped calls against composable context.",
    angle: 1.35,
    dist: 0.28,
  },
];

const canvas = document.getElementById("graph-canvas");
const ctx = canvas.getContext("2d");
const wrap = document.getElementById("canvas-wrap");
const tooltip = document.getElementById("tooltip");
const statsEl = document.getElementById("stats");

let nodes = [];
let edges = [];
let adjacency = [];
let pulses = [];
let flashes = [];
let signalTimer = 0;

let densityKey = DEFAULT_DENSITY;
let mode = "brain";
let pulseSpeed = 1;
let selectedId = null;
let hoverId = null;

let cam = { x: 0, y: 0, zoom: DEFAULT_ZOOM };
let dragging = false;
let dragStart = { x: 0, y: 0, camX: 0, camY: 0 };

let width = 0;
let height = 0;
let dpr = 1;
let worldR = 1;

/* Seeded RNG for stable regen per density */
function mulberry32(a) {
  return function () {
    let t = (a += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function generateGraph(targetCount) {
  const rand = mulberry32(targetCount * 9973);
  const n = [];
  const e = [];
  const idIndex = new Map();

  const addNode = (node) => {
    idIndex.set(node.id, n.length);
    n.push(node);
    return n.length - 1;
  };

  const hub = addNode({
    id: "hub",
    label: "The Crucible Brain",
    cluster: "hub",
    color: "#22d3ee",
    isAnchor: true,
    isHub: true,
    x: 0,
    y: 0,
    r: 16,
    desc: "Central AKOS intelligence — local-first, composable, disciplined API usage.",
    short: "Platform brain hub",
  });

  SPECIAL_ANCHORS.forEach((a) => {
    addNode({
      id: a.id,
      label: a.label,
      cluster: a.cluster,
      color: a.color,
      isAnchor: true,
      x: Math.cos(a.angle) * worldR * a.dist,
      y: Math.sin(a.angle) * worldR * a.dist,
      r: 9,
      desc: a.desc,
      short: a.label,
    });
  });

  const perCluster = Math.max(
    8,
    Math.floor((targetCount - 20) / CLUSTER_DEFS.length)
  );

  CLUSTER_DEFS.forEach((def, ci) => {
    const angle = (ci / CLUSTER_DEFS.length) * Math.PI * 2 - Math.PI / 2;
    const dist = worldR * (0.58 + rand() * 0.1);
    const cx = Math.cos(angle) * dist;
    const cy = Math.sin(angle) * dist;

    const anchorId = `${def.id}__anchor`;
    const ai = addNode({
      id: anchorId,
      label: def.label,
      cluster: def.id,
      color: def.color,
      isAnchor: true,
      x: cx,
      y: cy,
      r: 8,
      desc: def.desc,
      short: def.label,
    });

    const satellites = perCluster - 1;
    const clusterIndices = [];
    for (let s = 0; s < satellites; s++) {
      const a = rand() * Math.PI * 2;
      const d = (0.05 + Math.sqrt(rand()) * 0.16) * worldR;
      const idx = addNode({
        id: `${def.id}__${s}`,
        label: `${def.label.slice(0, 4)}·${s}`,
        cluster: def.id,
        color: def.color,
        isAnchor: false,
        x: cx + Math.cos(a) * d,
        y: cy + Math.sin(a) * d,
        r: 1.2 + rand() * 1.4,
        desc: `Conceptual ${def.label.toLowerCase()} asset.`,
        short: def.label,
      });
      clusterIndices.push(idx);
    }

    clusterIndices.forEach((si) => {
      e.push({ a: ai, b: si });
      if (rand() > 0.45) {
        const other = clusterIndices[Math.floor(rand() * clusterIndices.length)];
        if (other !== si) e.push({ a: si, b: other });
      }
    });
  });

  for (let i = 0; i < n.length; i++) {
    if (!n[i].isAnchor) continue;
    e.push({ a: hub, b: i });
  }

  const anchors = n.map((_, i) => i).filter((i) => n[i].isAnchor && !n[i].isHub);
  const crossCount = Math.floor(anchors.length * 2.5);
  for (let c = 0; c < crossCount; c++) {
    const a = anchors[Math.floor(rand() * anchors.length)];
    let b = anchors[Math.floor(rand() * anchors.length)];
    if (a === b) continue;
    e.push({ a, b, cross: true });
  }

  const unique = new Set();
  const edges = [];
  e.forEach((edge) => {
    const key = edge.a < edge.b ? `${edge.a}-${edge.b}` : `${edge.b}-${edge.a}`;
    if (unique.has(key)) return;
    unique.add(key);
    edges.push(edge);
  });

  return { nodes: n, edges };
}

function buildAdjacency() {
  adjacency = nodes.map(() => []);
  edges.forEach((edge, ei) => {
    adjacency[edge.a].push({ node: edge.b, edgeIndex: ei });
    adjacency[edge.b].push({ node: edge.a, edgeIndex: ei });
  });
}

function getLocalNetwork(startIdx) {
  const visited = new Set([startIdx]);
  const queue = [startIdx];
  const edgeSet = new Set();
  let depth = 0;
  const maxDepth = 2;

  while (queue.length && depth <= maxDepth) {
    const levelSize = queue.length;
    for (let i = 0; i < levelSize; i++) {
      const idx = queue.shift();
      adjacency[idx].forEach(({ node, edgeIndex }) => {
        edgeSet.add(edgeIndex);
        if (!visited.has(node)) {
          visited.add(node);
          if (depth < maxDepth) queue.push(node);
        }
      });
    }
    depth++;
  }
  return { nodes: visited, edges: edgeSet };
}

function spawnWaveFrom(startIdx) {
  const { edges: edgeSet } = getLocalNetwork(startIdx);
  let delay = 0;
  edgeSet.forEach((ei) => {
    const edge = edges[ei];
    const from =
      adjacency[edge.a].some((x) => x.edgeIndex === ei && x.node === edge.b) ? edge.a : edge.b;
    const to = from === edge.a ? edge.b : edge.a;
    if (!selectedNetwork || !selectedNetwork.nodes.has(from) || !selectedNetwork.nodes.has(to))
      return;
    pulses.push({
      a: from,
      b: to,
      t: 0,
      delay: delay * 0.04,
      speed: 0.35 + Math.random() * 0.15,
    });
    delay++;
  });
}

let selectedNetwork = null;

function selectNode(idx) {
  if (selectedId === idx) {
    selectedId = null;
    selectedNetwork = null;
    pulses = [];
    updatePanelEmpty();
    return;
  }
  selectedId = idx;
  selectedNetwork = getLocalNetwork(idx);
  pulses = [];
  spawnWaveFrom(idx);
  updatePanel(nodes[idx]);
}

function screenToWorld(sx, sy) {
  return {
    x: (sx - width / 2) / cam.zoom - cam.x,
    y: (sy - height / 2) / cam.zoom - cam.y,
  };
}

function findNodeAt(wx, wy, anchorsOnly = false) {
  let best = -1;
  let bestD = Infinity;
  for (let i = 0; i < nodes.length; i++) {
    const n = nodes[i];
    if (anchorsOnly && !n.isAnchor) continue;
    const hit = n.r + (n.isHub ? 8 : n.isAnchor ? 6 : 3);
    const d = Math.hypot(n.x - wx, n.y - wy);
    if (d < hit && d < bestD) {
      bestD = d;
      best = i;
    }
  }
  return best;
}

function resize() {
  const rect = wrap.getBoundingClientRect();
  dpr = Math.min(window.devicePixelRatio || 1, 2);
  width = rect.width;
  height = rect.height;
  canvas.width = Math.floor(width * dpr);
  canvas.height = Math.floor(height * dpr);
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  worldR = Math.min(width, height) * WORLD_RADIUS_FACTOR;
}

function flowActive(n) {
  if (n.isHub) return true;
  if (FLOW_HIGHLIGHT.has(n.id)) return true;
  if (FLOW_HIGHLIGHT.has(n.cluster)) return true;
  if (n.id.startsWith("knowledge")) return true;
  if (n.id.startsWith("experience-engine")) return true;
  if (n.id.startsWith("big-brain")) return true;
  if (n.id === "user" || n.cluster === "flow") return true;
  return false;
}

function nodeAlpha(i) {
  const n = nodes[i];
  if (mode === "flow") {
    return flowActive(n) ? 1 : 0.1;
  }
  if (selectedNetwork) {
    return selectedNetwork.nodes.has(i) ? 1 : 0.08;
  }
  if (mode === "cluster") {
    return n.isAnchor ? 1 : 0.45;
  }
  return n.isAnchor ? 1 : 0.58;
}

function edgeAlpha(edge, ei) {
  if (mode === "flow") {
    const a = flowActive(nodes[edge.a]);
    const b = flowActive(nodes[edge.b]);
    if (a && b) return 0.85;
    return 0.05;
  }
  const alphaA = nodeAlpha(edge.a);
  const alphaB = nodeAlpha(edge.b);
  let alpha = Math.min(alphaA, alphaB) * (edge.cross ? 0.35 : 0.55);
  if (selectedNetwork && selectedNetwork.edges.has(ei)) alpha = 0.95;
  return alpha;
}

function paint(targetCtx, w, h) {
  targetCtx.fillStyle = "#050810";
  targetCtx.fillRect(0, 0, w, h);

  const vignette = targetCtx.createRadialGradient(
    w / 2,
    h / 2,
    w * 0.08,
    w / 2,
    h / 2,
    Math.max(w, h) * 0.72
  );
  vignette.addColorStop(0, "rgba(34, 211, 238, 0.07)");
  vignette.addColorStop(0.45, "rgba(88, 28, 135, 0.04)");
  vignette.addColorStop(1, "rgba(4, 6, 10, 0.92)");
  targetCtx.fillStyle = vignette;
  targetCtx.fillRect(0, 0, w, h);

  targetCtx.save();
  targetCtx.translate(w / 2, h / 2);
  targetCtx.scale(cam.zoom, cam.zoom);
  targetCtx.translate(cam.x, cam.y);

  const now = performance.now();

  edges.forEach((edge, ei) => {
    const a = nodes[edge.a];
    const b = nodes[edge.b];
    const alpha = edgeAlpha(edge, ei);
    const edgeBoost = mode === "brain" && !selectedNetwork ? 1.15 : 1;

    targetCtx.beginPath();
    targetCtx.moveTo(a.x, a.y);
    targetCtx.lineTo(b.x, b.y);
    targetCtx.strokeStyle = edge.cross
      ? `rgba(167,139,250,${alpha * 0.55 * edgeBoost})`
      : `rgba(34,211,238,${alpha * 0.48 * edgeBoost})`;
    targetCtx.lineWidth = edge.cross ? 0.55 : selectedNetwork?.edges.has(ei) ? 1.25 : 0.65;
    targetCtx.stroke();
  });

  pulses.forEach((p) => {
    if (p.delay > 0) {
      p.delay -= 0.016;
      return;
    }
    p.t += 0.016 * pulseSpeed * p.speed;
    if (p.t > 1) return;
    const a = nodes[p.a];
    const b = nodes[p.b];
    const x = a.x + (b.x - a.x) * p.t;
    const y = a.y + (b.y - a.y) * p.t;
    const grad = targetCtx.createRadialGradient(x, y, 0, x, y, 12);
    grad.addColorStop(0, "rgba(255,255,255,0.95)");
    grad.addColorStop(0.3, "rgba(34,211,238,0.8)");
    grad.addColorStop(1, "rgba(34,211,238,0)");
    targetCtx.fillStyle = grad;
    targetCtx.beginPath();
    targetCtx.arc(x, y, 10, 0, Math.PI * 2);
    targetCtx.fill();

    targetCtx.strokeStyle = "rgba(34,211,238,0.7)";
    targetCtx.lineWidth = 2;
    targetCtx.beginPath();
    targetCtx.moveTo(a.x, a.y);
    const px = a.x + (b.x - a.x) * p.t;
    const py = a.y + (b.y - a.y) * p.t;
    targetCtx.lineTo(px, py);
    targetCtx.stroke();

    if (p.t >= 0.98 && !p.done) {
      p.done = true;
      flashes.push({ idx: p.b, until: now + 280 });
    }
  });
  pulses = pulses.filter((p) => p.t <= 1 || p.delay > 0);

  if (mode === "signal") {
    signalTimer += 0.016;
    if (signalTimer > 0.35) {
      signalTimer = 0;
      const ei = Math.floor(Math.random() * edges.length);
      const edge = edges[ei];
      pulses.push({ a: edge.a, b: edge.b, t: 0, delay: 0, speed: 0.25 + Math.random() * 0.2 });
    }
  }

  nodes.forEach((n, i) => {
    const alpha = nodeAlpha(i);
    const flash = flashes.find((f) => f.idx === i && f.until > now);
    const flashBoost = flash ? 1 : 0;

    if (mode === "cluster" && n.isAnchor && !n.isHub) {
      targetCtx.strokeStyle = `${n.color}44`;
      targetCtx.lineWidth = 1;
      targetCtx.setLineDash([4, 6]);
      targetCtx.beginPath();
      targetCtx.arc(n.x, n.y, worldR * 0.12, 0, Math.PI * 2);
      targetCtx.stroke();
      targetCtx.setLineDash([]);
    }

    const r = n.r + flashBoost * 3;
    const glow = targetCtx.createRadialGradient(n.x, n.y, 0, n.x, n.y, r * 3);
    glow.addColorStop(0, n.color + (flash ? "ff" : "cc"));
    glow.addColorStop(1, n.color + "00");
    targetCtx.fillStyle = glow;
    targetCtx.globalAlpha = alpha;
    targetCtx.beginPath();
    targetCtx.arc(n.x, n.y, r * 2.5, 0, Math.PI * 2);
    targetCtx.fill();

    targetCtx.fillStyle = n.color;
    targetCtx.globalAlpha = alpha;
    targetCtx.beginPath();
    targetCtx.arc(n.x, n.y, r, 0, Math.PI * 2);
    targetCtx.fill();

    if (n.isAnchor || n.isHub) {
      targetCtx.fillStyle = "rgba(255,255,255,0.92)";
      targetCtx.textAlign = "center";
      targetCtx.globalAlpha = alpha;
      if (n.isHub) {
        targetCtx.font = "bold 8px Inter, sans-serif";
        targetCtx.fillText("Crucible Brain", n.x, n.y - r - 6);
      } else {
        targetCtx.font = "600 6px Inter, sans-serif";
        targetCtx.fillText(n.label, n.x, n.y - r - 5);
      }
    }
    targetCtx.globalAlpha = 1;
  });

  if (selectedId !== null) {
    const n = nodes[selectedId];
    targetCtx.strokeStyle = "rgba(34,211,238,0.8)";
    targetCtx.lineWidth = 1.5;
    targetCtx.beginPath();
    targetCtx.arc(n.x, n.y, n.r + 10, 0, Math.PI * 2);
    targetCtx.stroke();
  }

  targetCtx.restore();
  flashes = flashes.filter((f) => f.until > now);
}

function rebuild() {
  const count = DENSITY[densityKey];
  const g = generateGraph(count);
  nodes = g.nodes;
  edges = g.edges;
  buildAdjacency();
  selectedId = null;
  selectedNetwork = null;
  pulses = [];
  flashes = [];
  hoverId = null;
  updatePanelEmpty();
  statsEl.textContent = `${nodes.length} nodes · ${edges.length} edges · ${densityKey} · mock data`;
}

function draw() {
  paint(ctx, width, height);
}

function exportPng() {
  hideTooltip();
  const exportCanvas = document.createElement("canvas");
  exportCanvas.width = Math.floor(width * dpr * EXPORT_SCALE);
  exportCanvas.height = Math.floor(height * dpr * EXPORT_SCALE);
  const exportCtx = exportCanvas.getContext("2d");
  exportCtx.setTransform(dpr * EXPORT_SCALE, 0, 0, dpr * EXPORT_SCALE, 0, 0);
  paint(exportCtx, width, height);

  const link = document.createElement("a");
  const stamp = new Date().toISOString().slice(0, 10);
  link.download = `forge-brain-${mode}-${densityKey}-${stamp}.png`;
  link.href = exportCanvas.toDataURL("image/png");
  link.click();
}

function loop() {
  draw();
  requestAnimationFrame(loop);
}

function updatePanelEmpty() {
  document.getElementById("panel-title").textContent = "Explore the graph";
  document.getElementById("panel-empty").style.display = "block";
  document.getElementById("panel-content").classList.remove("active");
}

function updatePanel(node) {
  const idx = nodes.findIndex((n) => n.id === node.id);
  document.getElementById("panel-title").textContent = node.label;
  document.getElementById("panel-empty").style.display = "none";
  document.getElementById("panel-content").classList.add("active");

  const cat = document.getElementById("panel-category");
  cat.textContent = node.isHub ? "Platform Core" : node.isAnchor ? "Anchor" : "Asset";
  cat.className = "cat-badge";

  const clusterDef = CLUSTER_DEFS.find((c) => c.id === node.cluster);
  document.getElementById("panel-cluster").textContent =
    clusterDef?.label || node.cluster || "Ecosystem";

  document.getElementById("panel-node-title").textContent = node.label;
  document.getElementById("panel-desc").textContent = node.desc;

  const rel = document.getElementById("rel-list");
  rel.innerHTML = "";
  if (idx < 0) return;
  const seen = new Set();
  adjacency[idx].forEach(({ node: ni }) => {
    const nb = nodes[ni];
    if (!nb.isAnchor || seen.has(nb.id)) return;
    seen.add(nb.id);
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "pill";
    btn.textContent = nb.label;
    btn.addEventListener("click", () => selectNode(ni));
    rel.appendChild(btn);
  });
}

function showTooltip(x, y, text) {
  tooltip.textContent = text;
  tooltip.classList.add("visible");
  tooltip.style.left = `${x + 14}px`;
  tooltip.style.top = `${y + 14}px`;
}

function hideTooltip() {
  tooltip.classList.remove("visible");
}

function initControls() {
  const modeBtns = document.getElementById("mode-btns");
  MODES.forEach((m) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = m.label;
    b.dataset.mode = m.id;
    if (m.id === mode) b.classList.add("active");
    b.addEventListener("click", () => {
      mode = m.id;
      modeBtns.querySelectorAll("button").forEach((btn) => {
        btn.classList.toggle("active", btn.dataset.mode === mode);
      });
    });
    modeBtns.appendChild(b);
  });

  const densityBtns = document.getElementById("density-btns");
  Object.keys(DENSITY).forEach((key) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = key.charAt(0).toUpperCase() + key.slice(1);
    b.dataset.density = key;
    if (key === densityKey) b.classList.add("active");
    b.addEventListener("click", () => {
      densityKey = key;
      densityBtns.querySelectorAll("button").forEach((btn) => {
        btn.classList.toggle("active", btn.dataset.density === densityKey);
      });
      rebuild();
    });
    densityBtns.appendChild(b);
  });

  document.getElementById("pulse-speed").addEventListener("input", (e) => {
    pulseSpeed = parseFloat(e.target.value);
  });

  document.getElementById("reset-btn").addEventListener("click", () => {
    cam = { x: 0, y: 0, zoom: DEFAULT_ZOOM };
    selectedId = null;
    selectedNetwork = null;
    pulses = [];
    updatePanelEmpty();
  });

  document.getElementById("export-btn").addEventListener("click", exportPng);
}

let dragMoved = false;

function initInput() {
  canvas.addEventListener("mousedown", (e) => {
    dragging = true;
    dragMoved = false;
    dragStart = { x: e.clientX, y: e.clientY, camX: cam.x, camY: cam.y };
  });
  window.addEventListener("mouseup", () => {
    dragging = false;
  });
  canvas.addEventListener("mousemove", (e) => {
    const rect = canvas.getBoundingClientRect();
    const sx = e.clientX - rect.left;
    const sy = e.clientY - rect.top;

    if (dragging) {
      if (Math.hypot(e.clientX - dragStart.x, e.clientY - dragStart.y) > 4) dragMoved = true;
      cam.x = dragStart.camX + (e.clientX - dragStart.x) / cam.zoom;
      cam.y = dragStart.camY + (e.clientY - dragStart.y) / cam.zoom;
      hideTooltip();
      return;
    }

    const w = screenToWorld(sx, sy);
    const idx = findNodeAt(w.x, w.y, false);
    if (idx >= 0 && nodes[idx].isAnchor) {
      hoverId = idx;
      showTooltip(e.clientX, e.clientY, nodes[idx].short + " — " + nodes[idx].desc.slice(0, 80));
    } else {
      hoverId = null;
      hideTooltip();
    }
  });
  canvas.addEventListener("click", (e) => {
    if (dragMoved) return;
    const rect = canvas.getBoundingClientRect();
    const w = screenToWorld(e.clientX - rect.left, e.clientY - rect.top);
    const idx = findNodeAt(w.x, w.y, true);
    if (idx >= 0) selectNode(idx);
  });
  canvas.addEventListener(
    "wheel",
    (e) => {
      e.preventDefault();
      const factor = e.deltaY > 0 ? 0.92 : 1.08;
      cam.zoom = Math.min(2.5, Math.max(0.4, cam.zoom * factor));
    },
    { passive: false }
  );
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      selectedId = null;
      selectedNetwork = null;
      pulses = [];
      updatePanelEmpty();
    }
  });
}

function init() {
  initControls();
  initInput();
  resize();
  rebuild();
  loop();
  window.addEventListener("resize", () => {
    resize();
  });
}

document.addEventListener("DOMContentLoaded", init);
