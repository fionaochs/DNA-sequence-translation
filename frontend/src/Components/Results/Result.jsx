import React from 'react';
import styles from './Result.css';

const Result = ({DNASequence, proteinName, organism, proteinLocation}) => {

    const sequenceNotFound = proteinLocation === undefined;

    return (
        <div className={styles.sequenceResult}>
            {sequenceNotFound ? (
                <div>
                    <h3>Sequence '{DNASequence}'</h3>
                    <h3>did not match any organisms on file</h3>
                </div>
            ) : (
                <div>
                    <h3 className={DNASequence}>Found sequence</h3>
                    <h3>'{DNASequence}'</h3>
                    <h3>with amino acid code '{proteinName}'</h3>
                    <h3>in organism '{organism}'</h3>
                    <h3>at location {proteinLocation}</h3>
                </div>
            )
            }
        </div>
    );
};

export default Result;