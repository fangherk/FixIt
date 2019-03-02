import React, { Component } from 'react';
import Middle from './Middle';
import MyHand from './MyHand';
import Orders from './Orders';
import Stats from './Stats';
import BestDeals from './BestDeals';
import Timer from './Timer';
import AccountingBook from './AccountingBook';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      stats:[["Stat 1","Data 1"], ["Stat 2", "Data2"], ["Stat 3", "Data 3"]],
      middle:[["QH", "YES"],["KH", "YES"],["JH","YES"]],
      offers:[],
      bids:[],
      bestOffer:"46",
      bestBid:"46"
    }

    this.addOrder = ((value, type) => {this.modifyOrders(value, type, "ADD")})
    this.deleteOrder = ((value, type) => {this.modifyOrders(value, type, "DELETE")})
    this.nextRound = this.nextRound.bind(this);

    this.getInitialData()

  }

  getMyCard() {
      //Back end to get a players hand of cards
      return ["QD"]
  }

  getInitialData() {
    let self = this
    fetch('http://127.0.0.1:5000/orders/1').then(function(response) {
      response.json().then(json => {
        self.setState({bids:json['bids']})
        self.setState({offers:json['offers']})
      })
    })
  }

  count(obj) { return Object.keys(obj).length; }

  modifyOrders(value, type, task) {
    //TODO Send to backend and refresh state (order could be made)
    let self = this

    fetch('http://127.0.0.1:5000/orders/1', {
      method:'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({"value":value,"type":type,"task":task})
    }).then(function(response) {
      response.json().then(json => {
        self.setState({bids:json['bids']})
        self.setState({offers:json['offers']})
      })
    })
  }

  nextRound() {

  }

  render() {
    return (
      <div className="App">
        <Middle cards={this.state.middle}/>
        <MyHand cards={this.getMyCard()}/>
        <Orders bids={this.state.bids} offers={this.state.offers} onSubmit={this.addOrder} onDelete={this.deleteOrder}/>
        {/* <Stats  stats={this.state.stats}/> */}
        <BestDeals bestBid={this.state.bestBid} bestOffer={this.state.bestOffer}/>
        <Timer onTimeUp={this.nextRound}/>
        <AccountingBook />
      </div>
    );
  }
}

export default App;
