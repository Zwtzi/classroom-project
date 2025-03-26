import React, { useState } from 'react';

const Register = ({ onRegister }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [userType, setUserType] = useState('alumno'); // Valor por defecto

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password === confirmPassword) {
            onRegister({ email, password, userType });
        } else {
            alert('Las contraseñas no coinciden');
        }
    };

    return (
        <div>
            <h1>Registro</h1>
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
                <input
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="Confirmar Contraseña"
                    required
                />
                <div>
                    <label>
                        <input
                            type="radio"
                            name="userType"
                            value="alumno"
                            checked={userType === 'alumno'}
                            onChange={(e) => setUserType(e.target.value)}
                        />
                        Alumno
                    </label>
                    <label>
                        <input
                            type="radio"
                            name="userType"
                            value="maestro"
                            checked={userType === 'maestro'}
                            onChange={(e) => setUserType(e.target.value)}
                        />
                        Maestro
                    </label>
                </div>
                <button type="submit">Registrarse</button>
            </form>
        </div>
    );
};

export default Register;
