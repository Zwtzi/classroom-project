import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Se asume que en el HTML existe un div con id 'root'
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
