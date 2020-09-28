import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    todos: []
  };

  componentDidMount() {
    this.getTodos();
  }

  // new
  getTodos() {
    axios
      .get('http://127.0.0.1:8000/api/')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }


  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <h3>{item.author}</h3>
            <span>{item.body}</span>
          </div>
          //   <table>
          //   <tr key={item.id}> <td>{item.title} {item.}</td></tr>
          //     </table>
          ))}
      </div>
    );

  }

}



export default App;