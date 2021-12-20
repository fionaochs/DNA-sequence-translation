import React from 'react';


const Result = ({DNASequence, proteinName, organism, proteinLocation}) => {

    function NoSequenceResult(){
        return <div>
            <h3>Sequence '{DNASequence}'</h3>
            <h3>did not match any organisms</h3>
        </div>
    }
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