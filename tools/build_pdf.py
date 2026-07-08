# The Crucible — Product Overview PDF builder (reportlab)
# Light minimal theme, molten-orange accent. Two-pass build for TOC page numbers.
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as _canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

PW, PH = letter  # 612 x 792
M = 64           # side margin
CW = PW - 2 * M  # content width = 484

# ---------- fonts ----------
GF = "/usr/share/fonts/truetype/google-fonts/"
LA = "/usr/share/fonts/truetype/lato/"
pdfmetrics.registerFont(TTFont("PopL", GF + "Poppins-Light.ttf"))
pdfmetrics.registerFont(TTFont("Pop", GF + "Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopM", GF + "Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("PopB", GF + "Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Lato", LA + "Lato-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LatoB", LA + "Lato-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LatoI", LA + "Lato-Italic.ttf"))
pdfmetrics.registerFont(TTFont("LatoBI", LA + "Lato-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("LatoS", LA + "Lato-Semibold.ttf"))
pdfmetrics.registerFont(TTFont("LatoL", LA + "Lato-Light.ttf"))
pdfmetrics.registerFontFamily("Lato", normal="Lato", bold="LatoB", italic="LatoI", boldItalic="LatoBI")
pdfmetrics.registerFontFamily("LatoL", normal="LatoL", bold="LatoS", italic="LatoI", boldItalic="LatoBI")

# ---------- palette ----------
INK    = HexColor("#181310")
INK2   = HexColor("#3B342D")
MUTE   = HexColor("#7A7066")
FAINT  = HexColor("#AFA69B")
RULE   = HexColor("#E9E2D9")
WARM   = HexColor("#FAF6F1")
PAPER  = HexColor("#FFFFFF")
ACCENT = HexColor("#E1560A")
ACC_D  = HexColor("#A63E06")
ACC_P  = HexColor("#FCEADF")
ACC_PP = HexColor("#FDF3EC")
DARK   = HexColor("#1D1712")
DARK2  = HexColor("#2B221A")
WHITE  = HexColor("#FFFFFF")
CREAM  = HexColor("#F4E8DD")

def S(name, font, size, leading, color, space_after=0, align=TA_LEFT):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading,
                          textColor=color, spaceAfter=space_after, alignment=align)

BODY   = S("body", "Lato", 10, 15.8, INK2)
BODYM  = S("bodym", "Lato", 9.5, 14.5, MUTE)
LEAD   = S("lead", "LatoL", 13.5, 20.5, INK)
CARD_B = S("cardb", "Lato", 9, 13.6, INK2)
CARD_M = S("cardm", "Lato", 8.6, 12.8, MUTE)

def tracked(c, x, y, text, font="PopM", size=8, color=ACCENT, track=1.8):
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(track)
    t.textOut(text)
    t.setCharSpace(0)  # reset Tc so spacing never leaks into later text
    c.drawText(t)

def tracked_w(text, font="PopM", size=8, track=1.8):
    return pdfmetrics.stringWidth(text, font, size) + track * max(0, len(text) - 1)

def para(c, text, x, y_top, w, style):
    """Draw paragraph with top-left anchor; return height used."""
    p = Paragraph(text, style)
    _, h = p.wrapOn(c, w, PH)
    p.drawOn(c, x, y_top - h)
    return h

def footer(c, page_no, label="THE CRUCIBLE — PRODUCT OVERVIEW"):
    c.setStrokeColor(RULE); c.setLineWidth(0.7)
    c.line(M, 46, PW - M, 46)
    tracked(c, M, 34, label, font="Pop", size=6.3, color=FAINT, track=1.6)
    c.setFont("Pop", 7.5); c.setFillColor(MUTE)
    c.drawRightString(PW - M, 33.5, f"{page_no:02d}")

def section_head(c, num, title, kicker=None, y=PH - 92):
    tracked(c, M, y, num, font="PopM", size=9, color=ACCENT, track=2.2)
    c.setStrokeColor(ACCENT); c.setLineWidth(1.4)
    nw = tracked_w(num, "PopM", 9, 2.2)
    c.line(M + nw + 12, y + 3, M + nw + 44, y + 3)
    c.setFont("PopL", 27); c.setFillColor(INK)
    c.drawString(M, y - 36, title)
    yy = y - 52
    if kicker:
        c.setFont("LatoI", 10.5); c.setFillColor(MUTE)
        c.drawString(M, yy, kicker)
        yy -= 14
    return yy - 12  # content start y

def rrect(c, x, y, w, h, r=8, fill=None, stroke=None, lw=0.9, dash=None):
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    if dash: c.setDash(*dash)
    c.roundRect(x, y, w, h, r, stroke=1 if stroke else 0, fill=1 if fill else 0)
    if dash: c.setDash()

def arrow(c, x1, y1, x2, y2, color=FAINT, lw=1.1, head=4.5):
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(lw)
    ang = math.atan2(y2 - y1, x2 - x1)
    xe, ye = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    c.line(x1, y1, xe, ye)
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(x2 - head * 1.9 * math.cos(ang - 0.42), y2 - head * 1.9 * math.sin(ang - 0.42))
    p.lineTo(x2 - head * 1.9 * math.cos(ang + 0.42), y2 - head * 1.9 * math.sin(ang + 0.42))
    p.close()
    c.drawPath(p, stroke=0, fill=1)

def chip(c, x, y, text, fill=ACC_P, tcolor=ACC_D, font="PopM", size=7.2, pad=7, h=15):
    w = pdfmetrics.stringWidth(text, font, size) + 2 * pad
    rrect(c, x, y, w, h, r=h / 2, fill=fill)
    c.setFont(font, size); c.setFillColor(tcolor)
    c.drawString(x + pad, y + (h - size) / 2 + 0.8, text)
    return w

def diamond(c, cx, cy, r, fill=ACCENT):
    p = c.beginPath()
    p.moveTo(cx, cy + r); p.lineTo(cx + r, cy); p.lineTo(cx, cy - r); p.lineTo(cx - r, cy)
    p.close()
    c.setFillColor(fill)
    c.drawPath(p, stroke=0, fill=1)

# =====================================================================
# PAGES — each fn: fn(c, pageno, toc) ; returns TOC entries it owns
# =====================================================================
PAGES = []
def page(fn):
    PAGES.append(fn)
    return fn

TOC_SECTIONS = []  # (num, title, pageno) filled on pass 1

def mark_toc(num, title, pageno, toc_pass):
    if toc_pass == 1:
        TOC_SECTIONS.append((num, title, pageno))

# ---------- 1 · COVER ----------
@page
def cover(c, pn, tp):
    c.setFillColor(PAPER); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    # faint accent geometry, bottom-right (pale fills; alpha unsupported)
    c.setFillColor(HexColor("#FDF6EF"))
    c.circle(PW - 60, 90, 320, stroke=0, fill=1)
    c.setFillColor(HexColor("#FBEDE1"))
    c.circle(PW - 60, 90, 220, stroke=0, fill=1)
    # top mark
    diamond(c, M + 7, PH - 72, 7)
    tracked(c, M + 26, PH - 76, "THE CRUCIBLE", font="PopM", size=9, color=INK, track=2.6)
    # center block
    yc = PH * 0.560
    c.setStrokeColor(ACCENT); c.setLineWidth(2)
    c.line(M, yc + 118, M + 40, yc + 118)
    tracked(c, M, yc + 96, "PRODUCT OVERVIEW · JULY 2026", font="PopM", size=8.5, color=ACCENT, track=2.4)
    c.setFont("PopL", 58); c.setFillColor(INK)
    c.drawString(M - 3, yc + 30, "The Crucible")
    c.setFont("PopL", 19); c.setFillColor(MUTE)
    c.drawString(M, yc - 8, "The AI Knowledge Operating System")
    c.setFont("LatoL", 11.5); c.setFillColor(INK2)
    c.drawString(M, yc - 46, "Transforming disconnected AI conversations into reusable,")
    c.drawString(M, yc - 62, "compounding intelligence.")
    # bottom contact
    c.setStrokeColor(RULE); c.setLineWidth(0.8)
    c.line(M, 108, PW - M, 108)
    c.setFont("PopM", 9); c.setFillColor(INK)
    c.drawString(M, 88, "Austin Brower")
    c.setFont("Lato", 9); c.setFillColor(MUTE)
    c.drawString(M, 74, "austinbrower94@outlook.com")
    c.setFont("LatoI", 9); c.setFillColor(FAINT)
    c.drawRightString(PW - M, 74, "Confidential — prepared for partners, investors, and collaborators")

# ---------- 2 · EPIGRAPH ----------
@page
def epigraph(c, pn, tp):
    c.setFillColor(DARK); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(HexColor("#251C15"))
    c.circle(90, PH - 80, 260, stroke=0, fill=1)
    diamond(c, M + 6, PH * 0.66 + 62, 6)
    c.setFont("PopL", 26); c.setFillColor(WHITE)
    y = PH * 0.66
    for line in ["We aren't building another", "AI assistant."]:
        c.drawString(M, y, line); y -= 38
    y -= 16
    c.setFont("PopL", 26); c.setFillColor(HexColor("#F0A26B"))
    for line in ["We're building the operating system", "AI should have had from", "the beginning."]:
        c.drawString(M, y, line); y -= 38
    c.setStrokeColor(HexColor("#4A3A2C")); c.setLineWidth(0.8)
    c.line(M, 120, PW - M, 120)
    tracked(c, M, 100, "THE CRUCIBLE · PRODUCT OVERVIEW", font="Pop", size=7, color=HexColor("#8A7A6B"), track=2.2)
    c.setFont("Pop", 7.5); c.setFillColor(HexColor("#8A7A6B"))
    c.drawRightString(PW - M, 100, f"{pn:02d}")

# ---------- 3 · CONTENTS ----------
@page
def contents(c, pn, tp):
    tracked(c, M, PH - 92, "CONTENTS", font="PopM", size=9, color=ACCENT, track=2.2)
    c.setFont("PopL", 27); c.setFillColor(INK)
    c.drawString(M, PH - 128, "What's inside")
    entries = TOC_SECTIONS if tp == 2 else []
    col_w = (CW - 30) / 2
    x = M; y0 = PH - 175; y = y0; line_h = 25.4
    half = math.ceil(len(entries) / 2) if entries else 11
    for i, (num, title, p) in enumerate(entries):
        if i == half:
            x = M + col_w + 30; y = y0
        c.setFont("PopM", 8); c.setFillColor(ACCENT)
        c.drawString(x, y, num)
        c.setFont("Lato", 9.6); c.setFillColor(INK2)
        c.drawString(x + 24, y, title)
        c.setFont("Lato", 9); c.setFillColor(FAINT)
        c.drawRightString(x + col_w, y, f"{p:02d}")
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(x, y - 7.5, x + col_w, y - 7.5)
        y -= line_h
    footer(c, pn)

# ---------- 4 · EXEC SUMMARY (narrative) ----------
@page
def exec1(c, pn, tp):
    mark_toc("01", "Executive Summary", pn, tp)
    y = section_head(c, "01", "Executive Summary")
    y -= para(c, "Every day, millions of people have brilliant conversations with AI — and then throw them away.", M, y, CW, LEAD) + 14
    y -= para(c,
        "A founder refines a positioning strategy across forty messages. A developer debugs an architecture "
        "across three sessions. A researcher synthesizes a literature review over a week of prompting. The next "
        "morning, all of it is gone. The context, the corrections, the hard-won understanding — reset to zero. "
        "<b>The most expensive part of working with AI isn't the tokens. It's the repetition.</b>", M, y, CW, BODY) + 12
    y -= para(c,
        "<b>The Crucible is an AI Knowledge Operating System.</b> It sits between people and the models they use, "
        "and it does the one thing no assistant does: it remembers, organizes, and compounds. Conversations become "
        "structured knowledge. Knowledge becomes reusable context. Context becomes leverage — so every session "
        "starts smarter than the last one ended.", M, y, CW, BODY) + 12
    y -= para(c,
        "The platform is built around a simple conviction: <b>AI conversations are a byproduct. Knowledge is the "
        "asset.</b> Today's tools optimize the conversation. The Crucible optimizes what survives it.", M, y, CW, BODY) + 12
    y -= para(c,
        "The Crucible is local-first, model-agnostic, and designed for people who use AI seriously — developers, "
        "researchers, agencies, founders, and the enterprises they work inside. It is currently in active "
        "development: architecture complete, desktop prototype functional, moving toward MVP.", M, y, CW, BODY) + 26
    # takeaway cards
    tracked(c, M, y, "WHAT TO TAKE AWAY", font="PopM", size=8, color=ACCENT, track=2)
    y -= 14
    cards = [
        ("Stateless is the problem", "AI workflows reset by design — taxing every user in tokens, time, and lost context."),
        ("The fix is a layer", "Not a better chatbot: an OS layer of persistent knowledge, visual organization, composable context."),
        ("The Crucible is that layer", "Forge, Core, Barrage, Siege, Aether — built around a persistent knowledge system: the Brain."),
    ]
    ch = 104; gap = 12; cw = (CW - 2 * gap) / 3
    for i, (t, b) in enumerate(cards):
        x = M + i * (cw + gap)
        rrect(c, x, y - ch, cw, ch, r=9, fill=WARM, stroke=RULE, lw=0.8)
        c.setStrokeColor(ACCENT); c.setLineWidth(2)
        c.line(x + 14, y - 18, x + 34, y - 18)
        c.setFont("PopM", 8.8); c.setFillColor(INK)
        c.drawString(x + 14, y - 34, t)
        para(c, b, x + 14, y - 44, cw - 28, CARD_M)
    footer(c, pn)

# ---------- 5 · PROBLEM p1 ----------
@page
def problem1(c, pn, tp):
    mark_toc("02", "The Problem", pn, tp)
    y = section_head(c, "02", "The Problem", "AI is brilliant. AI workflows are broken.")
    y -= para(c,
        "The models got remarkable. The workflow around them didn't. Anyone who uses AI daily recognizes "
        "five failure modes — and pays for them, in attention and in tokens, every single day.",
        M, y, CW, LEAD) + 22
    items = [
        ("01", "Groundhog Day prompting",
         "Every session starts from zero. You re-explain your project, your stack, your client, your preferences — again. "
         "For power users, a large share of prompt volume is re-establishing context the model already had yesterday."),
        ("02", "Lost context",
         "The best answer you ever got is buried in a conversation you can't find, from three weeks ago. Conversations "
         "are append-only logs: nothing is extracted, indexed, or connected."),
        ("03", "Disconnected conversations",
         "Your ChatGPT history doesn't know about your Claude history. Your work in Cursor doesn't know about either. "
         "Each tool is an island; intelligence built in one place is invisible everywhere else."),
        ("04", "Duplicated work",
         "Teams are worse off than individuals: five people independently prompt their way to the same answer, five "
         "times, at five times the cost. One person's AI work never becomes the team's knowledge."),
        ("05", "Token waste",
         "Re-sent context is the dominant cost of serious AI usage — long system prompts, re-pasted documents, "
         "re-explained constraints. Stateless workflows don't just cost attention. They cost money, linearly, forever."),
    ]
    for num, t, b in items:
        c.setFont("PopB", 15); c.setFillColor(ACC_P)
        c.drawString(M, y - 16, num)
        c.setFont("PopM", 11); c.setFillColor(INK)
        c.drawString(M + 34, y - 12, t)
        h = para(c, b, M + 34, y - 20, CW - 34, BODYM)
        y -= h + 40
    footer(c, pn)

# ---------- 6 · PROBLEM p2 (pattern underneath) ----------
@page
def problem2(c, pn, tp):
    y = PH - 100
    tracked(c, M, y, "02 · THE PROBLEM, CONTINUED", font="PopM", size=8, color=ACCENT, track=2)
    c.setFont("PopL", 22); c.setFillColor(INK)
    c.drawString(M, y - 32, "The pattern underneath")
    y -= 62
    y -= para(c,
        "All five failures share one root cause: <b>today's AI tools treat the conversation as the unit of work.</b> "
        "When the conversation ends, the work evaporates. There is no layer whose job is to catch what was learned, "
        "structure it, and hand it back.", M, y, CW, BODY) + 22
    # visual: evaporation vs accumulation
    bx, bw, bh = M, CW, 210
    rrect(c, bx, y - bh, bw, bh, r=10, fill=WARM, stroke=RULE, lw=0.8)
    half = bw / 2
    cx1 = bx + half / 2; cx2 = bx + half + half / 2
    top = y - 26
    tracked(c, cx1 - tracked_w("TODAY", "PopM", 7.5, 2) / 2, top, "TODAY", font="PopM", size=7.5, color=MUTE, track=2)
    tracked(c, cx2 - tracked_w("WITH THE CRUCIBLE", "PopM", 7.5, 2) / 2, top, "WITH THE CRUCIBLE", font="PopM", size=7.5, color=ACC_D, track=2)
    # left: bars that reset
    base = y - bh + 46
    for i in range(5):
        h = 26
        x = cx1 - 62 + i * 26
        c.setFillColor(HexColor("#DED5C9"))
        c.rect(x, base, 14, h, stroke=0, fill=1)
        c.setFont("Lato", 6.5); c.setFillColor(FAINT)
        c.drawCentredString(x + 7, base - 10, f"s{i+1}")
    c.setFont("LatoI", 8.5); c.setFillColor(MUTE)
    c.drawCentredString(cx1, y - bh + 16, "every session resets to zero")
    # right: compounding bars
    for i in range(5):
        h = 16 + i * 13
        x = cx2 - 62 + i * 26
        c.setFillColor(ACCENT if i == 4 else HexColor("#F2A276"))
        c.rect(x, base, 14, h, stroke=0, fill=1)
        c.setFont("Lato", 6.5); c.setFillColor(FAINT)
        c.drawCentredString(x + 7, base - 10, f"s{i+1}")
    c.setFont("LatoI", 8.5); c.setFillColor(ACC_D)
    c.drawCentredString(cx2, y - bh + 16, "every session deposits knowledge")
    c.setStrokeColor(RULE); c.setLineWidth(0.8)
    c.line(bx + half, y - bh + 14, bx + half, y - 14)
    y -= bh + 26
    y -= para(c,
        "Every other domain of computing solved this decades ago. Files persist. Databases persist. Code persists "
        "in version control. Only AI knowledge — arguably the most expensive knowledge we now produce — lives and "
        "dies inside a scrollback buffer.", M, y, CW, BODY) + 18
    rrect(c, M, y - 58, CW, 58, r=9, fill=ACC_PP, stroke=None)
    c.setFillColor(ACCENT); c.rect(M, y - 58, 3, 58, stroke=0, fill=1)
    para(c, "<b>The opportunity is not a smarter model. It is the missing layer between people and every model "
            "they'll ever use — the layer where knowledge survives.</b>", M + 18, y - 12, CW - 36, BODY)
    footer(c, pn)

# ---------- 7 · VISION ----------
@page
def vision(c, pn, tp):
    mark_toc("03", "The Vision", pn, tp)
    y = section_head(c, "03", "The Vision", "What is an AI Knowledge Operating System?")
    y -= para(c,
        "An operating system's job is to manage a scarce resource so applications don't have to. Classic operating "
        "systems manage compute, memory, and storage. <b>An AI Knowledge Operating System manages context</b> — "
        "the scarcest and most expensive resource of the AI era.", M, y, CW, LEAD) + 24
    tracked(c, M, y, "THE FOUR FUNCTIONS OF A KNOWLEDGE OS", font="PopM", size=8, color=ACCENT, track=2)
    y -= 16
    fns = [
        ("Persistence", "Nothing valuable is lost when a session ends. Insights, decisions, drafts, and corrections are captured into a durable knowledge system."),
        ("Organization", "Knowledge is structured — connected into a living graph of projects, clients, concepts, and relationships — rather than piled in chat logs."),
        ("Allocation", "The right knowledge is assembled into context at the right moment, so models receive what they need and nothing they don't."),
        ("Abstraction", "Models, tools, and providers become interchangeable resources underneath a stable layer the user actually lives in."),
    ]
    ch = 96; gap = 12; cw = (CW - gap) / 2
    for i, (t, b) in enumerate(fns):
        x = M + (i % 2) * (cw + gap)
        yy = y - (i // 2) * (ch + gap)
        rrect(c, x, yy - ch, cw, ch, r=9, fill=PAPER, stroke=RULE, lw=0.9)
        c.setFont("PopB", 20); c.setFillColor(ACC_P)
        c.drawString(x + 16, yy - 30, f"{i+1:02d}")
        c.setFont("PopM", 11); c.setFillColor(INK)
        c.drawString(x + 46, yy - 26, t)
        para(c, b, x + 16, yy - 42, cw - 32, CARD_B)
    y -= 2 * ch + gap + 26
    y -= para(c,
        "The result inverts the current experience of AI. Instead of every conversation starting at zero, "
        "<b>every conversation starts at everything you've learned so far.</b> Intelligence stops resetting "
        "and starts compounding — like interest.", M, y, CW, BODY) + 20
    rrect(c, M, y - 64, CW, 64, r=9, fill=DARK)
    c.setFont("PopL", 12.5); c.setFillColor(WHITE)
    c.drawString(M + 22, y - 28, "ChatGPT made AI conversational. Cursor made AI ambient in code.")
    c.setFont("PopM", 12.5); c.setFillColor(HexColor("#F0A26B"))
    c.drawString(M + 22, y - 47, "The Crucible makes AI cumulative.")
    footer(c, pn)

# ---------- 8 · WHY NOW ----------
@page
def whynow(c, pn, tp):
    mark_toc("04", "Why Now", pn, tp)
    y = section_head(c, "04", "Why Now", "Three curves are crossing — their intersection is this product.")
    rows = [
        ("Context windows grew faster than context management",
         "Models can hold hundreds of thousands of tokens — but users have no disciplined way to decide what belongs "
         "in the window. Bigger windows made the organization problem worse: the temptation is to paste everything, "
         "pay for everything, and attend to nothing."),
        ("AI spend became a real budget line",
         "When AI was a curiosity, waste was invisible. Now individuals carry multiple subscriptions and enterprises "
         "negotiate seven-figure model contracts. Token efficiency is a procurement question — and a layer that "
         "systematically removes redundant context pays for itself."),
        ("Work fragmented across models",
         "Nobody serious uses one model anymore: Claude for reasoning and writing, small models for speed, local "
         "models for privacy, specialized models for code. Multi-model reality demands a home above any single "
         "provider — exactly the position an operating system occupies."),
    ]
    for i, (t, b) in enumerate(rows):
        c.setFillColor(ACCENT)
        c.circle(M + 8, y - 10, 3.2, stroke=0, fill=1)
        if i < 2:
            c.setStrokeColor(RULE); c.setLineWidth(1)
            c.line(M + 8, y - 18, M + 8, y - 104)
        c.setFont("PopM", 12); c.setFillColor(INK)
        c.drawString(M + 26, y - 14, t)
        h = para(c, b, M + 26, y - 24, CW - 26, BODY)
        y -= h + 52
    y -= 4
    rrect(c, M, y - 88, CW, 88, r=9, fill=WARM, stroke=RULE, lw=0.8)
    tracked(c, M + 18, y - 22, "THE QUIETER SHIFT", font="PopM", size=7.5, color=ACC_D, track=2)
    para(c,
        "People have started to feel <b>ownership</b> over their AI work. Prompts get refined like code; conversations "
        "get saved and screenshotted. Users already know they're producing something valuable — they just have nowhere "
        "to keep it. The Crucible gives that instinct infrastructure.", M + 18, y - 32, CW - 36, CARD_B)
    footer(c, pn)

# ---------- 9 · PHILOSOPHY ----------
@page
def philosophy(c, pn, tp):
    mark_toc("05", "Product Philosophy", pn, tp)
    y = section_head(c, "05", "Product Philosophy", "Five principles govern every design decision in the platform.")
    prin = [
        ("Local-first",
         "Your knowledge lives on your machine, in formats you can open, in a system you control. The cloud is for "
         "sync and collaboration — a convenience, never a hostage-taker. If The Crucible disappeared tomorrow, your "
         "knowledge would still be yours, readable, and intact."),
        ("Composable context",
         "Context is built from parts — a project brief, a client profile, a set of constraints, a preferred voice. "
         "Like software components, these are written once, versioned, and assembled on demand. Prompting stops "
         "being typing and starts being composition."),
        ("Reusable intelligence",
         "Anything worth doing twice is worth capturing once. Workflows, prompts, skills, and solutions are "
         "first-class objects that can be invoked, shared, and improved — not folklore trapped in one person's "
         "chat history."),
        ("Knowledge compounding",
         "Value grows superlinearly with use. Each captured insight makes the graph denser; each connection makes "
         "retrieval sharper; each session deposits more than it withdraws. Day 100 should feel categorically "
         "different from day 1."),
        ("Human ownership",
         "The user is the editor-in-chief of their own intelligence. The system proposes — organizing, connecting, "
         "suggesting — but the human disposes. No black-box memory: everything the Brain knows is inspectable, "
         "correctable, and deletable."),
    ]
    for i, (t, b) in enumerate(prin):
        c.setFont("PopB", 26); c.setFillColor(ACC_P)
        c.drawString(M, y - 24, f"{i+1:02d}")
        c.setFont("PopM", 12.5); c.setFillColor(INK)
        c.drawString(M + 52, y - 16, t)
        h = para(c, b, M + 52, y - 26, CW - 52, BODYM)
        y -= max(h + 26, 60) + 24
    footer(c, pn)

# ---------- 10 · PLATFORM OVERVIEW ----------
@page
def platform(c, pn, tp):
    mark_toc("06", "Platform Overview", pn, tp)
    y = section_head(c, "06", "Platform Overview", "Six coordinated components. Each has one job.")
    comps = [
        ("The Crucible", "The platform", "The whole system: where raw conversations are transformed into durable intelligence."),
        ("Core", "Shared runtime", "The engine underneath everything — state, sync, and the shared services every surface depends on."),
        ("Forge", "Desktop workspace", "Where the work happens: a local-first workspace for conversing, building, and organizing."),
        ("Forge Brain", "Visual intelligence layer", "The visible, navigable map of everything you know — live inside Forge."),
        ("Barrage", "Cloud platform", "Sync, collaboration, and shared knowledge across devices and teams."),
        ("Siege", "Integration platform", "The bridge to everything else — tools, data sources, and services that feed and consume knowledge."),
        ("Aether", "Intelligence layer", "The ambient intelligence that organizes, connects, and improves knowledge over time."),
    ]
    row_h = 52
    for i, (name, role, desc) in enumerate(comps):
        if i > 0:
            c.setStrokeColor(RULE); c.setLineWidth(0.6)
            c.line(M, y + 8, PW - M, y + 8)
        c.setFont("PopM", 11.5); c.setFillColor(INK)
        c.drawString(M, y - 8, name)
        tracked(c, M, y - 22, role.upper(), font="Pop", size=6.4, color=ACC_D, track=1.4)
        para(c, desc, M + 150, y - 1, CW - 150, CARD_B)
        y -= row_h
    y -= 6
    y -= para(c,
        "<b>How they fit together:</b> Forge is the surface you touch. Core is the engine it runs on. Aether is the "
        "intelligence that works the knowledge while you work. Siege brings the outside world in. Barrage extends "
        "everything across devices and teammates. And The Crucible is the name for what they add up to: a place "
        "where raw material goes in and refined intelligence comes out — which is, of course, what a crucible is for.",
        M, y, CW, BODY)
    footer(c, pn)

# ---------- 11 · ECOSYSTEM DIAGRAM ----------
@page
def ecosystem(c, pn, tp):
    y = PH - 100
    tracked(c, M, y, "06 · PLATFORM OVERVIEW", font="PopM", size=8, color=ACCENT, track=2)
    c.setFont("PopL", 22); c.setFillColor(INK)
    c.drawString(M, y - 32, "The ecosystem, in one view")
    top = y - 70
    # The Crucible bar
    rrect(c, M, top - 54, CW, 54, r=10, fill=DARK)
    c.setFont("PopM", 13); c.setFillColor(WHITE)
    c.drawString(M + 20, top - 26, "The Crucible")
    c.setFont("LatoI", 9.5); c.setFillColor(HexColor("#C9B8A8"))
    c.drawRightString(PW - M - 20, top - 26, "AI Knowledge Operating System")
    c.setFont("Lato", 8); c.setFillColor(HexColor("#9A8A7A"))
    c.drawString(M + 20, top - 42, "the platform — everything below adds up to this")
    # connectors down
    yA = top - 54
    row_y = yA - 36
    bw3 = (CW - 2 * 16) / 3
    labels = [("Forge", "desktop workspace", True), ("Barrage", "cloud platform", False), ("Siege", "integration platform", False)]
    bh = 96
    for i, (name, sub, has_brain) in enumerate(labels):
        x = M + i * (bw3 + 16)
        arrow(c, x + bw3 / 2, yA - 4, x + bw3 / 2, row_y + 3, color=FAINT, lw=1)
        rrect(c, x, row_y - bh, bw3, bh, r=9, fill=PAPER, stroke=RULE, lw=1)
        c.setFillColor(ACCENT); c.rect(x, row_y - 3.5, bw3, 3.5, stroke=0, fill=1)
        c.setFont("PopM", 11.5); c.setFillColor(INK)
        c.drawString(x + 14, row_y - 24, name)
        c.setFont("Lato", 8); c.setFillColor(MUTE)
        c.drawString(x + 14, row_y - 37, sub)
        if has_brain:
            chip(c, x + 14, row_y - bh + 14, "Forge Brain · visual layer", fill=ACC_P, tcolor=ACC_D)
        elif i == 1:
            chip(c, x + 14, row_y - bh + 14, "sync · teams · sharing", fill=WARM, tcolor=MUTE)
        else:
            chip(c, x + 14, row_y - bh + 14, "tools · data · services", fill=WARM, tcolor=MUTE)
    # Aether band
    band_y = row_y - bh - 34
    for i in range(3):
        x = M + i * (bw3 + 16)
        arrow(c, x + bw3 / 2, row_y - bh - 4, x + bw3 / 2, band_y + 3, color=FAINT, lw=1)
    rrect(c, M, band_y - 46, CW, 46, r=9, fill=ACC_PP, stroke=ACCENT, lw=0.9, dash=(3, 2.4))
    c.setFont("PopM", 11); c.setFillColor(ACC_D)
    c.drawString(M + 18, band_y - 22, "Aether")
    c.setFont("LatoI", 9); c.setFillColor(ACC_D)
    c.drawString(M + 78, band_y - 22, "intelligence layer — organizes, connects, and improves knowledge over time")
    c.setFont("Lato", 8); c.setFillColor(HexColor("#C07B4E"))
    c.drawString(M + 18, band_y - 36, "ambient: works across every surface, continuously")
    # Core bar
    core_y = band_y - 46 - 34
    arrow(c, PW / 2, band_y - 50, PW / 2, core_y + 3, color=FAINT, lw=1)
    rrect(c, M, core_y - 52, CW, 52, r=9, fill=WARM, stroke=RULE, lw=1)
    c.setFont("PopM", 11.5); c.setFillColor(INK)
    c.drawString(M + 18, core_y - 24, "Core")
    c.setFont("LatoI", 9); c.setFillColor(MUTE)
    c.drawString(M + 62, core_y - 24, "shared runtime and intelligence engine — state, sync, services")
    c.setFont("Lato", 8); c.setFillColor(FAINT)
    c.drawString(M + 18, core_y - 39, "one runtime, many surfaces: every component above is a client of Core")
    # models chips
    my = core_y - 52 - 30
    arrow(c, PW / 2, core_y - 56, PW / 2, my + 18, color=FAINT, lw=1)
    tracked(c, M, my, "MODELS AS RESOURCES", font="PopM", size=7, color=MUTE, track=1.8)
    xx = M + 128
    for t in ["Claude", "local models", "specialized", "what's next"]:
        xx += chip(c, xx, my - 4, t, fill=PAPER, tcolor=INK2) + 8
    footer(c, pn)

# ---------- 12 · FORGE BRAIN ----------
@page
def forgebrain(c, pn, tp):
    mark_toc("07", "Forge Brain", pn, tp)
    y = section_head(c, "07", "Forge Brain", "Your knowledge, made visible.")
    y -= para(c,
        "Most knowledge tools are filing cabinets: you put things in folders and hope you remember the folder. "
        "Forge Brain is different in kind — a <b>visual intelligence layer</b>: a spatial, navigable rendering of "
        "your knowledge graph, live inside your workspace.", M, y, CW, LEAD) + 20
    feats = [
        ("You can see what you know",
         "Projects, clients, concepts, files, and conversations appear as a connected landscape. Clusters form around "
         "what you work on most. Bridges appear between domains you didn't realize were related."),
        ("You can steer with it",
         "Selecting a region of the Brain scopes your next conversation to that knowledge. Focus a client's cluster, "
         "and every model you talk to inherits that context — automatically, precisely, without pasting anything."),
        ("It grows as you work",
         "There is no filing step. As you converse and build, the Brain quietly acquires new material, proposes where "
         "it belongs, and strengthens the connections it touched. The Brain Gardener keeps it healthy over time."),
    ]
    for t, b in feats:
        diamond(c, M + 5, y - 9, 4)
        c.setFont("PopM", 11); c.setFillColor(INK)
        c.drawString(M + 20, y - 12, t)
        h = para(c, b, M + 20, y - 20, CW - 20, BODYM)
        y -= h + 40
    y -= 2
    rrect(c, M, y - 58, CW, 58, r=9, fill=ACC_PP)
    c.setFillColor(ACCENT); c.rect(M, y - 58, 3, 58, stroke=0, fill=1)
    para(c, "<b>Memory you can navigate beats memory you have to query.</b> When knowledge has a shape, you develop "
            "intuition about it — the way you know your own neighborhood better than any map service does.",
         M + 18, y - 13, CW - 36, BODY)
    footer(c, pn)

# ---------- 13 · BRAIN MAP ILLUSTRATION ----------
@page
def brainmap(c, pn, tp):
    y = PH - 100
    tracked(c, M, y, "07 · FORGE BRAIN", font="PopM", size=8, color=ACCENT, track=2)
    c.setFont("PopL", 22); c.setFillColor(INK)
    c.drawString(M, y - 32, "What a Brain looks like")
    c.setFont("LatoI", 10); c.setFillColor(MUTE)
    c.drawString(M, y - 50, "Conceptual rendering — clusters of knowledge, connected across domains.")
    top = y - 74
    bh = 430
    rrect(c, M, top - bh, CW, bh, r=12, fill=HexColor("#FBF8F4"), stroke=RULE, lw=1)
    # deterministic node layout: three clusters + bridges
    import random
    rnd = random.Random(7)
    clusters = [
        ("CLIENT · NORTHWIND", M + 120, top - 120, ACCENT, 9),
        ("PRODUCT · ATLAS", M + 350, top - 170, HexColor("#C77B45"), 8),
        ("RESEARCH · RETRIEVAL", M + 180, top - 320, HexColor("#8A6A4F"), 8),
    ]
    all_nodes = []
    for label, cx, cy, col, n in clusters:
        nodes = []
        for i in range(n):
            a = rnd.uniform(0, 6.283); r = rnd.uniform(16, 62)
            nodes.append((cx + r * math.cos(a), cy + r * 0.72 * math.sin(a), rnd.uniform(2.2, 5.4)))
        nodes.append((cx, cy, 7.5))
        # edges within cluster
        c.setStrokeColor(HexColor("#E3D8CA")); c.setLineWidth(0.7)
        for i in range(len(nodes)):
            x1, y1, _ = nodes[i]
            x2, y2, _ = nodes[(i * 3 + 1) % len(nodes)]
            c.line(x1, y1, x2, y2)
            x2, y2, _ = nodes[-1]
            c.line(x1, y1, x2, y2)
        for (nx, ny, nr) in nodes[:-1]:
            c.setFillColor(HexColor("#D9CBB9"))
            c.circle(nx, ny, nr, stroke=0, fill=1)
        # hub
        hx, hy, hr = nodes[-1]
        c.setFillColor(ACC_P)
        c.circle(hx, hy, hr + 7, stroke=0, fill=1)
        c.setFillColor(col); c.circle(hx, hy, hr, stroke=0, fill=1)
        tracked(c, hx + 14, hy + 8, label, font="PopM", size=6.8, color=INK2, track=1.4)
        all_nodes.append((hx, hy))
    # bridges between clusters (the interesting part)
    c.setStrokeColor(ACCENT); c.setLineWidth(1.1); c.setDash(4, 3)
    for i in range(len(all_nodes)):
        for j in range(i + 1, len(all_nodes)):
            x1, y1 = all_nodes[i]; x2, y2 = all_nodes[j]
            c.line(x1, y1, x2, y2)
    c.setDash()
    # bridge label
    mx = (all_nodes[0][0] + all_nodes[2][0]) / 2 + 96
    myy = (all_nodes[0][1] + all_nodes[2][1]) / 2
    rrect(c, mx, myy - 10, 170, 22, r=11, fill=PAPER, stroke=ACCENT, lw=0.8)
    c.setFont("LatoI", 7.8); c.setFillColor(ACC_D)
    c.drawString(mx + 10, myy - 2.5, "bridge: a connection you didn't file")
    # legend
    ly = top - bh + 24
    c.setFillColor(HexColor("#D9CBB9")); c.circle(M + 26, ly + 3, 3.4, stroke=0, fill=1)
    c.setFont("Lato", 8); c.setFillColor(MUTE); c.drawString(M + 36, ly, "memory / file / decision")
    c.setFillColor(ACCENT); c.circle(M + 176, ly + 3, 5, stroke=0, fill=1)
    c.drawString(M + 186, ly, "project or client hub")
    c.setStrokeColor(ACCENT); c.setDash(4, 3); c.setLineWidth(1.1)
    c.line(M + 306, ly + 3, M + 336, ly + 3); c.setDash()
    c.drawString(M + 344, ly, "cross-domain relationship")
    # caption under panel
    para(c, "Selecting any region scopes your next conversation to exactly that knowledge — context without pasting.",
         M, top - bh - 12, CW, S("cap", "LatoI", 9, 13, MUTE))
    footer(c, pn)

# ---------- 14 · KNOWLEDGE GRAPH ----------
@page
def kgraph(c, pn, tp):
    mark_toc("08", "The Knowledge Graph", pn, tp)
    y = section_head(c, "08", "The Knowledge Graph", "The data structure underneath the experience.")
    y -= para(c,
        "At the center of the Brain is a knowledge graph: a network of <b>entities</b> and <b>relationships</b> "
        "rather than a pile of documents. Conceptually, it represents:", M, y, CW, LEAD) + 18
    ents = [
        ("Memories", "Durable facts, decisions, and insights extracted from your work. “Client X prefers understated copy.” “We chose PostgreSQL in March, because…”"),
        ("Relationships", "The connections that make memories useful: this decision affects that project; this prompt works well with that model; this file supersedes that one."),
        ("Context", "Assembled views over the graph — the working set for a task, composed on demand from relevant memories, files, and constraints."),
        ("Projects & Clients", "Organizing anchors that mirror how work is actually structured, so knowledge lands where you think."),
        ("Workflows · Prompts · Skills · Models · Files", "The operational objects of AI work — versioned, and connected to the knowledge they operate on."),
    ]
    for t, b in ents:
        c.setFillColor(ACCENT); c.circle(M + 4, y - 8, 2.6, stroke=0, fill=1)
        c.setFont("PopM", 10.5); c.setFillColor(INK)
        c.drawString(M + 16, y - 11, t)
        h = para(c, b, M + 16, y - 18, CW - 16, CARD_M)
        y -= h + 34
    y -= 4
    y -= para(c,
        "<b>Why a graph and not folders?</b> Because knowledge doesn't live in one place. A pricing decision belongs "
        "simultaneously to a client, a project, a strategy discussion, and a spreadsheet. Folders force one home; "
        "the graph allows many. Retrieval stops depending on remembering <i>where</i> you put something and starts "
        "depending on anything you remember <i>about</i> it.", M, y, CW, BODY) + 14
    y -= para(c,
        "The graph is a representation, not a cage: everything remains exportable as ordinary, human-readable "
        "artifacts. <i>(Storage, retrieval, and ranking internals are proprietary and out of scope for this "
        "document.)</i>", M, y, CW, BODYM)
    footer(c, pn)

# ---------- 15 · KNOWLEDGE FLOW ----------
@page
def kflow(c, pn, tp):
    mark_toc("09", "Knowledge Flow", pn, tp)
    y = section_head(c, "09", "Knowledge Flow", "How work becomes reusable intelligence. This loop is the product.")
    # loop diagram
    steps = [("Work", "converse · build · decide"), ("Capture", "ambient, no note-taking"),
             ("Distill", "structure · dedupe · type"), ("Connect", "weave into the graph"),
             ("Reuse", "auto-assembled context")]
    n = len(steps); gap = 14
    bw = (CW - (n - 1) * gap) / n; bh = 64
    top = y - 10
    for i, (t, s_) in enumerate(steps):
        x = M + i * (bw + gap)
        last = i == n - 1
        rrect(c, x, top - bh, bw, bh, r=9, fill=(ACC_P if last or i == 0 else PAPER), stroke=(ACCENT if last or i == 0 else RULE), lw=1)
        c.setFont("PopM", 10.5); c.setFillColor(ACC_D if last or i == 0 else INK)
        c.drawCentredString(x + bw / 2, top - 26, t)
        c.setFont("Lato", 6.7); c.setFillColor(MUTE)
        c.drawCentredString(x + bw / 2, top - 40, s_)
        c.setFont("PopB", 8); c.setFillColor(FAINT)
        c.drawString(x + 8, top - 14, f"{i+1}")
        if i < n - 1:
            arrow(c, x + bw + 1, top - bh / 2, x + bw + gap - 1, top - bh / 2, color=ACCENT, lw=1.2)
    # return curve
    c.setStrokeColor(ACCENT); c.setLineWidth(1.2); c.setDash(4, 3)
    yb = top - bh - 16
    c.bezier(M + CW - bw / 2, top - bh - 2, M + CW - bw / 2, yb - 14, M + bw / 2, yb - 14, M + bw / 2, top - bh - 4)
    c.setDash()
    arrow(c, M + bw / 2, yb - 6, M + bw / 2, top - bh - 3, color=ACCENT, lw=1.2)
    c.setFont("LatoI", 8.5); c.setFillColor(ACC_D)
    c.drawCentredString(M + CW / 2, yb - 26, "every session starts smarter than the last one ended")
    y = yb - 48
    # stages explained
    expl = [
        ("1 · Work", "You converse, build, and decide — in Forge, with whatever models fit the task. Nothing about your workflow changes."),
        ("2 · Capture", "Valuable material is identified as you go: decisions, corrections, reusable explanations, finished artifacts. You are never asked to take notes on your own conversation."),
        ("3 · Distill", "Raw captures are refined into structured knowledge — deduplicated, summarized, typed (a decision, a preference, a fact, a workflow) — and stripped of conversational scaffolding."),
        ("4 · Connect", "Distilled knowledge is woven into the graph, linked to the projects, clients, and concepts it concerns. A note becomes a node: findable through every path that touches it."),
        ("5 · Reuse", "When related work begins, relevant knowledge is assembled into context automatically. The loop closes: yesterday's output is today's starting position."),
    ]
    for t, b in expl:
        c.setFont("PopM", 9.5); c.setFillColor(ACC_D)
        c.drawString(M, y - 10, t)
        h = para(c, b, M + 96, y - 1, CW - 96, CARD_B)
        y -= max(h, 22) + 15
    y -= 8
    para(c, "Each pass through the loop leaves the system smarter. Ten loops in, you have a working set. "
            "A thousand loops in, you have an institution.", M, y, CW, S("emph", "LatoI", 10.5, 15, INK2))
    footer(c, pn)

# ---------- 16 · EXPERIENCE ENGINE ----------
@page
def expengine(c, pn, tp):
    mark_toc("10", "The Experience Engine", pn, tp)
    y = section_head(c, "10", "The Experience Engine", "High level — implementation proprietary.")
    y -= para(c,
        "The Experience Engine is the part of the platform that learns <b>how you work</b> — distinct from "
        "<b>what you know.</b>", M, y, CW, LEAD) + 16
    y -= para(c,
        "Over time, it observes the texture of your usage: which prompts you reach for, which model handles which "
        "kind of task, what tone you correct toward, which workflows repeat. From that, it builds an experiential "
        "layer — so the platform doesn't just retrieve your knowledge, it applies your judgment.", M, y, CW, BODY) + 22
    tracked(c, M, y, "WHAT IT FEELS LIKE IN PRACTICE", font="PopM", size=8, color=ACCENT, track=2)
    y -= 14
    items = [
        "Drafts that arrive closer to your voice — before you've corrected anything.",
        "The right model pre-selected for the task at hand.",
        "A workflow suggested because you've run this sequence four times before.",
        "Context that already includes the constraint you always add manually.",
    ]
    ch = 46
    for t in items:
        rrect(c, M, y - ch, CW, ch, r=8, fill=WARM, stroke=RULE, lw=0.7)
        diamond(c, M + 18, y - ch / 2, 3.6)
        para(c, t, M + 34, y - 15, CW - 52, CARD_B)
        y -= ch + 10
    y -= 14
    rrect(c, M, y - 62, CW, 62, r=9, fill=DARK)
    c.setFont("PopL", 12); c.setFillColor(WHITE)
    c.drawString(M + 22, y - 27, "Where the Knowledge Graph is the platform's memory,")
    c.setFont("PopM", 12); c.setFillColor(HexColor("#F0A26B"))
    c.drawString(M + 22, y - 45, "the Experience Engine is its muscle memory.")
    footer(c, pn)

# ---------- 17 · BRAIN ARCHITECTURE ----------
@page
def brainarch(c, pn, tp):
    mark_toc("11", "Brain Architecture", pn, tp)
    y = section_head(c, "11", "Brain Architecture", "Knowledge has natural scopes. The Brain is organized around them.")
    # hierarchy diagram
    top = y - 6
    # Big Brain
    bbw = 250; bbx = M + 20
    bbc = bbx + bbw / 2
    rrect(c, bbx, top - 46, bbw, 46, r=9, fill=DARK)
    c.setFont("PopM", 11.5); c.setFillColor(WHITE)
    c.drawCentredString(bbc, top - 21, "Big Brain")
    c.setFont("Lato", 7.5); c.setFillColor(HexColor("#B9A896"))
    c.drawCentredString(bbc, top - 35, "everything you know — the source of truth")
    # Mini brains
    row_y = top - 46 - 34
    mw = (CW - 2 * 18) / 3; mh = 52
    minis = [("Mini Brain", "client · Northwind"), ("Mini Brain", "product · Atlas"), ("Mini Brain", "research domain")]
    for i, (t, s_) in enumerate(minis):
        x = M + i * (mw + 18)
        arrow(c, bbc + (i - 1) * 55, top - 48, x + mw / 2, row_y + 3, color=FAINT, lw=1)
        rrect(c, x, row_y - mh, mw, mh, r=8, fill=ACC_PP, stroke=ACCENT, lw=0.9)
        c.setFont("PopM", 10); c.setFillColor(ACC_D)
        c.drawCentredString(x + mw / 2, row_y - 22, t)
        c.setFont("Lato", 7.5); c.setFillColor(HexColor("#B06A3A"))
        c.drawCentredString(x + mw / 2, row_y - 36, s_)
    # Baby brains
    by = row_y - mh - 32
    bw2 = mw * 0.8; bh2 = 40
    for i in (0, 1):
        x = M + i * (mw + 18) + (mw - bw2) / 2
        arrow(c, M + i * (mw + 18) + mw / 2, row_y - mh - 3, x + bw2 / 2, by + 3, color=FAINT, lw=1)
        rrect(c, x, by - bh2, bw2, bh2, r=7, fill=PAPER, stroke=RULE, lw=0.9)
        c.setFont("PopM", 9); c.setFillColor(INK)
        c.drawCentredString(x + bw2 / 2, by - 17, "Baby Brain")
        c.setFont("Lato", 7); c.setFillColor(MUTE)
        c.drawCentredString(x + bw2 / 2, by - 29, "task working set")
    # Skills + Gardener chips at right
    sx = M + 2 * (mw + 18) + (mw - bw2) / 2
    rrect(c, sx, by - bh2, bw2, bh2, r=7, fill=WARM, stroke=RULE, lw=0.9)
    c.setFont("PopM", 9); c.setFillColor(INK)
    c.drawCentredString(sx + bw2 / 2, by - 17, "Skills")
    c.setFont("Lato", 7); c.setFillColor(MUTE)
    c.drawCentredString(sx + bw2 / 2, by - 29, "packaged capabilities")
    arrow(c, M + 2 * (mw + 18) + mw / 2, row_y - mh - 3, sx + bw2 / 2, by + 3, color=FAINT, lw=1)
    # Gardener orbit
    gx = M + CW - 14; gy = top - 20
    c.setStrokeColor(ACCENT); c.setLineWidth(0.9); c.setDash(3, 2.4)
    rrect(c, gx - 118, gy - 34, 118, 34, r=8, stroke=ACCENT, dash=(3, 2.4))
    c.setDash()
    c.setFont("PopM", 8.5); c.setFillColor(ACC_D)
    c.drawString(gx - 106, gy - 15, "Brain Gardener")
    c.setFont("Lato", 6.6); c.setFillColor(HexColor("#B06A3A"))
    c.drawString(gx - 106, gy - 26, "merge · prune · strengthen · flag")
    c.setStrokeColor(ACCENT); c.setDash(3, 2.4); c.setLineWidth(0.9)
    c.line(gx - 118, gy - 17, bbx + bbw + 4, top - 23)
    c.setDash()
    y = by - bh2 - 30
    defs = [
        ("Big Brain", "The whole of your knowledge — the complete graph, spanning every project and domain."),
        ("Mini Brains", "Scoped intelligences for a domain: a client, a product, a research area. Each sees everything relevant to its scope and nothing else — precise, fast, cheap to bring into context."),
        ("Baby Brains", "Task-level working sets: the minimal knowledge needed for one job. Spun up quickly, disposed of freely, promoted upward if they prove durable."),
        ("Skills", "Packaged capabilities refined by use — how “we figured this out once” becomes “the platform does this now.”"),
        ("Brain Gardener", "The continuous caretaker: merging duplicates, retiring stale facts, strengthening well-used paths, flagging contradictions for human review. Tending, not just storing."),
    ]
    for t, b in defs:
        c.setFont("PopM", 9.5); c.setFillColor(INK)
        c.drawString(M, y - 10, t)
        h = para(c, b, M + 104, y - 1, CW - 104, CARD_M)
        y -= max(h, 20) + 13
    y -= 6
    para(c, "<b>The rule underneath the hierarchy:</b> context should be as small as possible and as rich as necessary. "
            "Big Brain for breadth, Mini Brain for a domain, Baby Brain for the task at hand.", M, y, CW, BODY)
    footer(c, pn)

# ---------- 18 · BUILDER WORKFLOW ----------
@page
def builder(c, pn, tp):
    mark_toc("12", "The Builder Workflow", pn, tp)
    y = section_head(c, "12", "The Builder Workflow", "A day in the life — Maya, product engineer at an agency.")
    events = [
        ("8:40", "Start where you left off",
         "Maya opens Forge. No re-orientation ritual: the Brain surfaces yesterday's open thread — an API design "
         "discussion for client Northwind, decisions already distilled and pinned."),
        ("9:15", "Context without pasting",
         "She starts a session scoped to the Northwind Mini Brain. The model already knows the stack, the naming "
         "conventions, the client's tone, and the decision log. Her first message is the actual question — not three "
         "paragraphs of setup."),
        ("11:00", "A solved problem stays solved",
         "She hits a rate-limiting problem. The Brain recognizes its shape: a Skill captured from a different client, "
         "eight months ago. Proposed, applied, adapted. Twenty minutes instead of an afternoon."),
        ("14:30", "Work becomes assets",
         "She finishes a migration plan. Without ceremony, its key decisions join the graph, the prompt sequence that "
         "produced it is captured as a reusable workflow, and the artifact is linked to project and client."),
        ("16:45", "The team inherits it",
         "Through Barrage, the Northwind Mini Brain syncs to her teammate in another timezone — who starts his "
         "session with everything Maya's day produced, instead of a Slack message asking for context."),
    ]
    spine_x = M + 34
    for i, (tm, t, b) in enumerate(events):
        c.setFont("PopB", 10); c.setFillColor(ACCENT)
        c.drawRightString(spine_x - 12, y - 12, tm)
        c.setFillColor(ACCENT); c.circle(spine_x, y - 9, 3, stroke=0, fill=1)
        c.setFont("PopM", 10.5); c.setFillColor(INK)
        c.drawString(spine_x + 16, y - 12, t)
        h = para(c, b, spine_x + 16, y - 20, CW - (spine_x - M) - 16, BODYM)
        if i < len(events) - 1:
            c.setStrokeColor(RULE); c.setLineWidth(1)
            c.line(spine_x, y - 15, spine_x, y - h - 40)
        y -= h + 42
    y -= 0
    rrect(c, M, y - 66, CW, 66, r=9, fill=WARM, stroke=RULE, lw=0.8)
    tracked(c, M + 18, y - 20, "THE ACCOUNTING AT DAY'S END", font="PopM", size=7.5, color=ACC_D, track=2)
    para(c, "Perhaps <b>60% fewer tokens</b> than the stateless equivalent — and a knowledge base one day denser. "
            "Maya's next Northwind project starts further ahead than this one did.", M + 18, y - 30, CW - 36, CARD_B)
    footer(c, pn)

# ---------- 19 · TOKEN OPTIMIZATION ----------
@page
def tokens(c, pn, tp):
    mark_toc("13", "Token Optimization", pn, tp)
    y = section_head(c, "13", "Token Optimization", "Conceptual — no implementation details.")
    y -= para(c,
        "The Crucible's efficiency thesis is simple: <b>the cheapest token is the one you don't resend.</b>",
        M, y, CW, LEAD) + 18
    prin = [
        ("Reuse over repeat", "Context established yesterday should not be retyped today. Persistent knowledge amortizes the cost of context across every future session that touches it."),
        ("Precision over volume", "Big windows invite lazy context. Brain scoping (Big → Mini → Baby) sends the relevant slice, not the available one. Sharper context is cheaper and better — precision is a quality feature wearing a cost-saving costume."),
        ("Distillation over accumulation", "A forty-message conversation might contain three durable facts. The platform stores the three facts, not the forty messages — so recall is dense, not noisy."),
        ("The right model for the job", "Not every task needs the largest model. A platform that knows the task and the models can route accordingly — premium tokens where reasoning is hard, cheap tokens where it isn't."),
    ]
    for i, (t, b) in enumerate(prin):
        c.setFont("PopB", 15); c.setFillColor(ACC_P)
        c.drawString(M, y - 14, f"{i+1:02d}")
        c.setFont("PopM", 10.5); c.setFillColor(INK)
        c.drawString(M + 32, y - 11, t)
        h = para(c, b, M + 32, y - 19, CW - 32, CARD_M)
        y -= h + 34
    y -= 6
    # conceptual chart
    chh = 150; chw = CW
    rrect(c, M, y - chh, chw, chh, r=10, fill=WARM, stroke=RULE, lw=0.8)
    ox, oy = M + 46, y - chh + 34
    axw, axh = chw - 90, chh - 62
    c.setStrokeColor(FAINT); c.setLineWidth(0.9)
    c.line(ox, oy, ox, oy + axh)
    c.line(ox, oy, ox + axw, oy)
    c.setFont("Lato", 7); c.setFillColor(MUTE)
    c.saveState(); c.translate(ox - 12, oy + axh / 2); c.rotate(90)
    c.drawCentredString(0, 0, "cumulative context cost"); c.restoreState()
    c.drawCentredString(ox + axw / 2, oy - 14, "sessions over time")
    # stateless: straight steep line
    c.setStrokeColor(HexColor("#B4A897")); c.setLineWidth(1.6)
    c.line(ox, oy, ox + axw, oy + axh * 0.98)
    c.setFont("LatoI", 7.8); c.setFillColor(MUTE)
    c.drawString(ox + axw - 118, oy + axh * 0.98 - 12, "stateless workflow (linear waste)")
    # crucible: flattening curve
    c.setStrokeColor(ACCENT); c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(ox, oy)
    p.curveTo(ox + axw * 0.35, oy + axh * 0.52, ox + axw * 0.6, oy + axh * 0.40, ox + axw, oy + axh * 0.42)
    c.drawPath(p, stroke=1, fill=0)
    c.setFont("LatoI", 7.8); c.setFillColor(ACC_D)
    c.drawRightString(ox + axw, oy + axh * 0.42 + 8, "with The Crucible (reuse flattens the curve)")
    y -= chh + 20
    para(c, "<b>The intended economics:</b> for a serious user, The Crucible should be cheaper than not using it — "
            "efficiency savings on model spend exceeding the cost of the platform itself.", M, y, CW, BODY)
    footer(c, pn)

# ---------- 20 · SECURITY ----------
@page
def security(c, pn, tp):
    mark_toc("14", "Security & Privacy", pn, tp)
    y = section_head(c, "14", "Security & Privacy", "Local-first is a security posture, not a feature.")
    items = [
        ("Your machine is the primary residence", "The Brain lives locally; the platform is fully functional offline. Cloud services (Barrage) are additive — sync and collaboration — and always opt-in."),
        ("Transparent memory", "Everything the system knows is inspectable and editable. No hidden profile, no undisclosed learning. If the Brain knows it, you can see it, correct it, or delete it — permanently."),
        ("Data sovereignty by construction", "Knowledge exports to open, human-readable formats at any time. No lock-in by hostage-taking: the platform earns retention through value, not captivity."),
        ("Minimal disclosure to models", "Because context is composed deliberately, third-party models see the slice a task requires — not your whole knowledge base. Scoping is a privacy mechanism as much as an efficiency one."),
        ("Local models as a first-class path", "For sensitive domains, the roadmap includes fully local inference — knowledge and intelligence on your hardware, with nothing leaving the machine."),
        ("Enterprise posture", "Team deployment brings scoped sharing (share a Mini Brain, not your whole Brain), administrative controls, and auditability. Compliance work ships alongside the enterprise tier."),
    ]
    ch = 92; gap = 12; cw = (CW - gap) / 2
    for i, (t, b) in enumerate(items):
        x = M + (i % 2) * (cw + gap)
        yy = y - (i // 2) * (ch + gap)
        rrect(c, x, yy - ch, cw, ch, r=9, fill=PAPER, stroke=RULE, lw=0.9)
        c.setFillColor(ACCENT); c.rect(x, yy - ch, 3, ch, stroke=0, fill=1)
        c.setFont("PopM", 9.4); c.setFillColor(INK)
        c.drawString(x + 16, yy - 18, t)
        para(c, b, x + 16, yy - 27, cw - 30, CARD_M)
    y -= 3 * ch + 2 * gap + 28
    rrect(c, M, y - 58, CW, 58, r=9, fill=ACC_PP)
    c.setFillColor(ACCENT); c.rect(M, y - 58, 3, 58, stroke=0, fill=1)
    para(c, "<b>The principle behind all six:</b> a knowledge system is only trustworthy if leaving it is easy and "
            "reading it is possible. We design for the user who checks.", M + 18, y - 15, CW - 36, BODY)
    footer(c, pn)

# ---------- 21 · COMPETITIVE ----------
@page
def compete(c, pn, tp):
    mark_toc("15", "Competitive Landscape", pn, tp)
    y = section_head(c, "15", "Competitive Landscape", "A different unit of work.")
    y -= para(c,
        "The honest comparison is not “better or worse” — it is “optimizing a different thing.” "
        "Existing tools optimize the <b>session</b>. The Crucible optimizes the <b>accumulation across sessions</b>.",
        M, y, CW, LEAD) + 16
    # table
    cols = [90, 154, 240]
    heads = ["", "Optimizes / persists", "Where the workflow differs"]
    rows = [
        ("ChatGPT Projects", "Grouped conversations; chat history and some memory, within one vendor.",
         "Knowledge is structured and graph-connected, not a scrollback. Model-agnostic. Local-first."),
        ("Claude Projects", "Curated context per project — knowledge you manually maintain.",
         "Capture and organization are ambient, not manual; knowledge flows between projects via the graph."),
        ("NotebookLM", "Q&A over sources you upload; your sources persist, your insights don't.",
         "The Crucible treats your work itself as the source — outputs and decisions become knowledge, not just inputs."),
        ("Cursor", "AI in the code editor; code persists in git, the AI's context resets.",
         "The same compounding, beyond code: clients, research, strategy, writing — with codebase knowledge as one domain."),
        ("GitHub Copilot", "In-flow code suggestion; no user-owned knowledge layer.",
         "The Crucible is the layer above tools like this: what Copilot learns about your day evaporates; the Brain doesn't."),
        ("Notes tools", "Human-written records; whatever you had the discipline to write.",
         "Capture is automatic and AI-native. Notes are where knowledge is stored; the Brain is where it is used."),
    ]
    x0 = M
    # header row
    c.setFont("PopM", 7.6); c.setFillColor(MUTE)
    xx = x0
    for wdt, h in zip(cols, heads):
        if h:
            tracked(c, xx, y - 10, h.upper(), font="PopM", size=6.6, color=MUTE, track=1)
        xx += wdt
    y -= 18
    st_name = S("cname", "PopM", 9.2, 12, INK)
    st_cell = S("ccell", "Lato", 8.2, 12.2, INK2)
    st_diff = S("cdiff", "Lato", 8.2, 12.2, ACC_D)
    for name, opt, diff in rows:
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.line(x0, y, x0 + CW, y)
        y -= 10
        p1 = Paragraph(name, st_name); _, h1 = p1.wrapOn(c, cols[0] - 14, PH)
        p2 = Paragraph(opt, st_cell); _, h2 = p2.wrapOn(c, cols[1] - 24, PH)
        p3 = Paragraph(diff, st_diff); _, h3 = p3.wrapOn(c, cols[2] - 10, PH)
        rh = max(h1, h2, h3)
        p1.drawOn(c, x0, y - h1)
        p2.drawOn(c, x0 + cols[0], y - h2)
        p3.drawOn(c, x0 + cols[0] + cols[1], y - h3)
        y -= rh + 10
    y -= 8
    para(c, "<b>The pattern:</b> each neighbor solves persistence for one silo — one vendor, one editor, one document "
            "set — or relies on human discipline. The Crucible's bet is the layer: cross-model, cross-tool, ambient, "
            "and owned by the user.", M, y, CW, BODY)
    footer(c, pn)

# ---------- 22 · USE CASES ----------
@page
def usecases(c, pn, tp):
    mark_toc("16", "Use Cases", pn, tp)
    y = section_head(c, "16", "Use Cases", "The same loop, six lives.")
    cases = [
        ("The Developer", "Architecture decisions, debugging journeys, and review standards accumulate into a technical Brain. New codebase, same taste: conventions and hard-won lessons come along. The rate-limit problem solved in March is a Skill by April."),
        ("The Researcher", "Literature, notes, and synthesis conversations weave into a domain graph. The Brain surfaces the connection between this week's paper and a passage read eight months ago — the link human memory drops. Writing starts from organized understanding."),
        ("The Agency", "One Mini Brain per client: voice, history, constraints, decisions — instantly in context for anyone on the account. Onboarding means sharing a Brain, not scheduling four handoff calls. Institutional knowledge survives turnover."),
        ("The Founder", "Strategy debates, investor feedback, positioning drafts, metric definitions — connected instead of scattered across six tools. The story stays consistent because there is one canonical, evolving source of it."),
        ("The Student", "A degree's worth of learning, compounding rather than evaporating after each exam. Concepts link across courses; last semester's foundations are live context for this semester's questions. A second transcript — the one with the knowledge in it."),
        ("The Enterprise", "The team version of all of the above, plus what enterprises uniquely lose: continuity. Prompt spend drops as shared knowledge replaces duplicated discovery. Expertise stops walking out the door — scoped, shared, audited, owned."),
    ]
    ch = 126; gap = 12; cw = (CW - gap) / 2
    for i, (t, b) in enumerate(cases):
        x = M + (i % 2) * (cw + gap)
        yy = y - (i // 2) * (ch + gap)
        rrect(c, x, yy - ch, cw, ch, r=9, fill=(WARM if (i // 2 + i) % 2 == 0 else PAPER), stroke=RULE, lw=0.8)
        c.setStrokeColor(ACCENT); c.setLineWidth(2)
        c.line(x + 16, yy - 17, x + 36, yy - 17)
        c.setFont("PopM", 10.5); c.setFillColor(INK)
        c.drawString(x + 16, yy - 32, t)
        para(c, b, x + 16, yy - 40, cw - 32, CARD_M)
    footer(c, pn)

# ---------- 23 · ROADMAP ----------
@page
def roadmap(c, pn, tp):
    mark_toc("17", "Roadmap", pn, tp)
    y = section_head(c, "17", "Roadmap", "Prove the loop. Multiply it across people. Harden it for organizations.")
    phases = [
        ("Phase 1", "Forge MVP", "NOW", "The desktop workspace, the Brain, the knowledge loop. Single-user, local-first, multi-model chat with capture → distill → connect → reuse working end to end. Forge Brain visual layer, v1."),
        ("Phase 2", "Local AI", "", "Fully local inference for privacy-critical work. Knowledge and intelligence on-device; platform economics improve as local models absorb routine tasks."),
        ("Phase 3", "Team Collaboration", "", "Barrage matures: shared Mini Brains, scoped permissions, team knowledge flows. The compounding loop starts operating at group scale."),
        ("Phase 4", "Marketplace", "", "Skills, workflows, and prompt libraries become shareable and publishable. The ecosystem's best patterns circulate; creators are rewarded for packaged expertise."),
        ("Phase 5", "Enterprise", "", "Administration, compliance, auditability, deployment options. The knowledge OS as organizational infrastructure — procurement-ready."),
    ]
    spine_x = M + 10
    for i, (ph, t, badge, b) in enumerate(phases):
        active = i == 0
        c.setFillColor(ACCENT if active else PAPER)
        c.setStrokeColor(ACCENT if active else FAINT); c.setLineWidth(1.4)
        c.circle(spine_x, y - 10, 5.2, stroke=1, fill=1)
        if i < len(phases) - 1:
            c.setStrokeColor(RULE); c.setLineWidth(1.2)
            c.line(spine_x, y - 17, spine_x, y - 92)
        tracked(c, spine_x + 22, y - 8, ph.upper(), font="PopM", size=7, color=(ACC_D if active else FAINT), track=1.8)
        c.setFont("PopM", 12.5); c.setFillColor(INK)
        c.drawString(spine_x + 22, y - 26, t)
        if badge:
            chip(c, spine_x + 22 + pdfmetrics.stringWidth(t, "PopM", 12.5) + 12, y - 30, badge, fill=ACCENT, tcolor=WHITE, size=6.6, h=13, pad=6)
        h = para(c, b, spine_x + 22, y - 34, CW - 60, BODYM)
        y -= h + 62
    footer(c, pn)

# ---------- 24 · TECH PHILOSOPHY ----------
@page
def techphil(c, pn, tp):
    mark_toc("18", "Technical Philosophy", pn, tp)
    y = section_head(c, "18", "Technical Philosophy", "High-level architecture only — internals are deliberately absent.")
    # layered arch mini-diagram
    layers = [
        ("Surfaces", "Forge · Forge Brain · future clients", PAPER, RULE, INK),
        ("Intelligence", "Aether · Experience Engine · Knowledge Graph", ACC_PP, ACCENT, ACC_D),
        ("Runtime", "Core — state · sync · shared services", WARM, RULE, INK),
        ("Connectivity", "Barrage · Siege · Models (Claude, local, specialized)", PAPER, RULE, INK),
    ]
    lh = 42
    for i, (t, s_, fill, stroke, tc) in enumerate(layers):
        yy = y - i * (lh + 8)
        rrect(c, M, yy - lh, CW, lh, r=8, fill=fill, stroke=stroke, lw=0.9)
        c.setFont("PopM", 10); c.setFillColor(tc)
        c.drawString(M + 16, yy - 18, t)
        c.setFont("Lato", 8.5); c.setFillColor(MUTE if tc is INK else HexColor("#B06A3A"))
        c.drawString(M + 120, yy - 18, s_)
        c.setFont("Lato", 7); c.setFillColor(FAINT)
        if i < 3:
            arrow(c, M + CW - 24, yy - lh - 1, M + CW - 24, yy - lh - 7, color=FAINT, lw=0.9)
    y -= 4 * (lh + 8) + 14
    pts = [
        ("Layered, with a stable center", "Core provides one runtime for state, sync, and services; every surface is a client of it. Surfaces can multiply without re-solving the hard problems."),
        ("The knowledge model is the contract", "Components integrate through the graph's entities and relationships — not through each other's internals. Aether can improve continuously without breaking Forge; Siege can add integrations without touching Core."),
        ("Model-agnostic by architecture", "No provider's API shape leaks past the boundary. Models are resources the OS allocates — swappable per task, per policy, per price."),
        ("Local-first as engineering discipline", "Every feature is designed offline-first, then extended with sync — never the reverse. This ordering is what makes the ownership guarantees true rather than aspirational."),
        ("Boring where possible, novel where necessary", "The innovation budget is spent on the knowledge layer — the part that doesn't exist elsewhere. Everything else uses proven technology."),
    ]
    for t, b in pts:
        diamond(c, M + 4, y - 8, 3.2)
        c.setFont("PopM", 9.8); c.setFillColor(INK)
        c.drawString(M + 16, y - 11, t)
        h = para(c, b, M + 16, y - 18, CW - 16, CARD_M)
        y -= h + 30
    footer(c, pn)

# ---------- 25 · FUTURE VISION ----------
@page
def future(c, pn, tp):
    mark_toc("19", "Future Vision", pn, tp)
    y = section_head(c, "19", "Future Vision", "Where this goes, if it works.")
    spans = [
        ("NEAR", "Your second brain, actually",
         "The phrase has been marketing for a decade. A Brain that captures ambiently, organizes itself, and shows up "
         "usefully in every AI conversation is the version that earns the name."),
        ("MID", "Knowledge as a shareable good",
         "Skills and Mini Brains become artifacts people trade: an expert's packaged judgment, a firm's "
         "onboarding-in-a-Brain, a community's accumulated craft. Expertise gets a distribution format."),
        ("FAR", "The default layer",
         "Every era of computing acquired an organizing layer that later seemed inevitable: the filesystem, the "
         "database, the browser, version control. The AI era's missing layer is knowledge that compounds. Someone "
         "will build the place where human-AI work accumulates — the substrate people simply assume, the way "
         "developers assume git. We intend it to be The Crucible."),
    ]
    for tag, t, b in spans:
        chip(c, M, y - 18, tag, fill=ACC_P, tcolor=ACC_D, size=7, h=15)
        c.setFont("PopM", 13); c.setFillColor(INK)
        c.drawString(M + 56, y - 15, t)
        h = para(c, b, M + 56, y - 26, CW - 56, BODY)
        y -= h + 56
    y -= 6
    rrect(c, M, y - 96, CW, 96, r=10, fill=DARK)
    c.setFont("PopL", 13.5); c.setFillColor(WHITE)
    c.drawString(M + 24, y - 32, "AI's value will increasingly come not from what models know,")
    c.drawString(M + 24, y - 52, "but from what you and your models have learned together.")
    c.setFont("PopM", 11); c.setFillColor(HexColor("#F0A26B"))
    c.drawString(M + 24, y - 76, "That joint knowledge needs a home, an owner, and an operating system.")
    footer(c, pn)

# ---------- 26 · WHY CLAUDE ----------
@page
def whyclaude(c, pn, tp):
    mark_toc("20", "Why Claude", pn, tp)
    y = section_head(c, "20", "Why Claude", "Model-agnostic by design — Claude as the reference model, for structural reasons.")
    pts = [
        ("Long-context reasoning is the core operation",
         "The knowledge loop rests on distillation: reading substantial context and extracting exactly what matters. "
         "This is precisely where Claude leads. The quality of the Brain is bounded by the quality of distillation — "
         "which makes Claude quality the platform's ceiling-raiser."),
        ("Agentic infrastructure that matches our architecture",
         "Claude's agent tooling and the Model Context Protocol align with how Siege and Core are built. MCP is the "
         "natural interchange for a platform whose whole job is supplying models with the right context — a context "
         "platform meeting a context protocol."),
        ("Steerability protects the user's voice",
         "The Experience Engine works by applying learned preferences. That only works with a model that follows "
         "nuanced instructions faithfully rather than averaging them away."),
        ("Aligned values",
         "Human ownership, transparency, and safety aren't compliance items for this product; they're the philosophy. "
         "Building the reference experience on Anthropic's models is coherence, not convenience."),
        ("A shared demonstration",
         "The Crucible is a working argument that Claude plus persistent, well-organized context outperforms any "
         "model without it. Success here is evidence that context infrastructure — not just model scale — is where "
         "user value now compounds."),
    ]
    for i, (t, b) in enumerate(pts):
        c.setFont("PopB", 15); c.setFillColor(ACC_P)
        c.drawString(M, y - 14, f"{i+1:02d}")
        c.setFont("PopM", 10.8); c.setFillColor(INK)
        c.drawString(M + 32, y - 11, t)
        h = para(c, b, M + 32, y - 19, CW - 32, BODYM)
        y -= h + 40
    footer(c, pn)

# ---------- 27 · STATUS ----------
@page
def status(c, pn, tp):
    mark_toc("21", "Current Status", pn, tp)
    y = section_head(c, "21", "Current Status", "Stated plainly.")
    rows = [
        ("Stage", "Pre-launch. Prototype."),
        ("Architecture", "Complete. The platform structure in this document — Core, Forge, Forge Brain, Barrage, Siege, Aether, and the Brain model — is designed and documented."),
        ("Working today", "Forge desktop prototype with the core knowledge loop, in active development and internal use."),
        ("In progress", "Forge MVP hardening · Forge Brain visual layer · capture and distillation quality."),
        ("Not yet", "Public release · cloud collaboration (Barrage) · integrations platform (Siege) beyond initial connectors · revenue."),
        ("Team", "Early. Founder-led, actively building."),
    ]
    for t, b in rows:
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.line(M, y + 6, PW - M, y + 6)
        tracked(c, M, y - 12, t.upper(), font="PopM", size=7.5, color=ACC_D, track=1.6)
        h = para(c, b, M + 130, y - 3, CW - 130, BODY)
        y -= max(h, 20) + 26
    y -= 8
    rrect(c, M, y - 74, CW, 74, r=9, fill=WARM, stroke=RULE, lw=0.8)
    para(c, "This document describes the architecture and intent of the full platform honestly — including the parts "
            "still ahead of us. <b>We would rather earn belief with a clear map and a working prototype than with "
            "inflated claims.</b>", M + 20, y - 18, CW - 40, BODY)
    footer(c, pn)

# ---------- 28 · CTA ----------
@page
def cta(c, pn, tp):
    mark_toc("22", "An Invitation", pn, tp)
    y = section_head(c, "22", "An Invitation", "The right conversations, at the stage where they change the trajectory.")
    asks = [
        ("Anthropic · Claude Max for Builders",
         "Partnership on the reference implementation of context-rich, Claude-powered knowledge work. We are building "
         "on Claude; we'd like to build with Anthropic."),
        ("Investors",
         "A seed conversation about owning the knowledge layer of the AI era."),
        ("Design partners",
         "Agencies, research groups, and engineering teams who feel this problem weekly and want the fix early."),
        ("Builders",
         "Engineers and designers who want to work on the layer above the models — where the next decade of user "
         "value accumulates."),
    ]
    for t, b in asks:
        c.setStrokeColor(ACCENT); c.setLineWidth(2)
        c.line(M, y - 4, M + 22, y - 4)
        c.setFont("PopM", 11.5); c.setFillColor(INK)
        c.drawString(M + 34, y - 8, t)
        h = para(c, b, M + 34, y - 16, CW - 34, BODYM)
        y -= h + 42
    y -= 8
    rrect(c, M, y - 128, CW, 128, r=10, fill=DARK)
    c.setFont("PopL", 13); c.setFillColor(WHITE)
    c.drawString(M + 24, y - 32, "If the thesis resonates — that AI needs an operating system")
    c.drawString(M + 24, y - 51, "for knowledge, and that whoever builds it well will matter —")
    c.drawString(M + 24, y - 70, "we should talk.")
    c.setFont("PopM", 10.5); c.setFillColor(HexColor("#F0A26B"))
    c.drawString(M + 24, y - 96, "Austin Brower")
    c.setFont("Lato", 10); c.setFillColor(HexColor("#C9B8A8"))
    c.drawString(M + 24, y - 111, "austinbrower94@outlook.com")
    footer(c, pn)

# ---------- 29 · BACK COVER ----------
@page
def backcover(c, pn, tp):
    c.setFillColor(PAPER); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(HexColor("#FCF3EB"))
    c.circle(PW / 2, PH / 2, 200, stroke=0, fill=1)
    diamond(c, PW / 2, PH / 2 + 64, 10)
    c.setFont("PopL", 26); c.setFillColor(INK)
    c.drawCentredString(PW / 2, PH / 2 + 10, "The Crucible")
    c.setFont("LatoI", 11); c.setFillColor(MUTE)
    c.drawCentredString(PW / 2, PH / 2 - 14, "Where conversations become intelligence.")
    c.setFont("Lato", 8.5); c.setFillColor(FAINT)
    c.drawCentredString(PW / 2, 84, "© 2026 · Prepared by Austin Brower · austinbrower94@outlook.com")

# =====================================================================
def build(path, toc_pass):
    c = _canvas.Canvas(path, pagesize=letter)
    c.setTitle("The Crucible — Product Overview")
    c.setAuthor("Austin Brower")
    c.setSubject("The AI Knowledge Operating System")
    for i, fn in enumerate(PAGES, start=1):
        c.setFillColor(PAPER)
        c.rect(0, 0, PW, PH, stroke=0, fill=1)
        fn(c, i, toc_pass)
        c.showPage()
    c.save()

if __name__ == "__main__":
    import os

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "docs", "product", "The-Crucible-Product-Overview.pdf")
    build("/tmp/_pass1.pdf", 1)
    build(out, 2)
    print("wrote:", out)
    print("pages:", len(PAGES))
    print("toc:", TOC_SECTIONS)
