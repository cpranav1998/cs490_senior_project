import React from 'react';
import red_capstone_piece from '../svgs/red_capstone_piece.svg';
import { Stage, Layer, Circle, Text, Image } from 'react-konva';
import Konva from 'konva';
import '../App.css';


class RedCapstonePiece extends React.Component {
  constructor(props) {
    super(props)
    this.offsetX = props.offsetX
    this.offsetY = props.offsetY
  }
  render() {
    return (
      <Circle
        radius={20}
        fill="#f56b6b"
        stroke='black'
        strokeWidth={2}
        x={this.offsetX+20}
        y={this.offsetY+20}
        _useStrictMode
      />
    );
  }
}

export default RedCapstonePiece;
