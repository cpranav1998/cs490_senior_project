import React from 'react';
import square from './svgs/square.svg';
import { Stage, Layer, Rect, Text, Image } from 'react-konva';
import Konva from 'konva';
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
      bounding_rectangle: undefined,
      location: props.location
    }
  }
  get_piece_types = () => {
    return this.state.location.pieces.map(x => [x.type,x.player.name])
  }
  generate_piece_components = () => {
    if(this.state.location===undefined) {
      return
    }
    let offsetX = 3
    let offsetY = 3
    let elements = []
    this.get_piece_types().forEach(piece => {
      if (piece[0]==="vertical" && piece[1]==="red") {
        elements.push(<RedVerticalPiece offsetX={offsetX} offsetY={offsetY}/>)
      } else if (piece[0]==="vertical" && piece[1]==="green") {
        elements.push(<GreenVerticalPiece offsetX={offsetX} offsetY={offsetY}/>)
      } else if (piece[0]==="horizontal" && piece[1]==="red") {
        elements.push(<RedHorizontalPiece offsetX={offsetX} offsetY={offsetY}/>)
      } else if (piece[0]==="horizontal" && piece[1]==="green") {
        elements.push(<GreenHorizontalPiece offsetX={offsetX} offsetY={offsetY}/>)
      } else if (piece[0]==="capstone" && piece[1]==="red") {
        elements.push(<RedCapstonePiece offsetX={offsetX} offsetY={offsetY}/>)
      } else if (piece[0]==="capstone" && piece[1]==="green") {
        elements.push(<GreenCapstonePiece offsetX={offsetX} offsetY={offsetY}/>)
      }
      offsetX+=3
      offsetY+=3
    })
    return elements
  }
  render() {
    return (
      <div className="SquareDiv" style={{zIndex: 0, position: "relative"}}>
        <Stage width={80} height={80}>
          <Layer>
            <Rect
              width={70}
              height={70}
              fill="#cbd38c"
              stroke='black'
              strokeWidth={2}
              x={0}
              y={0}
              _useStrictMode
            />
            {this.generate_piece_components()}
          </Layer>
        </Stage>
      </div>
    );
  }
}

export default Square;
