import React from 'react';
import './App.css';
import Square from './Square.js'
import { Container, Row, Col } from 'react-grid-system';
import axios from 'axios';
import Terminal from "./Terminal.js"
class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      game: undefined,
      error: undefined,
      move: undefined
    }
  }
  generate_squares = () => {
    let rows = []
    for (let x = 0; x < 5; x++) {
      let row = []
      for (let y = 0; y < 5; y++) {
        row.push(
          <Col>
            <Square x={x} y={y} location={this.state.game===undefined? undefined:this.state.game.board.locations[x][y]}/>
          </Col>
        )
      }
      rows.push(row)
    }
    return rows
  }
  async newGame(type_of_game) {
    try {
      const response = await axios.get("http://localhost:5000/api/v1/new_game",
        { params: {type_of_game: type_of_game, p1_name: "red", p2_name:"green"}})
      console.log(response.data)
      this.setState({
        game: response.data,
        error: undefined,
      });
    } catch (error) {
      // Error 
      if (error.response) {
          /*
           * The request was made and the server responded with a
           * status code that falls out of the range of 2xx
           */
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
      } else if (error.request) {
          /*
           * The request was made but no response was received, `error.request`
           * is an instance of XMLHttpRequest in the browser and an instance
           * of http.ClientRequest in Node.js
           */
          console.log(error.request);
      } else {
          // Something happened in setting up the request and triggered an Error
          console.log('Error', error.message);
      }
      console.log(error);
      this.setState({
        error: error.message,
      });
    }
  }
  updateMove = (event) => {
    this.setState({move: event.target.value});
  }

  parseMove = (moveTokens) => {
    let processedBuilder = {}
    if (moveTokens[0]==="place") {
      processedBuilder["type_of_piece"]=moveTokens[1]
      processedBuilder["x"]=moveTokens[2]
      processedBuilder["y"]=moveTokens[3]
      this.placePiece(processedBuilder)
    } else if (moveTokens[0]==="move") {
      processedBuilder["x"]=moveTokens[1]
      processedBuilder["y"]=moveTokens[2]
      let locationsToPlace = []
      for (let i = 3; i < moveTokens.length; i+=3) {
        locationsToPlace.push([[moveTokens[i],moveTokens[i+1]],moveTokens[i+2]])
      }
      processedBuilder["locations_to_place"]=locationsToPlace
      this.moveStack(processedBuilder)
    }
    return processedBuilder
  }
  async placePiece(processedMoves) {

  }
  async moveStack(processedMoves) {

  }
  async sendMove() {
    this.parseMove(this.state.move.split(" "))
  }

  render() {
    const rows = this.generate_squares()
    return (
      <Container>
        <Row>
          <Col>
            <Container style={{float:"left", backgroundColor:"white", borderColor:"brown", width: "560px"}}>
              {rows.map((value,index)=> {return <Row>{value}</Row>})}
              <Row>
                <Col>
                  <a href="#" onClick={()=>this.newGame("Human-Human")}>
                    New Human-Human Game
                  </a>
                </Col>
              </Row>
            </Container>
          </Col>
          <Col>
            <Terminal style={{float:"left", backgroundColor:"white", borderColor:"brown"}} updateMove={this.updateMove.bind(this)} sendMove={this.sendMove.bind(this)}/>
          </Col>
        </Row>
      </Container>
    )
  }
}

export default App;
