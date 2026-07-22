<!-- ┌──────────────────────────────────────────────────────────────────────┐ -->
<!-- │   cornna · profile readme  (English — default)                       │ -->
<!-- │   Concept: a curated exhibition. Custom-painted hero, serif placard  │ -->
<!-- │   typography, framed gallery of works. Impressionist water-lily.     │ -->
<!-- │   canvas #F8FAFC · cobalt #1E40AF · cerulean #2563EB                 │ -->
<!-- │   sky #60A5FA · pale #DBEAFE · ochre #FBBF24                         │ -->
<!-- └──────────────────────────────────────────────────────────────────────┘ -->

<div align="center">

<!-- ░░ HERO — custom-painted masthead: one golden thread directs a constellation of ideas ░░ -->
<img width="100%" src="./assets/hero-v3.png" alt="cornna — AI-Native Developer · Vibe Coder · Agent Builder" />

</div>

<p align="center">
  <img src="https://img.shields.io/badge/English-1E40AF?style=for-the-badge&labelColor=1E40AF&color=1E40AF" alt="English" />
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-F8FAFC?style=for-the-badge&labelColor=F8FAFC&color=60A5FA" alt="中文" /></a>
</p>

<br/>

> "I'm not writing code — I collaborate with AI to land the *vibe* in my head as software."
> Like ripples spreading across water: a thought drops into the pond, and AI helps me push it to the shore.
>
> *Don't write code. Direct it.*

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=2" alt="" />
</div>

## ▍ 01 — Identity

```yaml
name:        cornna
handle:      sweetcornna  ·  github.com/sweetcornna
title:       AI-Native Developer / Vibe Coder
languages:   [Python, TypeScript, C, Go, Shell]
domains:
  - AI agents & assistants     # corlinman
  - Agent infrastructure       # Dormice · 5 upstream PRs merged
  - MCP ecosystem              # free-search-mcp, coin-mcp
  - Network & infrastructure   # OpenWrt plugins, clash, drcom
strengths:
  - Turn a vague idea into a working prototype in one evening.
  - Wire LLMs to anything via MCP / function calls / RAG.
  - Build full-stack tools end-to-end (FE + BE + agent loop).
  - Read & fix real bugs in 190k–380k★ agent codebases — merged PRs in both openclaw & Hermes.
mantra:      "Ship the vibe, polish the rough edges later."
```

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=2" alt="" />
</div>

## ▍ 02 — Arsenal

<div align="center">

