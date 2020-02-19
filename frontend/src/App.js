import React from 'react';
import './App.css';
import ReactTooltip from 'react-tooltip'
import Square from './Square.js'
import { Container, Row, Col } from 'react-grid-system';
import { Element } from 'react-scroll'
import axios from 'axios';
import Terminal from "./Terminal.js"
import takLogo from './takLogo.png';
/*

*/
class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      game: undefined,
      error: undefined,
      move: undefined,
      rows: [],
      terminal_elements: []
    }
  }
  generate_squares() {
    let rows = []
    for (let x = 0; x < 5; x++) {
      let row = []
      for (let y = 0; y < 5; y++) {
        row.push(
          <Col key={`col${x}${y}`}>
            <a
              data-tip={`x:${x}\ny:${y}`}
            >
              <Square 
                key={`square${x}${y}`} 
                x={x} 
                y={y} 
                location={this.state.game===undefined? undefined:this.state.game.board.locations[x][y]} 
                style={{position: "relative"}}
              />
            </a>
            <ReactTooltip />
          </Col>
        )
      }
      rows.push(row)
    }
    return rows
  }
  componentDidUpdate() {
    console.log(this.state)
  }
  async newGame(type_of_game) {
    try {
      const response = await axios.get("http://localhost:5000/api/v1/new_game",
        { params: {type_of_game: type_of_game, p1_name: "red", p2_name:"green"}})
      console.log(response.data)
      if("error" in response.data) {
        this.setState({
          error: response.data.error,
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
        })
      } else {
        this.setState({
          game: response.data,
          error: undefined,
          rows: []
        });
        this.setState({
          rows: this.generate_squares()
        });
        this.setState({
          terminal_elements: [`New ${type_of_game} Game!`]
        })
      }
    } catch (error) {
      console.log(error);
      this.setState({
        error: error.message,
      });
      this.setState({
        terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
      })
    }
  }
  updateMove = (event) => {
    this.setState({move: event.target.value});
  }

  parseMove(moveTokens) {
    let processedBuilder = {player: "player"}
    if (moveTokens[0]==="place") {
      processedBuilder["type_of_piece"]=moveTokens[1]
      processedBuilder["x"]=moveTokens[2]
      processedBuilder["y"]=moveTokens[3]
      processedBuilder["place_piece"]=0
      this.placePiece(processedBuilder)
    } else if (moveTokens[0]==="move") {
      processedBuilder["x"]=moveTokens[1]
      processedBuilder["y"]=moveTokens[2]
      processedBuilder["number"]=moveTokens[3]
      let locationsToPlace = []
      for (let i = 4; i < moveTokens.length; i+=3) {
        locationsToPlace.push(`${moveTokens[i]},${moveTokens[i+1]},${moveTokens[i+2]}`)
      }
      processedBuilder["locations_to_place"]=locationsToPlace.join("n")
      processedBuilder["move_stack"]=0
      console.log(processedBuilder)
      this.moveStack(processedBuilder)
    }
    return processedBuilder
  }
  async placePiece(processedMoves) {
    try {
      const response = await axios.get("http://localhost:5000/api/v1/move",
        { params: processedMoves})
      console.log(response.data)
      if("error" in response.data) {
        this.setState({
          error: response.data.error,
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
        })
      } else {
        this.setState({
          game: response.data,
          error: undefined,
          rows: []
        });
        this.setState({
          rows: this.generate_squares()
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`Move Made! ${this.state.game.turn==0?"Red":"Green"}'s turn now!`])
        })
        console.log(this.state.rows)
        this.forceUpdate();
        this.gameWon();
      }
    } catch (error) {
      console.log(error);
      this.setState({
        error: error.message,
      });
      this.setState({
        terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
      })
    }
  }
  async moveStack(processedMoves) {
    try {
      const response = await axios.get("http://localhost:5000/api/v1/move",
        { params: processedMoves})
      console.log(response.data)
      if("error" in response.data) {
        this.setState({
          error: response.data.error,
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
        })
      } else {
        this.setState({
          game: response.data,
          error: undefined,
          rows: []
        });
        this.setState({
          rows: this.generate_squares()
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`Move Made! ${this.state.game.turn==0?"Red":"Green"}'s turn now!`])
        })
        this.forceUpdate();
        this.gameWon();
      }
    } catch (error) {
      console.log(error);
      this.setState({
        error: error.message,
      });
      this.setState({
        terminal_elements: this.state.terminal_elements.concat([`${this.state.error}`])
      })
    }
  }
  sendMove() {
    this.parseMove(this.state.move.split(" "))
  } 
  async gameWon() {
    try {
      const response = await axios.get("http://localhost:5000/api/v1/game_won")
      console.log(response.data)
      if("error" in response.data) {
        this.setState({
          error: response.data.error,
        });
        this.setState({
          terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
        })
      } else {
        if(response.data.player_name !== "RUNNING"){
          this.setState({
            terminal_elements: this.state.terminal_elements.concat([`Winner is ${response.data.player_name}!!`])
          })
          console.log(this.state.rows)
          this.forceUpdate();
        }
      }
    } catch (error) {
      console.log(error);
      this.setState({
        error: error.message,
      });
      this.setState({
        terminal_elements: this.state.terminal_elements.concat([`ERROR: ${this.state.error}`])
      })
    }
  }
  render() {
    const terminal_components = this.state.terminal_elements.map(e=> 
      <Element name={`e`}>
        {e}
      </Element>
    )
    return (
      <Container>
        <Row>
          <Col>
            <Container style={{float:"left", backgroundColor:"white", borderColor:"brown", width: "560px", position: "relative", borderStyle:"solid"}}>
              <div style={{height:"10px"}} />
              {this.state.rows.map((value,index)=> {return <Row>{value}</Row>})}
              <Row>
                <Col>
                  <a href="#" onClick={()=>this.newGame("Human-Human")}>
                    New Human-Human Game
                  </a>
                </Col>
                <Col>
                  <a href="#" onClick={()=>this.newGame("Human-Computer")}>
                    New Human-Computer Game
                  </a>
                </Col>
                <Col>
                  <a href="#" onClick={()=>this.newGame("Computer-Computer")}>
                    New Computer-Computer Game
                  </a>
                </Col>
              </Row>
              <Row>
                <Col>
                  <a href="https://en.wikipedia.org/wiki/Tak_(game)" target="_blank">
                    <img src={takLogo} style={{"height": "170px", "width": "250px",}}/>
                  </a>
                </Col>
                <Col>
                  <p>
                    Instructions:<br />
                    Type moves into the text box on the right. Moves follow the following format:<br />
                    1. place [Horizontal | Vertical | Capstone] x y<br />
                    2. move x y number_of_pieces [first_x first_y number_of_pieces_to_place]*<br />
                  </p>
                </Col>
              </Row>
            </Container>
          </Col>
          <Col>
            <Terminal 
              style={{float:"left", backgroundColor:"white", borderColor:"brown"}} 
              updateMove={this.updateMove.bind(this)} 
              sendMove={this.sendMove.bind(this)}
              elements={terminal_components}
            />
          </Col>
        </Row>
      </Container>
    )
  }
}

export default App;
