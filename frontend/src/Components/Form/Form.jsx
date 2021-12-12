import React, { useState } from 'react';

const Form = () => {
    const [proteinName, setProteinName] = useState('');

    return (
        <form>
            <input type="text" value={proteinName} onChange={({ target }) => setProteinName(target.value)} placeholder="Protein sequence"/>
            <button>Find protein</button>
        </form>
    );
};

export default Form;