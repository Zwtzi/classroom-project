import React from 'react';

const ClassCard = ({ classItem }) => {
    return (
        <div className="class-card">
            <h2>{classItem.name}</h2>
            <p>{classItem.description}</p>
            {/* Otros detalles de la clase */}
        </div>
    );
};

export default ClassCard;
