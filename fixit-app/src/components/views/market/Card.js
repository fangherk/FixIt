import React from 'react';
import './stylesheets/Card.css';


export default class Card extends React.Component {

  render() {
    let card = `${this.props.value}${this.props.suite}`;
    let cardImg = require(`./assets/cards/${card}.png`);
    if (this.props.shown === "NO") {
      cardImg = require('./assets/cards/blue_back.png')
    }

    let className = ""
    switch(this.props.status) {
      case "middle":
        className = "Card-middle";
        break
      case "mine":
        className = "Card-mine";
        break
      default:
        break;
    }
    return (
      <div className={className}>
        <img className={`${className}-img`} src={cardImg} alt={card} />
      </div>
    );
    }
}
