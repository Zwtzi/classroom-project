import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { apiLogin } from '../api/api';  // Asegúrate de que esta función exista en api.js

const Login = ({ onLogin = async () => false }) => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(''); // Declarar el estado para el error

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(''); // Limpiar error previo

        // Realizar la autenticación a través de la API
        const success = await apiLogin({ email, password });
        if (success) {
            navigate('/dashboard');
        } else {
            setError('Usuario o contraseña incorrectos');
        }
    };

    return (
        <div>
            <h1>Iniciar Sesión</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Correo electrónico"
                    required
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Contraseña"
                    required
                />
                <button type="submit">Ingresar</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <p>
                ¿No tienes una cuenta? <Link to="/register">Regístrate aquí</Link>
            </p>
        </div>
    );
};

export default Login;
