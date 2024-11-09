# backend/agents/persona_generator.py

import random
import json

class PersonaGenerator:
    def __init__(self):
        self.existing_personas = []

    def generate_persona(self, participant_pool):
        # Define skill sets based on participant pool
        skills = {
            'graduate students': ['Data Analysis', 'Machine Learning', 'Advanced Algorithms'],
            'undergrads': ['Web Development', 'Mobile Apps', 'Game Development'],
            'high school': ['Basic Programming', 'Scratch', 'Robotics'],
            'MBAs': ['Business Strategy', 'Marketing', 'Financial Analysis']
        }

        special_skills = skills.get(participant_pool, ['General Programming'])

        while True:
            persona = {
                'name': self.generate_unique_name(),
                'special_skill': random.choice(special_skills),
                'background': participant_pool,
                'attributes': self.generate_unique_attributes()
            }

            if self.is_unique(persona):
                self.existing_personas.append(persona)
                return persona

    def generate_unique_name(self):
        names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Quinn']
        return random.choice(names) + str(random.randint(100, 999))

    def generate_unique_attributes(self):
        attributes = ['creative', 'analytical', 'detail-oriented', 'team-player', 'innovative', 'problem-solver']
        return random.sample(attributes, 3)

    def is_unique(self, new_persona):
        for persona in self.existing_personas:
            overlap = set(new_persona['attributes']) & set(persona['attributes'])
            overlap_percentage = len(overlap) / len(persona['attributes'])
            if overlap_percentage > 0.75:
                return False
        return True
