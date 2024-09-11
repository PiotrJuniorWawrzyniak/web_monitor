//import logo from './logo.svg';
//import './App.css';
//
//function App() {
//  return (
//    <div className="App">
//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>
//    </div>
//  );
//}
//
//export default App;

import './App.css';
import LiveUpdateComponent from './LiveUpdateComponent'; // zaimportuj nowy komponent

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Live Monitoring Update</h1>
        <LiveUpdateComponent />  {/* wstawienie nowego komponentu */}
      </header>
    </div>
  );
}

export default App;
