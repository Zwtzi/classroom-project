const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const login = async (credentials) => {
    const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
    });
    return response.json();
};
export const fetchClases = async () => {
    try {
        const response = await fetch(`${API_URL}/classes`);
        if (!response.ok) {
            throw new Error('Error al obtener las clases');
        }
        return await response.json();
    } catch (error) {
        console.error('Error en fetchClases:', error);
        throw error;
    }
};

export const register = async (userData) => {
    const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });
    return response.json();
};

// Otras funciones para interactuar con la API
