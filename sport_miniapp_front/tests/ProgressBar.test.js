import React from 'react'; 
import { render } from '@testing-library/react'; 
// your component that you want to test 
import ProgressBar from '../src/components/ProgressBar/ProgressBar';
describe('ProgressBar', () => { 
  // test case 
  it('The element filling in progress bar is displayed correctly', () => { 
    const { getByTestId } = render(<ProgressBar />);
    const fillElement = getByTestId('fill-bar')
    expect(fillElement).toBeInTheDocument();
  }); 
});