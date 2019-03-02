import React from 'react';
import Card from './Card';
import './stylesheets/Middle.css';

export default class Middle extends React.Component {
  renderCard(value, suite, isShown = "YES") {
    let value_suite = `${value}${suite}`;
    return (<Card status="middle" key={value_suite} value={value} suite={suite} shown={isShown}/>)
  }

  render() {
    let middle = this.props.cards
    let cardTable = []
    for (let i = 0; i < middle.length; i++) {
      let middleCard = middle[i]
      let card = middleCard[0]

      cardTable.push(this.renderCard(card[0], card[1], middleCard[1]))

    }

    return (
      <div className="middle">
        {cardTable}
      </div>
    )

  }

}
