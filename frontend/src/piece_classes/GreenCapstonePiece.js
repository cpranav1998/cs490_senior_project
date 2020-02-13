import React from 'react';
import green_capstone_piece from '../svgs/green_capstone_piece.svg';
import '../App.css';


class GreenCapstonePiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="GreenCapstonePiece">
         <img src={green_capstone_piece} className="GreenCapstonePiece" alt="green_capstone_piece" />
      </div>
    );
  }
}

export default GreenCapstonePiece;
