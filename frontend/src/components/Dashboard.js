import React from 'react';
import ClassCard from './ClassCard';

const Dashboard = ({ classes }) => {
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
