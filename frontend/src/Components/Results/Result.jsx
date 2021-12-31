import React from 'react';
import styles from './Result.css';

const Result = ({DNASequence, proteinName, organism, proteinLocation}) => {

    const sequenceNotFound = proteinName === undefined;

    return (
        <div className={styles.sequenceResult}>
            {sequenceNotFound ? (
                <div>
                    <h3>DNA sequence <span>{DNASequence}</span></h3>
                    <h3>did not match any organisms on file</h3>
                </div>
            ) : (
                <div>
                    <h3 className={DNASequence}>Found DNA sequence <span>{DNASequence}</span></h3>
                    <h3>at location <span>{proteinLocation}</span></h3>
                    <h3>in protein <span>{proteinName}</span></h3>
                    <h3>in organism <span>{organism}</span></h3>
                </div>
            )
            }
        </div>
    );
};

export default Result;