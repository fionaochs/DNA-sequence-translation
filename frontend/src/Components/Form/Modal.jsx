import React from 'react'
import styles from './Form.css';

const SearchModal = ({DNASequence}) => {

    return (
        <div className={styles.modalDiv}>
            <h3>Starting async task to find your protein with submitted sequence <span>{DNASequence}</span></h3>
            <h3>Close modal and hit <span>Get results</span> to see your results</h3>
        </div>
    )

}

export default SearchModal;