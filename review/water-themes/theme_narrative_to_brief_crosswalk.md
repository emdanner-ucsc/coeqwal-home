# Crosswalk: theme narrative (8-section) → standard brief format (9-section)

Maps the public **theme narrative** template used by the four new PDFs (Rivers and
Salmon, Farms and groundwater, Community water systems, Balancing needs in the Delta)
onto the **nine standard brief sections** defined in
`shared/COEQWAL_Visual_Design_Spec.md` (the "Brief section architecture" rules) and
implemented in `theme_ag_gw_brief_prototype_v0_1.html`.

Purpose: show exactly where the two formats line up and where they diverge, so we can
decide whether theme narratives are a separate format or should be folded into the
standard brief format.

(Throughout, **§** means "section" — so §1 = section 1.)

> **The root mismatch is the unit of analysis.** A theme narrative describes a *theme
> across multiple scenarios* — a range of management strategies and hydroclimates,
> rather than a single one. An LOI brief and a Scenario brief each describe *one
> scenario*. So the brief
> sections that are inherently single-scenario — the one-sentence finding (§1), the
> single headline figure (§3), the management-vs-climate decomposition (§4, which is a
> within-scenario contrast), and the single location hook (§6) — have no clean home in
> a narrative that is deliberately reporting the spread across many scenarios. The
> divergence below is therefore not just "the narrative is figure-light"; the two
> formats are answering different units of question (one theme over N scenarios vs. one
> scenario). This is flagged per-row as **[scenario-scope]** where it applies.

Match legend: ● direct · ◐ partial · ○ none.

---

## A. Narrative section → brief section

| # | Theme narrative section | Maps to brief section | Match | Notes on the divergence |
|---|---|---|---|---|
| 1 | The core question | 1. Headline | ◐ | **Inverted in kind + [scenario-scope].** Narrative opens with an *open question* ("Can California's rivers support healthy salmon…?"). The brief headline is a *one-sentence finding* about a single scenario — a declarative answer. A theme spanning many scenarios has no single finding to assert, which is partly why it falls back on a question. |
| 2 | Why this matters | 2. What this is | ◐ | Overlap on framing/stakes, but each carries something the other lacks. Narrative gives broad public context (history, climate pressure); brief "What this is" adds the **scenario / strategy / hydroclimate / tier glossary callouts** the narrative omits. |
| 3 | What this theme focuses on (Box 1/2/3) | 2. What this is / 5. Pattern | ◐ | No dedicated brief slot. The boxes describe the system mechanisms and the outcomes in scope — partly scope (→2), partly "how to read the system" (→5). Splits across two brief sections. |
| 4 | What to keep in mind | 8. What this doesn't say | ● | Strongest match. Both are caveats/limits (multi-year patterns not single-year predictions; flows alone don't restore ecosystems; habitat/levees/invasives not evaluated). Narrative version is longer and more pedagogical. |
| 5 | What management strategies are explored | 4. Operations and climate / 2. What this is | ◐ | **[scenario-scope].** Lists the operational levers explored in this theme (pumping limits, functional flows, carryover) *across* its scenarios. A brief instead names the one strategy its scenario embodies and decomposes it against climate. The narrative's plural-strategy framing is the opposite of the brief's single-strategy §4. |
| 6 | What the models show (Trade-offs / Equity / Resilience) | 3. What the model shows + 5. Pattern across scenarios | ◐ | **[scenario-scope].** The results core. A brief shows one scenario's headline figure (§3), its ops/climate decomposition (§4), and how to read it (§5). The narrative summarizes the *pattern across the theme's scenarios* in three prose paragraphs — no single figure, no per-scenario specifics, because the subject is the spread itself. |
| 7 | How to explore this theme further | 9. Explore further | ● | Direct match — deep link / next-step into the explorer. |
| 8 | Closing line (shared tagline) | — | ○ | No brief equivalent. The shared "Together, these views make trade-offs, equity, and resilience visible…" line has no slot in the standard format. |

---

## B. Brief sections with weak or no narrative coverage (gaps to fill if reconciling)

| Brief section | Covered by narrative? | Match | What's missing |
|---|---|---|---|
| 1. Headline | §1 (as a question) | ◐ | **[scenario-scope]** Needs a declarative one-sentence finding for one scenario; a theme has no single finding. |
| 2. What this is | §2 + §3 + §5 | ◐ | Scope is present; the **glossary callouts** (scenario / strategy / hydroclimate / tier) are not. |
| 3. What the model shows | §6 (prose only) | ◐ | **[scenario-scope]** No **headline figure** — the standard format's centerpiece is one scenario's result. |
| 4. Operations and climate | §5 / §6 (mentioned) | ◐ | **[scenario-scope]** No **management-vs-climate decomposition** — a within-one-scenario contrast. (Cf. core concept #17 / "no decomposition on raw output.") |
| 5. Pattern across scenarios | §3 / §6 | ◐ | Mechanisms described, but no "how to read the figure" across scenarios. |
| 6. About specific places | — | ○ | **[scenario-scope]** Narratives are theme-level / system-wide; **no single location-of-interest hook**. |
| 7. Related briefs | — | ○ | **No cross-link block** to sibling briefs. |
| 8. What this doesn't say | §4 | ● | Well covered. |
| 9. Explore further | §7 | ● | Well covered. |

---

## C. Read of the divergence

**The divergence is scope, not just style.** The four brief sections that don't map
cleanly — §1 finding, §3 headline figure, §4 ops/climate decomposition, §6 place hook —
are all the sections that only make sense *for a single scenario*. A theme narrative is
deliberately the other unit of analysis: one theme reported across multiple scenarios
and hydroclimates. You can't state one finding, show one figure, or decompose one
scenario's operations vs. climate when the whole point is to show the spread across
several scenarios. So the mismatch isn't that the narrative is underbuilt — it's that the
standard brief format was written around the single-scenario LOI/Scenario brief, and a
theme spans multiple scenarios by design.

The two formats still share **three clean matches** (caveats → §8, explore-further →
§9, and loosely the opening hook → §1). The narrative is a **system-wide, multi-scenario,
figure-light, question-led explainer**; the brief is a **single-scenario, finding-led,
figure-centered, place-specific report**.

This points to three options:

1. **Treat theme narratives as a separate, documented format** (the way the
   brief-article format is already set apart in the Visual Design Spec). The standard
   format's single-scenario sections (§1 finding, §3 figure, §4 decomposition, §6 place
   hook) are the expected exceptions; keep the shared ones (§8 caveats, §9 explore).
2. **Make a theme version of the standard format** where the single-scenario sections
   are redefined for multiple scenarios: §1 becomes the core question, §3 becomes an
   across-scenario distribution view, §4 becomes "strategies explored" rather than one
   decomposition, §6 becomes "across regions" rather than one place.
3. **Force the narrative into the nine sections as-is** — not recommended, because it
   would require inventing a single finding, figure, and place that a theme doesn't have.

Recommendation: option 1 or 2, written up as a documented exception, rather than
pretending the single-scenario format fits a multi-scenario theme.
