import React, {Component, Fragment} from 'react';
import axios from 'axios';
import { Col, CardGroup, Card, } from 'react-bootstrap';

class BookList extends Component {

    state = {
        books: []
    };

    componentDidMount() {
        this.getBooks();
    }

    getBooks() {
        axios
            .get('http://127.0.0.1:8000/api/v1/')
            .then(res => {
                this.setState({books: res.data});
            })
            .catch(err => {
                console.log(err);
            });
    }

    render(){
        return(
            <Fragment>
                {this.state.books.map(elt =>(
                    <Col key={elt.id} lg={3} style={{padding:'15px'}}>
                        <CardGroup>
                            <Card.Img variant="top" src={`${elt.picture}`} style={{maxWidth:'100%', height:'300px', width:'230px'}} />
                            <Card.Title style={{textAlign:'center'}}>{elt.title}</Card.Title>
                        </CardGroup>
                    </Col>
                ))}
            </Fragment>
        )
    }
}

export default BookList;