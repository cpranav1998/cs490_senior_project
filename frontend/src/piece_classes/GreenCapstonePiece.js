import React from 'react';
import green_capstone_piece from '../svgs/green_capstone_piece.svg';
import { Stage, Layer, Circle, Text, Image } from 'react-konva';
import Konva from 'konva';
import '../App.css';


class GreenCapstonePiece extends React.Component {
  constructor(props) {
    super(props)
    this.offsetX = props.offsetX
    this.offsetY = props.offsetY
  }
  render() {
    return (
      <Circle
        draggable
        radius={20}
        fill="#51bd55"
        stroke='black'
        strokeWidth={2}
        x={this.offsetX+20}
        y={this.offsetY+20}
        _useStrictMode
      />
    );
  }
}

export default GreenCapstonePiece;
