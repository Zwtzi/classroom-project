import React, { useState } from 'react';

const AddClassForm = ({ onAddClass }) => {
    const [className, setClassName] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onAddClass({ name: className, description });
        setClassName('');
        setDescription('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={className}
                onChange={(e) => setClassName(e.target.value)}
                placeholder="Nombre de la clase"
                required
            />
            <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Descripción"
                required
            />
            <button type="submit">Agregar Clase</button>
        </form>
    );
};

export default AddClassForm;
