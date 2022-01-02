export const FetchResults = () => {
    // production
    // return fetch(`https://ginkgo-back-end.herokuapp.com/api/${proteinName}`)

    // development
    return fetch(`http://localhost:8000/api/results/tasks`)
        .then(res => res.json())
        .then(res => JSON.parse(res))
        .then(results => results.map(obj => (
            JSON.parse(obj.fields.result)[0]
        )))
        // .then(res => JSON.parse(res))
        .then(results => results.map(protein => ({
            proteinId: protein.id,
            DNASequence: protein.sequence,
            proteinName: protein.proteinName,
            proteinLocation: protein.proteinLocation,
            organism: protein.organism
        })))
        // .then(results => {
        //     return results
        // })
        .catch(err => console.log(err))
};

export const PostProtein = (proteinName) => {
    const formattedName = proteinName.toUpperCase();

    // production
    // return fetch(`https://ginkgo-back-end.herokuapp.com/api/${proteinName}`)

    // development
    return fetch(`http://localhost:8000/api/${formattedName}`)
        .then(results => console.log(results))
        .catch(err => console.log(err))
};
