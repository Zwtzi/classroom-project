import React, { useEffect, useState } from 'react';
import { fetchClases } from '../api/api';
import ClassCard from '../components/ClassCard';

const Dashboard = () => {
    const [classes, setClasses] = useState([]);

    useEffect(() => {
        // Llamada a la API para obtener las clases
        const getClasses = async () => {
            try {
                const data = await fetchClases();
                setClasses(data);
            } catch (error) {
                console.error("Error al obtener las clases:", error);
            }
        };
        getClasses();
    }, []);

    return (
        <div>
            <h1>Panel Principal</h1>
            <div className="classes-container">
                {classes.map((classItem) => (
                    <ClassCard key={classItem.id} classItem={classItem} />
                ))}
            </div>
        </div>
    );
};

export default Dashboard;
