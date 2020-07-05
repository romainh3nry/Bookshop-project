import React from 'react';
import './App.css';
import { Container, Row } from 'react-bootstrap';
import BookList from "./BookCard";
import {BrowserRouter as Router, Switch, Route, Link} from "react-router-dom";
import AddBook from "./AddBook";

function App() {
  return (
      <Router>
          <div className="App">
              <h3>BookShop</h3>
              <Link to="/">Home</Link> | <Link to="/add">Add a book</Link>
              <hr/>
              <Container>
                  <Row>
                      <BookList />
                  </Row>
              </Container>
          </div>
          <Switch>
              <Route path="/add">
                  <AddBook />
              </Route>
          </Switch>
      </Router>
  );
}

export default App;
