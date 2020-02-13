import React from 'react';
import green_horizontal_piece from '../svgs/green_horizontal_piece.svg';
import '../App.css';


class GreenHorizontalPiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="GreenHorizontalPiece">
         <img src={green_horizontal_piece} className="GreenHorizontalPiece" alt="green_horizontal_piece" />
      </div>
    );
  }
}

export default GreenHorizontalPiece;
