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
