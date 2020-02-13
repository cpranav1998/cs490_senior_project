import React from 'react';
import square from './svgs/square.svg';
import GreenCapstonePiece from './piece_classes/GreenCapstonePiece.js';
import RedCapstonePiece from './piece_classes/RedCapstonePiece.js';
import GreenVerticalPiece from './piece_classes/GreenVerticalPiece.js';
import RedVerticalPiece from './piece_classes/RedVerticalPiece.js';
import GreenHorizontalPiece from './piece_classes/GreenHorizontalPiece.js';
import RedHorizontalPiece from './piece_classes/RedHorizontalPiece.js';
import './App.css';


class Square extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      location: props.location
    }
  }
  get_piece_types = () => {
    return this.state.location.pieces.map(x => [x.type,x.player.name])
  }
  generate_piece_components = () => {
    let elements = []
    for (const piece in this.get_piece_types()) {
      if (piece.type==="vertical" && piece.name==="red") {
        elements.append(<RedVerticalPiece/>)
      } else if (piece.type==="vertical" && piece.name==="green") {
        elements.append(<GreenVerticalPiece/>)
      } else if (piece.type==="horizontal" && piece.name==="red") {
        elements.append(<RedHorizontalPiece/>)
      } else if (piece.type==="horizontal" && piece.name==="green") {
        elements.append(<GreenHorizontalPiece/>)
      } else if (piece.type==="capstone" && piece.name==="red") {
        elements.append(<RedCapstonePiece/>)
      } else if (piece.type==="capstone" && piece.name==="green") {
        elements.append(<GreenCapstonePiece/>)
      }
    }
    return elements
  }
  render() {
    return (
      <div className="Square">
         <img src={square} className="Square" alt="square" />
      </div>
    );
  }
}

export default Square;
