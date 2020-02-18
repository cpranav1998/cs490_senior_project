import React from 'react';
import red_horizontal_piece from '../svgs/red_horizontal_piece.svg';
import { Stage, Layer, Rect, Text, Image } from 'react-konva';
import Konva from 'konva';
import '../App.css';


class RedHorizontalPiece extends React.Component {
  constructor(props) {
    super(props)
    this.offsetX = props.offsetX
    this.offsetY = props.offsetY
  }
  render() {
    return (
      <Rect
        width={40}
        height={40}
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

export default RedHorizontalPiece;
