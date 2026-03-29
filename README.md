# Reality Agents v0.1 — Self-Evolving Agent Framework

A curiosity-driven, self-evolving agent framework based on Reality OS principles.

## Architecture

```
┌─────────────────────────────────────┐
│         CURIOUSITY ENGINE           │
│    (Dopamine budget, exploration    │
│     vs exploitation, Wrong Room)    │
├─────────────────────────────────────┤
│         META-EVOLVER                │
│    (Agent evolves its own           │
│     strategies over time)           │
├─────────────────────────────────────┤
│         PERSISTENT MEMORY           │
│    (Episodic, semantic, procedural  │
│     with experience distillation)   │
├─────────────────────────────────────┤
│         AGENT CORE                  │
│    (Perceive → Decide → Execute     │
│     → Evaluate → Adapt)             │
├─────────────────────────────────────┤
│         ORCHESTRATOR                │
│    (Multi-agent coordination:       │
│     parallel/sequential/            │
│     competitive/cooperative)        │
└─────────────────────────────────────┘
```

## Core Principles (from Reality OS)

| Reality OS Principle | Agent Implementation |
|---------------------|---------------------|
| Dopamine = curiosity driver | CuriosityEngine manages exploration budget |
| Curiosity > optimization | 70% explore, 30% exploit default ratio |
| Accountability loop | Agent evaluates outcomes and adapts strategies |
| Wrong Room principle | Agent seeks challenging environments |
| Meta-cognition | Agent observes and evolves its own strategies |
| Persistent memory | Three memory types with periodic distillation |
| Agentic amplification | Multi-agent orchestration with shared memory |

## Modules

| Module | Purpose |
|--------|---------|
| `curiosity_engine.py` | Drives exploration based on entropy and novelty |
| `memory.py` | Persistent semantic memory with experience distillation |
| `meta_evolver.py` | Agent evolves its own prompts and strategies |
| `agent.py` | Base agent class with self-evaluation |
| `orchestrator.py` | Multi-agent coordination |
| `main.py` | Entry point and demo |

## Quick Start

```bash
# Run the demo
python main.py
```

## Creating a Custom Agent

```python
from agent import Agent
from orchestrator import Orchestrator

# Create specialized agents
researcher = Agent(name="researcher", domain="research")
coder = Agent(name="coder", domain="coding")

# Orchestrate
orchestrator = Orchestrator(mode="cooperative")
orchestrator.register_agent(researcher)
orchestrator.register_agent(coder)

# Run tasks
results = orchestrator.distribute_task("Build a prediction market bot")

# Evaluate
orchestrator.evaluate_all(results, feedback={
    "researcher": {"success": True, "feedback": "Good analysis"},
    "coder": {"success": False, "feedback": "Needs better error handling"},
})

# Watch them evolve
print(orchestrator.get_collective_status())
```

## The Wrong Room Principle

```python
# Agent seeks the most challenging environment
rooms = [
    {"name": "easy", "difficulty": 0.2, "my_skill_level": 0.8},
    {"name": "medium", "difficulty": 0.5, "my_skill_level": 0.5},
    {"name": "hard", "difficulty": 0.9, "my_skill_level": 0.3},  # Wrong room!
]

chosen = agent.curiosity.seek_wrong_room(rooms)
# Agent chooses "hard" — where it's NOT the best
```

## Evolution

The agent evolves through three mechanisms:

1. **Strategy adaptation** — Successful strategies get reinforced, failing ones get mutated
2. **Memory distillation** — Episodic patterns become semantic knowledge
3. **Population evolution** — Poor strategies are removed, good ones are duplicated and varied

## Status

- v0.1 — Prototype
- No LLM integration yet (framework only)
- Pure Python, no external dependencies

## Roadmap

- [ ] LLM integration (OpenAI, Anthropic, local models)
- [ ] Semantic memory (vector embeddings)
- [ ] Tool co-evolution
- [ ] Web research capabilities
- [ ] Integration with Sakana AI Scientist
- [ ] Wrong Room Collective community features

---

Built by Sunset 🌅 for the Wrong Room Collective
