import React from 'react';
import Notice from '../components/Notice';

const ClassDetail = ({ classItem }) => {
    return (
        <div>
            <h1>{classItem.name}</h1>
            <p>{classItem.description}</p>
            <div className="notices">
                {classItem.notices.map((notice) => (
                    <Notice key={notice.id} notice={notice} />
                ))}
            </div>
            {/* Lista de alumnos y otros detalles */}
        </div>
    );
};

export default ClassDetail;
