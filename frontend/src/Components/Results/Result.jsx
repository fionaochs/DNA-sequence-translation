import React from 'react';


const Result = ({DNASequence, proteinName, organism, proteinLocation}) => {

    return (
        <div>
            <h3>Found sequence '{DNASequence}'</h3>
            <h3>in protein '{proteinName}'</h3>
            <h3>in organism '{organism}'</h3>
            <h3>at location {proteinLocation}</h3>
        </div>
    );
};

export default Result;