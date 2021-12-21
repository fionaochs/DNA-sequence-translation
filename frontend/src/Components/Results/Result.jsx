import React from 'react';
import styles from './Result.css';

const Result = ({DNASequence, proteinName, organism, proteinLocation}) => {

    function NoSequenceResult(){
        return <div>
            <h3>Sequence '{DNASequence}'</h3>
            <h3>did not match any organisms on file</h3>
        </div>
    }
    return (
        <div className={styles.sequenceResult}>
            <h3>Found sequence '{DNASequence}'</h3>
            <h3>in protein '{proteinName}'</h3>
            <h3>in organism '{organism}'</h3>
            <h3>at location {proteinLocation}</h3>
        </div>
    );
};

export default Result;