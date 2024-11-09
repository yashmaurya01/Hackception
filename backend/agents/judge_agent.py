# backend/agents/judge_agent.py

from agents.agent_base import AgentBase

class JudgeAgent(AgentBase):
    def __init__(self, name, judging_criteria):
        super().__init__(name, 'Judge', {})
        self.judging_criteria = judging_criteria

    def evaluate_project(self, project_submission):
        prompt = f"Evaluate the following project based on the criteria {self.judging_criteria}:\n\n{project_submission}"
        return self.generate_response(prompt)
