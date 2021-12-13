import React from 'react';


const Result = ({ proteinName, proteinLocation }) => {

    return (
        <div>
            <h2>Protein</h2>
            <h2>{proteinName}</h2>
            <h2>{proteinLocation}</h2>
        </div>
    );
};

export default Result;