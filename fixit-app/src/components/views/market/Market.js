import React, { Component } from 'react';

import Middle from './Middle';
import MyHand from './MyHand';
import Orders from './Orders';
import BestDeals from './BestDeals';
import Timer from './Timer';
import AccountingBook from './AccountingBook';
import './stylesheets/Market.css';

export default class Market extends Component {
  constructor(props) {
    super(props)
    this.state = {
      middle:[["QH", "YES"],["KH", "YES"],["JH","YES"]],
      card:"3H",
      offers:[],
      bids:[],
      bestOffer:"46",
      bestBid:"46",
      accounting:[]
    }
    this.name = this.props.location.state['name']

    this.getMarketData()
    this.marketUpdates = setInterval(this.getMarketData.bind(this), 500)

    this.addOrder = ((value, type) => {this.modifyOrders(value, type, "ADD")})
    this.deleteOrder = ((value, type) => {this.modifyOrders(value, type, "DELETE")})
    this.nextRound = this.nextRound.bind(this);
  }

  setStateMod(state_key, state_value) {
    if ((this.state[state_key] !== state_value) || (this.state[state_key].length !== state_value.length)) {
      this.setState({[state_key]:state_value})
    }
  }

  getMarketData() {
    let self = this
    fetch('http://127.0.0.1:8000/orders/' + this.name).then(function(response) {
      response.json().then(json => {
        self.setStateMod('bids', json['player']['bids'])
        self.setStateMod('offers', json['player']['offers'])
        self.setStateMod('card', json['player']['card'])
        self.setStateMod('accounting', json['accounting'])
      })
    })
  }

count(obj) { return Object.keys(obj).length; }

modifyOrders(value, type, task) {
  //TODO Send to backend and refresh state (order could be made)
  let self = this

  fetch('http://127.0.0.1:8000/orders/' + this.name, {
    method:'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({"value":value,"type":type,"task":task})
    }).then(function(response) {
      response.json().then(json => {
        self.setState({bids:json['player']['bids']})
        self.setState({offers:json['player']['offers']})
      })
    })
  }

  nextRound() {

  }

  render() {
    return (
      <div className="Market">
        <Middle cards={this.state.middle}/>
        <MyHand card="5H"/>
        <Orders bids={this.state.bids} offers={this.state.offers} onSubmit={this.addOrder} onDelete={this.deleteOrder}/>
        <BestDeals bestBid={this.state.bestBid} bestOffer={this.state.bestOffer}/>
        <Timer onTimeUp={this.nextRound}/>
        <AccountingBook accounting={this.state.accounting}/>
      </div>
    );
  }

}
