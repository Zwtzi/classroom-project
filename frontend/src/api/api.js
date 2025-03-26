const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000"; // Usa variable de entorno o localhost

// 🟢 Función para registrar usuario
export const registerUser = async (userData) => {
    const response = await fetch(`${API_URL}/auth/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
    });

    if (!response.ok) {
        throw new Error("Error en el registro");
    }

    return response.json();
};

// 🟢 Función para iniciar sesión
export const login = async (credentials) => {
    const response = await fetch(`${API_URL}/auth/login`, { // Corregido: Agregado `/auth`
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
    });

    if (!response.ok) {
        throw new Error("Error en el inicio de sesión");
    }

    return response.json();
};

// 🟢 Función para obtener clases
export const fetchClases = async () => {
    try {
        const response = await fetch(`${API_URL}/classes`);
        if (!response.ok) {
            throw new Error("Error al obtener las clases");
        }
        return await response.json();
    } catch (error) {
        console.error("Error en fetchClases:", error);
        throw error;
    }
};

export const apiLogin = async ({ email, password }) => {
    try {
        const response = await fetch('http://localhost:8000/auth/login', {  // Ajusta la URL a tu API
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            return true;  // El login fue exitoso
        } else {
            console.error(data.message);
            return false;  // El login falló
        }
    } catch (error) {
        console.error('Error en la solicitud:', error);
        return false;
    }
};
