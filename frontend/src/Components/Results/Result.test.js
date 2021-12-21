import React from 'react';
import {render, screen, fireEvent, waitFor, cleanup} from '@testing-library/react';
import Result from './Result';

describe('Rating component', () => {
    afterEach(() => cleanup());
    it('renders Result', () => {
        let result = {};
        const {asFragment} = render(<Result result={result}/>);
        expect(asFragment()).toMatchSnapshot();
    });

    it('changes the result form when new result submitted', async () => {
        // const {container} = render(<Result />);
        // const DNASequence = container.querySelector('DNASequence')
        const DNASequence = await screen.getByDisplayValue('DNASequence');

        // fireEvent.change(container.firstChild.value, {target: {value: 'AACGTTA'}});
        // await waitFor(() => {
        //     expect(container.firstChild).toBe('AACGTTA');
        // });
        fireEvent.change(DNASequence, {target: {value: 'AACGTTA'}});
        await waitFor(() => {
            expect(DNASequence.value).toBe('AACGTTA');
        });
    });
    it('find result text in display', async () => {
        render(<Result />);
        const linkElement = screen.getByText(/Found sequence/i);
        expect(linkElement).toBeInTheDocument();
    });
});