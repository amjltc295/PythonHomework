import React, { Component } from 'react';
import logo from './python.png';
import './App.css';
import ResultTable from './results'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>
            Introduction to Computer (計算機概論), Fall 2018, NTUCSIE <br/>
            Python Homework Learderboard
          </h1>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <ResultTable />
        </header>
      </div>
    );
  }
}

export default App;
