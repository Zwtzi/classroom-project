import React, { useState } from 'react';
import { registerUser } from "../api/api";

const Register = ({ onRegister }) => {
    const [nombre, setNombre] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [userType, setUserType] = useState('alumno'); // Valor por defecto

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert('Las contraseñas no coinciden');
            return;
        }
        try {
            // Se utiliza registerUser para hacer la petición a la ruta correcta (/auth/register)
            const response = await registerUser({ nombre, email, password, tipo: userType });
            console.log('Registro exitoso', response);
            // Puedes utilizar la función onRegister si la necesitas para actualizar el estado o redirigir
            if (onRegister) onRegister(response);
        } catch (error) {
            console.error('Error en el registro', error);
            // Aquí puedes agregar manejo adicional del error, como mostrar un mensaje al usuario
        }
    };

    return (
        <div>
            <h1>Registro</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)}
                    placeholder="Nombre completo"
                    required
                />
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
                            value="profesor"
                            checked={userType === 'profesor'}
                            onChange={(e) => setUserType(e.target.value)}
                        />
                        Profesor
                    </label>
                </div>
                <button type="submit">Registrarse</button>
            </form>
        </div>
    );
};

export default Register;
