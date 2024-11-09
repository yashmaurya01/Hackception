# backend/agents/participant_agent.py

from agents.agent_base import AgentBase

class ParticipantAgent(AgentBase):
    def __init__(self, name, role, persona, team_id):
        super().__init__(name, role, persona)
        self.team_id = team_id
        self.special_skill = persona['special_skill']

    def work_on_task(self, task_description):
        prompt = f"As a {self.role} with expertise in {self.special_skill}, " \
                 f"and attributes {', '.join(self.persona['attributes'])}, " \
                 f"please {task_description}"
        return self.generate_response(prompt)
