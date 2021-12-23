import React from 'react';
import {render, screen, fireEvent, waitFor, cleanup} from '@testing-library/react';
import Results from './Results';

describe('Rating component', () => {
    afterEach(() => cleanup());
    it('renders Results list', () => {
        const {asFragment} = render(<Results/>);
        expect(asFragment()).toMatchSnapshot();
    });
});