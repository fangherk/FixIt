import React from 'react';
import './stylesheets/MyHand.css';
import Card from './Card';

export default class MyHand extends React.Component {
  renderCard(value, suite) {
    return (<Card status="mine" value={value} suite={suite}/>)
  }

  render() {
    return (
      <div className="my-hand">
        {this.renderCard(this.props.card[0], this.props.card[1])}
      </div>
    )

  }
}