[![langs](https://skillicons.dev/icons?i=py,ts,js,c,go,bash,html,css&theme=light&perline=8)](https://skillicons.dev)

[![ai](https://skillicons.dev/icons?i=openai,pytorch,tensorflow,sklearn,sqlite,postgres,redis,anaconda&theme=light&perline=8)](https://skillicons.dev)

[![stack](https://skillicons.dev/icons?i=fastapi,flask,nodejs,express,vue,react,nextjs,tailwind&theme=light&perline=8)](https://skillicons.dev)

[![infra](https://skillicons.dev/icons?i=docker,linux,nginx,git,github,githubactions,vscode,vim&theme=light&perline=8)](https://skillicons.dev)

</div>

<br/>

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryColor':'#DBEAFE','primaryTextColor':'#1E293B','primaryBorderColor':'#1E40AF','lineColor':'#2563EB','tertiaryColor':'#F8FAFC','fontFamily':'Space Grotesk','fontSize':'15px'}}}%%
graph LR
    V((Vibe<br/>Coding)):::core
    V --> A[AI Agents]:::node
    V --> M[MCP Servers]:::node
    V --> I[Agent Infrastructure]:::node
    A --> P1[corlinman]:::leaf
    A --> P2[copy-trader]:::leaf
    M --> P3[free-search-mcp]:::leaf
    M --> P4[coin-mcp]:::leaf
    I --> P5[Dormice]:::leaf
    I --> P6[Open-source fixes]:::leaf
    V --> L[LLM Learning]:::node
    L --> P7[lingma]:::leaf
    L --> P8[mathodology]:::leaf

    classDef core fill:#1E40AF,stroke:#1E40AF,stroke-width:3px,color:#fff,font-weight:bold
    classDef node fill:#DBEAFE,stroke:#2563EB,stroke-width:1.5px,color:#1E293B
    classDef leaf fill:#F8FAFC,stroke:#60A5FA,stroke-width:1px,color:#1E40AF
```

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=3" alt="" />
</div>

## ▍ 03 — Signature Work

<sub>A curated room. One flagship, four companions — each an oil study of what it does.</sub>

<br/>

<!-- ╔══ FLAGSHIP — corlinman, C-position ══╗ -->

<a href="https://github.com/sweetcornna/corlinman">
  <img width="100%" src="./assets/projects/corlinman.png" alt="corlinman — a glowing companion" />
</a>

<table>
<tr>
<td valign="middle">

### `01` &nbsp; corlinman&nbsp;·&nbsp;Personal AI Agent

> My own **24×7 digital alter-ego** — schedule, reminders, long-horizon tasks, cross-platform orchestration, all handed off to it. **Vibe-coded from scratch**, turning "I wish I had an assistant" into a long stream of git pushes. My personal bet on what an AI agent should be.

<sub>*Personal AI agent — Python · LLM · Agent Loop · Tools — 2026*</sub>

<a href="https://github.com/sweetcornna/corlinman">
  <img src="https://img.shields.io/badge/Enter%20the%20repo%20%E2%86%92-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" />
</a>

</td>
</tr>
</table>

<br/>

<!-- ╔══ COMPANIONS — 2×2 gallery ══╗ -->

<table>
<tr>

<td width="50%" valign="top">

<a href="https://github.com/BitMiracle-AI/Dormice">
  <img width="100%" src="./assets/projects/dormice.png" alt="Dormice — a persistent agent sandbox sleeping between four lifecycle chambers" />
</a>

#### `02` &nbsp; Dormice&nbsp;·&nbsp;Persistent Agent Sandboxes

The **SQLite of agent sandboxes** — self-hosted and E2B-compatible, with persistent sandboxes that cool from active to frozen, stopped, and optionally S3-archived. **5 PRs merged upstream** across real-host installation, firewall/sysctl safety, doctor verification, and operator docs.

<sub>*Agent sandboxes — TypeScript · Docker · gVisor · SQLite · E2B — 5 PRs merged — 2026*</sub>

<a href="https://github.com/BitMiracle-AI/Dormice">Enter the repo →</a>

</td>

<td width="50%" valign="top">

<a href="https://github.com/sweetcornna/mathodology">
  <img width="100%" src="./assets/projects/mathodology.png" alt="mathodology — integral and sigma" />
</a>

#### `03` &nbsp; mathodology&nbsp;·&nbsp;MCM Collaboration Platform

An **AI-augmented** platform for math-modeling contests. Paper · code · data · visualization — all in one workflow.

<sub>*MCM collaboration platform — Python · LLM · RAG — 2026*</sub>

<a href="https://github.com/sweetcornna/mathodology">Enter the repo →</a>

</td>

</tr>
<tr>

<td width="50%" valign="top">

<a href="https://github.com/sweetcornna/lingma">
  <img width="100%" src="./assets/projects/lingma.png" alt="lingma — code blocks on water" />
</a>

#### `04` &nbsp; lingma&nbsp;·&nbsp;Visual Coding Classroom

**AI-generated exercises × visual programming** so beginners actually keep going. The LLM writes step-by-step drills; drag the blocks and run.

<sub>*Visual coding classroom — TypeScript · Vue · LLM — 2026*</sub>

<a href="https://github.com/sweetcornna/lingma">Enter the repo →</a>

</td>

<td width="50%" valign="top">

<a href="https://github.com/sweetcornna/free-search-mcp">
  <img width="100%" src="./assets/projects/free-search-mcp.png" alt="free-search-mcp — magnifier and nodes" />
</a>

#### `05` &nbsp; free-search-mcp&nbsp;·&nbsp;Keyless Search MCP

Gives any LLM agent internet access — multi-engine + Playwright fallback + FTS5 cache, **no API key required**.

<sub>*Keyless search MCP — Python · MCP · Playwright — 2026*</sub>

<a href="https://github.com/sweetcornna/free-search-mcp">Enter the repo →</a>

</td>

</tr>
</table>

<br/>

<div align="center">
  <a href="https://github.com/sweetcornna?tab=repositories">
    <img src="https://img.shields.io/badge/Browse%20all%2044%20works%20%E2%86%92-F8FAFC?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" />
  </a>
</div>

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=3" alt="" />
</div>

## ▍ 04 — Open Source

<sub>Brushstrokes left on the giants — real bugs fixed in 190k–380k★ agent codebases. Every PR is a public, reviewable record.</sub>

<br/>

<table>
<tr>

<td width="50%" valign="top">

#### openclaw&nbsp;·&nbsp;<img src="https://img.shields.io/badge/%E2%AD%90-379k%2B-FBBF24?style=flat-square&labelColor=1E40AF" alt="379k+ stars" />

Open-source personal AI agent runtime (★379k). **5 PRs merged by maintainers** into the runtime core and platform adapters: [#87698](https://github.com/openclaw/openclaw/pull/87698) — `fix(gateway): emit subagent_ended hook` (+499/-5, gives plugin-SDK subagent runs a real lifecycle event via a proper `SubagentRunRecord`; fixes #59164); [#89508](https://github.com/openclaw/openclaw/pull/89508) — `fix(models): clarify provider model registration hint` (fixes #89192); [#89800](https://github.com/openclaw/openclaw/pull/89800) — `fix(agents): resolve webchat current session status` (+133/-21, keeps WebChat `current` on the effective requester session; fixes #89773); [#89806](https://github.com/openclaw/openclaw/pull/89806) — `fix(feishu): avoid axios interceptor internals` (+90/-35, registers the Feishu User-Agent override through the public interceptor API instead of mutating axios internals); and [#89855](https://github.com/openclaw/openclaw/pull/89855) — `fix(telegram): avoid duplicate dm chat window context` (+96/-1, stops repeated Telegram DM chat-window context in existing private sessions; fixes #87566). More PRs in review. Same lineage as my own corlinman: local-first · files-as-skills/memory · multi-channel.

<sub>*5 fixes merged into the runtime core and platform adapters by maintainers — more PRs in review.*</sub>

<a href="https://github.com/openclaw/openclaw/pull/87698"><img src="https://img.shields.io/badge/PR%20%2387698%20%E2%9C%93%20MERGED-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" alt="PR #87698 merged" /></a>
<a href="https://github.com/openclaw/openclaw/pull/89508"><img src="https://img.shields.io/badge/PR%20%2389508%20%E2%9C%93%20MERGED-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" alt="PR #89508 merged" /></a>
<a href="https://github.com/openclaw/openclaw/pull/89800"><img src="https://img.shields.io/badge/PR%20%2389800%20%E2%9C%93%20MERGED-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" alt="PR #89800 merged" /></a>
<a href="https://github.com/openclaw/openclaw/pull/89806"><img src="https://img.shields.io/badge/PR%20%2389806%20%E2%9C%93%20MERGED-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" alt="PR #89806 merged" /></a>
<a href="https://github.com/openclaw/openclaw/pull/89855"><img src="https://img.shields.io/badge/PR%20%2389855%20%E2%9C%93%20MERGED-1E40AF?style=for-the-badge&labelColor=F8FAFC&color=1E40AF" alt="PR #89855 merged" /></a>

</td>

<td width="50%" valign="top">

#### Hermes Agent&nbsp;·&nbsp;<img src="https://img.shields.io/badge/%E2%AD%90-197k%2B-FBBF24?style=flat-square&labelColor=1E40AF" alt="197k+ stars" />

Nous Research's open-source agent framework (★197k). **2 PRs merged by maintainers**: [#33817](https://github.com/NousResearch/hermes-agent/pull/33817) — `fix(gateway): FIFO queue for busy_input_mode` (+195/-7, preserves each rapid follow-up message as its own turn instead of overwriting one pending slot; closes #28503); and [#38098](https://github.com/NousResearch/hermes-agent/pull/38098) — `fix(docker): accept Unraid uid mappings` (fixes #38070). More fix PRs in review; plus original **persona + event** extensions in my own repo [personal_hermes](https://github.com/sweetcornna/personal_hermes).

<sub>*2 PRs merged upstream by maintainers — concurrency & deployment fixes; more in review.*</sub>

<a href="https://github.com/NousResearch/hermes-agent/pull/33817"><img src="https://img.shields.io/badge/PR%20%2333817%20%E2%9C%93%20MERGED-2563EB?style=for-the-badge&labelColor=F8FAFC&color=2563EB" alt="PR #33817 merged" /></a>
<a href="https://github.com/NousResearch/hermes-agent/pull/38098"><img src="https://img.shields.io/badge/PR%20%2338098%20%E2%9C%93%20MERGED-2563EB?style=for-the-badge&labelColor=F8FAFC&color=2563EB" alt="PR #38098 merged" /></a>

</td>

</tr>
</table>

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=3" alt="" />
</div>

## ▍ 05 — Telemetry

<div align="center">

<img src="https://komarev.com/ghpvc/?username=sweetcornna&label=Profile%20views&color=1E40AF&style=flat-square" />&nbsp;
<img src="https://img.shields.io/badge/dynamic/json?label=Followers&query=followers&url=https%3A%2F%2Fapi.github.com%2Fusers%2Fsweetcornna&color=1E40AF&labelColor=F8FAFC&style=flat-square&logo=github&logoColor=1E40AF" />&nbsp;
<img src="https://img.shields.io/badge/dynamic/json?label=Following&query=following&url=https%3A%2F%2Fapi.github.com%2Fusers%2Fsweetcornna&color=2563EB&labelColor=F8FAFC&style=flat-square" />&nbsp;
<img src="https://img.shields.io/badge/dynamic/json?label=Public%20repos&query=public_repos&url=https%3A%2F%2Fapi.github.com%2Fusers%2Fsweetcornna&color=2563EB&labelColor=F8FAFC&style=flat-square" />

<br/><br/>

<img width="68%" src="https://streak-stats.demolab.com?user=sweetcornna&theme=highcontrast&hide_border=true&background=F8FAFC&ring=1E40AF&fire=FBBF24&currStreakLabel=1E40AF&sideLabels=1E40AF&dates=2563EB&sideNums=1E40AF&currStreakNum=FBBF24&stroke=DBEAFE" alt="streak" />

<br/><br/>

<img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=sweetcornna&bg_color=F8FAFC&color=1E40AF&line=2563EB&point=FBBF24&area_color=DBEAFE&area=true&hide_border=true&custom_title=Contribution%20Pulse&title_color=1E40AF" alt="activity" />

<br/><br/>

<img width="96%" src="https://raw.githubusercontent.com/sweetcornna/sweetcornna/output/github-contribution-grid-snake-dark.svg" alt="contribution snake" />

<br/><br/>

<sub>ACHIEVEMENTS</sub><br/>
<img src="https://img.shields.io/badge/%F0%9F%A6%88%20Pull%20Shark-%C3%972-1E40AF?style=for-the-badge&labelColor=F8FAFC" />&nbsp;
<img src="https://img.shields.io/badge/%F0%9F%A4%A0%20Quickdraw-%C3%971-2563EB?style=for-the-badge&labelColor=F8FAFC" />&nbsp;
<img src="https://img.shields.io/badge/%E2%AD%90%20Starstruck-%C3%971-2563EB?style=for-the-badge&labelColor=F8FAFC" />&nbsp;
<img src="https://img.shields.io/badge/%F0%9F%9A%80%20YOLO-%C3%971-2563EB?style=for-the-badge&labelColor=F8FAFC" />

</div>

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=2,8,12,20,24&height=2" alt="" />
</div>

## ▍ 06 — Reach

<div align="center">

<a href="https://github.com/sweetcornna">
  <img src="https://img.shields.io/badge/GitHub-F8FAFC?style=for-the-badge&logo=github&logoColor=1E40AF" />
</a>
<a href="mailto:ymy_live@outlook.com">
  <img src="https://img.shields.io/badge/Email-F8FAFC?style=for-the-badge&logo=gmail&logoColor=1E40AF" />
</a>
<a href="https://github.com/sweetcornna?tab=repositories">
  <img src="https://img.shields.io/badge/All%20Repos-F8FAFC?style=for-the-badge&logo=github&logoColor=1E40AF" />
</a>

<br/><br/>

<sub>Open to collaborate on AI agents · MCP servers · education automation · on-chain tooling. Email me directly.</sub>

</div>

<br/>

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:F8FAFC,50:60A5FA,100:DBEAFE&height=120&section=footer&animation=fadeIn" />
  <sub><i>Made with vibe — directed, not written.</i></sub>
</div>
