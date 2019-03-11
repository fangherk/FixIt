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
      middle:["QH"],
      turn:0,
      card:"10H",
      offers:[],
      bids:[],
      bestOffer:"0",
      bestBid:"0",
      accounting:[]
    }
    this.name = this.props.location.state['name']

    this.getMarketData(true)
    this.marketUpdates = setInterval(this.getMarketData.bind(this), 500)

    this.addOrder = ((value, type) => {this.modifyOrders(value, type, "ADD")})
    this.deleteOrder = ((value, type) => {this.modifyOrders(value, type, "DELETE")})
    this.nextRound = this.nextRound.bind(this);
  }

  getMarketData(initial = false) {
    fetch('http://127.0.0.1:8000/orders/' + this.name).then( (response) => {
      response.json().then(json => {
        this.setState({
          bids: json['player']['bids'],
          offers: json['player']['offers'],
          turn: json['turn'],
          accounting: json['accounting'],
          middle: json['middle'],
          card: json['player']['card'],
          bestOffer: json['bestOffer'],
          bestBid: json['bestBid']
        })
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
        self.setState({
          bids:json['player']['bids'],
          offers:json['player']['offers']
        })
      })
    })
  }

  nextRound() {

  }

  render() {
    return (
      <div className="Market">
        <Middle cards={this.state.middle} turn={this.state.turn}/>
        <MyHand card={this.state.card}/>
        <Orders bids={this.state.bids} offers={this.state.offers} onSubmit={this.addOrder} onDelete={this.deleteOrder}/>
        <BestDeals bestBid={this.state.bestBid} bestOffer={this.state.bestOffer}/>
        <Timer onTimeUp={this.nextRound}/>
        <AccountingBook accounting={this.state.accounting}/>
      </div>
    );
  }

}
