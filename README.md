# Agent Skills Treasure

## 📖 Overview
Agent Skills Treasure is a centralized repository for sharing skills and agent documentation files in markdown format. It provides a structured and organized resource for different agents, ensuring clarity, consistency, and ease of collaboration across implementations.

## 🎯 Purpose
The repository is designed to:
- Maintain a unified collection of agent-related skills and documentation.
- Serve as a reference point for developers working with multiple agents.
- Encourage standardized practices for documenting agent capabilities.

## 📂 Repository Structure
```
/skills/ → Skill-specific markdown files
/agents/ → Documentation files for different agents
README.md → Project overview and usage guidelines
```

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/Pratham-31s/agent-skills-treasure.git
```
2. Navigate to the project directory:
```bash
cd agent-skills-treasure
```
3. Explore the `skills` and `agents` folders to access documentation.

## 🛠️ Usage Examples
### Referencing a Skill in an Agent System Prompt
You can directly reference or inject these standardized markdown skill files into your agent's system instructions or context window:

```python
def load_agent_skill(skill_name):
    path = f"./skills/{skill_name}.md"
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Example: Injecting a specific skill into the system prompt
coding_skill = load_agent_skill("python-interpreter")
system_prompt = f"You are a helpful AI assistant.\\n\\nHere are your available capabilities:\\n{coding_skill}"
```

### Formatting Agent Instructions
When creating a new file under `/agents/`, follow this standardized blueprint:
```markdown
# Agent Name

## Core Role
[Brief description of the agent's primary identity and objective]

## Enabled Skills
- [Skill Name 1](../skills/skill-name-1.md)
- [Skill Name 2](../skills/skill-name-2.md)

## Behavior & Constraints
- Always use active voice.
- Do not make assumptions without checking data.
```

## 📝 Contribution Guidelines
Contributions are welcome to expand and refine this repository:
- Ensure markdown files are well-structured and consistent.
- Follow naming conventions for clarity.
- Submit pull requests with clear descriptions of changes.

## 📌 License
This repository is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Acknowledgments
Thanks to contributors and collaborators who help maintain and improve this resource for the community.
