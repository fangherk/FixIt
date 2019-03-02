import React, { Component } from "react";
import { Link, Route, Switch } from 'react-router-dom';

import Market from './views/market/Market'
import Lobby from './views/lobby/Lobby'

export default class App extends Component {
  render() {
    return (
      <div>
      <Route path="/market" component = {Market}/>
      <Route path="/lobby" component = {Lobby}/>
      </div>
    );
  }
}
