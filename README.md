# Hackception: A Multi-Agent Hackathon Simulator

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Simulation Parameters](#simulation-parameters)
  - [Running the Simulation](#running-the-simulation)
  - [Intermediate Checkpoints](#intermediate-checkpoints)
- [Frontend Interface](#frontend-interface)
  - [Landing Page](#landing-page)
  - [Live Streaming Conversations](#live-streaming-conversations)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Hackception is an AI-driven hackathon simulator where all participants, organizers, and judges are GPT-based AI agents. The simulator creates a virtual hackathon environment where AI teams collaborate on projects, code solutions, and present demos, all while interacting with AI organizers and being evaluated by AI judges.

## Features
- **Customizable Hackathon Setup**: Define the number of participants, team sizes, themes, judging criteria, and update intervals.
- **AI Participant Teams**: Simulate teams working collaboratively on projects, including planning, coding, and presenting.
- **Role Assignment**: Each team member assumes a specific role—Frontend Developer, Backend Developer, or ML Engineer.
- **Unique Personas**:
  - Agents have creative personas with expertise and unique special skills.
  - A dedicated agent generates these personas, ensuring less than 75% overlap between any two agents.
- **AI Organizers**: Manage event logistics, collect updates, enforce deadlines, and facilitate communication.
- **AI Judges**: Evaluate projects based on predefined criteria, providing rankings and detailed feedback.
- **Communication Logging**: All interactions are recorded in separate channels for transparency and review.
- **Multi-Stage Simulation**: The hackathon progresses through stages with clear checkpoints, mimicking a real event.
- **Frontend Visualization**:
  - **Landing Page**: Displays a high-level project overview with engaging graphics.
  - **User Input**: Allows users to input the theme and participant pool information (e.g., graduate students, undergrads, high school, MBAs).
  - **Live Streaming**: Agent conversations are streamed live on the UI.

## Getting Started
### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for frontend)
- OpenAI API Key
- Git (for cloning the repository)
- Virtual Environment (recommended)

### Installation
#### Backend Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hackception.git
   cd hackception
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

#### Frontend Setup
1. **Navigate to Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

## Usage
### Simulation Parameters
Configure the simulation parameters in the `config.yaml` file:
- `number_of_participants`: Total AI participants (e.g., 30).
- `team_size`: Maximum team size (up to 3).
- `participant_pool`: Participant background (e.g., graduate students, undergrads, high school, MBAs).
- `hackathon_theme`: The theme or problem statement for the projects.
- `judging_criteria`: Criteria for evaluating projects (e.g., Innovation, Feasibility, Presentation).
- `update_rounds`: Number of hourly updates required from teams.

### Running the Simulation
#### Backend
1. **Configure Parameters**
   Edit the `config.yaml` file to set your desired parameters.

2. **Start the Backend Server**
   ```bash
   python main.py
   ```

#### Frontend
1. **Start the Frontend Server**
   ```bash
   cd frontend
   npm start
   ```

2. **Access the Application**
   Open your web browser and navigate to `http://localhost:3000`.

### Intermediate Checkpoints
The simulation progresses through the following stages:
1. **Team Formation**
   - Participants are grouped into teams of up to 3 members.
   - Each team has members with roles: Frontend Developer, Backend Developer, and ML Engineer.
   - A dedicated agent generates unique personas with special skills for each participant, ensuring less than 75% overlap with existing personas.

2. **Project Ideation**
   - Teams brainstorm project ideas aligning with the hackathon theme.
   - Each team submits a project proposal to the organizers.

3. **Planning and Assignment**
   - Teams plan their project roadmap.
   - Roles are assigned specific tasks based on their expertise and unique skills.

4. **Development Phase**
   - Teams begin coding and developing their projects.
   - Focus on creating a Minimum Viable Product (MVP).

5. **Hourly Updates**
   - Teams submit updates to organizers at each interval.
   - Organizers provide feedback or assistance as needed.

6. **Final Submission**
   - Teams submit their final projects before the deadline.
   - Submissions include code, documentation, and a presentation/demo.

7. **Judging**
   - Judges evaluate projects based on the criteria.
   - Detailed feedback and scores are provided for each team.

8. **Results Announcement**
   - The top 3 teams are announced.
   - Overall feedback is shared with all participants.

## Frontend Interface
### Landing Page
- **Overview**: Displays a high-level summary of the hackathon with engaging graphics.
- **User Input**:
  - **Hackathon Theme**: Enter the theme or problem statement for the hackathon.
  - **Participant Pool**: Select the participant background (e.g., graduate students, undergrads).

### Live Streaming Conversations
- **Team Channels**: View conversations between team members.
- **Organizer Channel**: See updates and communications with organizers.
- **Judge Channel**: Post-hackathon evaluations and feedback.

### Usage Instructions
1. **Navigate to the Landing Page**
   Open `http://localhost:3000` in your browser.

2. **Input Hackathon Details**
   - Enter the hackathon theme.
   - Select the participant pool.

3. **Start the Hackathon**
   - Click the "Start Hackathon" button to trigger the simulation.

4. **Monitor the Simulation**
   - Watch live-streamed conversations between agents.
   - Switch between different channels to view team collaborations and updates.

## Project Structure
- **backend/**: Contains backend code and agent classes.
  - **agents/**: AI agent classes for participants, organizers, and judges.
  - **persona_generator.py**: Agent responsible for creating unique personas.
  - **main.py**: Main script to run the backend server.
  - **config.yaml**: Configuration file for simulation parameters.
  - **logs/**: Stores communication logs and outputs.
- **frontend/**: Contains frontend React application.
  - **src/**: Source code for the UI components.
  - **components/**: React components for different UI elements.
  - **styles/**: CSS and styling files.
  - **App.js**: Main React application.
  - **public/**: Static files and assets.
- **requirements.txt**: Python dependencies.
- **package.json**: Frontend dependencies.
- **README.md**: Project documentation.
- **LICENSE**: Project license information.

## Contributing
Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yashmaurya01/hackception.git
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Make Changes**
   - Implement your feature or fix.

5. **Commit Changes**
   ```bash
   git commit -m "Add YourFeature"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/YourFeature
   ```

7. **Submit a Pull Request**
   - Go to the original repository and click "New Pull Request".

## License
This project is licensed under the MIT License - see the LICENSE file for details.


