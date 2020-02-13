import React from 'react';
import red_vertical_piece from '../svgs/red_vertical_piece.svg';
import '../App.css';


class RedVerticalPiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="RedVerticalPiece">
         <img src={red_vertical_piece} className="RedVerticalPiece" alt="red_vertical_piece" />
      </div>
    );
  }
}

export default RedVerticalPiece;
