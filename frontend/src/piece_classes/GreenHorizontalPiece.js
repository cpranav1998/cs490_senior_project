import React from 'react';
import green_horizontal_piece from '../svgs/green_horizontal_piece.svg';
import { Stage, Layer, Rect, Text, Image } from 'react-konva';
import Konva from 'konva';
import '../App.css';


class GreenHorizontalPiece extends React.Component {
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
        fill="#51bd55"
        stroke='black'
        strokeWidth={2}
        x={this.offsetX}
        y={this.offsetY}
        _useStrictMode
      />
    );
  }
}

export default GreenHorizontalPiece;
