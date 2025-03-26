import React from 'react';

const Notice = ({ notice }) => {
    return (
        <div className="notice">
            <h3>{notice.title}</h3>
            <p>{notice.content}</p>
            {/* Otros detalles del aviso */}
        </div>
    );
};

export default Notice;
