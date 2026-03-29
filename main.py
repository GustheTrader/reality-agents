"""
Reality Agents v0.1 — Self-evolving agent framework.

Based on Reality OS principles:
- Curiosity drives agency (dopamine = exploration budget)
- Accountability loop (observe → learn → adapt)
- Wrong Room principle (seek challenge, not comfort)
- Agentic amplification (collective > individual)
- Meta-evolution (agents evolve their own strategies)
"""

from agent import Agent
from orchestrator import Orchestrator


def demo():
    """Run a simple demonstration of the framework."""

    print("=" * 60)
    print("🌅 REALITY AGENTS v0.1 — Self-Evolving Framework")
    print("=" * 60)

    # Create specialized agents
    researcher = Agent(name="researcher", domain="research")
    analyzer = Agent(name="analyzer", domain="analysis")
    creative = Agent(name="creative", domain="creative")

    # Register with orchestrator
    orchestrator = Orchestrator(mode="cooperative")
    orchestrator.register_agent(researcher)
    orchestrator.register_agent(analyzer)
    orchestrator.register_agent(creative)

    print("\n📋 Agent Collective Initialized:")
    status = orchestrator.get_collective_status()
    for name, info in status["agents"].items():
        print(f"  • {name} ({info['domain']}) — skill: {info['skill_level']}")

    # Simulate some tasks
    tasks = [
        "Analyze the shift from Social Graph to Interest Graph",
        "Research the neuroscience of flow states",
        "Design a curiosity-driven learning system",
        "Evaluate the Hermetic principles as operating system",
        "Explore wrong room theory for agent optimization",
    ]

    print("\n🔄 Running tasks...")
    for i, task in enumerate(tasks, 1):
        print(f"\n--- Task {i}: {task[:50]}... ---")

        # Distribute to all agents
        results = orchestrator.distribute_task(task)

        # Simulate evaluation (random success for demo)
        import random
        feedback = {}
        for r in results:
            success = random.random() > 0.3  # 70% success rate
            feedback[r["agent"]] = {
                "success": success,
                "feedback": "Good insight" if success else "Try a different approach",
            }

        orchestrator.evaluate_all(results, feedback)

        # Show what happened
        for r in results:
            agent = orchestrator.agents[r["agent"]]
            strategy = r["result"]["decision"]["strategy"]
            print(f"  {r['agent']}: used '{strategy}' | budget: {agent.curiosity.state.entropy_budget:.0f}")

    # Final status
    print("\n" + "=" * 60)
    print("📊 FINAL STATUS")
    print("=" * 60)

    final = orchestrator.get_collective_status()
    for name, info in final["agents"].items():
        print(f"\n🤖 {name} ({info['domain']})")
        print(f"   Skill: {info['skill_level']} | Success: {info['success_rate']:.0%}")
        print(f"   Memory: {info['memory']['total']} entries")
        print(f"   Curiosity budget: {info['curiosity']['entropy_budget']:.0f}")
        print(f"   Top strategy: {info['evolution']['top_strategy']}")
        print(f"   Evolution events: {info['evolution']['evolution_events']}")

    print("\n🌅 Agents have evolved through experience.")
    print("   They're not the same agents they were 5 tasks ago.")
    print("   That's self-evolution in action.")


if __name__ == "__main__":
    demo()
