import React from 'react';
import './stylesheets/Lobby.css';


var HEADERS = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*'
}
export default class Lobby extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      players:[],
      value:'',
    }
    this.name = ''

    this.handleTextChange = this.handleTextChange.bind(this)
    this.addUserName = this.addUserName.bind(this)
    this.sendReady = this.sendReady.bind(this)
    this.getServerData()
    this.lobbyUpdates = setInterval(this.getServerData.bind(this), 500)
  }

  showUsers() {
    /** takes list of players and displays their names in tables **/
    let rows = []
    for (let i = 0; i < this.state.players.length; i++) {
      let current_name = this.state.players[i]
      rows.push(<tr key={i}><td className="lobby-row">{current_name}</td></tr>)


    }
    return rows

  }

  sendReady() {
    /** sends to server that player is ready to start game **/
    fetch('http://127.0.0.1:8000/lobby/ready')
  }

  getServerData() {
    /** fetches data about the game **/
    let self = this
    fetch('http://127.0.0.1:8000/lobby').then(function(response) {
      response.json().then(json => {
        if (self.state.players.length !== json['players'].length) {
          self.setState({players:json['players']})
        }

        if (json['ready'] === true) {
          clearInterval(self.lobbyUpdates)
          self.props.toGame(self.name)
        }
      })
    })
  }

  addUserName(event) {
    /** Adds a user to the game **/
    let text = this.state.value.replace(/\s/g,'')
    if (text.length === 0 || this.state.players.includes(text)) {
      event.preventDefault()
      return
    }

    let self = this
    fetch('http://127.0.0.1:8000/lobby?task=join', {
      method:'PUT',
      headers:HEADERS,
      body: JSON.stringify({'name':text})
    }).then(function(response) {
      response.json().then(json => {
        self.setState({players:json['players']})
      })
    })
    this.name = text
    this.setState({value:''})
    event.preventDefault()
  }

  handleTextChange(event) {
    this.setState({value: event.target.value})

  }

  render() {
    return (
      <div className="Lobby">
        <div className="addPlayer">
          <form className="name-form" onSubmit={this.addUserName}>
            <input className="name-input" placeholder="Enter name" value={this.state.value} onChange={this.handleTextChange} />
          </form>
          <button onClick={this.sendReady}> </button>
        </div>
        <table className = "player-table" unselectable="on">
          <tbody>
            {this.showUsers()}
          </tbody>
        </table>
      </div>
    );
  }
}
