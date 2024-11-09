// frontend/src/components/LandingPage.js

import React, { useState } from 'react';

function LandingPage({ startSimulation }) {
  const [themeInput, setThemeInput] = useState('');
  const [participantPoolInput, setParticipantPoolInput] = useState('undergrads');

  const handleStart = () => {
    if (themeInput.trim() === '') {
      alert('Please enter a hackathon theme.');
      return;
    }
    startSimulation(themeInput, participantPoolInput);
  };

  return (
    <div className="landing-page">
      <h1>Hackception</h1>
      <p>Simulate a hackathon where AI agents collaborate and compete.</p>
      <input
        type="text"
        placeholder="Enter Hackathon Theme"
        value={themeInput}
        onChange={(e) => setThemeInput(e.target.value)}
      />
      <select
        value={participantPoolInput}
        onChange={(e) => setParticipantPoolInput(e.target.value)}
      >
        <option value="graduate students">Graduate Students</option>
        <option value="undergrads">Undergraduates</option>
        <option value="high school">High School Students</option>
        <option value="MBAs">MBA Students</option>
      </select>
      <button onClick={handleStart}>Start Hackathon</button>
    </div>
  );
}

export default LandingPage;
