import React from 'react'; 
import { render } from '@testing-library/react'; 
// your component that you want to test 
import BarContainer from '../src/components/BarsContainer/BarContainer';
describe('BarContainer', () => { 
  // test case 
  it('Progress bars displaying properly', () => { 
    const { getByTestId } = render(<BarContainer />);
    const barElement = getByTestId('list-of-two-progress-bars')
    expect(barElement).toBeInTheDocument();
  }); 
});