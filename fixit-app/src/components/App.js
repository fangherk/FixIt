import React, { Component } from "react";
import { Route, Switch } from 'react-router-dom';
import { Redirect } from 'react-router'


import Market from './views/market/Market'
import Lobby from './views/lobby/Lobby'
import './App.css'

export default class App extends Component {
  constructor(props) {
    super(props)
    this.toMarket = this.toMarket.bind(this)
    this.state = {toGame: false}
    this.name = ''

  }
  toMarket(name) {
    this.name = name
    this.setState({toGame: true})

  }

  render() {
    let shouldRedirect = this.state.toGame === true
    let redirectTo = <Redirect
                       to={{
                         pathname: '/market',
                         state: { name: this.name }
                       }} />


    return (
    <div className="App">
      <Switch>
        <Route path='/market' component={ Market }/>
        {shouldRedirect && redirectTo}


        <Route
          path='/'
          render={(props) => <Lobby {...props} toGame={this.toMarket}/>}
        />


      </Switch>
    </div>
    );
  }
}
