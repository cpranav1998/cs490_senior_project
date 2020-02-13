import React from 'react';
import green_vertical_piece from '../svgs/green_vertical_piece.svg';
import '../App.css';


class GreenVerticalPiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="GreenVerticalPiece">
         <img src={green_vertical_piece} className="GreenVerticalPiece" alt="green_vertical_piece" />
      </div>
    );
  }
}

export default GreenVerticalPiece;
