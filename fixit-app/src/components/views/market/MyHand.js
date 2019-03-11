import React from 'react';
import './stylesheets/MyHand.css';
import Card from './Card';

export default class MyHand extends React.Component {
  renderCard(value, suite) {
    return (<Card status="mine" value={value} suite={suite}/>)
  }

  render() {
    const VAL_TO_SUIT = {"1":"A","11":"J", "12":"Q", "13":"K"}

    let suite = this.props.card[this.props.card.length-1]
    let value = this.props.card.substring(0,this.props.card.length-1)

    if (value in VAL_TO_SUIT) {
      value = VAL_TO_SUIT[value]
    }

    return (
      <div className="my-hand">
        {this.renderCard(value, suite)}
      </div>
    )

  }
}
