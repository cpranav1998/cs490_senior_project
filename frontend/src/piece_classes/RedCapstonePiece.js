import React from 'react';
import red_capstone_piece from '../svgs/red_capstone_piece.svg';
import '../App.css';


class RedCapstonePiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="RedCapstonePiece">
         <img src={red_capstone_piece} className="RedCapstonePiece" alt="red_capstone_piece" />
      </div>
    );
  }
}

export default RedCapstonePiece;
