import React from 'react';
import red_vertical_piece from '../svgs/red_vertical_piece.svg';
import { Stage, Layer, Rect, Text, Image } from 'react-konva';
import Konva from 'konva';
import '../App.css';


class RedVerticalPiece extends React.Component {
  constructor(props) {
    super(props)
    this.offsetX = props.offsetX
    this.offsetY = props.offsetY
  }
  render() {
    return (
      <Rect
        width={40}
        height={20}
        fill="#f56b6b"
        stroke='black'
        strokeWidth={2}
        x={this.offsetX}
        y={this.offsetY}
        _useStrictMode
      />
    );
  }
}

export default RedVerticalPiece;
