// frontend/src/components/ConversationView.js

import React, { useState, useEffect } from 'react';

function ConversationView() {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const eventSource = new EventSource('http://localhost:5000/stream');
        eventSource.onmessage = (e) => {
            const data = JSON.parse(e.data);
            setMessages((prevMessages) => [...prevMessages, data]);
        };
        return () => {
            eventSource.close();
        };
    }, []);

    return (
        <div className="conversation-view">
            <h2>Live Conversations</h2>
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className="message">
                        <strong>{msg.sender}</strong>: {msg.content}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ConversationView;
