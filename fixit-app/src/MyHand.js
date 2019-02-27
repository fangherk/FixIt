import React from 'react';
import './MyHand.css';
import Card from './Card';

export default class MyHand extends React.Component {
  renderCard(value, suite) {
    return (<Card status="mine" key={value} value={value} suite={suite} />)
  }

  render() {
    let hand = this.props.cards
    let cardTable = []
    for (let i = 0; i < hand.length; i++) {
      let card = hand[i]
      cardTable.push(this.renderCard(card[0], card[1]))
    }
    return (
      <div className="my-hand">
        {cardTable}
      </div>
    )

  }
}
