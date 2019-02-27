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

    this.addOrder = this.addOrder.bind(this);
    this.deleteOrder = this.deleteOrder.bind(this);
    this.nextRound = this.nextRound.bind(this);
  }

  getMyCard() {
      //Back end to get a players hand of cards
      return ["QD"]
  }

  addOrder(value, type) {
    //TODO Send to backend and refresh state (order could be made)
    let book = [];
    if (type === "BUY") {
      book = this.state.bids
      book.push(value)
      this.setState({bids:book})
    } else {
      book = this.state.offers
      book.push(value)
      this.setState({offers:book})
    }

  }

  deleteOrder(value, type) {
    //TODO Send to backend that order is deleted
    let book = [];
    if (type === "BUY") {
      book = this.state.bids;
      let del_ind = book.indexOf(value);
      book.splice(del_ind, 1);
      this.setState({bids:book})
    } else {
      book = this.state.offers;
      let del_ind = book.indexOf(value);
      book.splice(del_ind, 1);
      this.setState({offers:book})
    }
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
