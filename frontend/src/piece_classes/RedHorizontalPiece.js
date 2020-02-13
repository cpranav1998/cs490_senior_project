import React from 'react';
import red_horizontal_piece from '../svgs/red_horizontal_piece.svg';
import '../App.css';


class RedHorizontalPiece extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="RedHorizontalPiece">
         <img src={red_horizontal_piece} className="RedHorizontalPiece" alt="red_horizontal_piece" />
      </div>
    );
  }
}

export default RedHorizontalPiece;
