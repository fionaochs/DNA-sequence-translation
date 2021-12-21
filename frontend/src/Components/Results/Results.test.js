import React from 'react';
import {render, screen, fireEvent, waitFor, cleanup} from '@testing-library/react';
import Results from './Results';

describe('Rating component', () => {
    afterEach(() => cleanup());
    it('renders Rating', () => {
        const {asFragment} = render(<Results/>);
        expect(asFragment()).toMatchSnapshot();
    });

    it('changes the the list of results', async () => {
        render(<Results/>);
        const textInput = await screen.findByText('Results');
        expect(textInput).toBeInTheDocument();
    });
});