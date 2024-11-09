# backend/main.py

import yaml
import threading
import time
import random
from agents.persona_generator import PersonaGenerator
from agents.participant_agent import ParticipantAgent
from agents.organizer_agent import OrganizerAgent
from agents.judge_agent import JudgeAgent
from server import add_message

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def run_simulation(theme_input=None, participant_pool_input=None):
    config = load_config()
    if theme_input:
        config['hackathon_theme'] = theme_input
    if participant_pool_input:
        config['participant_pool'] = participant_pool_input

    participant_pool = config['participant_pool']
    num_participants = config['number_of_participants']
    team_size = config['team_size']
    hackathon_theme = config['hackathon_theme']
    judging_criteria = config['judging_criteria']
    update_rounds = config['update_rounds']

    # Initialize organizer
    organizer = OrganizerAgent(name="Organizer")

    # Generate personas
    persona_generator = PersonaGenerator()
    participants = []
    roles = ['Frontend Developer', 'Backend Developer', 'ML Engineer']
    for i in range(num_participants):
        persona = persona_generator.generate_persona(participant_pool)
        role = roles[i % len(roles)]
        participant = ParticipantAgent(name=persona['name'], role=role, persona=persona, team_id=None)
        participants.append(participant)

    # Form teams
    teams = {}
    for i in range(0, len(participants), team_size):
        team_members = participants[i:i+team_size]
        team_id = f"Team_{i//team_size + 1}"
        for member in team_members:
            member.team_id = team_id
        teams[team_id] = team_members
        organizer.teams[team_id] = team_members

    # Project Ideation and Planning
    for team_id, team_members in teams.items():
        idea_prompt = f"Collaboratively brainstorm a project idea for the theme: {hackathon_theme}"
        for member in team_members:
            idea = member.generate_response(idea_prompt)
            # print(f"{member.name} ({member.role}) from {team_id} suggests: {idea}")
            add_message(f"{member.name} ({member.role}) from {team_id}", idea)

    # Development Phase with Updates
    for round_num in range(update_rounds):
        print(f"\n--- Update Round {round_num + 1} ---\n")
        update_prompt = organizer.broadcast_message("Please provide your hourly update on the project progress.")
        for team_id, team_members in teams.items():
            for member in team_members:
                task_description = f"work on your assigned tasks for the project."
                update = member.work_on_task(task_description)
                # print(f"{member.name} ({member.role}) from {team_id} updates: {update}")
                add_message(f"{member.name} ({member.role}) from {team_id}", update)

        time.sleep(1)  # Simulate time between updates

    # Final Submission
    project_submissions = {}
    for team_id, team_members in teams.items():
        submission = ""
        for member in team_members:
            submission += member.work_on_task("finalize your part and compile the project documentation.\n")
        project_submissions[team_id] = submission

    # Judging
    judges = [JudgeAgent(name=f"Judge_{i+1}", judging_criteria=judging_criteria) for i in range(3)]
    results = {}
    for team_id, submission in project_submissions.items():
        total_score = 0
        for judge in judges:
            evaluation = judge.evaluate_project(submission)
            # print(f"{judge.name} evaluates {team_id}: {evaluation}")
            add_message(f"{judge.name} evaluates {team_id}", evaluation)
            # Parse evaluation to extract scores (simplified for this example)
            score = random.uniform(1, 10)
            total_score += score
        average_score = total_score / len(judges)
        results[team_id] = average_score

    # Announce Winners
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    # print("\n--- Hackathon Results ---\n")
    for rank, (team_id, score) in enumerate(sorted_results[:3], start=1):
        # print(f"Rank {rank}: {team_id} with average score {score:.2f}")
        add_message(f"Hackathon Results", f"Rank {rank}: {team_id} with average score {score:.2f}")

if __name__ == "__main__":
    run_simulation()
