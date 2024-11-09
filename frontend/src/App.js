// frontend/src/App.js

import React, { useState } from 'react';
import LandingPage from './components/LandingPage';
import ConversationView from './components/ConversationView';

function App() {
    const [simulationStarted, setSimulationStarted] = useState(false);
    const [theme, setTheme] = useState('');
    const [participantPool, setParticipantPool] = useState('');

    const startSimulation = (themeInput, participantPoolInput) => {
        setTheme(themeInput);
        setParticipantPool(participantPoolInput);
        setSimulationStarted(true);
        // Send data to backend to start simulation
        fetch('http://localhost:5000/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ theme: themeInput, participant_pool: participantPoolInput }),
        });
    };

    return (
        <div className="App">
            {!simulationStarted ? (
                <LandingPage startSimulation={startSimulation} />
            ) : (
                <ConversationView />
            )}
        </div>
    );
}

export default App;
