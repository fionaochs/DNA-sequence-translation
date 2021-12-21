import React from 'react';
import {render, cleanup} from '@testing-library/react';
import Form from './Form';

describe('Form component', () => {
    afterEach(() => cleanup());
    it('renders Form', () => {
        const {asFragment} = render(<Form/>);
        expect(asFragment()).toMatchSnapshot();
    });
    it('changes the inputted sequence value', async () => {
        render(<Form/>);
        const textInput = await screen.getByLabelText('Sequence');
screen.
        fireEvent.change(textInput, {target: {value: 'AAGTTA'}});
        await waitFor(() => {
            expect(textInput.value).toBe('AAGTTA');
        });
    });
});