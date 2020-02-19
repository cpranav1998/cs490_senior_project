import React from 'react';
import './App.css';
import { Link, DirectLink, Element, Events, animateScroll as scroll, scrollSpy, scroller } from 'react-scroll'
import { Container, Row, Col } from 'react-grid-system';

class Terminal extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
      <div className="Terminal">
        <Container>
          <Row style={{backgroundColor:"white", borderStyle:"solid", borderColor:"brown"}}>
            <Col>
            <div style={{height:"10px"}} />
            <Element name="PastMoves" className="element" id="containerElement" style={{
                position: 'relative',
                height: '500px',
                overflow: 'scroll',
                width: '430px',
                backgroundColor:"white",
                borderStyle:"solid"
              }}>
              {this.props.elements}
            </Element>
            <p>
              Type a move below:<br />
              E.g.<br />
              place Horizontal 0 0<br />
              move 0 0 3 0 1 2 0 2 1<br />
            </p>
            <form onSubmit={this.props.sendMove} style={{
                position: 'relative',
                height: '100px',
                width: '200px',
                overflow:"visible",
                display: "inline-block"
              }}>
              <label>
                <textarea onChange={(e)=>this.props.updateMove(e)} style={{
                  position: 'relative',
                  height: '40px',
                  width: '430px',
                  overflow:"visible",
                  display: "inline-block"
                }}/>
              </label>
              <input type="submit" value="Submit" />
            </form>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Terminal;