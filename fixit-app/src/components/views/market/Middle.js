import React from 'react';
import Card from './Card';
import './stylesheets/Middle.css';

export default class Middle extends React.Component {
  renderCard(value, suite, isShown = true) {
    let value_suite = `${value}${suite}`;
    return (<Card status="middle" key={value_suite} value={value} suite={suite} shown={isShown}/>)
  }

  render() {
    let middle = this.props.cards
    let cardTable = []
    const VAL_TO_SUIT = {"1":"A","11":"J", "12":"Q", "13":"K"}
    for (let i = 0; i < middle.length; i++) {
      let middleCard = middle[i]


      let suite = middleCard[middleCard.length-1]
      let value = middleCard.substring(0, middleCard.length-1)

      if (value in VAL_TO_SUIT) {
        value = VAL_TO_SUIT[value]
      }

      cardTable.push(this.renderCard(value, suite, i < this.props.turn))

    }

    return (
      <div className="middle">
        {cardTable}
      </div>
    )

  }

}
